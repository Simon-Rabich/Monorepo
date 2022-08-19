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
from typing import Optional, Dict

# Internal packages
from apalib.configurations.configs import QA_DEVELOP_CONFIG, BASIC_CONFIG, ENVIRONMENT_CONFIG, CICD_CONFIG, QA_MILESTONE_CONFIG, \
    QA_STAGING_CONFIG, US_1A_CONFIG, US_2B_CONFIG


ENVIRONMENT_CLUSTER_NAME_TO_CONFIG: Dict[str, dict] = {"qa-develop": QA_DEVELOP_CONFIG,
                                                       "qa-milestone": QA_MILESTONE_CONFIG,
                                                       "qa-staging": QA_STAGING_CONFIG,
                                                       "us-1a": US_1A_CONFIG,
                                                       "us-2b": US_2B_CONFIG,
                                                       }


def get_config() -> dict:
    config: dict = BASIC_CONFIG
    environment_name: Optional[str] = config["ENVIRONMENT"]
    if environment_name is not None:
        config.update(ENVIRONMENT_CONFIG)
        config.update(ENVIRONMENT_CLUSTER_NAME_TO_CONFIG.get(environment_name, {}))  # config of specific env
        return config

    if os.getenv('CI'):
        config.update(CICD_CONFIG)
        return config

    return config
