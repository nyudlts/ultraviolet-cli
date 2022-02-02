# -*- coding: utf-8 -*-
#
# Copyright (C) 2022 NYU Libraries.
#
# ultraviolet-cli is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Invenio module for custom UltraViolet commands."""

import click
from ..utils import service_user_token

@click.group()
def ingest():
    """
    An entry point for fixtures subcommands, e.g., ingest
    """
    pass

@ingest.command()

@click.option('-u', '--url', required=True, type=str,
              default='https://127.0.0.1:5000/api',
              help='Invenio REST API base URL.')

@click.option('-r', '--records-dir', required=True,
              type=click.Path(exists=True),
              default='./fixtures', help='Path to directory of fixtures')

@click.option('-t', '--token', help='REST API token; if none provided, new service-user will be created')

def fixtures(url, records_dir, token=None):
    """
    Ingests UV records from a directory of subdirs.
    Each subdir respresents an item.
    Each subdir MUST contain ONE .json metadata record.
    Each subdir MAY contain ONE directory labelled 'resources' with resources to post to the item.
    """

    click.secho('Invenio REST API.....: ', nl=False, bold=True, fg='green')
    click.secho(url)

    click.secho('Records directory..: ', nl=False, bold=True, fg='green')
    click.secho(records_dir)

    if token is None:
        print("No auth token found; creating new service user account")
        token = service_user_token()

    print("token:", token)
