# -*- coding: utf-8 -*-
#
# Copyright (C) 2022 NYU Libraries.
#
# ultraviolet-cli is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Invenio module for custom UltraViolet commands."""

import click
import os

def token_from_user(email, name='token'):
    """
    Create + return token for a given user.
    """
    token = os.popen(f'invenio tokens create --name {name} --user {email}').read()
    return token
