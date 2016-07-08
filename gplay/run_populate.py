#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os, os.path

cmd = "../../../store-listing-toolkit/populate-v2.py metadata -platform android -prj-path . -sheet 1U7kv0k3myrcJtE1nOAdp7oDK_JxafVFnicabnu6ZBfE -customized-metadata-path ../src/gplay/metadata"
print cmd
os.system(cmd)
