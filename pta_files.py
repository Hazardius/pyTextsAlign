#!/usr/bin/env python
# -*- coding: utf-8 -*-

import codecs
import sys

""" This file contains logic of file IN/OUT operations. """

def open_file(path):
    """ Opening a file specified by a path. Returns a file content."""
    f = open(path, 'r')
    ret_val = [line.decode("utf-8-sig") for line in f]
    f.close()
    return ret_val

def save_file(path, content):
    """ Saving output to the specified path."""
    content = [line for line in content.split("\n")]
    f = codecs.open(path, "w", "utf-8-sig")
    for line in content:
        f.write(line + "\n")
    f.close()
