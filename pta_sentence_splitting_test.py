#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from pta_sentence_splitting import psi_toolkit_api_sentence_splitting as ptass

class pta_sentence_splitting_tests(unittest.TestCase):

    def test_english_pt_sentence_splitting_test(self):
        self.maxDiff = None
        english_sentence = u"It was a M.Sc. Bartholomew Czeci. He mastered " +\
            u"among others Nietzsche. It is difficult to determine why Mr. " +\
            u"Bronek suddenly disappeared."
        expected = [u"It was a M.Sc.", u"Bartholomew Czeci.", u"He mastered " +\
            u"among others Nietzsche.", u"It is difficult to determine why " +\
            u"Mr. Bronek suddenly disappeared."]
        results = ptass(english_sentence, "en")
        self.assertEqual(expected, results)

    def test_polish_pt_sentence_splitting_test(self):
        self.maxDiff = None
        polish_sentence = u"Był to mgr inż. Bartłomiej Czeci. Opanował on " +\
            u"m.in. Nietzschego. Trudno jest określić dlaczego Mr. Bronek " +\
            u"nagle zniknął."
        expected = [u"Był to mgr inż. Bartłomiej Czeci.", u"Opanował on" +\
            u" m.in. Nietzschego.", u"Trudno jest określić dlaczego Mr. " +\
            u"Bronek nagle zniknął."]
        results = ptass(polish_sentence, "pl")
        self.assertEqual(expected, results)

if __name__ == '__main__':
    unittest.main()

