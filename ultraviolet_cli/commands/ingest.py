# -*- coding: utf-8 -*-
#
# Copyright (C) 2022 NYU Libraries.
#
# ultraviolet-cli is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Invenio module for custom UltraViolet commands."""

import click
import os

from .. import config, utils

@click.group()
def ingest():
    """
    An entry point for ingest subcommands, e.g., fixtures
    """
    pass


"""
define fixture ingest
"""
@ingest.command()
@click.option('-u', '--url', required=True, type=str,
              default='https://127.0.0.1:5000/api',
              help='Invenio REST API base URL. Default=https://127.0.0.1:5000/api')
@click.option('-d', '--dir', required=True,
              type=click.Path(exists=True),
              default='./fixtures', help='Path to directory of fixtures. Default=./fixtures')
@click.option('-t', '--token', help='REST API token')
def fixtures(url, dir, token):
    """
    Post UV fixture records via REST API from a directory.
    Each subdir respresents an item.
    Each subdir MUST contain ONE .json metadata record.
    Each subdir MAY contain ONE directory labelled 'resources' with resources to post to the item.
    """

    click.secho('Invenio REST API: ', nl=False, bold=True, fg='green')
    click.secho(url)

    click.secho('Fixtures directory: ', nl=False, bold=True, fg='green')
    click.secho(dir)

    if token is None:
        token = utils.token_from_user(email=config.FIXTURES_DEFAULT_USER, name='default-su-token')

    click.secho('Auth Token: ', nl=False, bold=True, fg='green')
    click.secho(token)
