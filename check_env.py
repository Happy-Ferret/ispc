#!/usr/bin/python
#
#  Copyright (c) 2013, Intel Corporation
#  All rights reserved.
# 
#  Redistribution and use in source and binary forms, with or without
#  modification, are permitted provided that the following conditions are
#  met:
# 
#    * Redistributions of source code must retain the above copyright
#      notice, this list of conditions and the following disclaimer.
# 
#    * Redistributions in binary form must reproduce the above copyright
#      notice, this list of conditions and the following disclaimer in the
#      documentation and/or other materials provided with the distribution.
# 
#    * Neither the name of Intel Corporation nor the names of its
#      contributors may be used to endorse or promote products derived from
#      this software without specific prior written permission.
# 
# 
#   THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS
#   IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED
#   TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A
#   PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER
#   OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
#   EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
#   PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
#   PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
#   LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
#   NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
#   SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
 
# // Author: Filippov Ilia

import common
import sys
import os
import string
print_debug = common.print_debug
error = common.error
detect_version = common.detect_version

exists = [False, False, False, False, False, False, False, False]
names = ["m4", "bison", "flex", "sde", "ispc", "clang", "gcc", "icc"]

PATH_dir = string.split(os.getenv("PATH"), os.pathsep)
for counter in PATH_dir:
    for i in range(0,8):
        if os.path.exists(counter + os.sep + names[i]):
            exists[i] = True

print_debug("=== in PATH: ===\n", False, "")
print_debug("Tools:\n", False, "")
for i in range(0,3):
    if exists[i]:
        print_debug(detect_version(names[i] + " --version"), False, "")
    else:
        error("you don't have " + names[i], 0)
if exists[0] and exists[1] and exists[2]:
    if common.check_tools(2):
        print_debug("versions are ok\n", False, "")
print_debug("\nSDE:\n", False, "")
if exists[3]:
    print_debug(detect_version(names[3] + " --version"), False, "")
else:
    error("you don't have " + names[3], 2)
print_debug("\nISPC:\n", False, "")
if exists[4]:
    print_debug(detect_version(names[4] + " --version"), False, "")
else:
    error("you don't have " + names[4], 2)
print_debug("\nC/C++ compilers:\n", False, "")
for i in range(5,8):
    if exists[i]:
        print_debug(detect_version(names[i] + " --version"), False, "")
    else:
        error("you don't have " + names[i], 2)

print_debug("\n=== in ISPC specific environment variables: ===\n", False, "")
if os.environ.get("LLVM_HOME") == None:
    error("you have no LLVM_HOME", 2)
else:
    print_debug("Your LLVM_HOME:" + os.environ.get("LLVM_HOME") + "\n", False, "")
if os.environ.get("ISPC_HOME") == None:
    error("you have no ISPC_HOME", 2)
else:
    print_debug("Your ISPC_HOME:" + os.environ.get("ISPC_HOME") + "\n", False, "")
    if os.path.exists(os.environ.get("ISPC_HOME") + os.sep + "ispc"):
        print_debug("You have ISPC in your ISPC_HOME: " +
        detect_version(os.environ.get("ISPC_HOME") + os.sep + "ispc" + " --version"), False, "")
    else:
        error("you don't have ISPC in your ISPC_HOME", 2)
if os.environ.get("SDE_HOME") == None:
    error("You have no SDE_HOME", 2)
else:
    print_debug("Your SDE_HOME:" + os.environ.get("SDE_HOME") + "\n", False, "")
    if os.path.exists(os.environ.get("SDE_HOME") + os.sep + "sde"):
        print_debug("You have sde in your SDE_HOME: " +
        detect_version(os.environ.get("SDE_HOME") + os.sep + "sde" + " --version"), False, "")
    else:
        error("you don't have any SDE in your ISPC_HOME", 2)