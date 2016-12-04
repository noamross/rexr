
<!-- README.md is generated from README.Rmd. Please edit that file -->
rexr
====

[![Project Status: WIP - Initial development is in progress, but there has not yet been a stable, usable release suitable for the public.](http://www.repostatus.org/badges/latest/wip.svg)](http://www.repostatus.org/#wip) [![MIT Licensed - Copyright 2016 EcoHealth Alliance](https://img.shields.io/badge/license-MIT-blue.svg)](https://badges.mit-license.org/) [![Travis-CI Build Status](https://travis-ci.org/noamross/rexr.svg?branch=master)](https://travis-ci.org/noamross/rexr) [![AppVeyor Build Status](https://ci.appveyor.com/api/projects/status/github/noamross/rexr?branch=master&svg=true)](https://ci.appveyor.com/project/noamross/rexr) [![codecov](https://codecov.io/gh/noamross/rexr/branch/master/graph/badge.svg)](https://codecov.io/gh/noamross/rexr)

This package wraps the [rexpy python module](https://github.com/tdda/tdda/tree/master/rexpy), part of the TDDA module, which generates automatic *constraints* on data sets given examples. More info can be found on [the TDDA blog](http://www.tdda.info/introducing-rexpy-automatic-discovery-of-regular-expressions).

This is an extremely alpha package wrapping some pretty beta code, so use with caution! It does not currently work on Windows.

Installation
------------

You can install rexr from github with:

``` r
# install.packages("devtools")
devtools::install_github("noamross/rexr")
```

Since rexr calls python code via the [**SnakeCharmR**](https://github.com/asieira/SnakeCharmR) package, you need Python &gt;= 2.7 and a build environment to install it.

Usage
-----

`rex_extract()` generates regular expressions that match a character vector. The RexPy library attempts to create a minimal set of regexes that narrowly capture all the values.

``` r
library(rexr)
rex_extract(c("EH1", "7JQ", "WC1", "4AA", "G2", "3PQ"))
#> [1] "^[A-Za-z0-9]{2,3}$"
rex_extract(c("123-AA-971", "12-DQ-802", "198-AA-045", "1-BA-834"))
#> [1] "^\\d{1,3}\\-[A-Z]{2}\\-\\d{3}$"
```
