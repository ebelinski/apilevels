# Copyright 2023 Peter Bentley.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

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
# displays them.  NB relies on the fact that if only a single month is requested, the data
# is in a different format, with one CSV row per Android version.
#
# If an 'update' argument is given will attempt to update the data in index.md.  It's
# a pretty crude parser which relies on the data for each Android version being inserted
# in the table row for a particular API level, see level_to_version dict below.

versions_to_report_on = [
    '14', '13', '12', '11', '10', '9',
    '8.1', '8.0', '7.1', '7.0', '6', '5.1', '5.0',
    '4.4', '4.3', '4.2', '4.1', '4.0'
]

level_to_version = {
    33: '13', 32: '12', 30: '11', 29: '10', 28: '9',
    27: '8.1', 26: '8.0', 25: '7.1', 24: '7.0', 23: '6', 22: '5.1', 21: '5.0',
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


def update_index(values: dict[str, float]):
    infilename = 'index.md'
    tmpfilename = 'index.tmp'
    level_re = re.compile('.*Level (\\d+)')
    data_re = re.compile('(.*progress-cell.html.* percentage=)([0-9.]+)(.*)')
    state = 'init'
    api_level = None
    with open(infilename, mode='r', encoding="utf-8") as infile:
        with open(tmpfilename, mode='w', encoding="utf-8") as outfile:
            for line in infile:
                match state:
                    case 'init':
                        if line.startswith('<table class="full-width">'):
                            state = 'table'
                    case 'table':
                        if '<tr>' in line:
                            state = 'row'
                        if line.startswith('</table>'):
                            state = 'done'
                    case 'row':
                        if '</tr>' in line:
                            state = 'table'
                            api_level = None
                        match = re.match(level_re, line)
                        if match:
                            if api_level:
                                raise AssertionError('Parse error')
                            api_level = int(match[1])
                        match = re.match(data_re, line)
                        if match:
                            if not api_level:
                                raise AssertionError('Parse error')
                            if api_level in level_to_version:
                                value = values[level_to_version[api_level]]
                                newline = "{}{:.01f}{}\n".format(match[1], value, match[3])
                                outfile.write(newline)
                                api_level = None
                                continue
                    case 'done':
                        pass
                    case _:
                        raise AssertionError('Invalid state')
                outfile.write(line)
    os.rename(tmpfilename, infilename)


def report_and_maybe_update(do_update: bool):
    values = accumulate(download(generate_stats_url()))
    if do_update:
        update_index(values)
    for key in versions_to_report_on:
        print("Android {}: {:.02f}".format(key, values[key]))


if __name__ == '__main__':
    report_and_maybe_update(len(sys.argv) > 1 and 'update' in sys.argv[1])
