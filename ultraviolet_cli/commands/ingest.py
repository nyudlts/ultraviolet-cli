# -*- coding: utf-8 -*-
#
# Copyright (C) 2022 NYU Libraries.
#
# ultraviolet-cli is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Invenio module for custom UltraViolet commands."""

import click

@click.group()
@click.version_option()

def cli():
    """
    Ingests UV records from a directory of subdirs.
    Each subdir respresents an item.
    Each subdir MUST contain ONE .json metadata record.
    Each subdir MAY contain ONE directory labelled 'resources' with resources to post to the item.
    """

@cli.command()

@click.option('-u', '--url', required=True, type=str,
              default='https://127.0.0.1:5000/api',
              help='Invenio REST API base URL.')

@click.argument('records_dir', required=True,  type=click.Path(exists=True))

def ingest(url, records_dir):
    """
    Ingests UV records from a directory of subdirs.
    """

    click.secho('Invenio REST API.....: ', nl=False, bold=True, fg='green')
    click.secho(url)

    click.secho('Records directory..: ', nl=False, bold=True, fg='green')
    click.secho(records_dir)
