# -*- coding: utf-8 -*-
#
# Copyright (C) 2022 NYU Libraries.
#
# ultraviolet-cli is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Module tests."""

from flask import Flask

from ultraviolet_cli import ultravioletcli


def test_version():
    """Test version import."""
    from ultraviolet_cli import __version__
    assert __version__


def test_init():
    """Test extension initialization."""
    app = Flask('testapp')
    ext = ultravioletcli(app)
    assert 'ultraviolet-cli' in app.extensions

    app = Flask('testapp')
    ext = ultravioletcli()
    assert 'ultraviolet-cli' not in app.extensions
    ext.init_app(app)
    assert 'ultraviolet-cli' in app.extensions
