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
from .commands.communities_create import create_communities
from invenio_app.factory import create_app
from .utils import create_cli

cli = create_cli(create_app=create_app)

cli.add_command(fixtures)
cli.add_command(create_communities)
