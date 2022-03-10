---
layout: default
---
{::options parse_block_html="true" /}

This is an overview of all Android versions and their corresponding identifiers for Android developers. Anyone is welcome to open [an issue or pull request](https://github.com/ebelinski/apilevels). Happy developing!

<div id="compact-toc">
* TOC
{:toc}
</div>

<table class="full-width">
  <tr>
    <th colspan="2">
      Version
    </th>
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
    <td colspan="2">
      <b><a href="https://developer.android.com/about/versions/13">Android 13</a></b> <sup class="beta">DEV</sup>
    </td>
    <td>Level 33</td>
    <td><code>T</code></td>
    <td>
      Tiramisu
      <sup id="fnref:2"><a href="#fn:2" class="footnote">2</a></sup>
    </td>
    <td rowspan="2"><i>No data</i></td>
    <td rowspan="2"><i>TBA</i></td>
  </tr>

  <tr>
    <td rowspan="2">
      <b><a href="https://developer.android.com/about/versions/12">Android 12</a></b>
    </td>
    <td>
      12L <sup class="beta">BETA</sup>
    </td>
    <td>Level 32</td>
    <td><code>S_V2</code></td>
    <td rowspan="2">
      Snow Cone
      <sup id="fnref:2"><a href="#fn:2" class="footnote">2</a></sup>
    </td>
  </tr>
  
  <tr>
    <td>12</td>
    <td>Level 31</td>
    <td><code>S</code></td>
    {% include progress-cell.html percentage=7.3 %}
    <td>2021</td>
  </tr>

  <tr>
    <td rowspan="2" colspan="2">
      <b><a href="https://developer.android.com/about/versions/11">Android 11</a></b>
    </td>
    <td>Level 30</td>
    <td><code>R</code></td>
    <td>
      Red Velvet Cake
      <sup id="fnref:2"><a href="#fn:2" class="footnote">2</a></sup>
    </td>
    {% include progress-cell.html percentage=44.3 %}
    <td rowspan="2">2020</td>
  </tr>
  <tr class="table-notes"><td colspan="4">
    <ul>
      <li><code>targetSdk</code> <a href="https://developer.android.com/distribute/play-policies">must be 30+</a> for new apps and app updates.</li>
    </ul>
  </td></tr>

  <tr>
    <td colspan="2">
      <b><a href="https://developer.android.com/about/versions/10">Android 10</a></b>
    </td>
    <td>Level 29</td>
    <td><code>Q</code></td>
    <td>
      Quince Tart
      <sup id="fnref:2"><a href="#fn:2" class="footnote">2</a></sup>
    </td>
    {% include progress-cell.html percentage=68.4 %}
    <td>2019</td>
  </tr>

  <tr>
    <td colspan="2">
      <b><a href="https://developer.android.com/about/versions/pie">Android 9</a></b>
    </td>
    <td>Level 28</td>
    <td><code>P</code></td>
    <td>Pie</td>
    {% include progress-cell.html percentage=80.4 %}
    <td>2018</td>
  </tr>

  <tr>
    <td rowspan="2">
      <b><a href="https://developer.android.com/about/versions/oreo">Android 8</a></b>
    </td>
    <td>8.1</td>
    <td>Level 27</td>
    <td><code>O_MR1</code></td>
    <td rowspan="2">Oreo</td>
    {% include progress-cell.html percentage=86.7 %}
    <td rowspan="2">2017</td>
  </tr>
  <tr>
    <td>8.0</td>
    <td>Level 26</td>
    <td><code>O</code></td>
    {% include progress-cell.html percentage=89.4 %}
  </tr>

  <tr>
    <td rowspan="2">
      <b><a href="https://developer.android.com/about/versions/nougat">Android 7</a></b>
    </td>
    <td>7.1</td>
    <td>Level 25</td>
    <td><code>N_MR1</code></td>
    <td rowspan="2">Nougat</td>
    {% include progress-cell.html percentage=91.1 %}
    <td rowspan="2">2016</td>
  </tr>
  <tr>
    <td>7.0</td>
    <td>Level 24</td>
    <td><code>N</code></td>
    {% include progress-cell.html percentage=93.8 %}
  </tr>

  <tr>
    <td colspan="2">
      <b><a href="https://developer.android.com/about/versions/marshmallow">Android 6</a></b>
    </td>
    <td>Level 23</td>
    <td><code>M</code></td>
    <td>Marshmallow</td>
    {% include progress-cell.html percentage=96.6 %}
    <td>2015</td>
  </tr>

  <tr>
    <td rowspan="3">
      <b><a href="https://developer.android.com/about/versions/lollipop">Android 5</a></b>
    </td>
    <td>5.1</td>
    <td>Level 22</td>
    <td><code>LOLLIPOP_MR1</code></td>
    <td rowspan="2">Lollipop</td>
    {% include progress-cell.html percentage=98.4 %}
    <td>2015</td>
  </tr>
  <tr>
    <td rowspan="2">5.0</td>
    <td>Level 21</td>
    <td><code>LOLLIPOP</code>, <code>L</code></td>
    <td rowspan="23"><i>No data</i></td>
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
      4.4W <sup id="fnref:3"><a href="#fn:3" class="footnote">3</a></sup>
    </td>
    <td>Level 20</td>
    <td><code>KITKAT_WATCH</code></td>
    <td rowspan="2">KitKat</td>
  </tr>
  <tr>
    <td rowspan="2">4.4</td>
    <td>Level 19</td>
    <td><code>KITKAT</code></td>
    <td rowspan="3">2013</td>
  </tr>
  <tr class="table-notes"><td colspan="3">
    <ul>
      <li>Google Play services <a href="https://android-developers.googleblog.com/2021/07/google-play-services-discontinuing-jelly-bean.html">do not support Android versions</a> below API level 19.</li>
    </ul>
  </td></tr>
  <tr>
    <td>4.3</td>
    <td>Level 18</td>
    <td><code>JELLYBEAN_MR2</code></td>
    <td rowspan="3">Jelly Bean</td>
  </tr>
  <tr>
    <td>4.2</td>
    <td>Level 17</td>
    <td><code>JELLYBEAN_MR1</code></td>
    <td rowspan="2">2012</td>
  </tr>
  <tr>
    <td>4.1</td>
    <td>Level 16</td>
    <td><code>JELLYBEAN</code></td>
  </tr>
  <tr>
    <td>4.0.3 – 4.0.4</td>
    <td>Level 15</td>
    <td><code>ICE_CREAM_SANDWICH_MR1</code></td>
    <td rowspan="2">Ice Cream Sandwich</td>
    <td rowspan="7">2011</td>
  </tr>
  <tr>
    <td rowspan="2">4.0.1 – 4.0.2</td>
    <td>Level 14</td>
    <td><code>ICE_CREAM_SANDWICH</code></td>
  </tr>
  <tr class="table-notes"><td colspan="3">
    <ul>
      <li><a href="https://developer.android.com/jetpack">Jetpack</a>/<a href="https://developer.android.com/jetpack/androidx">AndroidX</a> libraries <a href="https://developer.android.com/topic/libraries/support-library#api-versions">require</a> a <code>minSdk</code> of 14 or higher.</li>
    </ul>
  </td></tr>

  <tr>
    <td rowspan="3"><b>Android 3</b></td>
    <td>3.2</td>
    <td>Level 13</td>
    <td><code>HONEYCOMB_MR2</code></td>
    <td rowspan="3">Honeycomb</td>
  </tr>
  <tr>
    <td>3.1</td>
    <td>Level 12</td>
    <td><code>HONEYCOMB_MR1</code></td>
  </tr>
  <tr>
    <td>3.0</td>
    <td>Level 11</td>
    <td><code>HONEYCOMB</code></td>
  </tr>

  <tr>
    <td rowspan="6"><b>Android 2</b></td>
    <td>2.3.3 – 2.3.7</td>
    <td>Level 10</td>
    <td><code>GINGERBREAD_MR1</code></td>
    <td rowspan="2">Gingerbread</td>
  </tr>
  <tr>
    <td>2.3.0 – 2.3.2</td>
    <td>Level 9</td>
    <td><code>GINGERBREAD</code></td>
    <td rowspan="3">2010</td>
  </tr>
  <tr>
    <td>2.2</td>
    <td>Level 8</td>
    <td><code>FROYO</code></td>
    <td>Froyo</td>
  </tr>
  <tr>
    <td>2.1</td>
    <td>Level 7</td>
    <td><code>ECLAIR_MR1</code></td>
    <td rowspan="3">Eclair</td>
  </tr>
  <tr>
    <td>2.0.1</td>
    <td>Level 6</td>
    <td><code>ECLAIR_0_1</code></td>
    <td rowspan="5">2009</td>
  </tr>
  <tr>
    <td>2.0</td>
    <td>Level 5</td>
    <td><code>ECLAIR</code></td>
  </tr>

  <tr>
    <td rowspan="4"><b>Android 1</b></td>
    <td>1.6</td>
    <td>Level 4</td>
    <td><code>DONUT</code></td>
    <td>Donut</td>
  </tr>
  <tr>
    <td>1.5</td>
    <td>Level 3</td>
    <td><code>CUPCAKE</code></td>
    <td>Cupcake</td>
  </tr>
  <tr>
    <td>1.1</td>
    <td>Level 2</td>
    <td><code>BASE_1_1</code></td>
    <td>Petit Four</td>
  </tr>
  <tr>
    <td>1.0</td>
    <td>Level 1</td>
    <td><code>BASE</code></td>
    <td><i>None</i></td>
    <td>2008</td>
  </tr>
</table>

## Definitions

#### Gradle files

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

#### Code files

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

## Footnotes

<div class="footnotes">
  <ol>
    <li id="fn:1">
      <p>Cumulative usage distribution figures were last updated on <b>March 2, 2022</b> using data from <a href="https://gs.statcounter.com/android-version-market-share/mobile-tablet/worldwide">Statcounter GlobalStats</a>. These figures may have changed significantly since the last update. You may update the figures yourself with a <a href="https://github.com/ebelinski/apilevels">pull request</a>. <a href="#fnref:1" class="reversefootnote">↩</a></p>
    </li>
    <li id="fn:2">
      <p>The codenames for Android 10 and above in the table are the internal codenames. Beginning with Android 10, Google dropped the usage of codenames publicly.</p>
    </li>
    <li id="fn:3">
      <p>Android 4.4W is the first Android release for Android Wear. <a href="#fnref:3" class="reversefootnote">↩</a></p>
    </li>
  </ol>
</div>

## See also

* [Build.VERSION_CODES](https://developer.android.com/reference/android/os/Build.VERSION_CODES) official reference
* [Codenames, Tags, and Build Numbers](https://source.android.com/setup/start/build-numbers)
