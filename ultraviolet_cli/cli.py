# -*- coding: utf-8 -*-
#
# Copyright (C) 2022 NYU Libraries.
#
# ultraviolet-cli is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Invenio module for custom UltraViolet commands."""

import click
import os

from .commands.fixtures import fixtures

@click.group(help='Invenio module for custom UltraViolet commands.')
@click.version_option()

def cli():
    pass

cli.add_command(fixtures)
