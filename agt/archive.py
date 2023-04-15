from pydoc import cli
import click,json
from agt import client

def delete_archive(vault_name: str, archive_id: str) -> dict:
    """Delete an archive"""
    response = client.delete_archive(vaultName=vault_name, archiveId=archive_id)
    return response

@click.group(name='archive')
def archive_grp() -> None:
    """Archive"""
    pass

@archive_grp.command(name='delete')
@click.argument('vault_name', required=True)
@click.argument('archive_id', required=True)
def delete_archive_cli(vault_name: str, archive_id: str) -> None:
    """Delete an archive"""

    response = delete_archive(vault_name, archive_id)

    click.echo(response)

@archive_grp.command(name='delete_all')
@click.argument('infile', required=True, type=click.File('r'))
def delete_all_archives_cli(infile: click.File) -> None:
    job_output = json.loads(infile.read())
    vault_arn = job_output['VaultARN']
    vault_name = vault_arn.split('/')[1]
    archive_list = job_output['ArchiveList']
    with click.progressbar(archive_list, label='Deleting archives') as bar:
        for archive in bar:
            archive_id = archive['ArchiveId']
            delete_archive(vault_name, archive_id)
    