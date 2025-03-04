import pytest

from ultraviolet_cli.commands.delete_record_soft import delete_record_soft
from ultraviolet_cli.proxies import current_rdm_records


@pytest.mark.parametrize("removal_reason_id,note", [
    ("retracted", "Officially removed by NYU staff."),
])
def test_delete_record_soft(
    running_app,
    minimal_record,
    cli_runner,
    removal_reason_id,
    note
):
    """Create a record, publish it, then delete it using the CLI."""
    # Use the superuser identity from running_app
    identity = running_app.superuser_identity

    # 1. Create a draft record
    draft = current_rdm_records.records_service.create(
        identity=identity,
        data=minimal_record
    )

    # 2. Publish the record
    published = current_rdm_records.records_service.publish(
        identity=identity,
        id_=draft.id
    )
    pid = published["id"]

    # 3. Invoke the CLI command to soft-delete the record
    result = cli_runner(
        delete_record_soft,
        [pid, removal_reason_id, note]
    )

    # 4. Assert CLI command returned 0 (success)
    assert result.exit_code == 0
    assert (f"Deleted record {pid} successfully "
            "(tombstone created).") in result.output
