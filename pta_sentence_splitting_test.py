#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from pta_sentence_splitting import sentence_splitting

class pta_sentence_splitting_tests(unittest.TestCase):

    def test_polish_sentence_splitting_test(self):
        self.maxDiff = None
        polish_sentence = u"Był to mgr inż. Bartłomiej Czeci. Opanował on " +\
            u"m.in. Nietzschego. Trudno jest określić dlaczego Mr. Bronek " +\
            u"nagle zniknął."
        expected = [u"Był to mgr inż. Bartłomiej Czeci.", u"Opanował on " +\
            u"m.in. Nietzschego.", u"Trudno jest określić dlaczego Mr. " +\
            u"Bronek nagle zniknął."]
        results = sentence_splitting(polish_sentence)
        self.assertEqual(expected, results)

if __name__ == '__main__':
    unittest.main()

