# -*- coding: utf-8 -*-
#
# Copyright (C) 2022 NYU Libraries.
#
# ultraviolet-cli is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Proxy definitions."""

import flask
from werkzeug.local import LocalProxy

current_communities = LocalProxy(lambda: flask.current_app.extensions["invenio-communities"])
"""Proxy to the extension."""

current_app = LocalProxy(lambda: flask.current_app)
"""Proxy to the current app."""

current_rdm_records = LocalProxy(lambda: flask.current_app.extensions["invenio-rdm-records"])
"""Proxy to RDM Records module."""
