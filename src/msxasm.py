#!/usr/bin/env python

# ------------------------------------------------------------------------------
# msxasm.py is an MSX Assembler in Python
#
# Copyright (C) 2016 msxasmpy team <https://github.com/msxdev/msxasmpy>
#
# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#  <http://www.apache.org/licenses/LICENSE-2.0>
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ------------------------------------------------------------------------------

import argparse

def assemble(asmfile):
    print("Assembling \"%s\"" % asmfile)

    with open(asmfile, 'r') as f:
        s = f.read()
    print(s)

def main():
    app_name = "msxasmpy"
    app_ver = "0.0.1"
    app_year = "2016"
    app_author = "msxasmpy team"
    app_url = "https://github.com/msxdev/msxasmpy"
    app_banner = "{name} {version} (C) {year} {author} {url}".format(
        name = app_name,
        version = app_ver,
        year = app_year,
        author = app_author,
        url = app_url
    )

    parser = argparse.ArgumentParser(description=app_banner)	# prog='PROG'
    parser.add_argument('-v', '--version', action='version', version='%(prog)s version ' + app_ver)
    parser.add_argument('inputfiles', metavar='file.asm', type=str, nargs='+',
        help='file to assemble')
    args = parser.parse_args()

    for inputfile in args.inputfiles:
        assemble(inputfile)

if __name__ == "__main__": main()
