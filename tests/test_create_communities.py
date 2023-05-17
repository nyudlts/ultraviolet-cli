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
from ultraviolet_cli.commands.create_communities import create_communities


def test_cli_create_communities(cli_runner):
    """Test create user CLI."""

    result = cli_runner(
        create_communities, None, "--desc", "Test Community", "testcommunity"
    )
    assert result.exit_code == 1


# def test_cli_wrong_owner():
#     """Test create user CLI."""
#
#     result = CliRunner().invoke(
#         create_communities, ["--desc", "Test Community",
#         "--owner", "wrongowner@abc.com", "testcommunity"]
#     )
#     assert result.output == 0
#
#
# def test_cli_duplicate_community():
#     """Test create user CLI."""
#
#     result = CliRunner().invoke(
#         create_communities, ["--desc", "Test Community", "testcommunity"]
#     )
#     assert result.output == 0
#     result = CliRunner().invoke(
#         create_communities, ["--desc", "Test Community", "testcommunity"]
#     )
#     assert result.output == 0
