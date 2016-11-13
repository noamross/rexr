.onLoad <- function(libname, pkgname) {
  path <- system.file("", package="rtdda")
  SnakeCharmR::py.exec("import sys")
  SnakeCharmR::py.exec(paste0("sys.path.append('", path, "')"))
  SnakeCharmR::py.exec("from tdda import rexpy")
}

#' Automatic discovery of regular-expression constraints
#' @param strings a character vector of value for which a matching regular
#'   expression is wanted
#' @examples
#'   rex_extract(c("EH1", "7JQ", "WC1", "4AA", "G2", "3PQ"))
#'   rex_extract(c("123-AA-971", "12-DQ-802", "198-AA-045", "1-BA-834"))
#' @export
#' @importFrom SnakeCharmR py.call
rex_extract <- function(strings) {
  py.call("rexpy.extract", strings)
}


