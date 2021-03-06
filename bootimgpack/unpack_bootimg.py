#!/usr/bin/python

# Copyright 2015 duanqz
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

"""
Usage: pack_bootimg.py BOOT_IMG [OUTPUT_DIR]
       - BOOT_IMG     : the input boot image to be unpacked
       - OUTPUT_DIR   : the output director after unpack. If not present, BOOT_IMG.img will be used
"""

__author__ = 'duanqz@gmail.com'


from internal import bootimg
import sys
import traceback


if __name__ == '__main__':
    argc = len(sys.argv)
    if argc <= 1:
        print __doc__
        exit(1)

    if argc > 1:
        boot_img = sys.argv[1]
        output = boot_img + ".out"

    if argc > 2:
        output = sys.argv[2]

    try:
        bootimg.unpack(boot_img, output)
    except ValueError as ve:
        traceback.print_exc()
        # See help.xml ERR_UNPACK_BOOTIMG_FAILED
        sys.exit(153)
