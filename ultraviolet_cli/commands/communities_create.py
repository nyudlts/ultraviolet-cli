import click
from flask import current_app
from flask.cli import with_appcontext
import json

from ..proxies import current_app
from ..utils import create_community_data
from ..tasks import create_community, add_role_to_community


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
    help="Automatically adds the Group to the community. Group/Role needs to be provided as input and "
         "needs to be created prior. Adds the given group as a reader by default",
)
@click.argument('name')
@with_appcontext
def create_communities(desc, type, visibility, policy, owner, add_group, name):
    """Create a community for Ultraviolet"""
    click.secho("Creating community...", fg="yellow")

    community_data = create_community_data(name, desc, type, visibility, policy)
    click.secho(f"Created community data:\n{json.dumps(community_data, indent=2)}", fg="green")
    community = create_community(community_data, owner)
    click.secho(f"Created community {name} successfully with ID: {community.id}. Optionally, you can append this ID "
                f"to COMMUNITIES_AUTO_UPDATE list in invenio.cfg to setup automatic update of community group "
                f"members.", fg="green")
    if add_group:
        click.secho(f"Adding group {add_group} to community...", fg="yellow")
        add_role_to_community(community, add_group, "reader", True)
        click.secho(f"Added role {add_group} successfully", fg="green")
