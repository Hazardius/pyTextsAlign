#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

import pta_alignment

class pta_alignment_tests(unittest.TestCase):

    def test_short_text_just_alignment_test(self):
        self.maxDiff = None
        polish_sentences = [u"Był to mgr inż. Bartłomiej Czeci.", u"Opanował" +\
            u" on m.in. Nietzschego.", u"Trudno jest określić dlaczego Mr. " +\
            u"Bronek nagle zniknął."]
        english_sentences = [u"It was a M.Sc.", u"Bartholomew Czeci.",\
            u"He mastered among others Nietzsche.", u"It is difficult to " +\
            u"determine why Mr. Bronek suddenly disappeared."]
        expected = [([u"Był to mgr inż. Bartłomiej Czeci."],\
              [u"It was a M.Sc."]),\
            ([u"Opanował on m.in. Nietzschego."], [u"Bartholomew Czeci."]),\
            ([u"Trudno jest określić dlaczego Mr. Bronek nagle zniknął."],\
              [u"He mastered among others Nietzsche."]),\
            ([], [u"It is difficult to determine why Mr. Bronek suddenly disappeared."])]
        results = pta_alignment.naive_alignment(polish_sentences, english_sentences)
        self.assertEqual(expected, results)

if __name__ == '__main__':
    unittest.main()

