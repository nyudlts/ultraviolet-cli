# -*- coding: utf-8 -*-
#
# Copyright (C) 2022 NYU Libraries.
#
# ultraviolet-cli is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Invenio module for custom UltraViolet commands."""

import json

import click
from flask.cli import with_appcontext

from ultraviolet_cli.tasks import add_role_to_community, create_community
from ultraviolet_cli.utils import create_community_data


@click.command()
@click.option(
    "-d",
    "--desc",
    type=str,
    required=True,
    help="A description of the community to be created",
)
@click.option(
    "-t",
    "--type",
    type=click.Choice(['organization', 'event', 'topic', 'project']),
    show_default=True,
    default="organization",
    help="Type of the Community to be created.",
)
@click.option(
    "-v",
    "--visibility",
    type=click.Choice(['public', 'restricted']),
    show_default=True,
    default="public",
    help="Visibility of the community.",
)
@click.option(
    "-p",
    "--policy",
    type=click.Choice(['open', 'closed']),
    show_default=True,
    default="open",
    help="Policy to be set for the members and records of the community.",
)
@click.option(
    "-o",
    "--owner",
    type=str,
    show_default=True,
    default="owner@nyu.edu",
    help="Email address of the designated owner of the community.",
)
@click.option(
    "-g",
    "--add-group",
    type=str,
    help="Automatically adds the Group to the community. "
         "Group/Role needs to be provided as input and "
         "needs to be created prior. Adds the given group "
         "as a reader by default.",
)
@click.argument('name')
@with_appcontext
def create_communities(desc, type, visibility, policy,
                       owner, add_group, name):
    """Create a community for Ultraviolet."""
    click.secho("Creating community...", fg="yellow")

    community_data = create_community_data(
        name, desc, type, visibility, policy
    )
    click.secho(
        f"Created community data:"
        f"\n{json.dumps(community_data, indent=2)}",
        fg="green"
    )
    community = create_community(community_data, owner)
    click.secho(f"Created community {name} successfully with ID: "
                f"{community.id}. Optionally, you can append this "
                f"ID to COMMUNITIES_AUTO_UPDATE list in invenio.cfg"
                f" to setup automatic update of community group "
                f"members.", fg="green")
    if add_group:
        click.secho(
            f"Adding group {add_group} to community...",
            fg="yellow"
        )
        add_role_to_community(community, add_group, "reader", True)
        click.secho(
            f"Added role {add_group} successfully",
            fg="green"
        )

    return 1
