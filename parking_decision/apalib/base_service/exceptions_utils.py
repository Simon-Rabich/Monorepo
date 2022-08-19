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


def throws(*exception_names):
    """
    This method is actually the equivalent of a "throws" declaration, we say what we expect to be thrown in the code
    We wrap with this decorator
    :param exception_names:
    :return:
    """

    def add_exception(f):
        normalized_exc_names = set()
        normalized_exc_types = set()
        for exc in exception_names:
            if issubclass(exc, BaseException):
                normalized_exc_names.add(exc.__name__)
                normalized_exc_types.add(exc)
            else:
                raise ValueError("@throws accepts only strings or Exception classes")
        f.handled_exceptions_names = normalized_exc_names  # this set uses string to check for type name & error message
        f.handled_exceptions_types = \
            normalized_exc_types  # this set uses types instead of strings, so it checks for base classes as well
        return f

    return add_exception
