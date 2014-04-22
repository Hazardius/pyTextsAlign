#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

import pta_alignment
from pta_alignment import alignment, atype, lang
from pta_files import open_file

class pta_alignment_tests(unittest.TestCase):

    # def test_short_text_naive_alignment(self):
    #     self.maxDiff = None
    #     polish_text = (u"Był to mgr inż. Bartłomiej Czeci. Opanował on " +\
    #         u"m.in. Nietzschego. Trudno jest określić dlaczego Mr. Bronek " +\
    #         u"nagle zniknął.", lang.POLISH)
    #     english_text = (u"It was a M.Sc. Bartholomew Czeci. He mastered " +\
    #         u"among others Nietzsche. It is difficult to determine why Mr. " +\
    #         u"Bronek suddenly disappeared.", lang.ENGLISH)
    #     expected = [[[u"Był to mgr inż. Bartłomiej Czeci."],\
    #           [u"It was a M.Sc."]],\
    #         [[u"Opanował on m.in. Nietzschego."], [u"Bartholomew Czeci."]],\
    #         [[u"Trudno jest określić dlaczego Mr. Bronek nagle zniknął."],\
    #           [u"He mastered among others Nietzsche."]],\
    #         [[], [u"It is difficult to determine why Mr. Bronek suddenly" +\
    #           u" disappeared."]]]
    #     results = alignment(atype.NAIVE, polish_text, english_text).core
    #     self.assertEqual(expected, results)

    # def test_short_text_single_alignment(self):
    #     self.maxDiff = None
    #     polish_text = (u"Był to mgr inż. Bartłomiej Czeci. Opanował on " +\
    #         u"m.in. Nietzschego. Trudno jest określić dlaczego Mr. Bronek " +\
    #         u"nagle zniknął.", lang.POLISH)
    #     english_text = (u"It was a M.Sc. Bartholomew Czeci. He mastered " +\
    #         u"among others Nietzsche. It is difficult to determine why Mr. " +\
    #         u"Bronek suddenly disappeared.", lang.ENGLISH)
    #     expected = [[[u"Był to mgr inż. Bartłomiej Czeci."],\
    #           [u"It was a M.Sc.", u"Bartholomew Czeci."]],\
    #         [[u"Opanował on m.in. Nietzschego."],\
    #           [u"He mastered among others Nietzsche."]],\
    #         [[u"Trudno jest określić dlaczego Mr. Bronek nagle zniknął."],\
    #           [u"It is difficult to determine why Mr. Bronek suddenly" +\
    #           " disappeared."]]]
    #     results = alignment(atype.SIMPLE, polish_text, english_text).core
    #     self.assertEqual(expected, results)

    def test_plit_text_naive_alignment(self):
        self.maxDiff = None
        polish_text = ("example_files/pl_nowak.txt", lang.POLISH)
        italian_text = ("example_files/it_nowak.txt", lang.ITALIAN)
        expected = [[[u"Dr hab. Nowak stworzył niepowtarzalne dzieło. Jego " +\
            u"doskonała konsystencja pozwala na zupełnie nowe zastosowania " +\
            u"gumy w przemyśle."], [u"ASN Nowak ha creato un'opera unica."]],\
            [[], [u"La sua eccellente consistenza permette di completamente " +\
            u"nuove applicazioni nell'industria della gomma."]]]
        results = alignment(atype.NAIVE, polish_text, italian_text).core
        self.assertEqual(expected, results)

    def test_plit_text_simple_alignment(self):
        self.maxDiff = None
        polish_text = ("example_files/pl_nowak.txt", lang.POLISH)
        italian_text = ("example_files/it_nowak.txt", lang.ITALIAN)
        expected = [[[u"Dr hab. Nowak stworzył niepowtarzalne dzieło. Jego " +\
            u"doskonała konsystencja pozwala na zupełnie nowe zastosowania " +\
            u"gumy w przemyśle."], [u"ASN Nowak ha creato un'opera unica.",\
              u"La sua eccellente consistenza permette di completamente " +\
              u"nuove applicazioni nell'industria della gomma."]]]
        results = alignment(atype.SIMPLE, polish_text, italian_text).core
        self.assertEqual(expected, results)

    def test_itpl_text_simple_alignment(self):
        self.maxDiff = None
        polish_text = ("example_files/pl_nowak.txt", lang.POLISH)
        italian_text = ("example_files/it_nowak.txt", lang.ITALIAN)
        expected = [[[u"ASN Nowak ha creato un'opera unica.",\
              u"La sua eccellente consistenza permette di completamente " +\
              u"nuove applicazioni nell'industria della gomma."],\
              [u"Dr hab. Nowak stworzył niepowtarzalne dzieło. Jego " +\
            u"doskonała konsystencja pozwala na zupełnie nowe zastosowania " +\
            u"gumy w przemyśle."]]]
        results = alignment(atype.SIMPLE, italian_text, polish_text).core
        self.assertEqual(expected, results)

    def test_itpl_text_simple_alignment_plus_save(self):
        self.maxDiff = None
        polish_text = ("example_files/pl_nowak.txt", lang.POLISH)
        italian_text = ("example_files/it_nowak.txt", lang.ITALIAN)
        expected = u'"ASN Nowak ha creato un\'opera unica." ' +\
              u'"La sua eccellente consistenza permette di completamente ' +\
              u'nuove applicazioni nell\'industria della gomma." @|@ ' +\
              u'"Dr hab. Nowak stworzył niepowtarzalne dzieło. Jego ' +\
            u'doskonała konsystencja pozwala na zupełnie nowe zastosowania ' +\
            u'gumy w przemyśle." \n'
        itpl_align = alignment(atype.SIMPLE, italian_text, polish_text)
        itpl_align.save("tmp2.tmp")
        f = open("tmp2.tmp", 'r')
        results = ""
        for line in f:
            results += line.decode("utf-8-sig")
        f.close()
        self.assertEqual(expected, results)

if __name__ == '__main__':
    unittest.main()

