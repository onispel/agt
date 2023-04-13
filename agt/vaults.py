import click

from agt import client
from agt.format import format_table, format_json, format_list


def list_vaults() -> dict:
    """List all vaults"""
    response = client.list_vaults()['VaultList']
    return response

def describe_vault(vault_name: str) -> dict:
    """Describe a vault"""
    response = client.describe_vault(vaultName=vault_name)
    return response


@click.group(name='vaults')
def vaults_grp() -> None:
    """Vaults"""
    pass

@vaults_grp.command(name='list')
@click.option('--table', 'outfmt', flag_value='table', default=True, help='Show table (default)')
@click.option('--list', 'outfmt', flag_value='list', default=True, help='Show list')
@click.option('--json', 'outfmt', flag_value='json', help='Show json')
def list_vaults_cli(outfmt) -> None:
    """List all vaults"""

    response = list_vaults()

    match outfmt:
        case 'table': output = format_table(response,exclude=['VaultARN'],fmt='psql')
        case 'list': output = format_list(response,exclude=['VaultARN'],fmt='psql')
        case 'json': output = format_json(response)

    click.echo(output)


@vaults_grp.command(name='describe')
@click.argument('vault_name')
@click.option('--table', 'outfmt', flag_value='table', help='Show table')
@click.option('--list', 'outfmt', flag_value='list', default=True, help='Show json (default)')
@click.option('--json', 'outfmt', flag_value='json', help='Show json (default)')
def describe_vault_cli(vault_name: str, outfmt:str) -> None:
    """Describe a vault"""

    response = describe_vault(vault_name)

    match outfmt:
        case 'table': output = format_table(response,exclude=['VaultARN','ResponseMetadata'],fmt='psql')
        case 'list': output = format_list(response,exclude=['VaultARN','ResponseMetadata'],fmt='psql')
        case 'json': output = format_json(response)

    click.echo(output)