#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

""" This file contains alignement methods used by a pyTextsAlign. """

def count_word_number(text):
    return len(re.split(r'[^0-9A-Za-ząĄęĘśŚżŻźŹćĆńŃłŁóÓ\.-]+', text))

def enum(**enums):
    return type('Enum', (), enums)

