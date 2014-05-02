#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import urllib
import urllib2
import string
import sys

import PSIToolkit

from pta_files import open_file
from subprocess import call

""" This file contains sentence splitting methods used by a pyTextsAlign. """

def psi_toolkit_py_sentence_splitting(text, l_code):
    psi = PSIToolkit.PipeRunner('segment --lang ' + l_code + ' ! json-simple-writer --tags segment')
    return json.loads(psi.run(text))

def psi_toolkit_local_sentence_splitting(path, l_code):
    command = "cat \"" + path + "\" | psi-pipe segment --lang " + l_code + " ! json-simple-writer --tags segment > tmp.tmp"
    return_code = call(command, shell=True)
    ret_val = ""
    # with open("tmp.tmp") as f_in:
    #     ret_val = f_in.read().replace("\n\n", "\n")
    with open("tmp.tmp", 'r') as f:
        for line in f:
            if len(line) > 1:
                ret_val += line.decode("utf-8-sig")
    list_ret = ret_val[2:-2:].replace('","', "@|@").split("@|@")
    return [string.lstrip(sentence) for sentence in list_ret]

def psi_toolkit_api_sentence_splitting(sentence, l_code):
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
