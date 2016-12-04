# -*- coding: utf-8 -*-

"""
checkpandas.py: comparison mechanism for pandas dataframes (and csv files)

Source repository: http://github.com/tdda/tdda

License: MIT

Copyright (c) Stochastic Solutions Limited 2016
"""

from __future__ import absolute_import
from __future__ import print_function
from __future__ import division
from __future__ import unicode_literals

import csv

try:
    import pandas as pd
except ImportError:
    pd = None


class PandasNotImplemented(object):
    """
    Null implementation of PandasComparison, used when pandas not available.
    """
    def __getattr__(self, name):
        return lambda *args, **kwargs: self.method(name, *args, **kwargs)

    def method(self, name, *args, **kwargs):
        raise NotImplementedError('%s: Pandas not available.' % name)


class PandasComparison(object):
    """
    Comparison class for pandas dataframes (and csv files).
    """

    def __new__(cls, *args, **kwargs):
        if pd is None:
            return PandasNotImplemented()
        return super(PandasComparison, cls).__new__(cls)

    def __init__(self, print_fn=None, verbose=True):
        """
        Constructor for an instance of the PandasComparison class.

        The optional print_fn parameter is a function to be used to
        display information while comparison operations are running.
        If specified, it should be a function with the same signature
        as python's builtin (__future__) print function.
        """
        self.print_fn = print_fn
        self.verbose = verbose

    def check_dataframe(self, df, ref_df, actual_path=None, expected_path=None,
                        check_data=None, check_types=None, check_order=None,
                        check_extra_cols=None, sortby=None,
                        condition=None, precision=None, msgs=None):
        """
        Compare two pandas dataframes.

        df                Actual dataframe
        ref_df            Expected dataframe
        actual_path       Path for file where actual dataframe originated,
                          used for error messages.
        expected_path     Path for file where expected dataframe originated,
                          used for error messages.
        check_types       Option to specify fields to use to compare typees.
        check_order       Option to specify fields to use to compare field
                          order.
        check_data        Option to specify fields to use to compare cell
                          values.
        check_extra_cols  Option to specify fields in the actual dataset
                          to use to check that there are no unexpected
                          extra columns.
        sortby            Option to specify fields to sort by before comparing.
        condition         Filter to be applied to datasets before comparing.
                          It can be None, or can be a function that takes
                          a dataframe as its single parameter and returns
                          a vector of booleans (to specify which rows should
                          be compared).
        precision         Number of decimal places to compare float values.
        msgs              List of strings

        Returns a tuple (failures, msgs), containing the number of failures,
        and a list of error messages.

        the comparison 'Option' flags can be of any of the following:
            - None (to apply that kind of comparison to all fields)
            - False (to skip that kind of comparison completely)
            - a list of field names
            - a function taking a dataframe as its single parameter, and
              returning a list of field names to use.
        """

        same = True
        if msgs is None:
            msgs = []

        if precision is None:
            precision = 6

        check_types = resolve_option_flag(check_types, ref_df)
        check_extra_cols = resolve_option_flag(check_extra_cols, df)

        missing_cols = []
        extra_cols = []
        wrong_types = []
        wrong_ordering = False
        for c in check_types:
            if c not in list(df):
                missing_cols.append(c)
            elif df[c].dtype != ref_df[c].dtype:
                wrong_types.append((c, df[c].dtype, ref_df[c].dtype))
        if check_extra_cols:
            extra_cols = set(check_extra_cols) - set(list(ref_df))
        if check_order != False and not missing_cols:
            check_order = resolve_option_flag(check_order, ref_df)
            c1 = [c for c in list(df) if c in check_order]
            c2 = [c for c in list(ref_df) if c in check_order]
            wrong_ordering = (list(df[c1]) != list(ref_df[c2]))
        same = not any((missing_cols, extra_cols, wrong_types, wrong_ordering))

        if not same:
            if actual_path or expected_path:
                self.info(msgs, 'Differences found: %s %s'
                                % (actual_path or '', expected_path or ''))
            self.info(msgs, 'Column check failed.')
            if missing_cols:
                self.info(msgs, 'Missing columns: %s' % missing_cols)
            if extra_cols:
                self.info(msgs, 'Extra columns: %s' % list(extra_cols))
            if wrong_types:
                for (c, dtype, ref_dtype) in wrong_types:
                    self.info(msgs,
                              'Wrong column type %s (%s, expected %s)'
                              % (c, dtype, ref_dtype))
            if wrong_ordering:
                c1 = [c for c in list(df) if c in check_types]
                c2 = [c for c in list(ref_df) if c in check_types]
                ordermsg = 'mysterious difference, they appear to be the same!'
                for i, c in enumerate(c1):
                    if i >= len(c2):
                        ordermsg = 'not enough columns'
                        break
                    elif c != c2[i]:
                        ordermsg = ('found %s, expected %s' % (c, c2[i]))
                        break
                self.info(msgs, 'Wrong column ordering: %s' % ordermsg)
        else:
            if sortby:
                sortby = resolve_option_flag(sortby, ref_df)
                df.sort_values(sortby, inplace=True)
                ref_df.sort_values(sortby, inplace=True)
            if condition:
                df = df[condition(df)].reindex()
                ref_df = ref_df[condition(ref_df)].reindex()
            same = len(df) == len(ref_df)
            if not same:
                self.info(msgs, 'Length check failed.')
                self.info(msgs, 'Found %d records, expected %d'
                                % (len(df), len(ref_df)))
            else:
                check_data = resolve_option_flag(check_data, ref_df)
                if check_data:
                    df = df[check_data]
                    ref_df = ref_df[check_data]
                    rounded = df.round(precision).reset_index(drop=True)
                    ref_rounded = ref_df.round(precision).reset_index(drop=True)
                    same = rounded.equals(ref_rounded)
                    if not same:
                        self.info(msgs, 'Contents check failed.')
                        for c in list(ref_rounded):
                            if not rounded[c].equals(ref_rounded[c]):
                                self.info(msgs, 'Column values differ: %s' % c)
        return (0 if same else 1, msgs)

    def check_csv_file(self, actual_path, expected_path, loader=None,
                       check_data=None, check_types=None, check_order=None,
                       condition=None, sortby=None, precision=6, msgs=None,
                       **kwargs):
        """
        Checks two csv files are the same, by comparing them as dataframes.

        actual_path     Pathname for actual csv file.
        expected_path   Pathname for expected csv file.
        loader          A function to use to read a csv file to obtain
                        a pandas dataframe. If None, then a default csv
                        loader is used, which takes the same parameters
                        as the standard pandas pd.read_csv() function.
        **kwargs        Any additional named parameters are passed straight
                        through to the loader function.

        The other parameters are the same as those used by check_dataframe,
        Returns a tuple (failures, msgs), containing the number of failures,
        and a list of error messages.
        """

        ref_df = self.load_csv(expected_path, loader=loader, **kwargs)
        df = self.load_csv(actual_path, loader=loader, **kwargs)
        return self.check_dataframe(df, ref_df,
                                    actual_path=actual_path,
                                    expected_path=expected_path,
                                    check_data=check_data,
                                    check_types=check_types,
                                    check_order=check_order,
                                    condition=condition, sortby=sortby,
                                    precision=precision,
                                    msgs=msgs)

    def check_csv_files(self, actual_paths, expected_paths,
                        check_data=None, check_types=None, check_order=None,
                        condition=None, sortby=None, msgs=None, **kwargs):
        """
        Wrapper around the check_csv_file() method, used to compare
        collections of actual and expected csv files.

        actual_paths    List of pathnames for actual csv file.
        expected_paths  List of pathnames for expected csv file.
        loader          A function to use to read a csv file to obtain
                        a pandas dataframe. If None, then a default csv
                        loader is used, which takes the same parameters
                        as the standard pandas pd.read_csv() function.
        **kwargs        Any additional named parameters are passed straight
                        through to the loader function.

        The other parameters are the same as those used by check_dataframe.
        Returns a tuple (failures, msgs), containing the number of failures,
        and a list of error messages.

        Returns a tuple (failures, msgs), containing the number of failures,
        and a list of error messages.

        Note that this function compares ALL of the pairs of actual/expected
        files, and if there are any differences, then the number of failures
        returned reflects the total number of differences found across all
        of the files, and the msgs returned contains the error messages
        accumulated across all of those comparisons. In other words, it
        doesn't stop as soon as it hits the first error, it continues through
        right to the end.
        """
        failures = 0
        for (actual_path, expected_path) in zip(actual_paths, expected_paths):
            try:
                r = self.check_csv_file(actual_path, expected_path,
                                        check_data=check_data,
                                        check_types=check_types,
                                        check_order=check_order,
                                        sortby=sortby,
                                        condition=condition, msgs=msgs,
                                        **kwargs)
                (n, msgs) = r
                failures += n
            except Exception as e:
                self.info(msgs, 'Error comparing %s and %s (%s %s)'
                                % (actual_path, expected_path,
                                   e.__class__.__name__, str(e)))
                failures += 1
        return (failures, msgs)

    def info(self, msgs, s):
        """
        Add an item to the list of messages, and also display it immediately
        if verbose is set.
        """
        msgs.append(s)
        if self.verbose and self.print_fn:
            self.print_fn(s)

    def load_csv(self, csvfile, loader=None, **kwargs):
        """
        Function for constructing a pandas dataframe from a csv file.
        """
        if loader is None:
            loader = default_csv_loader
        return loader(csvfile, **kwargs)


def default_csv_loader(csvfile, **kwargs):
    """
    Default function for reading a csv file.

    Wrapper around the standard pandas pd.read_csv() function, but with
    slightly different defaults:

    index_col             is None
    infer_datetime_format is True
    quotechar             is ""
    quoting               is csv.QUOTE_MINIMAL
    escapechar            is \
    na_values             are the empty string, NaN, and NULL
    keep_default_na       is False
    """
    options = {
        'index_col': None,
        'infer_datetime_format': True,
        'quotechar': '"',
        'quoting': csv.QUOTE_MINIMAL,
        'escapechar': '\\',
        'na_values': ['', 'NaN', 'NULL'],
        'keep_default_na': False,
    }
    options.update(kwargs)
    return pd.read_csv(csvfile, **options)


def resolve_option_flag(flag, df):
    """
    Method to resolve an option flag, which may be any of:
       - None or True:     use all columns in the dataframe
       - None:             use no columns 
       - list of columns   use these columns
       - function returning a list of columns
    """
    if flag is None or flag is True:
        return list(df)
    elif flag is False:
        return []
    elif hasattr(flag, '__call__'):
         return flag(df)
    else:
        return flag

