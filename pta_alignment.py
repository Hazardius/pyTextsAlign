#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

from pta_sentence_splitting import psi_toolkit_api_sentence_splitting as ptiss
from pta_tools import count_word_number, enum

""" This file contains alignement methods used by a pyTextsAlign. """

atype = enum(NAIVE = 0, SIMPLE = 1)
lang = enum(ENGLISH = 'en', ITALIAN = 'it', POLISH = 'pl')

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

    def simple_alignment(self, l1_sentences, l2_sentences):
        """Simple but better than naive way to align sentences."""
        l1i = 0
        l1len = len(l1_sentences)
        l2i = 0
        l2len = len(l2_sentences)
        list_r = []
        flag = False
        while (l1i != l1len and l2i != l2len):
            (end_l1, end_l2) = self.__search_the_end__(l1_sentences,\
                l2_sentences, l1i, l2i)
            left = []
            for itera in range(l1i, end_l1 + 1):
                left.append(l1_sentences[itera])
            right = []
            for itera in range(l2i, end_l2 + 1):
                right.append(l2_sentences[itera])
            list_r.append([left, right])
            l1i = end_l1 + 1
            l2i = end_l2 + 1
        return list_r

    def __search_the_end__(self, l1_sentences, l2_sentences, l1i, l2i):
        l1conc_len = count_word_number(l1_sentences[l1i])
        l2conc_len = count_word_number(l2_sentences[l2i])
        if l1conc_len > l2conc_len:
            concl_len = l1conc_len
            concs_len = l2conc_len
            act_l = l1i
            act_s = l2i
            end_s = len(l2_sentences)
            shorter_sen = l2_sentences
        else:
            concl_len = l2conc_len
            concs_len = l1conc_len
            act_l = l2i
            act_s = l1i
            end_s = len(l1_sentences)
            shorter_sen = l1_sentences
        while (concl_len - concs_len >= 3):
            if act_s + 1 != end_s:
                added = count_word_number(shorter_sen[act_s + 1])
                if concl_len - concs_len - added > -3:
                    concs_len += added
                    act_s += 1
                else:
                    break
            else:
                break
        if l1conc_len > l2conc_len:
            return (act_l, act_s)
        else:
            return (act_s, act_l)
