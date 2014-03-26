#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib
import sys

""" This file contains sentence splitting methods used by a pyTextsAlign. """

def sentence_splitting(sentence):
    """Dumb way to split sentence. Split on every dot, question and
    exclamation mark."""
    temp_set = { "value" : sentence.replace(" ", "+").encode(sys.stdout.encoding) }
    address = "http://mrt.wmi.amu.edu.pl/json.psis?pipe=segment+--lang pl+!" +\
        "+write-simple+--tags+segment&" + urllib.urlencode(temp_set)
    print address
    try:
        urlobject = urllib2.urlopen(address)
        urlcontent = urlobject.read()
    except:
        print "\tCould not open '%s'" % address
        return set()
    print urlcontent
    return urlcontent
