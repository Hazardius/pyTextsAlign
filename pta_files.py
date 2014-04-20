#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" This file contains logic of file IN/OUT operations. """

def open_file(path):
    """ Opening a file specified by a path. Returns a file content."""
    f = open(path, 'r')
    return [line.decode("utf-8-sig").encode("utf-8") for line in f]

def save_file(path, content):
    """ Saving output to the specified path."""
    file = codecs.open(path, "w", "utf-8")
    for line in content:
        file.write(line)
    file.close()
