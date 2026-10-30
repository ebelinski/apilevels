# API Levels

Hello! This is the source code for [Android API Levels](https://apilevels.com), a microsite that displays Android versions and their corresponding identifiers for Android developers. It is built with [Jekyll](https://jekyllrb.com/) and deployed on [GitHub Pages](https://pages.github.com/). Changes merged into the `main` branch are automatically deployed.

## Getting started

To make contributions, you can submit pull requests with changes to the relevant files. If you would like to build the website locally, follow these instructions:

1. Install the [correct version](/.ruby-version) of Ruby, ideally using a tool such as [rbenv](https://github.com/rbenv/rbenv).
2. Install the project Ruby dependencies: `bundle install`.
3. Start the local Jekyll server: `bundle exec jekyll serve`.

The website should now be visible in a browser at http://127.0.0.1:4000/.

## Updating usage figures

The cumulative usage figures come from [Statcounter GlobalStats](https://gs.statcounter.com/android-version-market-share/mobile-tablet/worldwide). To download the previous month's figures and write them into `index.md`, run:

```
python3 usage_reporter.py update
```

Run it without `update` to only print the figures.

## Contributing

You may open [issues](https://github.com/ebelinski/apilevels/issues) for suggestions and [pull request](https://github.com/ebelinski/apilevels/pulls) for proposed changes. All contributors must follow the [code of conduct](/CODE_OF_CONDUCT.md). Any contributions you make must follow the [license](#license).

All of the website content is in the [index.md](/index.md), which has a mix of HTML and Markdown code. It's a bit messy, but it works!

## License

This repository is licenced under the [MIT License](/LICENSE).
