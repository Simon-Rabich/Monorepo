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
# Author: Naum Raviz (nraviz@tenable.com) on 01/08/2022

# STD packages
from unittest.mock import MagicMock

# Internal packages
from business_queries.get_cracked_passwords_bq import GetCrackedPasswordsBQ
from dals.password_dictionary_dal import PasswordDictionaryDAL
from dtos.password_dictionary_dto import PasswordDictionaryDTO
from sdk.constants.cracking_method_enum import CrackingMethod
from sdk.dtos.cracked_password import CrackedPassword
from sdk.dtos.cracked_passwords import CrackedPasswords
from sdk.exceptions.exceptions import HashedPasswordsListTooBig

from tests.base_test import TestBase


class TestGetCrackedPasswordsBQ(TestBase):

    def setUp(self) -> None:
        super().setUp()
        self._password_dictionary_dal_mock = MagicMock(spec=PasswordDictionaryDAL)
        self._get_cracked_passwords_bq = \
            GetCrackedPasswordsBQ(password_dictionary_dal=self._password_dictionary_dal_mock)

    def test_execute(self):
        # Arrange
        hashed_passwords = ["cracked_hash1", "cracked_hash2", "cracked_hash3", "not_cracked_hash"]
        clear_texts = ["some_clear_text1", "some_clear_text2", "some_clear_text3"]
        passwords_dictionary_dtos = \
            [PasswordDictionaryDTO(hash=hashed_pass, clear_text=clear_text)
             for hashed_pass, clear_text in zip(hashed_passwords, clear_texts)]
        self._password_dictionary_dal_mock.get_passwords_dictionary.return_value = passwords_dictionary_dtos
        cracked_passwords = [CrackedPassword(is_cracked=True, hash=hashed_pass, clear_text=clear_text,
                                             cracking_method=CrackingMethod.DICTIONARY)
                             for hashed_pass, clear_text in zip(hashed_passwords, clear_texts)]
        cracked_passwords.append(CrackedPassword(is_cracked=False, hash=hashed_passwords[3]))
        expected_result = CrackedPasswords(cracked_passwords=cracked_passwords)
        # Act
        result = self._get_cracked_passwords_bq.execute(hashed_passwords=hashed_passwords)
        # Assert
        self.assertEqual(expected_result, result)

    def test_execute__when_length_of_list_is_greater_than_100__should_raise_exception(self):
        hashed_passwords = [str(i) for i in range(101)]
        with self.assertRaises(HashedPasswordsListTooBig):
            self._get_cracked_passwords_bq.execute(hashed_passwords=hashed_passwords)
