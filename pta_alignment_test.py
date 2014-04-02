#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

import pta_alignment
from pta_alignment import alignment, atype

class pta_alignment_tests(unittest.TestCase):

    def test_short_text_naive_alignment(self):
        self.maxDiff = None
        polish_text = u"Był to mgr inż. Bartłomiej Czeci. Opanował on " +\
            u"m.in. Nietzschego. Trudno jest określić dlaczego Mr. Bronek " +\
            u"nagle zniknął."
        english_text = u"It was a M.Sc. Bartholomew Czeci. He mastered " +\
            u"among others Nietzsche. It is difficult to determine why Mr. " +\
            u"Bronek suddenly disappeared."
        expected = [[[u"Był to mgr inż. Bartłomiej Czeci."],\
              [u"It was a M.Sc."]],\
            [[u"Opanował on m.in. Nietzschego."], [u"Bartholomew Czeci."]],\
            [[u"Trudno jest określić dlaczego Mr. Bronek nagle zniknął."],\
              [u"He mastered among others Nietzsche."]],\
            [[], [u"It is difficult to determine why Mr. Bronek suddenly disappeared."]]]
        results = alignment(atype.NAIVE, (polish_text, "pl"),\
            (english_text, "en")).core
        self.assertEqual(expected, results)

if __name__ == '__main__':
    unittest.main()

