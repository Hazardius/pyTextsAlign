#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" This file contains alignement methods used by a pyTextsAlign. """

def naive_alignment(l1_sentences, l2_sentences):
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
    list = []
    for itera in range(shorter_l):
        list.append(([l1_sentences[itera]], [l2_sentences[itera]]))
    for itera in range(longer_l - shorter_l):
        if sh == 1:
            list.append(([l1_sentences[itera + shorter_l]], []))
        else:
            list.append(([], [l2_sentences[itera + shorter_l]]))
    return list
    