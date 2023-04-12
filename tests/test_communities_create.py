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
from ultraviolet_cli.commands.communities_create import create_communities


def test_cli_create_communities(app):
    """Test create user CLI."""
    runner = app.test_cli_runner()

    result = runner.invoke(
        create_communities, ["testcommunity", "--desc", "Test Community"]
    )
    assert result.exit_code != 0
