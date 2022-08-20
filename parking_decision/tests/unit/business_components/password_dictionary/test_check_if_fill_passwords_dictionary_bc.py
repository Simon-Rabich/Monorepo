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
from unittest.mock import MagicMock

from business_components.password_dictionary.check_if_fill_passwords_dictionary_bc import \
    CheckIfFillPasswordsDictionaryBC
from dals.password_dictionary_dal import PasswordDictionaryDAL
from db.models.password_dictionary import PasswordDictionary
from tests.base_test import TestBase


class TestCheckIfFillPasswordsDictionaryBC(TestBase):

    def setUp(self) -> None:
        super().setUp()
        self._password_dictionary_dal_mock = MagicMock(spec=PasswordDictionaryDAL)
        self._check_if_fill_passwords_dictionary_bc =\
            CheckIfFillPasswordsDictionaryBC(password_dictionary_dal=self._password_dictionary_dal_mock)

    def test_execute__when_default_version_should_be_added(self):
        self._version_from_db_mock = None
        self._password_dictionary_dal_mock.get_data_version.return_value = self._version_from_db_mock
        result = self._check_if_fill_passwords_dictionary_bc.execute()
        self._password_dictionary_dal_mock.update_data_version.\
            assert_called_once_with(version=PasswordDictionary.DATA_VERSION)
        self.assertEqual(True, result)

    def test_execute__when_version_should_be_changed(self):
        self._version_from_db_mock = str(int(PasswordDictionary.DATA_VERSION) - 1)
        self._password_dictionary_dal_mock.get_data_version.return_value = self._version_from_db_mock
        result = self._check_if_fill_passwords_dictionary_bc.execute()
        self._password_dictionary_dal_mock.update_data_version. \
            assert_called_once_with(version=PasswordDictionary.DATA_VERSION)
        self.assertEqual(True, result)

    def test_execute__when_version_is_not_different__should_do_nothing(self):
        self._version_from_db_mock = PasswordDictionary.DATA_VERSION
        self._password_dictionary_dal_mock.get_data_version.return_value = self._version_from_db_mock
        result = self._check_if_fill_passwords_dictionary_bc.execute()
        self._password_dictionary_dal_mock.update_data_version.assert_not_called()
        self.assertEqual(False, result)
