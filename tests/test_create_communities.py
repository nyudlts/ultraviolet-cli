# -*- coding: utf-8 -*-
#
# Copyright (C) 2022 NYU Libraries.
#
# ultraviolet-cli is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Tests for Create Communities

See https://pytest-invenio.readthedocs.io/ for documentation on which test
fixtures are available.
"""
from click.testing import CliRunner

from ultraviolet_cli.commands.create_communities import create_communities


def test_cli_create_communities():
    """Test create user CLI."""

    result = CliRunner().invoke(
        create_communities, ["--desc", "Test Community", "testcommunity"]
    )
    assert result.return_value == 0


def test_cli_wrong_owner():
    """Test create user CLI."""

    result = CliRunner().invoke(
        create_communities, ["--desc", "Test Community", "--owner", "wrongowner@abc.com", "testcommunity"]
    )
    assert result.return_value == -1


def test_cli_duplicate_community(app, db, search_clear, cli_runner):
    """Test create user CLI."""

    result = CliRunner().invoke(
        create_communities, ["--desc", "Test Community", "testcommunity"]
    )
    assert result.return_value == 0
    result = CliRunner().invoke(
        create_communities, ["--desc", "Test Community", "testcommunity"]
    )
    assert result.return_value == -2
