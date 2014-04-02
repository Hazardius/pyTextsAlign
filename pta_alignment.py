#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

from pta_sentence_splitting import psi_toolkit_api_sentence_splitting as ptiss
from pta_tools import enum

""" This file contains alignement methods used by a pyTextsAlign. """

atype = enum(NAIVE = 0, SIMPLE = 1)

class alignment(object):
    """Simple alignment class."""
    def __init__(self, al_type, (text1, l1_code), (text2, l2_code)):
        """Constructor."""
        sentences1 = ptiss(text1, l1_code)
        sentences2 = ptiss(text2, l2_code)
        if al_type == 0:
            self.core = self.naive_alignment(sentences1, sentences2)
        elif al_type == 1:
            self.core = self.simple_alignment(sentences1, sentences2)

    def naive_alignment(self, l1_sentences, l2_sentences):
        """Dumb way to align sentences. 1 to 1 till the end of sentences on both
        sides."""
        sh = 1
        longer_l = len(l1_sentences)
        shorter_l = len(l2_sentences)
        if shorter_l > longer_l:
            temp = shorter_l
            shorter_l = longer_l
            longer_l = temp
            sh = 2
        list_r = []
        for itera in range(shorter_l):
            list_r.append([[l1_sentences[itera]], [l2_sentences[itera]]])
        for itera in range(longer_l - shorter_l):
            if sh == 1:
                list_r.append([[l1_sentences[itera + shorter_l]], []])
            else:
                list_r.append([[], [l2_sentences[itera + shorter_l]]])
        return list_r

    def simple_alignment(l1_sentences, l2_sentences):
        """Simple but better than naive way to align sentences."""
        l1i = 0
        l1len = len(l1_sentences)
        l2i = 0
        l2len = len(l2_sentences)
        list_r = []
        while (l1i != l1len and l2i != l2len):
            l1s_len = len(re.split(r'[^0-9A-Za-z]+', l1_sentences[l1i]))
            l2s_len = len(re.split(r'[^0-9A-Za-z]+', l2_sentences[l2i]))
            print l1s_len
            print l2s_len

