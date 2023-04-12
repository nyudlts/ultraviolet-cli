# -*- coding: utf-8 -*-
#
# Copyright (C) 2022 NYU Libraries.
#
# ultraviolet-cli is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Invenio module for custom Ultravaiolet commands"""

from .ext import ultravioletcli
from .version import __version__
from .proxies import current_communities

__all__ = ('__version__', 'ultravioletcli', 'current_communities')
