# -*- coding: utf-8 -*-
#
# Copyright (C) 2022 NYU Libraries.
#
# ultraviolet-cli is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Invenio module for custom UltraViolet commands."""

import json
import os

import click
from flask.cli import FlaskGroup
from flask.helpers import get_debug_flag


def create_cli(create_app=None):
    """Create CLI for ``ultraviolet-cli`` command.

    :param create_app: Flask application factory.
    :returns: Click command group.
    """
    # Flask 2.0 removed support for passing script_info argument. Below
    # function is thus
    def create_cli_app(*args):
        """Application factory for CLI app.

        Internal function for creating the CLI. When invoked via
        ``ultraviolet-cli`` FLASK_APP must be set.
        """
        if create_app is None:
            # This part is only used for the "inveniomanage" command.
            if len(args) == 0:
                # Flask v2
                # Create a barebones Flask application.
                app = Flask("ultraviolet-cli")
            else:
                # Flask v1
                # Fallback to normal Flask behavior
                info = args[0]
                info.create_app = None
                app = info.load_app()
        else:
            app = create_app(debug=get_debug_flag())
        return app

    @click.group(cls=FlaskGroup, create_app=create_cli_app)
    def cli(**params):
        """Command Line Interface for Ultraviolet."""
        pass

    return cli


def token_from_user(email, name='token'):
    """Create + return token for a given user."""
    token = os.popen(
        f'invenio tokens create --name {name} --user {email}'
    ).read().strip()
    return token


def create_community_data(name, description, type, visibility, policy):
    """Create fake communities for demo purposes."""
    data_to_use = {
        "access": {
            "visibility": visibility,
            "member_policy": policy,
            "record_policy": policy,
        },
        "slug": ('-'.join(name.split())).lower(),
        "metadata": {
            "title": name,
            "description": description,
            "type": {
                "id": type
            },
        },
    }
    return json.loads(json.dumps(data_to_use))
