# -*- coding: utf-8 -*-
#
# Copyright (C) 2022 NYU Libraries.
#
# ultraviolet-cli is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Tests for Create Draft Records

See https://pytest-invenio.readthedocs.io/ for documentation on which test
fixtures are available.
"""


import json

import pytest

from ultraviolet_cli.commands.create_draft_records import create_draft_records


# Fixture for valid data
@pytest.fixture
def valid_data():
    return {
        "access": {"record": "public", "files": "public"},
        "files": {"enabled": True},
        "metadata": {
            "title": "A Romans story",
            "publication_date": "2020-06-01",
            "publisher": "Acme Inc",
            "resource_type": {"id": "image-photo"},
            "creators":
                [{
                    "person_or_org": {"name": "Troy Inc.",
                                      "type": "organizational"}
                }]
        }
    }


# Test CLI's response to invalid data input (missing required fields).
# Expects a non-zero exit code and 'Invalid data' error message.
def test_create_draft_records_invalid_data(cli_runner):
    invalid_data = {"metadata": {"title": "Invalid Data"}}
    result = cli_runner(
        create_draft_records,
        ["-o", "adminUV@test.com", "-d", json.dumps(invalid_data)]
    )
    assert result.exit_code == -1
    assert "Invalid data" in result.output


# Test CLI's response to an invalid user.
# Expects a non-zero exit code and
# 'Could not get user successfully' error message.
def test_create_draft_records_invalid_user(cli_runner, valid_data):
    result = cli_runner(
        create_draft_records,
        ["-o", "nonexistent@test.com", "-d", json.dumps(valid_data)]
    )
    assert result.exit_code == -1
    assert "Could not get user successfully" in result.output


# Test CLI's response to creating a draft record
# with an existing location.
# Expects a zero exit code and confirmation message
# for using existing location.
def test_create_draft_records_existing_location(cli_runner, valid_data):
    result = cli_runner(
        create_draft_records,
        [
            "-n", "existing-location",
            "-o", "adminUV@test.com",
            "-d", json.dumps(valid_data)
        ]
    )
    assert result.exit_code == 0
    assert (
        "Draft record created with bucket location: existing-location"
        in result.output
    )

    result = cli_runner(
        create_draft_records,
        [
            "-n", "existing-location",
            "-o", "adminUV@test.com",
            "-d", json.dumps(valid_data)
        ]
    )
    assert result.exit_code == 0
    assert (
        "Draft record created with bucket location: existing-location"
        in result.output
    )


# Test CLI's response to location creation failure.
# Expects a non-zero exit code and 'Cannot create or
# retrieve Location' error message.
def test_create_draft_records_location_creation_failure(
        cli_runner, valid_data, mocker):
    # Mock the Location creation to simulate a failure
    mocker.patch(
        'invenio_files_rest.models.Location.query.filter_by'
    ).return_value.one_or_none.return_value = None

    mocker.patch(
        'invenio_db.db.session.commit',
        side_effect=Exception("Database error")
    )

    result = cli_runner(
        create_draft_records,
        [
            "-n", "failing-location",
            "-o", "adminUV@test.com",
            "-d", json.dumps(valid_data)
        ]
    )
    assert result.exit_code == -1
    assert "Cannot create or retrieve Location" in result.output


# Test CLI's response to record creation failure.
# Expects a non-zero exit code, 'Cannot create record' error message
def test_create_draft_records_record_creation_failure(
        cli_runner, valid_data, mocker):
    # Mock the record creation to simulate a failure
    mocker.patch(
        'ultraviolet_cli.proxies.current_rdm_records.records_service.create',
        side_effect=Exception("Record creation error")
    )

    result = cli_runner(
        create_draft_records,
        ["-o", "adminUV@test.com", "-d", json.dumps(valid_data)]
    )
    assert result.exit_code == -1
    assert "Cannot create record" in result.output


# Test CLI's response to record creation failure
# with successful location creation.
# Expects a non-zero exit code, 'Cannot create record' error message,
# and confirmation of location removal.
def test_create_draft_records_location_cleanup_on_failure(
        cli_runner, valid_data, mocker):
    # Mock location creation success but record creation failure
    location_mock = mocker.Mock()
    mocker.patch(
        'invenio_files_rest.models.Location.query.filter_by'
    ).return_value.one_or_none.return_value = None

    mocker.patch(
        'invenio_files_rest.models.Location',
        return_value=location_mock
    )
    mocker.patch(
        'ultraviolet_cli.proxies.current_rdm_records.records_service.create',
        side_effect=Exception("Record creation error")
    )

    result = cli_runner(
        create_draft_records,
        [
            "-n", "cleanup-location",
            "-o", "adminUV@test.com",
            "-d", json.dumps(valid_data)
        ]
    )
    assert result.exit_code == -1
    assert "Cannot create record" in result.output
    assert (
        "Remove created location due to record creation failure"
        in result.output
    )


# Test CLI's response to creating a draft record with the default location.
# Expects a zero exit code and confirmation message for default location.
def test_create_draft_records_default_location(cli_runner, valid_data):
    result = cli_runner(
        create_draft_records,
        ["-o", "adminUV@test.com", "-d", json.dumps(valid_data)]
    )
    assert result.exit_code == 0
    assert "Draft record created with default bucket location" in result.output


# Test CLI's response to creating a draft record with a custom location.
# Expects a zero exit code and confirmation message for custom location.
def test_create_draft_records_custom_location(cli_runner, valid_data):
    result = cli_runner(
        create_draft_records,
        [
            "-n", "custom-location",
            "-o", "adminUV@test.com",
            "-d", json.dumps(valid_data)
        ]
    )
    assert result.exit_code == 0
    assert (
        "Draft record created with bucket location: custom-location"
        in result.output
    )
