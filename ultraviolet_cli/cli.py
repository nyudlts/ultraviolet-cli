# -*- coding: utf-8 -*-
#
# Copyright (C) 2022 NYU Libraries.
#
# ultraviolet-cli is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Invenio module for custom UltraViolet commands."""

import click
import os

from .commands.ingest import ingest

@click.group(help='Invenio module for custom UltraViolet commands.')

def cli():
    pass


cli.add_command(ingest)
