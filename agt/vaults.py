import click

from agt import client
from agt.format import format_vaults_table, format_vaults_json


def list_vaults() -> dict:
    """List all vaults"""
    response = client.list_vaults()['VaultList']
    return response


@click.group(name='vaults')
def vaults_grp() -> None:
    """Vaults"""
    pass

@vaults_grp.command(name='list')
@click.option('--table', 'outfmt', flag_value='table', default=True, help='Show table (default)')
@click.option('--json', 'outfmt', flag_value='json', help='Show json')
def list_vaults_cli(outfmt) -> None:
    """List all vaults"""

    response = list_vaults()

    match outfmt:
        case 'table': output = format_vaults_table(response,exclude=['VaultARN'],fmt='psql')
        case 'json': output = format_vaults_json(response)

    click.echo(output)

