from ultraviolet_cli.commands.communities_create import create_communities


def test_cli_create_communities(app):
    """Test create user CLI."""
    runner = app.test_cli_runner()

    result = runner.invoke(create_communities, ["testcommunity", "--desc", "Test Community"])
    assert result.exit_code != 0
