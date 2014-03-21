#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from pta_files import open_file

class PTAFiles(unittest.TestCase):

    def test_open_file_correct_txt(self):
        self.maxDiff = None
        results = open_file("example_files/Birds in a Cage.txt")
        expected = [u"\"Why do you weep?\" inquired the young siskin of the old,\n",
          u"\"You're more comfortable in this cage than out in the cold.\"\n",
          u"\"You were born caged,\" said the elder, \"this was your morrow;\n",
          "\"I was free, now I'm caged—hence the cause of my sorrow.\"\n"]
        self.assertEqual(expected, results)