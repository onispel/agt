import click

from agt import client

def list_jobs(vault_name: str) -> dict:
    """List all jobs"""
    response = client.list_jobs(vaultName=vault_name)['JobList']
    return response

@click.group(name='jobs')
def jobs_grp() -> None:
    """Jobs"""
    pass

@jobs_grp.command(name='list')
@click.argument('vault_name', required=True)
def list_jobs_cli(vault_name: str) -> None:
    """List all jobs"""
    response = list_jobs(vault_name)
    click.echo(response)