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


class BaseService:
    """
    Every service class should inheritance this class.
    """

    @classmethod
    def start(cls):
        pass

    @classmethod
    def pre_run(cls):
        pass

    @classmethod
    def run(cls):
        """
        For production use
        """
        cls.pre_run()
        cls.start()
