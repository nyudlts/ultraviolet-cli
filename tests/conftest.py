# -*- coding: utf-8 -*-
#
# Copyright (C) 2022 NYU Libraries.
#
# ultraviolet-cli is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Pytest configuration.

See https://pytest-invenio.readthedocs.io/ for documentation on which test
fixtures are available.
"""
import pytest
from invenio_app.factory import create_app as create_ui_api


@pytest.fixture(scope='module')
def celery_config():
    """Override pytest-invenio fixture.

    TODO: Remove this fixture if you add Celery support.
    """
    return {}


@pytest.fixture(scope='module')
def create_app():
    """Create an API and UI for testing Invenio related features."""
    return create_ui_api


# @pytest.fixture(scope="module")
# def cli_runner(base_app):
#     """Create a CLI runner for testing a CLI command."""
#
#     def cli_invoke(command, *args, input=None):
#         return base_app.test_cli_runner().invoke(command, args, input=input)
#
#     return cli_invoke
