import click

from agt import __version__

@click.command(name='version')
def version() -> None:
    click.echo(__version__)