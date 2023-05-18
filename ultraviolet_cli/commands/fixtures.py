# -*- coding: utf-8 -*-
#
# Copyright (C) 2022 NYU Libraries.
#
# ultraviolet-cli is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Invenio module for custom UltraViolet commands."""


import glob
import json
import os
from time import sleep

import click
import requests
from jsonschema import Draft4Validator
from urllib3.exceptions import InsecureRequestWarning

from .. import config, utils

# Suppress InsecureRequestWarning warnings from urllib3.
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)


def create_record_draft(metadata, api, token):
    """Create a record draft using Requests."""
    sleep(1)

    try:
        r = requests.get(api, timeout=5, verify=False)
        r.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(
            f'Couldn\'t connect to api at {api}. Is the application running?'
        )
        raise SystemExit(e)

    headers = {
        'content-type': 'application/json',
        'authorization': f'Bearer {token}'
    }

    response = requests.post(url=api,
                             data=json.dumps(metadata),
                             headers=headers,
                             verify=False)

    response.raise_for_status()
    return response.json()


def delete_record_draft(pid, api, token):
    """Delete a record draft using Requests."""
    sleep(1)
    url = '/'.join((api.strip('/'), pid, 'draft'))

    try:
        r = requests.get(api, timeout=5, verify=False)
        r.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(
            f'Couldn\'t connect to api at {api}. Is the application running?'
        )
        raise SystemExit(e)

    headers = {
        'authorization': f'Bearer {token}'
    }

    try:
        response = requests.delete(url=url, headers=headers, verify=False)
        return response
    except Exception as err:
        print(f'Unable to delete draft with pid {pid}')


def publish_record(record_metadata, access_token):
    """Publish a record using Requests."""
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
def fixtures():
    """An entry point for fixtures subcommands, e.g., ingest, purge."""
    pass


@fixtures.command()
@click.option('-a', '--api', required=True, type=str,
              default=config.DEFAULT_RECORDS_API_URL,
              help=f'Invenio REST API base URL. '
                   f'Default={config.DEFAULT_RECORDS_API_URL}')
@click.option('-d', '--dir', required=True,
              type=click.Path(exists=True),
              default=config.DEFAULT_FIXTURES_DIR,
              help=f'Path to directory of fixtures. '
                   f'Default={config.DEFAULT_FIXTURES_DIR}')
@click.option('-o', '--output', required=True, type=str,
              default=config.DEFAULT_FIXTURES_OUTFILE,
              help=f'Where new fixture pid mappings will be written')
@click.option('-t', '--token', help='REST API token')
def ingest(api, dir, output, token):
    """Post local dir of UV fixture draft records via REST API."""
    click.secho('REST API: ', nl=False, bold=True, fg='green')
    click.secho(api)

    click.secho('Fixtures directory: ', nl=False, bold=True, fg='green')
    click.secho(dir)

    if token is None:
        token = utils.token_from_user(
            email=config.DEFAULT_FIXTURES_USER, name='default-su-token'
        )

    click.secho('Auth Token: ', nl=False, bold=True, fg='green')
    click.secho(token)

    records = glob.glob(f'{dir}/**/*.json', recursive=True)
    click.secho(
        f'\nFound {len(records)} records', nl=True, bold=True, fg='blue'
    )

    results = json.loads(
        open(output).read()
    ) if os.path.exists(output) else {}

    for file in records:
        click.secho(f'Posting record from {file}', nl=True, fg='blue')
        dict = json.loads(open(file).read())
        draft = create_record_draft(dict, api, token)
        uv_id = os.path.dirname(file).split('/')[-1]

        results[draft['id']] = uv_id

        os.makedirs(os.path.dirname(output), exist_ok=True)
        with open(output, "w") as f:
            json.dump(results, f)

        # record  = publish_record(draft, token)


@fixtures.command()
@click.option('-a', '--api', required=True, type=str,
              default=config.DEFAULT_RECORDS_API_URL,
              help=f'Invenio REST API base URL. '
                   f'Default={config.DEFAULT_RECORDS_API_URL}')
@click.option('-d', '--dir', required=True,
              type=click.Path(exists=True),
              default=config.DEFAULT_FIXTURES_DIR,
              help=f'Path to directory of fixtures. '
                   f'Default={config.DEFAULT_FIXTURES_DIR}')
@click.option('-o', '--output', required=True, type=str,
              default=config.DEFAULT_FIXTURES_OUTFILE,
              help=f'Where new fixture pid mappings will '
                   f'be written')
@click.option('-t', '--token', help='REST API token')
def purge(api, dir, output, token):
    """Delete all UV fixture draft records via REST API."""
    click.secho('REST API: ', nl=False, bold=True, fg='green')
    click.secho(api)

    if token is None:
        token = utils.token_from_user(
            email=config.DEFAULT_FIXTURES_USER, name='default-su-token'
        )

    click.secho('Auth Token: ', nl=False, bold=True, fg='green')
    click.secho(token)

    results = json.loads(
        open(output).read()
    ) if os.path.exists(output) else {}

    for pid, uv_id in results.copy().items():
        res = delete_record_draft(pid, api, token)
        if res.ok:
            click.secho(
                f'Delecting draft record {uv_id} aka {pid}',
                nl=True, bold=True, fg='blue'
            )
            results.pop(pid)

    os.makedirs(os.path.dirname(output), exist_ok=True)
    with open(output, "w") as f:
        json.dump(results, f)


@fixtures.command()
@click.option('-d', '--dir', required=True,
              type=click.Path(exists=True),
              default=config.DEFAULT_FIXTURES_DIR,
              help=f'Path to directory of fixtures. '
                   f'Default={config.DEFAULT_FIXTURES_DIR}')
@click.option('-s', '--schema-file', required=True,
              type=click.Path(exists=True),
              default=config.DEFAULT_SCHEMA_PATH,
              help=f'Path to json schema. '
                   f'Default={config.DEFAULT_SCHEMA_PATH}')
def validate(dir, schema_file):
    """Validate local dir of fixture records against JSON schema."""
    click.secho(
        'Fixtures directory: ', nl=False, bold=True, fg='green'
    )
    click.secho(dir)

    click.secho('JSON Schema: ', nl=False, bold=True, fg='green')
    click.secho(schema_file)

    records = glob.glob(f'{dir}/**/*.json', recursive=True)
    click.secho(
        f'\nFound {len(records)} records',
        nl=True, bold=True, fg='blue'
    )

    schema = json.loads(open(schema_file).read())
    Draft4Validator.check_schema(schema)
    validator = Draft4Validator(schema, format_checker=None)

    for file in records:
        dict = json.loads(open(file).read())
        try:
            validator.validate(dict)
            click.secho(f'{file} passes', nl=True, fg='blue')
        except BaseException as error:
            click.secho(f'{file} fails', nl=True, fg='red')
            print('An exception occurred: {}'.format(error))
