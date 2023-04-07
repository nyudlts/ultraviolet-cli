from ultraviolet_cli.commands.communities_create import communities_create


def test_cli_create_communities(app):
    """Test create user CLI."""
    runner = app.test_cli_runner()

    result = runner.invoke(communities_create.create_communities, ["testcommunity", "--desc", "Test Community"])
    assert result.exit_code != 0
