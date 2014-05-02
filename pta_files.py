#!/usr/bin/env python
# -*- coding: utf-8 -*-

import codecs
import sys

""" This file contains logic of file IN/OUT operations. """

def open_file(path):
    """ Opening a file specified by a path.
    Returns a file content as list of non-empty lines."""
    with open(path) as f_in:
        return filter(None, (line.rstrip() for line in f_in))

def save_file(path, content):
    """ Saving output to the specified path."""
    content = [line for line in content.split("\n")]
    f = codecs.open(path, "w", "utf-8")
    for line in content:
        f.write(line + "\n")
    f.close()
