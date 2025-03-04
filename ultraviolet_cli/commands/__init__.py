# -*- coding: utf-8 -*-
#
# Copyright (C) 2022 NYU Libraries.
#
# ultraviolet-cli is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Invenio module for custom UltraViolet commands."""

from .create_communities import create_communities
from .delete_record_soft import delete_record_soft
from .delete_record_hard import delete_record_hard
from .fixtures import create_record_draft, delete_record_draft, fixtures, \
    ingest, publish_record, purge, validate

__all__ = (
    "create_communities",
    "delete_record_soft",
    "delete_record_hard",
    "create_record_draft",
    "delete_record_draft",
    "publish_record",
    "fixtures",
    "ingest",
    "purge",
    "validate",
    "update_vocabularies",
    'create_draft_records',
)
