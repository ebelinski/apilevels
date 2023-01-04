---
layout: default
---
{::options parse_block_html="true" /}

This is an overview of all Android versions and their corresponding identifiers for Android developers. Anyone is welcome to open [an issue or pull request](https://github.com/ebelinski/apilevels). Happy developing!

<div id="compact-toc">
* TOC
{:toc}
</div>

<div class="table-responsive">
<table class="full-width">
  <tr>
    <th>Version</th>
    <th>SDK / API level</th>
    <th><a href="https://developer.android.com/reference/kotlin/android/os/Build.VERSION_CODES">Version code</a></th>
    <th>Codename</th>
    <th>
      Cumulative<br>usage
      <sup id="fnref:1"><a href="#fn:1" class="footnote">1</a></sup>
    </th>
    <th>Year</th>
  </tr>
  <tr>
    <td>
      <b><a href="https://developer.android.com/about/versions/13">Android 13</a></b>
    </td>
    <td>Level 33</td>
    <td><code>TIRAMISU</code></td>
    <td>
      Tiramisu
      <sup id="fnref:2"><a href="#fn:2" class="footnote">2</a></sup>
    </td>
    {% include progress-cell.html rowspan=1 percentage=6.8 %}
    <td rowspan="2">2022</td>
  </tr>
  <tr>
    <td rowspan="3">
      <b><a href="https://developer.android.com/about/versions/12">Android 12</a></b>
    </td>
    <td>
      Level 32
      <span class="subversion">Android 12L</span>
    </td>
    <td><code>S_V2</code></td>
    <td rowspan="2">
      Snow Cone
      <sup id="fnref:2"><a href="#fn:2" class="footnote">2</a></sup>
    </td>
    {% include progress-cell.html rowspan=3 percentage=35.0 %}
  </tr>
  <tr>
    <td>Level 31 <span class="subversion">Android 12</span></td>
    <td><code>S</code></td>
    <td rowspan="2">2021</td>
  </tr>
  <tr class="table-notes"><td colspan="3">
    <ul>
      <li><code>targetSdk</code> <a href="https://developer.android.com/google/play/requirements/target-sdk">must be 31+</a> for new apps.</li>
      <li><code>targetSdk</code> <a href="https://support.google.com/googleplay/android-developer/answer/11926878">will need to be 31+</a> for app updates by Nov 2022 and <i>all existing apps</i> by Nov 2023. <sup id="fnref:3"><a href="#fn:3" class="footnote">3</a></sup></li>
    </ul>
  </td></tr>
  <tr>
    <td rowspan="2">
      <b><a href="https://developer.android.com/about/versions/11">Android 11</a></b>
    </td>
    <td>Level 30</td>
    <td><code>R</code></td>
    <td>
      Red Velvet Cake
      <sup id="fnref:2"><a href="#fn:2" class="footnote">2</a></sup>
    </td>
    {% include progress-cell.html rowspan=2 percentage=58.6 %}
    <td rowspan="2">2020</td>
  </tr>
  <tr class="table-notes"><td colspan="3">
    <ul>
      <li><code>targetSdk</code> <a href="https://developer.android.com/google/play/requirements/target-sdk">must be 30+</a> for app updates, and new WearOS apps.</li>
      <li><code>targetSdk</code> <a href="https://support.google.com/googleplay/android-developer/answer/11926878">will need to be 30+</a> for <i>all existing apps</i> by November 2022. <sup id="fnref:3"><a href="#fn:3" class="footnote">3</a></sup></li>
    </ul>
  </td></tr>
  <tr>
    <td>
      <b><a href="https://developer.android.com/about/versions/10">Android 10</a></b>
    </td>
    <td>Level 29</td>
    <td><code>Q</code></td>
    <td>
      Quince Tart
      <sup id="fnref:2"><a href="#fn:2" class="footnote">2</a></sup>
    </td>
    {% include progress-cell.html rowspan=1 percentage=77.0 %}
    <td>2019</td>
  </tr>
  <tr>
    <td rowspan="2">
      <b><a href="https://developer.android.com/about/versions/pie">Android 9</a></b>
    </td>
    <td>Level 28</td>
    <td><code>P</code></td>
    <td>Pie</td>
    {% include progress-cell.html rowspan=2 percentage=85.7 %}
    <td rowspan="2">2018</td>
  </tr>
  <tr class="table-notes"><td colspan="3">
    <ul>
      <li><code>targetSdk</code> <a href="https://developer.android.com/google/play/requirements/target-sdk">must be 28+</a> for Wear OS app updates.</li>
    </ul>
  </td></tr>
  <tr>
    <td rowspan="2">
      <b><a href="https://developer.android.com/about/versions/oreo">Android 8</a></b>
    </td>
    <td>Level 27 <span class="subversion">Android 8.1</span></td>
    <td><code>O_MR1</code></td>
    <td rowspan="2">Oreo</td>
    {% include progress-cell.html rowspan=1 percentage=90.6 %}
    <td rowspan="2">2017</td>
  </tr>
  <tr>
    <td>Level 26 <span class="subversion">Android 8.0</span></td>
    <td><code>O</code></td>
    {% include progress-cell.html rowspan=1 percentage=92.5 %}
  </tr>
  <tr>
    <td rowspan="2">
      <b><a href="https://developer.android.com/about/versions/nougat">Android 7</a></b>
    </td>
    <td>Level 25 <span class="subversion">Android 7.1</span></td>
    <td><code>N_MR1</code></td>
    <td rowspan="2">Nougat</td>
    {% include progress-cell.html rowspan=1 percentage=93.7 %}
    <td rowspan="2">2016</td>
  </tr>
  <tr>
    <td>Level 24 <span class="subversion">Android 7.0</span></td>
    <td><code>N</code></td>
    {% include progress-cell.html rowspan=1 percentage=96.1 %}
  </tr>
  <tr>
    <td>
      <b><a href="https://developer.android.com/about/versions/marshmallow">Android 6</a></b>
    </td>
    <td>Level 23</td>
    <td><code>M</code></td>
    <td>Marshmallow</td>
    {% include progress-cell.html rowspan=1 percentage=97.9 %}
    <td>2015</td>
  </tr>
  <tr>
    <td rowspan="3">
      <b><a href="https://developer.android.com/about/versions/lollipop">Android 5</a></b>
    </td>
    <td>Level 22 <span class="subversion">Android 5.1</span></td>
    <td><code>LOLLIPOP_MR1</code></td>
    <td rowspan="2">Lollipop</td>
    {% include progress-cell.html rowspan=1 percentage=99.1 %}
    <td>2015</td>
  </tr>
  <tr>
    <td>Level 21 <span class="subversion">Android 5.0</span></td>
    <td><code>LOLLIPOP</code>, <code>L</code></td>
    {% include progress-cell.html rowspan=2 percentage=99.3 %}
    <td rowspan="3">2014</td>
  </tr>
  <tr class="table-notes"><td colspan="3">
    <ul>
      <li><a href="https://developer.android.com/jetpack/compose">Jetpack Compose</a> requires a <code>minSdk</code> of 21 or higher.</li>
    </ul>
  </td></tr>
  <tr>
    <td rowspan="9"><b>Android 4</b></td>
    <td>
      Level 20
      <span class="subversion">Android 4.4W</span> <sup id="fnref:4"><a href="#fn:4" class="footnote">4</a></sup>
    </td>
    <td><code>KITKAT_WATCH</code></td>
    <td rowspan="2">KitKat</td>
    <td rowspan="22"><i>No data</i></td>
  </tr>
  <tr>
    <td>
      Level 19
      <span class="subversion">Android 4.4</span>
    </td>
    <td><code>KITKAT</code></td>
    <td rowspan="3">2013</td>
  </tr>
  <tr class="table-notes"><td colspan="3">
    <ul>
      <li>Google Play services <a href="https://android-developers.googleblog.com/2021/07/google-play-services-discontinuing-jelly-bean.html">do not support Android versions</a> below API level 19.</li>
    </ul>
  </td></tr>
  <tr>
    <td>Level 18 <span class="subversion">Android 4.3</span></td>
    <td><code>JELLY_BEAN_MR2</code></td>
    <td rowspan="3">Jelly Bean</td>
  </tr>
  <tr>
    <td>Level 17 <span class="subversion">Android 4.2</span></td>
    <td><code>JELLY_BEAN_MR1</code></td>
    <td rowspan="2">2012</td>
  </tr>
  <tr>
    <td>Level 16 <span class="subversion">Android 4.1</span></td>
    <td><code>JELLY_BEAN</code></td>
  </tr>
  <tr>
    <td>Level 15 <span class="subversion">Android 4.0.3 – 4.0.4</span></td>
    <td><code>ICE_CREAM_SANDWICH_MR1</code></td>
    <td rowspan="2">Ice Cream Sandwich</td>
    <td rowspan="7">2011</td>
  </tr>
  <tr>
    <td>Level 14 <span class="subversion">Android 4.0.1 – 4.0.2</span></td>
    <td><code>ICE_CREAM_SANDWICH</code></td>
  </tr>
  <tr class="table-notes"><td colspan="3">
    <ul>
      <li><a href="https://developer.android.com/jetpack">Jetpack</a>/<a href="https://developer.android.com/jetpack/androidx">AndroidX</a> libraries <a href="https://developer.android.com/topic/libraries/support-library#api-versions">require</a> a <code>minSdk</code> of 14 or higher.</li>
    </ul>
  </td></tr>
  <tr>
    <td rowspan="3"><b>Android 3</b></td>
    <td>Level 13 <span class="subversion">Android 3.2</span></td>
    <td><code>HONEYCOMB_MR2</code></td>
    <td rowspan="3">Honeycomb</td>
  </tr>
  <tr>
    <td>Level 12 <span class="subversion">Android 3.1</span></td>
    <td><code>HONEYCOMB_MR1</code></td>
  </tr>
  <tr>
    <td>Level 11 <span class="subversion">Android 3.0</span></td>
    <td><code>HONEYCOMB</code></td>
  </tr>
  <tr>
    <td rowspan="6"><b>Android 2</b></td>
    <td>Level 10 <span class="subversion">Android 2.3.3 – 2.3.7</span></td>
    <td><code>GINGERBREAD_MR1</code></td>
    <td rowspan="2">Gingerbread</td>
  </tr>
  <tr>
    <td>Level 9 <span class="subversion">Android 2.3.0 – 2.3.2</span></td>
    <td><code>GINGERBREAD</code></td>
    <td rowspan="3">2010</td>
  </tr>
  <tr>
    <td>Level 8 <span class="subversion">Android 2.2</span></td>
    <td><code>FROYO</code></td>
    <td>Froyo</td>
  </tr>
  <tr>
    <td>Level 7 <span class="subversion">Android 2.1</span></td>
    <td><code>ECLAIR_MR1</code></td>
    <td rowspan="3">Eclair</td>
  </tr>
  <tr>
    <td>Level 6 <span class="subversion">Android 2.0.1</span></td>
    <td><code>ECLAIR_0_1</code></td>
    <td rowspan="5">2009</td>
  </tr>
  <tr>
    <td>Level 5 <span class="subversion">Android 2.0</span></td>
    <td><code>ECLAIR</code></td>
  </tr>
  <tr>
    <td rowspan="4"><b>Android 1</b></td>
    <td>Level 4 <span class="subversion">Android 1.6</span></td>
    <td><code>DONUT</code></td>
    <td>Donut</td>
  </tr>
  <tr>
    <td>Level 3 <span class="subversion">Android 1.5</span></td>
    <td><code>CUPCAKE</code></td>
    <td>Cupcake</td>
  </tr>
  <tr>
    <td>Level 2 <span class="subversion">Android 1.1</span></td>
    <td><code>BASE_1_1</code></td>
    <td>Petit Four</td>
  </tr>
  <tr>
    <td>Level 1 <span class="subversion">Android 1.0</span></td>
    <td><code>BASE</code></td>
    <td><i>None</i></td>
    <td>2008</td>
  </tr>
</table>
</div>

## Target version policy

#### Policy rules
<div class="table-responsive">
<table class="full-width">
  <tr>
    <th class="nowrap">Name</th>
    <th>Definition</th>
  </tr>
  <tr>
    <td class="nowrap"><code>new app</code></td>
    <td>Must target an android api level <strong>within one year</strong> from the latest major Android OS version.</td>
  </tr>
  <tr>
    <td class="nowrap"><code>update app</code></td>
    <td>Must target an android api level <strong>within one year</strong> from the latest major Android OS version.</td>
  </tr>
  <tr>
    <td class="nowrap"><code>existing app</code></td>
    <td>Must target an android api level <strong>within two years</strong> from the latest major Android OS version. Otherwise you have to expect <a href="https://android-developers.googleblog.com/2022/04/expanding-plays-target-level-api-requirements-to-strengthen-user-security.html">restrictions</a>.</td>
  </tr>
  <tr>
    <td class="nowrap"><code>wear os app</code></td>
    <td>Must target an android api level <strong>within two years</strong> from the latest major Android OS version. Otherwise you have to expect <a href="https://android-developers.googleblog.com/2022/04/expanding-plays-target-level-api-requirements-to-strengthen-user-security.html">restrictions</a>.</td>
  </tr>
  <tr>
    <td class="nowrap"><code>automobil app</code></td>
    <td>Must target an android api level <strong>within two years</strong> from the latest major Android OS version. Otherwise you have to expect <a href="https://android-developers.googleblog.com/2022/04/expanding-plays-target-level-api-requirements-to-strengthen-user-security.html">restrictions</a>.</td>
  </tr>
</table>
</div>

#### Required targetSdkVersion for your app in the Google Play Store

This is a list that shows which <code>targetSdkVersion</code> your app needs in the Google Play Store, without any <a href="https://android-developers.googleblog.com/2022/04/expanding-plays-target-level-api-requirements-to-strengthen-user-security.html">restrictions</a>.

<div class="table-responsive">
<table class="full-width">
  <tr>
    <th>SDK / API level</th>
    <th>Release date</th>
    <th>new app</th>
    <th>update app</th>
    <th>existing app</th>
    <th>wear os app</th>
    <th>automobil app</th>
  </tr>
  <tr>
    <td>Level 33</td>
    <td><code>2022-08-15</code></td>
    <td>✅</td>
    <td>✅</td>
    <td>✅</td>
    <td>✅</td>
    <td>✅</td>
  </tr>
  <tr>
    <td>Level 32</td>
    <td><code>2022-03-07</code></td>
    <td>✅</td>
    <td>✅</td>
    <td>✅</td>
    <td>✅</td>
    <td>✅</td>
  </tr>
  <tr>
    <td>Level 31</td>
    <td><code>2021-10-04</code></td>
    <td>✅</td>
    <td>✅</td>
    <td>✅</td>
    <td>✅</td>
    <td>✅</td>
  </tr>
  <tr>
    <td>Level 30</td>
    <td><code>2020-09-08</code></td>
    <td>❌</td>
    <td>❌</td>
    <td>✅</td>
    <td>✅</td>
    <td>✅</td>
  </tr>
  <tr>
    <td>Level 29</td>
    <td><code>2019-09-03</code></td>
    <td>❌</td>
    <td>❌</td>
    <td>❌</td>
    <td>❌</td>
    <td>❌</td>
  </tr>
</table>
</div>

#### Links
* [targetSdkVersion policy rules](https://support.google.com/googleplay/android-developer/answer/11926878#zippy=%2Ci-have-a-live-app-on-google-play-that-targets-api-or-lower-that-i-do-not-plan-to-update-what-are-my-options)
* [SDK/API release dates](https://de.wikipedia.org/wiki/Liste_von_Android-Versionen)

## Definitions

#### Gradle files

<div class="table-responsive">
<table class="full-width">
  <tr>
    <th class="nowrap">Kotlin variable</th>
    <th class="nowrap">Groovy variable</th>
    <th>Definition</th>
  </tr>
  <tr>
    <td class="nowrap"><code>minSdk</code></td>
    <td class="nowrap"><code>minSdkVersion</code></td>
    <td>The minimum SDK version your app will support, defined in <code>build.gradle</code>. For example, if your <code>minSdk</code> is 26, this SDK version corresponse to API Level 26 and Android 8, so your app will only run on devices with Android 8 or higher.</td>
  </tr>
  <tr>
    <td class="nowrap"><code>targetSdk</code></td>
    <td class="nowrap"><code>targetSdkVersion</code></td>
    <td>The SDK version that your app targets, defined in <code>build.gradle</code>. This should always be the same as <code>compileSdk</code>.</td>
  </tr>
  <tr>
    <td class="nowrap"><code>compileSdk</code></td>
    <td class="nowrap"><code>compileSdkVersion</code></td>
    <td>The SDK version that your app compiles against, defined in <code>build.gradle</code>. Android Studio uses this SDK version to build your AABs and APKs. This should always be the same as <code>targetSdk</code>.</td>
  </tr>
</table>
</div>

#### App type

<div class="table-responsive">
<table class="full-width">
  <tr>
    <th class="nowrap">Name</th>
    <th>Definition</th>
  </tr>
  <tr>
    <td class="nowrap"><code>new app</code></td>
    <td>An app that is not yet published on Google Play (i.e., a brand new app).</td>
  </tr>
  <tr>
    <td class="nowrap"><code>update app</code></td>
    <td>A new version of the app that you’re submitting for review to replace your existing app.</td>
  </tr>
  <tr>
    <td class="nowrap"><code>existing app</code></td>
    <td>An app that is published on Google Play.</td>
  </tr>
</table>
</div>

#### Code files

<div class="table-responsive">
<table class="full-width">
  <tr>
    <th>Variable</th>
    <th>Definition</th>
  </tr>
  <tr>
    <td class="nowrap"><code>Build.VERSION.SDK_INT</code></td>
    <td>The SDK version of the Android OS currently running on the user's device. For example, on a device running Android 11, this value will be <code>30</code> (aka <code>Build.VERSION_CODES.R</code>), even if the target and compile SDK of the app is different.</td>
  </tr>
</table>
</div>

## Footnotes

<div class="footnotes">
  <ol>
    <li id="fn:1">
      <p>Cumulative usage distribution figures were last updated on <b>December 6, 2022</b> using data from <a href="https://gs.statcounter.com/android-version-market-share/mobile-tablet/worldwide">Statcounter GlobalStats</a>. These figures may have changed significantly since the last update. You may update the figures yourself with a <a href="https://github.com/ebelinski/apilevels">pull request</a>. <a href="#fnref:1" class="reversefootnote">↩</a></p>
    </li>
    <li id="fn:2">
      <p>The codenames for Android 10 and above in the table are the internal codenames. Beginning with Android 10, Google dropped the usage of codenames publicly. <a href="#fnref:2" class="reversefootnote">↩</a></p>
    </li>
    <li id="fn:3">
      <p>In 2022, Google began imposing <a href="https://support.google.com/googleplay/android-developer/answer/11926878">minimum <code>targetSdk</code> requirements for existing apps</a>, in addition new apps and app updates. Existing apps that are not updated to meet <code>targetSdk</code> requirements by their deadlines will be <a href="https://android-developers.googleblog.com/2022/04/expanding-plays-target-level-api-requirements-to-strengthen-user-security.html">subject to restrictions</a>. This requirement excludes Wear OS apps. <a href="#fnref:3" class="reversefootnote">↩</a></p>
    </li>
    <li id="fn:4">
      <p>Android 4.4W is the first Android release for Android Wear. <a href="#fnref:4" class="reversefootnote">↩</a></p>
    </li>
  </ol>
</div>

## See also

* [Build.VERSION_CODES](https://developer.android.com/reference/android/os/Build.VERSION_CODES) official reference
* [Codenames, Tags, and Build Numbers](https://source.android.com/setup/start/build-numbers)