#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import urllib
import urllib2
import string
import sys

""" This file contains sentence splitting methods used by a pyTextsAlign. """

def psi_toolkit_api_sentence_splitting(sentence, l_code):
    """Dumb way to split sentence. Split on every dot, question and
    exclamation mark."""
    host = "http://mrt.wmi.amu.edu.pl/json.psis?pipe=segment+--lang+" + l_code\
        + "+!+json-simple-writer+--tags+segment+&input=" + sentence.\
        encode("utf-8").replace(' ', '+')
    try:
        req = urllib2.Request(host)
        response_stream = urllib2.urlopen(req)
        json_response = response_stream.read()
        json_dic = json.loads(json_response)
        return [string.lstrip(sentence) for sentence in json_dic[u'output']]
    except:
        print "\tCould not open '%s'" % host
        return []
