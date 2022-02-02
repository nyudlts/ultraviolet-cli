# -*- coding: utf-8 -*-
#
# Copyright (C) 2022 NYU Libraries.
#
# ultraviolet-cli is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Invenio module for custom UltraViolet commands."""

import click
import os

def service_user_token():
    """
    create service user token
    """

    os.popen("invenio users create uv-cli-su@testing.org --password=123456 --active")
    os.popen("invenio roles add uv-cli-su@testing.org admin")
    token = os.popen("invenio tokens create --name uv-cli-su --user uv-cli-su@testing.org").read()

    return token
