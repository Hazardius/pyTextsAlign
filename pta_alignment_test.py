#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

import pta_alignment
from pta_alignment import alignment, atype, lang

class pta_alignment_tests(unittest.TestCase):

    def test_short_text_naive_alignment(self):
        self.maxDiff = None
        polish_text = (u"Był to mgr inż. Bartłomiej Czeci. Opanował on " +\
            u"m.in. Nietzschego. Trudno jest określić dlaczego Mr. Bronek " +\
            u"nagle zniknął.", lang.POLISH)
        english_text = (u"It was a M.Sc. Bartholomew Czeci. He mastered " +\
            u"among others Nietzsche. It is difficult to determine why Mr. " +\
            u"Bronek suddenly disappeared.", lang.ENGLISH)
        expected = [[[u"Był to mgr inż. Bartłomiej Czeci."],\
              [u"It was a M.Sc."]],\
            [[u"Opanował on m.in. Nietzschego."], [u"Bartholomew Czeci."]],\
            [[u"Trudno jest określić dlaczego Mr. Bronek nagle zniknął."],\
              [u"He mastered among others Nietzsche."]],\
            [[], [u"It is difficult to determine why Mr. Bronek suddenly" +\
              u" disappeared."]]]
        results = alignment(atype.NAIVE, polish_text, english_text).core
        self.assertEqual(expected, results)

    def test_short_text_single_alignment(self):
        self.maxDiff = None
        polish_text = (u"Był to mgr inż. Bartłomiej Czeci. Opanował on " +\
            u"m.in. Nietzschego. Trudno jest określić dlaczego Mr. Bronek " +\
            u"nagle zniknął.", lang.POLISH)
        english_text = (u"It was a M.Sc. Bartholomew Czeci. He mastered " +\
            u"among others Nietzsche. It is difficult to determine why Mr. " +\
            u"Bronek suddenly disappeared.", lang.ENGLISH)
        expected = [[[u"Był to mgr inż. Bartłomiej Czeci."],\
              [u"It was a M.Sc.", u"Bartholomew Czeci."]],\
            [[u"Opanował on m.in. Nietzschego."],\
              [u"He mastered among others Nietzsche."]],\
            [[u"Trudno jest określić dlaczego Mr. Bronek nagle zniknął."],\
              [u"It is difficult to determine why Mr. Bronek suddenly" +\
              " disappeared."]]]
        results = alignment(atype.SIMPLE, polish_text, english_text).core
        self.assertEqual(expected, results)

    def test_plit_text_naive_alignment(self):
        self.maxDiff = None
        polish_text = (u"Dr hab. Nowak stworzył niepowtarzalne dzieło. Jego " +\
            u"doskonała konsystencja pozwala na zupełnie nowe zastosowania " +\
            u"gumy w przemyśle.", lang.POLISH)
        italian_text = (u"ASN Nowak ha creato un'opera unica. La sua " +\
            u"eccellente consistenza permette di completamente nuove " +\
            u"applicazioni nell'industria della gomma.", lang.ITALIAN)
        expected = [[[u"Dr hab. Nowak stworzył niepowtarzalne dzieło. Jego " +\
            u"doskonała konsystencja pozwala na zupełnie nowe zastosowania " +\
            u"gumy w przemyśle."], [u"ASN Nowak ha creato un'opera unica."]],\
            [[], [u"La sua eccellente consistenza permette di completamente " +\
            u"nuove applicazioni nell'industria della gomma."]]]
        results = alignment(atype.NAIVE, polish_text, italian_text).core
        self.assertEqual(expected, results)

    def test_plit_text_simple_alignment(self):
        self.maxDiff = None
        polish_text = (u"Dr hab. Nowak stworzył niepowtarzalne dzieło. Jego " +\
            u"doskonała konsystencja pozwala na zupełnie nowe zastosowania " +\
            u"gumy w przemyśle.", lang.POLISH)
        italian_text = (u"ASN Nowak ha creato un'opera unica. La sua " +\
            u"eccellente consistenza permette di completamente nuove " +\
            u"applicazioni nell'industria della gomma.", lang.ITALIAN)
        expected = [[[u"Dr hab. Nowak stworzył niepowtarzalne dzieło. Jego " +\
            u"doskonała konsystencja pozwala na zupełnie nowe zastosowania " +\
            u"gumy w przemyśle."], [u"ASN Nowak ha creato un'opera unica.",\
              u"La sua eccellente consistenza permette di completamente " +\
              u"nuove applicazioni nell'industria della gomma."]]]
        results = alignment(atype.SIMPLE, polish_text, italian_text).core
        self.assertEqual(expected, results)

if __name__ == '__main__':
    unittest.main()

