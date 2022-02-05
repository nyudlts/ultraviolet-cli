# -*- coding: utf-8 -*-
#
# Copyright (C) 2022 NYU Libraries.
#
# ultraviolet-cli is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Invenio module for custom UltraViolet commands."""

import click
import glob
import json
import os
import requests
import sys

from time import sleep
from urllib3.exceptions import InsecureRequestWarning

from .. import config, utils

# Suppress InsecureRequestWarning warnings from urllib3.
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)


def create_record_draft(metadata, api_url, access_token):
    sleep(1)
    url = '/'.join((api_url.strip('/'), 'records'))

    try:
        r = requests.get(url, timeout=5, verify=False)
        r.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f'Couldn\'t connect to api at {url}. Is the application running?')
        raise SystemExit(e)


    headers = {
        'content-type': 'application/json',
        'authorization': f'Bearer {access_token}'
    }

    response = requests.post(url=url,
                             data=json.dumps(metadata),
                             headers=headers,
                             verify=False)
    response.raise_for_status()

    return response.json()

def publish_record(record_metadata, access_token):
    """Publish record using InvenioRDM REST API.
    Args:
        record_metadata (dict): The record draft metadata with links to publish route.
        access_token (str): A valid bearer token to be used to create the new record.
    Returns:
        dict: The record metadata returned by InvenioRDM.
    Raises:
        ConnectionError: If the server is not reachable.
        HTTPError: If the server response indicates an error.
        ValueError: If resource file does not exist.
    """
    sleep(1)
    url = record_metadata['links']['publish']

    headers = {
        'authorization': f'Bearer {access_token}'
    }

    response = requests.post(url=url,
                             headers=headers,
                             verify=False)

    return response.json()

@click.group()
def ingest():
    """
    An entry point for ingest subcommands, e.g., fixtures
    """
    pass


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

    click.secho('REST API: ', nl=False, bold=True, fg='green')
    click.secho(url)

    click.secho('Fixtures directory: ', nl=False, bold=True, fg='green')
    click.secho(dir)

    if token is None:
        token = utils.token_from_user(email=config.FIXTURES_DEFAULT_USER, name='default-su-token')

    click.secho('Auth Token: ', nl=False, bold=True, fg='green')
    click.secho(token)

    records = glob.glob(f'{dir}/**/*.json', recursive=True)
    click.secho(f'\nFound {len(records)} records', nl=True, bold=True, fg='blue')

    for file in records:
        click.secho(f'Posting record from {file}', nl=True, fg='blue')

        dict    = json.loads(open(file).read())
        draft   = create_record_draft(dict, url, token)
        # record  = publish_record(draft, token)
