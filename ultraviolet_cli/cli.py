# -*- coding: utf-8 -*-
#
# Copyright (C) 2022 NYU Libraries.
#
# ultraviolet-cli is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Invenio module for custom UltraViolet commands."""

from flask import current_app
import os
from invenio_app.factory import create_app

from .commands.create_communities import create_communities
from .commands.delete_record import delete_record
from .commands.fixtures import fixtures
from .commands.upload_files import upload_files
from .utils import create_cli

cli = create_cli(create_app=create_app)
SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI", "postgresql+psycopg2://nyudatarepository:changeme@localhost/nyudatarepository")

cli.add_command(fixtures)
cli.add_command(create_communities)
cli.add_command(delete_record)
cli.add_command(upload_files)
