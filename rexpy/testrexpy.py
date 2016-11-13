# -*- coding: utf-8 -*-

"""
URLs1

 http\:\/\/[a-z]{3,4}\.[a-z]{3,4}
 http\:\/\/[a-z]{5,19}\.com\/
 [a-z]{4,5}\:\/\/[a-z]{3}\.[a-z]{6,19}\.com
 http\:\/\/www\.[a-z]{6,19}\.com\/
 http\:\/\/www\.[a-z]{6,19}\.co\.uk\/

** With s replacing space and backslashes removed, spaced in groups:

 111111111   222  33333333333  4  5555555555   6  777  8  99  10
 http        ://  [a-z]{3,4}   .  [a-z]{3,4}
 http        ://  [a-z]{5,19}  .  com          /
 [a-z]{4,5}  ://  [a-z]{3}     .  [a-z]{6,19}  .  com
 http        ://  www          .  [a-z]{6,19}  .  com  /
 http        ://  www          .  [a-z]{6,19}  .  co   .  uk  /

--> :// is very special in col 2

 111111111   222  33333333333  4  5555555555   6  777  8  99  10
 http        ://  [a-z]{3,4}   .  [a-z]{3,4}
 http        ://  [a-z]{5,19}  .  com          /
 [a-z]{4,5}  ://  [a-z]{3}     .  [a-z]{6,19}  .  com
 http        ://  www          .  [a-z]{6,19}  .  com  /
 http        ://  www          .  [a-z]{6,19}  .  co   .  uk  /

--> /, when present is always last in RH group

 111111111   222  33333333333  4  5555555555   6  777  8  99  10
 http        ://  [a-z]{3,4}   .  [a-z]{3,4}
 http        ://  [a-z]{5,19}  .  com                         /
 [a-z]{4,5}  ://  [a-z]{3}     .  [a-z]{6,19}  .  com
 http        ://  www          .  [a-z]{6,19}  .  com         /
 http        ://  www          .  [a-z]{6,19}  .  co   .  uk  /



Goal:

 111111111   222  33333333333  4  5555555555   6  777  8  99  10
 http        ://  [a-z]{3,4}   .  [a-z]{3,4}
 http        ://  [a-z]{5,19}  .  com                         /
 [a-z]{4,5}  ://  [a-z]{3}     .  [a-z]{6,19}  .  com
 http        ://  www          .  [a-z]{6,19}  .  com         /
 http        ://  www          .  [a-z]{6,19}  .  co   .  uk  /

URLs 1 + 2:

 [a-z]{3,4}\.[a-z]{2,4}
 [a-z]{5,19}\.com\/
 [a-z]{3,4}[\.\/\:]{1,3}[a-z]{3,19}\.[a-z]{3,4}
 http\:\/\/[a-z]{5,19}\.com\/
 [a-z]{4,5}\:\/\/[a-z]{3}\.[a-z]{6,19}\.com
 http\:\/\/www\.[a-z]{6,19}\.com\/
 http\:\/\/www\.[a-z]{6,19}\.co\.uk\/

** With s replacing space and backslashes removed, spaced in groups:

 11111111111  2222222222  33333333333  4  55555555555  6  777  8  99  10
 [a-z]{3,4}   .           [a-z]{2,4}
 [a-z]{5,19}  .           com          /
 [a-z]{3,4}   [./:]{1,3}  [a-z]{3,19}  .  [a-z]{3,4}
 http         ://         [a-z]{5,19}  .  com          /
 [a-z]{4,5}   ://         [a-z]{3}     .  [a-z]{6,19}  .  com
 http         ://         www          .  [a-z]{6,19}  .  com  /
 http         ://         www          .  [a-z]{6,19}  .  co   .  uk  /

Goal:

 11111111111  2222222222  33333333333  4  55555555555  6  777  8  99  10
                          [a-z]{3,4}   .  [a-z]{2,4}
                          [a-z]{5,19}  .  com                         /
 [a-z]{3,4}   [./:]{1,3}  [a-z]{3,19}  .  [a-z]{3,4}
 http         ://         [a-z]{5,19}  .  com                         /
 [a-z]{4,5}   ://         [a-z]{3}     .  [a-z]{6,19}  .  com
 http         ://         www          .  [a-z]{6,19}  .  com         /
 http         ://         www          .  [a-z]{6,19}  .  co   .  uk  /



TELEPHONES 2

 \(\d{3,4}\)\ \d{3,4}\ \d{4}
 \+\d{1,2}\ \d{2,3}\ \d{3,4}\ \d{4}

** With s replacing space and backslashes removed, spaced in groups:

 1  2222222  3  4444444  5555555   666666  77777  8888
 (  d{3,4}   )  s        d{3,4}    s       d{4}
 +  d{1,2}   s  d{2,3}   s         d{3,4}  s      d{4}

-->  Space at pos -2

 1  2222222  3  4444444  5555555   666666  77777  8888
 (  d{3,4}   )  s        d{3,4}            s      d{4}
 +  d{1,2}   s  d{2,3}   s         d{3,4}  s      d{4}

-->  Space at pos -2 within left group

 1  2222222  3  4444444  5555555   666666  77777  8888
 (  d{3,4}   )           s         d{3,4}  s      d{4}
 +  d{1,2}   s  d{2,3}   s         d{3,4}  s      d{4}



Goal

 1  2222222  3  4444444  5555555   666666  77777  8  9999
 (  d{3,4}   )  s        d{3,4}    s       d{4}
 +  d{1,2}      s        d{2,3}    s       d{3,4} s  d{4}





TELEPHONES 5

 \d{3}\ \d{3}\ \d{4}
 \d{3}\-\d{3}\-\d{4}
 1\ \d{3}\ \d{3}\ \d{4}
 \(\d{3}\)\ \d{3}\ \d{4}

** With s replacing space and backslashes removed, spaced in groups:

 1111  2222  3333  4  5555  6  7777
 d{3}  s     d{3}  s  d{4}
 d{3}  -     d{3}  -  d{4}
 1     s     d{3}  s  d{3}  s  d{4}
 (     d{3}  )     s  d{3}  s  d{4}

--> Last group is always 4 digits

 1111  2222  3333  4  5555  6  7777
 d{3}  s     d{3}  s           d{4}
 d{3}  -     d{3}  -           d{4}
 1     s     d{3}  s  d{3}  s  d{4}
 (     d{3}  )     s  d{3}  s  d{4}

--> Group -2 with left part is always 3 digits

 1111  2222  3333  4  5555  6  7777
 d{3}  s              d{3}  s  d{4}
 d{3}  -              d{3}  -  d{4}
 1     s     d{3}  s  d{3}  s  d{4}
 (     d{3}  )     s  d{3}  s  d{4}

--> Last of left of left is always space or hyphen

 1111  2222  3333  4  5555  6  7777
 d{3}              s  d{3}  s  d{4}
 d{3}              -  d{3}  -  d{4}
 1     s     d{3}  s  d{3}  s  d{4}
 (     d{3}  )     s  d{3}  s  d{4}

--> Within left three, there is always a block of 3 digits

 1  2  3333  4  5  6666  7  8888
       d{3}     s  d{3}  s  d{4}
       d{3}     -  d{3}  -  d{4}
 1  s  d{3}     s  d{3}  s  d{4}
 (     d{3}  )  s  d{3}  s  d{4}


Goal:

 1  2222  3  4444  5  6666  7  8888
             d{3}  s  d{3}  s  d{4}
             d{3}  -  d{3}  -  d{4}
    1     s  d{3}  s  d{3}  s  d{4}
 (  d{3}  )        s  d{3}  s  d{4}



TELS 1-5

 \d{3}\ \d{3}\ \d{4}
 \d{3,4}[\-\.]\d{3}[\-\.]\d{4}
 1\ \d{3}\ \d{3}\ \d{4}
 \(\d{3,4}\)\ \d{3,4}\ \d{4}
 \+\d{1,2}\ \d{2,3}\ \d{3,4}\ \d{4}


** With s replacing space and backslashes removed, spaced in groups:

 111111  222222  3333  444444  555555  666666  7777  8888
 d{3}    s       d{3}  s       d{4}
 d{3,4}  [-.]    d{3}  [-.]    d{4}
 1       s       d{3}  s       d{3}    s       d{4}
 (       d{3,4}  )     s       d{3,4}  s       d{4}
 +       d{1,2}  s     d{2,3}  s       d{3,4}  s     d{4}


Goal:

 1  222222  3333  444444  555555  6666  777777  8  9999
    d{3}          s       d{3}    s     d{4}
    d{3,4}  [-.]          d{3}    [-.]  d{4}
    1             s       d{3}    s     d{3}    s  d{4}
 (  d{3,4}  )     s       d{3,4}  s     d{4}
 +  d{1,2}        s       d{2,3}  s     d{3,4}  s  d{4}
"""

from __future__ import division
from __future__ import print_function
from __future__ import absolute_import
from __future__ import unicode_literals

import os
import re
import sys
import unittest

try:
    import pandas
except:
    pandas = None
pd = pandas

#from artists.miro.writabletestcase import WritableTestCase
from tdda.rexpy import *


class TestUtilityFunctions(unittest.TestCase):
    def test_signature(self):
        self.assertEqual(signature([]), '')

        self.assertEqual(signature([('c', 1)]), 'c')

        self.assertEqual(signature([('C', 3), ('.', 1),
                                    ('C', 2), ('.', 1),
                                    ('C', 2)]), 'C.C.C')

        self.assertEqual(signature([('C', 8), ('.', 1),
                                    ('C', 4), ('.', 1),
                                    ('C', 4), ('.', 1),
                                    ('C', 4), ('.', 1),
                                    ('C', 12)]), 'C.C.C.C.C')

        self.assertEqual(signature([('.', 1),
                                    ('C', 4), ('.', 1), (' ', 1),
                                    ('C', 3), (' ', 1),
                                    ('C', 4)]), '.C. C C')

        self.assertEqual(signature([('C', 4), ('.', 1),
                                    ('C', 2), ('.', 1),
                                    ('C', 5), ('.', 1),
                                    ('C', 2), ('.', 1,),
                                    ('C', 2), (' ', 1), ('.', 1),
                                    ('C', 5)]), 'C.C.C.C.C .C')

        self.assertEqual(signature([('C', 4), ('.', 1),
                                    ('C', 2), ('.', 1),
                                    ('C', 5), ('.', 1),
                                    ('C', 2), ('.', 1),
                                    ('C', 2), ('*', 1), ('.', 1),
                                    ('C', 5)]), 'C.C.C.C.C*.C')


    def test_get_omnipresent_at_pos(self):
        c = {
            ('a', 1, 1, 'fixed'): {1: 7, -1: 7, 3: 4},
            ('b', 1, 1, 'fixed'): {2: 6, 3: 4},
            ('c', 1, 1): {3: 1, 4: 2, 2: 7},
            ('d', 1, 1, 'fixed'): {1: 1}
        }

        self.assertEqual(get_omnipresent_at_pos(c, 7),
                         [((u'a', 1, 1, u'fixed'), -1),
                          ((u'a', 1, 1, u'fixed'), 1),
                          ((u'c', 1, 1), 2)])

        self.assertEqual(get_omnipresent_at_pos(c, 6),
                         [((u'b', 1, 1, u'fixed'), 2)])


        self.assertEqual(get_omnipresent_at_pos(c, 5), [])

        self.assertEqual(get_omnipresent_at_pos({}, 1), [])

        self.assertEqual(get_omnipresent_at_pos({}, 0), [])

    def test_length_stats(self):
        # Testing with strings, but works with lists etc. too
        self.assertEqual(length_stats(['abc', 'def', 'ghi']), (True, 3))
        self.assertEqual(length_stats(['a', 'def', 'gh']), (False, 3))
        self.assertEqual(length_stats([]), (True, 0))

    def test_left_parts1(self):
        # For this test, the fragments are always present in the positions
        p1 = [('a',), ('b',), ('c',), ('d',), ('e',), ('f',)]
        p2 = [('A',), ('b',), ('C',), ('d',), ('E',)]
        p3 = [('.',), ('b',), ('.',), ('d',)]
        fixed = [(('b',), 1), (('d',),  3)]
        expected = [
            [[('a',)],          [('A',)],  [('.',)]],
            [[('b',)],          [('b',)],  [('b',)]],
            [[('c',)],          [('C',)],  [('.',)]],
            [[('d',)],          [('d',)],  [('d',)]],
            [[('e',), ('f',)],  [('E',)],  []]
        ]
        self.assertEqual(left_parts([p1, p2, p3], fixed), expected)

    def test_left_parts2(self):
        # For this test, the fragments are always present in the positions
        p1 = [('a',), ('b',), ('c',), ('d',), ('e',), ('f',)]
        p2 = [('a',), ('B',), ('C',), ('d',), ('E',)]
        p3 = [('a',), ('b',), ('c',), ('d',)]
        fixed = [(('a',), 0), (('c',),  3)]
        expected = [
            [[('a',)],           [('a',)],          [('a',)]],
            [[('b',), ('c',)],   [('B',), ('C',)],  [('b',), ('c',)]],
            [[('d',)],           [('d',)],          [('d',)]],
            [[('e',), ('f',)],   [('E',)],          []]
        ]
        self.assertEqual(left_parts([p1, p2, p3], fixed), expected)

    def test_right_parts1(self):
        p1 = [('F',), ('e',), ('d',), ('c',), ('b',), ('a',)]
        p2 = [('E',), ('d',), ('C',), ('b',), ('A',)]
        p3 = [('d',), ('.',), ('b',), ('.',)]
        fixed = [(('b',), 2), (('d',),  4)]
        expected = [
            [[('F',), ('e',)],  [('E',)],  []],
            [[('d',)],          [('d',)],  [('d',)]],
            [[('c',)],          [('C',)],  [('.',)]],
            [[('b',)],          [('b',)],  [('b',)]],
            [[('a',)],          [('A',)],  [('.',)]],
        ]
        self.assertEqual(right_parts([p1, p2, p3], fixed), expected)

    def test_right_parts2(self):
        p1 = [('F',), ('e',), ('d',), ('c',), ('b',), ('a',)]
        p2 = [('E',), ('d',), ('C',), ('b',), ('a',)]
        p3 = [('d',), ('.',), ('.',), ('a',)]
        fixed = [(('a',), 1), (('d',),  4)]
        expected = [
            [[('F',), ('e',)],  [('E',)],  []],
            [[('d',)],          [('d',)],  [('d',)]],
            [[('c',), ('b',)],  [('C',), ('b',)],  [('.',), ('.',)]],
            [[('a',)],          [('a',)],  [('a',)]],
        ]
        self.assertEqual(right_parts([p1, p2, p3], fixed), expected)

    def test_ndigits(self):
        self.assertEqual(ndigits(1, 1), '1')
        self.assertEqual(ndigits(2, 1), '1' * 2)
        self.assertEqual(ndigits(1, 2), '2')
        self.assertEqual(ndigits(2, 2), '2' * 2)
        self.assertEqual(ndigits(0, 2), '')
        self.assertEqual(ndigits(11, 9), '9' * 11)
        self.assertEqual(ndigits(9, 11), 'B' * 9)
        self.assertEqual(ndigits(9, 10), 'A' * 9)
        self.assertEqual(ndigits(10,9), '9' * 10)
        self.assertEqual(ndigits(10,10), 'A' * 10)
        self.assertEqual(ndigits(5,35), 'Z' * 5)
        # Not really designed for more than 35 parts.
        # But if it happens, just carries on
        self.assertEqual(ndigits(5, 36), chr(ord('Z') + 1) * 5)
        # Also not supposed to take digits below 1.
        # but...
        self.assertEqual(ndigits(4, 0), '0' * 4)

    def test_aligned_parts1(self):
        part1 = [
                    [('a', 1, 1, 'fixed'), ('b', 1, 1, 'fixed')],
                    [('c', 1, 1, 'fixed')],
                ]
        part2 = [
                    [('/', 1, 1, 'fixed')],
                    [('/', 1, 1, 'fixed')],
                ]
        parts = [part1, part2]
        expected = '\n'.join(['|1 2|3|',
                              ' a b /',
                              ' c   /'])
        self.assertEqual(aligned_parts(parts), expected)

    def test_aligned_parts2(self):
        part1 = [
                    [('a', 1, 1, 'fixed'), ('b', 1, 1, 'fixed')],
                    [('c', 1, 1, 'fixed')],
                ]
        part2 = [
                    [],
                    [('/', 1, 1, 'fixed')],
                ]
        part3 = [
                    [('.', 1, 1, 'fixed')],
                    [],
                ]
        part4 = [
                    [('!', 1, 1, 'fixed')],
                    [('!', 1, 1, 'fixed')],
                ]
        parts = [part1, part2, part3, part4]
        expected = '\n'.join(['|1 2|3|4|5|',
                              ' a b   . !',
                              ' c   /   !'])
        self.assertEqual(aligned_parts(parts), expected)



class TestHelperMethods(unittest.TestCase):

    def test_coarse_character_classification(self):
        for i in range(ord('A'), ord('Z') + 1):
            self.assertEqual(coarse_classify_char(chr(i)), 'C')
        for i in range(ord('a'), ord('z') + 1):
            self.assertEqual(coarse_classify_char(chr(i)), 'C')
        for i in range(ord('0'), ord('9') + 1):
            self.assertEqual(coarse_classify_char(chr(i)), 'C')
        for c in ' \t\r\n\f\v':
            self.assertEqual(coarse_classify_char(c), ' ')
        for c in '!"#$%&' + "'" + '()*+,-.' + '\\' + ':;<=>?@[\]^_`{|}~':
            self.assertEqual(coarse_classify_char(c), '.')
        for i in range(0, 0x1c):  # 1C to 1F are considered whitespace
                                  # in unicode
            c = chr(i)
            if not c in '\t\r\n\f\v':
                self.assertEqual(coarse_classify_char(c), '*')

    def test_coarse_string_classification(self):
        for i in range(ord('A'), ord('Z') + 1):
            self.assertEqual(coarse_classify_char(chr(i)), 'C')
        for i in range(ord('a'), ord('z') + 1):
            self.assertEqual(coarse_classify_char(chr(i)), 'C')
        for i in range(ord('0'), ord('9') + 1):
            self.assertEqual(coarse_classify_char(chr(i)), 'C')
        for c in ' \t\r\n\f\v':
            self.assertEqual(coarse_classify_char(c), ' ')
        for c in ' \t\r\n\f\v':
            self.assertEqual(coarse_classify_char(c), ' ')
        for c in '!"#$%&' + "'" + '()*+,-.' + '\\' + ':;<=>?@[\]^_`{|}~':
            self.assertEqual(coarse_classify_char(c), '.')
        for i in range(0, 0x1c):  # 1C to 1F are considered whitespace
                                  # in unicode
            c = chr(i)
            if not c in '\t\r\n\f\v':
                self.assertEqual(coarse_classify_char(c), '*')
        self.assertEqual(coarse_classify_char(chr(127)), '*')

    def test_coarse_classification(self):
        self.assertEqual(coarse_classify('255-SI-32'),
                                         'CCC.CC.CC')
        guid = '1f65c9e8-cf9a-4e53-b7d0-c48a26a21b7c'
        sig  = 'CCCCCCCC.CCCC.CCCC.CCCC.CCCCCCCCCCCC'
        self.assertEqual(coarse_classify(guid), sig)
        self.assertEqual(coarse_classify('(0131) 123 4567'),
                                         '.CCCC. CCC CCCC')
        self.assertEqual(coarse_classify('2016-01-02T10:11:12 +0300z'),
                                         'CCCC.CC.CCCCC.CC.CC .CCCCC')
        self.assertEqual(coarse_classify('2016-01-02T10:11:12\a+0300z'),
                                         'CCCC.CC.CCCCC.CC.CC*.CCCCC')

    def test_run_length_encoding(self):
        self.assertEqual(run_length_encode(''), ())

        self.assertEqual(run_length_encode('c'), (('c', 1),))

        self.assertEqual(run_length_encode('CCC.CC.CC'),
                                           (('C', 3), ('.', 1),
                                            ('C', 2), ('.', 1),
                                            ('C', 2)))

        sig  = 'CCCCCCCC.CCCC.CCCC.CCCC.CCCCCCCCCCCC'
        self.assertEqual(run_length_encode(sig), (('C', 8), ('.', 1),
                                         ('C', 4), ('.', 1),
                                         ('C', 4), ('.', 1),
                                         ('C', 4), ('.', 1),
                                         ('C', 12)))

        self.assertEqual(run_length_encode('.CCCC. CCC CCCC'),
                         (('.', 1),
                          ('C', 4), ('.', 1), (' ', 1),
                          ('C', 3), (' ', 1),
                          ('C', 4)))

        self.assertEqual(run_length_encode('CCCC.CC.CCCCC.CC.CC .CCCCC'),
                         (('C', 4), ('.', 1),
                          ('C', 2), ('.', 1),
                          ('C', 5), ('.', 1),
                          ('C', 2), ('.', 1,),
                          ('C', 2), (' ', 1), ('.', 1),
                          ('C', 5)))

        self.assertEqual(run_length_encode('CCCC.CC.CCCCC.CC.CC*.CCCCC'),
                         (('C', 4), ('.', 1),
                          ('C', 2), ('.', 1),
                          ('C', 5), ('.', 1),
                          ('C', 2), ('.', 1),
                          ('C', 2), ('*', 1), ('.', 1),
                          ('C', 5)))

    def test_cleaning(self):
        examples = ['123-AB-321', ' 123-AB-321', '', None, '321-BA-123 ']
        keys = ['123-AB-321', '321-BA-123']
        x = Extractor(examples, extract=False)
        self.assertEqual(set(x.example_freqs.keys()), set(keys))
        self.assertEqual(x.n_stripped, 2)
        self.assertEqual(x.n_empties, 1)
        self.assertEqual(x.n_nulls, 1)
        items = x.example_freqs.keys()
        self.assertEqual(set(items), {'123-AB-321', '321-BA-123'})

    def test_batch_rle_extract_single(self):
        examples = ['123-AB-321', ' 123-AB-321', '', None, '321-BA-123 ']
        x = Extractor(examples)
        freqs = x.results.rle_freqs
        self.assertEqual(len(freqs), 1)
        key = (('C', 3), ('.', 1), ('C', 2), ('.', 1), ('C', 3))
        self.assertEqual(list(freqs.keys()), [key])
        self.assertEqual(freqs[key], 2)

    def test_batch_rle_extract_pair(self):
        examples = ['123-AB-321', ' 12-AB-4321', '', None, '321-BA-123 ']
        x = Extractor(examples)
        freqs = x.results.rle_freqs
        self.assertEqual(len(freqs), 2)
        key1 = (('C', 3), ('.', 1), ('C', 2), ('.', 1), ('C', 3))
        key2 = (('C', 2), ('.', 1), ('C', 2), ('.', 1), ('C', 4))
        keys = [key1, key2]
        self.assertEqual(set(freqs.keys()), set(keys))
        self.assertEqual(freqs[key1], 2)
        self.assertEqual(freqs[key2], 1)

    def test_rle2re(self):
        rle = (('C', 3), ('.', 1), ('C', 2), ('.', 1), ('C', 3))
        an = Cats.AlphaNumeric.re_string
        punc = Cats.Punctuation.re_string
        regex = rle2re(rle)
        self.assertEqual(regex,
                         '^%s{3}%s%s{2}%s%s{3}$' % (an, punc, an, punc, an))
        cre = re.compile(regex)
        for s in ['123-AB-321', '321-BA-123']:
            self.assertIsNotNone(re.match(cre, s))

    def test_vrle(self):
        key1 = (('C', 3), ('.', 1), ('C', 2), ('.', 1), ('C', 3))
        key2 = (('C', 2), ('.', 1), ('C', 2), ('.', 1), ('C', 4))
        keys = [key1, key2]
        range_rles = to_vrles(keys)
        self.assertEqual(range_rles, [(('C', 2, 3), ('.', 1, 1),
                                       ('C', 2, 2), ('.', 1, 1),
                                       ('C', 3, 4))])

    def test_vrle2re(self):
        key1 = (('C', 3), ('.', 1), ('C', 2), ('.', 1), ('C', 3))
        key2 = (('C', 2), ('.', 1), ('C', 2), ('.', 1), ('C', 4))
        keys = [key1, key2]
        rrle = [('C', 2, 3), ('.', 1, 1),
                ('C', 2, 2), ('.', 1, 1),
                ('C', 3, 4)]
        an = Cats.AlphaNumeric.re_string
        punc = Cats.Punctuation.re_string
        expected = '^%s{2,3}%s%s{2}%s%s{3,4}$' % (an, punc, an, punc, an)
        self.assertEqual(vrle2re(rrle), expected)

    def test_sort_by_len(self):
        # Really designed for sorting lists/tuples, but everything with
        # a length will behave the same
        x = Extractor(['a'])
        self.assertEqual(x.sort_by_length([]), [])
        self.assertEqual(x.sort_by_length(['a']), ['a'])
        self.assertEqual(x.sort_by_length(['a', 'ab']), ['a', 'ab'])
        self.assertIn(x.sort_by_length(
                ['abcdef', '', 'aa', 'bb', 'ccc', 'zzyy', '1']),
                (['', '1', 'aa', 'bb', 'ccc', 'zzyy', 'abcdef'],
                 ['', '1', 'bb', 'aa', 'ccc', 'zzyy', 'abcdef']))

    def test_split_left(self):
        x = Extractor(['a'])
        http = [('http', 1, 1, 'fixed'),
                ('://', 1, 1, 'fixed'),
                ('a', 1, 5),
                ('.', 1, 1, 'fixed'),
                ('com', 1, 1, 'fixed')]
        https = [('https', 1, 1, 'fixed'),
                 ('://', 1, 1, 'fixed'),
                 ('a', 1, 4),
                 ('#', 1, 1, 'fixed'),
                 ('co', 1, 1, 'fixed'),
                 ('.', 1, 1, 'fixed'),
                 ('uk', 1, 1, 'fixed'),
                 ('/', 1, 1, 'fixed')]
        patterns = [http, https]
        results = x.merge_fixed_omnipresent_at_pos(patterns)
        expected = [
                [
                    [(u'http', 1, 1, u'fixed')],
                    [(u'https', 1, 1, u'fixed')]
                ],

                [
                    [(u'://', 1, 1, u'fixed')],
                    [(u'://', 1, 1, u'fixed')],
                ],

                [
                    [(u'a', 1, 5),
                     (u'.', 1, 1, u'fixed'),
                     (u'com', 1, 1, u'fixed')],

                    [(u'a', 1, 4),
                     (u'#', 1, 1, u'fixed'),
                     (u'co', 1, 1, u'fixed'),
                     (u'.', 1, 1, u'fixed'),
                     (u'uk', 1, 1, u'fixed'),
                     (u'/', 1, 1, u'fixed')]
                ],
        ]
        self.assertEqual(results, expected)


class TestExtraction(unittest.TestCase):
    def test_re_pqs_id(self):
        iids = ['123-AB-321', ' 12-AB-4321', '', None, '321-BA-123 ']
        self.assertEqual(extract(iids),
                         [r'^\d{2,3}\-[A-Z]{2}\-\d{3,4}$'])

    def test_re_uuid(self):
        uuids = ['1f65c9e8-cf9a-4e53-b7d0-c48a26a21b7c',
                 '88888888-4444-4444-4444-cccccccccccc',
                 'aaaaaaaa-1111-0000-9999-0123456789ab',
                 '22ecc913-68eb-4cfb-a9cc-18df44137a4c',
                 '634962c3-8bc1-4b51-b36d-3dcbfdc92b63',
                 'aac65b99-92ff-11e6-b97d-b8f6b118f191',
                 '6fa459ea-ee8a-3ca4-894e-db77e160355e',
                 '886313e1-3b8a-5372-9b90-0c9aee199e5d']
        self.assertEqual(extract(uuids),
                         ['^[0-9a-f]{8}\\-[0-9a-f]{4}\\-[0-9a-f]{4}\\-'
                          '[0-9a-f]{4}\\-[0-9a-f]{12}$'])

        uuid4s = ['2ffb8eaa-dd75-41c2-aca6-0444914b8713',
                  'f69c5651-0b97-4909-b896-8ef0891f81ff',
                  '13f984fe-65db-4646-99d4-a93c06f78472',
                  '50a886d2-78c9-4b7b-81a9-25caf4deb212',
                  '2d4429df-9a80-4581-9565-27880ce171b0',
                  '857e0ec6-1511-478b-93a3-15ac9212fd0d']

        self.assertEqual(extract(uuid4s),       # Not refining down yet
                         [r'^[0-9a-f]{8}\-[0-9a-f]{4}\-[0-9a-f]{4}\-'
                          r'[0-9a-f]{4}\-[0-9a-f]{12}$'])


    tels1 = [
        '(0131) 496 0091',
        '(0131) 496 0161',
        '(0131) 496 0107',
        '(020) 7946 0106',
        '(020) 7946 0642',
        '(0141) 496 0927',
        '(0141) 496 0595',
        '(0141) 496 0236',
        '(0141) 496 0324'
    ]
    def test_tels1(self):
        self.assertEqual(extract(self.tels1),
                         [r'^\(\d{3,4}\)\ \d{3,4}\ \d{4}$'])


    tels2 = [
        '+44 131 496 0091',
        '(0131) 496 0161',
        '+44 131 496 0107',
        '(020) 7946 0106',
        '+44 20 7946 0642',
        '+44 141 496 0927',
        '(0141) 496 0595',
        '+1 202 555 0181',
        '(0141) 496 0324',
    ]
    def test_tels2(self):
        self.assertEqual(set(extract(self.tels2)),
                         set([r'^\+\d{1,2}\ \d{2,3}\ \d{3,4}\ \d{4}$',
                              r'^\(\d{3,4}\)\ \d{3,4}\ \d{4}$']))


    tels3 = [
        '0131-222-9876',
        '0207.987.2287'
    ]
    def test_tels3(self):
        self.assertEqual(extract(self.tels3),
                         [r'^\d{4}[\-\.]\d{3}[\-\.]\d{4}$'])


    tels4 = [
        '222-678-8834',
        '321-123-1234',
        '212-988-0321',
        '191-777-2043'
    ]
    def test_tels4(self):
#        print(extract(self.tels4))
        self.assertEqual(extract(self.tels4),
                         [r'^\d{3}\-\d{3}\-\d{4}$'])


    tels5 = [
        '212-988-0321',
        '987-654-3210',
        '476 123 8829',
        '123 456 7890',
        '1 701 734 9288',
        '1 177 441 7712',
        '(617) 222 0529',
        '(222) 111 9276',
    ]
    def test_tels5(self):
#        print(Extractor(self.tels5))
        self.assertEqual(extract(self.tels5), [
            r'^\d{3}\ \d{3}\ \d{4}$',
            r'^\d{3}\-\d{3}\-\d{4}$',
            r'^1\ \d{3}\ \d{3}\ \d{4}$',
            r'^\(\d{3}\)\ \d{3}\ \d{4}$',
        ])

    def test_tels_1to5(self):
        tels = self.tels1 + self.tels2 + self.tels3 + self.tels4 + self.tels5
#        print(Extractor(tels, tag=True))
        self.assertEqual(extract(tels), [
            r'^\d{3}\ \d{3}\ \d{4}$',
            r'^\d{3,4}[\-\.]\d{3}[\-\.]\d{4}$',
            r'^1\ \d{3}\ \d{3}\ \d{4}$',
            r'^\(\d{3,4}\)\ \d{3,4}\ \d{4}$',
            r'^\+\d{1,2}\ \d{2,3}\ \d{3,4}\ \d{4}$',
        ])


    urls1 = [
        'http://www.stochasticsolutions.com/',
        'http://apple.com/',
        'http://stochasticsolutions.com/',
        'http://www.stochasticsolutions.co.uk/',
        'http://www.google.co.uk/',
        'http://www.google.com',
        'http://www.google.com/',
        'http://www.stochasticsolutions.com',
        'http://web.stochasticsolutions.com',
        'https://www.stochasticsolutions.com',
        'http://tdda.info',
        'http://web.web',
    ]

    def test_urls1(self):

#        print()
#        x = Extractor(self.urls1, verbose=True)
#        x = Extractor(self.urls1, verbose=True)
#        print(str(x))
        self.assertEqual(set(extract(self.urls1)),
                         set([r'^http\:\/\/www\.[a-z]{6,19}\.com\/$',
                              r'^http\:\/\/[a-z]{3,4}\.[a-z]{3,4}$',
                              r'^http\:\/\/[a-z]{5,19}\.com\/$',
                              r'^[a-z]{4,5}\:\/\/[a-z]{3}\.[a-z]{6,19}\.com$',
                              r'^http\:\/\/www\.[a-z]{6,19}\.co\.uk\/$',]))

        # Sorted by length, these forms are:These are all:
        #
        #    C+.+C+.C+
        #    C+.+C+.C+.
        #    C+.+C+.C+.C+
        #    C+.+C+.C+.C+.
        #    C+.+C+.C+.C+.C+.

        # So: C+.+C+.C+(.C+)*.?
        # But that's a bit general!


        # Really want:
        #    '^https?\:\/\/([a-z]+\.)+[a-z]+\/?$'
        # Quite a way to go!
        #   - Small categoricals (http|https)
        #   - Related small categoricals (http|https) --> https?)
        #   - {6-19} --> +  (but when?)
        #   -  (C|C.C|C.C.C) --> (C.)+C   (i.e. concept of separation
        #                                  as opposed to terminators)


    urls2 = [
        'stochasticsolutions.com/',
        'apple.com/',
        'stochasticsolutions.com/',
        'http://www.stochasticsolutions.co.uk/',
        'http://www.google.co.uk/',
        'http://www.google.com',
        'http://www.google.com/',
        'http://www.guardian.co.uk/',
        'http://www.guardian.com',
        'http://www.guardian.com/',
        'http://www.stochasticsolutions.com',
        'web.stochasticsolutions.com',
        'https://www.stochasticsolutions.com',
        'tdda.info',
        'gov.uk',
        'http://web.web',
    ]
    def test_urls2(self):

#        print()
#        x = Extractor(self.urls2, verbose=True)
#        x = Extractor(self.urls2)
#        print(str(x))
        self.assertEqual(set(extract(self.urls2)), {
            r'^[a-z]{3,4}\.[a-z]{2,4}$',
            r'^[a-z]{5,19}\.com\/$',
            r'^[a-z]{3,4}[\.\/\:]{1,3}[a-z]{3,19}\.[a-z]{3}$',
            r'^[a-z]{4,5}\:\/\/www\.[a-z]{6,19}\.com$',
            r'^http\:\/\/www\.[a-z]{6,8}\.com\/$',
            r'^http\:\/\/www\.[a-z]{6,19}\.co\.uk\/$',
        })

    def test_urls_all(self):

#        print()
#        x = Extractor(self.urls2, verbose=True)
#        x = Extractor(self.urls1 + self.urls2)
#        print(str(x))
        self.assertEqual(set(extract(self.urls1 + self.urls2)), {
            r'^[a-z]{3,4}\.[a-z]{2,4}$',
            r'^[a-z]{5,19}\.com\/$',
            r'^[a-z]{3,4}[\.\/\:]{1,3}[a-z]{3,19}\.[a-z]{3,4}$',
            r'^http\:\/\/[a-z]{5,19}\.com\/$',
            r'^[a-z]{4,5}\:\/\/[a-z]{3}\.[a-z]{6,19}\.com$',
            r'^http\:\/\/www\.[a-z]{6,19}\.com\/$',
            r'^http\:\/\/www\.[a-z]{6,19}\.co\.uk\/$',
        })

    @unittest.skipIf(pandas is None, 'No pandas here')
    def testpdextract(self):
        df = pd.DataFrame({'a3': ["one", "two", pd.np.NaN],
                           'a45': ['three', 'four', 'five']})

        re3 = pdextract(df['a3'])
        re45 = pdextract(df['a45'])
        re345 = pdextract([df['a3'], df['a45']])

        self.assertEqual(re3, ['^[a-z]{3}$'])
        self.assertEqual(re45, ['^[a-z]{4,5}$'])
        self.assertEqual(re345, ['^[a-z]{3,5}$'])

    @unittest.skipIf(pandas is None, 'No pandas here')
    def testpdextract(self):
        df = pd.DataFrame({'ab': ["one", True, pd.np.NaN]})
        self.assertRaisesRegexp(ValueError, 'Non-null, non-string',
                                pdextract, df['ab'])

    # def testextractcli(self):
    #     examples_dir = os.path.join(os.path.abspath(__file__), 'examples')
    #     ids_path = os.path.join(examples_dir, 'ids.txt')
    #     params = get_params(ids_path)
    #     main(params)



if __name__ == '__main__':
    unittest.main()

