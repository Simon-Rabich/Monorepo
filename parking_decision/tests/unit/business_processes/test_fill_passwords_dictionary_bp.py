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
# Author: Naum Raviz (nraviz@tenable.com) on 21/07/2022

# STD packages
from typing import Type
from unittest.mock import MagicMock

# Internal packages
from apalib.utils.ntlm import ntlm_over_ntlm
from business_components.password_dictionary.check_if_fill_passwords_dictionary_bc import \
    CheckIfFillPasswordsDictionaryBC
from business_processes.fill_passwords_dictionary_bp import FillPasswordsDictionaryBP
from dals.password_dictionary_dal import PasswordDictionaryDAL
from db.models.password_dictionary import PasswordDictionary
from dtos.password_dictionary_dto import PasswordDictionaryDTO
from helpers.s3_communication import S3Communication
from tests.base_test import TestBase


class TestFillPasswordsDictionaryBP(TestBase):

    def setUp(self) -> None:
        super().setUp()
        self._password_dictionary_dal_mock = MagicMock(spec=PasswordDictionaryDAL)
        self._s3_communication_mock = MagicMock(spec=S3Communication)
        self._check_if_fill_passwords_dictionary_bc_mock = MagicMock(spec=CheckIfFillPasswordsDictionaryBC)
        self._fill_passwords_dictionary_bp = \
            FillPasswordsDictionaryBP(password_dictionary_dal=self._password_dictionary_dal_mock,
                                      s3_communication=self._s3_communication_mock,
                                      check_if_fill_passwords_dictionary_bc=self._check_if_fill_passwords_dictionary_bc_mock)

    def test_execute(self):
        self._check_if_fill_passwords_dictionary_bc_mock.execute.return_value = True
        clear_text_lines = [str(i) for i in range(101)]
        self._s3_communication_mock.get_clear_text_lines.return_value = clear_text_lines
        self._fill_passwords_dictionary_bp.execute()
        self._password_dictionary_dal_mock.add_passwords_dictionary. \
            assert_any_call(password_dictionary_dtos=[PasswordDictionaryDTO(hash=ntlm_over_ntlm(pwd=clear_text),
                                                                            clear_text=clear_text) for
                                                      clear_text in
                                                      clear_text_lines[0:100]])
        self._password_dictionary_dal_mock.add_passwords_dictionary. \
            assert_any_call(password_dictionary_dtos=[PasswordDictionaryDTO(hash=ntlm_over_ntlm(pwd=clear_text_lines[100]),
                                                                            clear_text=clear_text_lines[100])])

    def test_execute__when_filling_is_not_required__should_do_nothing(self):
        self._check_if_fill_passwords_dictionary_bc_mock.execute.return_value = False
        self._fill_passwords_dictionary_bp.execute()
        self._s3_communication_mock.get_clear_text_lines.assert_not_called()
        self._password_dictionary_dal_mock.add_passwords_dictionary.assert_not_called()
