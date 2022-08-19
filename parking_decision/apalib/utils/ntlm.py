#!/usr/bin/env python3
#    ___                      _
#   / __\   _ _ __ ___  _ __ | |_ ___  _ __ ___
#  / / | | | | '_ ` _ \| '_ \| __/ _ \| '_ ` _ \
# / /__| |_| | | | | | | |_) | || (_) | | | | | |
# \____/\__, |_| |_| |_| .__/ \__\___/|_| |_| |_|
#       |___/          |_|
#
# CYMPTOM LABS Copyright 2022. All rights reserved.
#
# Author: Naum Raviz (nraviz@tenable.com) on 02/08/2022

# STD packages
import binascii

# External packages
from Cryptodome.Hash import MD4


def ntlm_over_ntlm(pwd: str):
    h = MD4.new(pwd.encode("utf-16le")).digest()
    ntlm = binascii.hexlify(h).decode("utf8")
    ntlm_over_ntlm_hash = MD4.new(ntlm.encode("utf-16le")).digest()
    return binascii.hexlify(ntlm_over_ntlm_hash).decode("utf8")
