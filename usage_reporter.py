# MIT License
#
# Copyright (c) 2023 Pete Bentley
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import csv
import os
import re
import sys

import requests
import urllib.parse
from datetime import datetime
from typing import Optional

# Usage: python usage_reporter.py [update]
#
# If no update argument is given, downloads stats for the previous calendar month and
# displays them.  Note that this relies on the fact that if only a single month is requested,
# the data is returned in a different format, with one CSV row per Android version.
#
# If an 'update' argument is given this script will attempt to update the data in index.md.  It's
# a pretty crude parser which relies on the data for each Android version being inserted
# in the table row for a particular API level, see level_to_version dict below.
#
# MacOS Note:  Should work with the python3 that comes with the Xcode command line tools, but
# you'll need to install the 'requests' module, for example:
#      python3 -m pip install requests

versions_to_report_on = [
    '14.0', '13.0', '12.0', '11.0', '10.0', '9.0',
    '8.1', '8.0', '7.1', '7.0', '6.0', '5.1', '5.0',
    '4.4', '4.3', '4.2', '4.1', '4.0'
]

level_to_version = {
    33: '13.0', 32: '12.0', 30: '11.0', 29: '10.0', 28: '9.0',
    27: '8.1', 26: '8.0', 25: '7.1', 24: '7.0', 23: '6.0', 22: '5.1', 21: '5.0',
    20: '4.4', 18: '4.3', 17: '4.2', 16: '4.1', 15: '4.0'
}


def generate_stats_url() -> str:
    base = 'https://gs.statcounter.com/android-version-market-share/mobile-tablet/chart.php?'
    parameters = {
        'device_hidden': 'mobile+tablet',
        'multi-device': 'true',
        'statType_hidden': 'android_version',
        'region_hidden': 'ww',
        'granularity': 'monthly',
        'statType': 'Android Version',
        'region': 'Worldwide',
        'csv': '1'
    }
    date_string = last_month_as_string()
    parameters['fromMonthYear'] = date_string
    parameters['toMonthYear'] = date_string
    return base + join_parameters(parameters)


def last_month_as_string() -> str:
    month = datetime.now().month
    year = datetime.now().year
    if month == 1:
        month = 12
        year -= 1
    else:
        month -= 1
    return "{}-{:02d}".format(year, month)


def join_parameters(parameters: dict[str, str]) -> str:
    parameter_string = ''
    separator = ''
    for key in parameters:
        value = urllib.parse.quote(parameters[key])
        parameter_string += '{}{}={}'.format(separator, key, value)
        separator = '&'
    return parameter_string


def version_key(line: str) -> Optional[str]:
    return next(
        (key for key in versions_to_report_on if line.startswith(key)),
        None)


def download(url: str) -> dict[str, float]:
    response = requests.get(url)
    response.raise_for_status()

    lines = (line.decode('utf-8') for line in response.iter_lines())
    values = dict()
    for row in csv.reader(lines):
        key = version_key(row[0])
        if key:
            values[key] = float(row[1])
    return values


def accumulate(input_values: dict[str, float]) -> dict[str, float]:
    cumulative = 0.0
    values = dict()
    for key in versions_to_report_on:
        cumulative += input_values[key]
        values[key] = cumulative
    return values


class ParseError(AssertionError):
    pass


class IndexUpdater:
    def __init__(self):
        self.values = None
        self.in_filename = 'index.md'
        self.tmp_filename = 'index.tmp'
        # Matches and extracts a level number from anywhere in a line of text.
        self.level_re = re.compile('.*Level (\\d+)')
        # Matches a line with a progressive-cell and extracts the current value.
        self.data_re = re.compile('(.*progress-cell.html.* percentage=)([0-9.]+)(.*)')
        # Matches and extracts the "last updated" date.
        self.updated_re = re.compile(
            '(\\s+<p>Cumulative.*updated on <b>)(\\w+ \\d+, \\d+)(</b> using.*)')
        # Current 'state', which is a reference to the method to use to process the next line.
        self.process = self.init
        # Last API level found which has not yet been used, else None.
        self.api_level = None
        # True once all substitutions have been made.
        self.finished = False
        self.seen_api_levels = set()

    def update_index(self, values: dict[str, float]):
        self.values = values
        with open(self.in_filename, mode='r', encoding="utf-8") as infile:
            with open(self.tmp_filename, mode='w', encoding="utf-8") as self.outfile:
                for line in infile:
                    self.outfile.write(self.process(line))
        if not self.finished:
            raise ParseError('Failed to find all values')
        for level in level_to_version.keys():
            if level not in self.seen_api_levels:
                raise ParseError('Did not update data for API level' + level)
        os.rename(self.tmp_filename, self.in_filename)

    # Initial state: looking for the first table in the file.
    def init(self, line: str) -> str:
        if '<table ' in line:
            self.process = self.table
        return line

    # State while processing the first table, but not currently within a table row.
    def table(self, line: str) -> str:
        if '<tr>' in line:
            self.process = self.table_row
        if '</table>' in line:
            self.process = self.update_date
        return line

    # State while processing a table row.
    def table_row(self, line: str) -> str:
        match = re.match(self.data_re, line)
        if match:
            if not self.api_level or self.api_level not in level_to_version:
                raise ParseError('API level unknown')
            new_value = self.values[level_to_version[self.api_level]]
            self.api_level = None
            return "{}{:.01f}{}\n".format(match[1], new_value, match[3])
        else:
            match = re.match(self.level_re, line)
            if match:
                if self.api_level:
                    raise ParseError('Multiple API levels found')
                self.api_level = int(match[1])
                self.seen_api_levels.add(self.api_level)
            elif '</tr>' in line:
                self.process = self.table
                self.api_level = None
        return line

    # State reached after all usage has been updated and we are looking for the update date
    def update_date(self, line: str) -> str:
        match = re.match(self.updated_re, line)
        if match:
            self.process = self.done
            return ("{}{}{}\n"
                    .format(match[1], datetime.now().strftime("%B %d, %Y"), match[3]))
        return line

    # State reached after all substitutions have been performed.
    def done(self, line: str) -> str:
        self.finished = True
        return line


def report_and_maybe_update(do_update: bool):
    values = accumulate(download(generate_stats_url()))
    if do_update:
        updater = IndexUpdater()
        updater.update_index(values)
    for key in versions_to_report_on:
        print("Android {}: {:.02f}".format(key, values[key]))


if __name__ == '__main__':
    report_and_maybe_update(len(sys.argv) > 1 and 'update' in sys.argv[1])
