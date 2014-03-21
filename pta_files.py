#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" This file contains logic of file IN/OUT operations. """

def open_file(path):
    """ Opening a file specified by a path. Returns a """
    f = open(path, 'r')
    return [line.decode("utf-8-sig").encode("utf-8") for line in f]
