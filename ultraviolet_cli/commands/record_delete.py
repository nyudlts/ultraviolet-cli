import click
from flask.cli import with_appcontext
from invenio_access.permissions import system_identity

from ultraviolet_cli.proxies import current_rdm_records


@click.command()
@click.argument('pid')
@with_appcontext
def record_delete(pid):
    """Delete Record from Ultraviolet"""
    try:
        current_rdm_records.records_service.delete(system_identity, pid)
    except Exception:
        click.secho(f"Could not delete record: PID {pid} not found", fg="red")
        return False
    click.secho(f"Deleted record {pid} successfully",fg="green")
    return True
