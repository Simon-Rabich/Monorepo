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
import os
from pathlib import Path


# For local run (also tests run).
BASIC_CONFIG = {
                # Environment
                "ENVIRONMENT": os.getenv('CLUSTER_NAME'),

                # DynamoDB
                "PASSWORDS_DICTIONARY_TABLE_NAME": "apa-password_cracker-passwords_dictionary",

                # AWS
                "AWS_ENDPOINT_URL": "http://localhost:4566",
                "AWS_REGION": "us-east-1",

                # S3
                "CLEAR_TEXT_FILES_BUCKET_NAME": "lumin-ds-test-2",
                "CLEAR_TEXT_FILES_FOLDER_PATH": "attack_path/password_cracker/clear_text_files/",

                # Web service
                "HOST_IP_WEB_SERVICE": "0.0.0.0",
                "HOST_PORT_WEB_SERVICE": 8000,
                "MAX_BATCH_SIZE": 100,

                # Logs
                "LOGS_DIR": f"{Path.home()}/logs",
               }

##############################################################################
##############################################################################

CICD_CONFIG = {
                # AWS
                "AWS_ENDPOINT_URL": "http://localstack:4566",
              }

##############################################################################
##############################################################################

ENVIRONMENT_CONFIG = {  # AWS
                        "AWS_ENDPOINT_URL": None,

                        # DynamoDB
                        "PASSWORDS_DICTIONARY_TABLE_NAME": f"{BASIC_CONFIG['ENVIRONMENT']}-apa-password_cracker-passwords_dictionary",

                        # S3
                        "CLEAR_TEXT_FILES_BUCKET_NAME": f"tenable-eng-data-lake-{BASIC_CONFIG['ENVIRONMENT']}",

                        # Logs
                        "LOGS_DIR": f"/app/logs",

                      }

##############################################################################
##############################################################################

QA_DEVELOP_CONFIG = {}

##############################################################################
##############################################################################

QA_MILESTONE_CONFIG = {}

##############################################################################
##############################################################################

QA_STAGING_CONFIG = {}

##############################################################################
##############################################################################

US_1A_CONFIG = {}

##############################################################################
##############################################################################

US_2B_CONFIG = {}
