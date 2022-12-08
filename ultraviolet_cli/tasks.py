# -*- coding: utf-8 -*-
#
# Copyright (C) 2022 NYU Libraries.
#
# ultraviolet-cli is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

from .proxies import current_communities
from flask import current_app
from invenio_access.utils import get_identity
from invenio_pidstore.errors import PIDAlreadyExists
from invenio_accounts.models import User
from invenio_access.permissions import system_identity


def create_community(data, owner):
    """Create a demo community."""
    service = current_communities.service
    try:
        owner_identity = get_identity(User.query.filter_by(email=owner).one())
        community = service.create(data=data, identity=owner_identity)
        return community
    except PIDAlreadyExists:
        pass


def add_role_to_community(community, group, role, visibility):
    """Add a role to a community."""
    members_service = current_communities.service.members
    members_service.add(
        system_identity,
        community.id,
        {
            "members": [
                {"type": "group", "id": group}
            ],
            "role": role,
            "visible": visibility,
        },
    )



