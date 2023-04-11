import click

from agt import __version__

@click.command(name='version')
def version() -> None:
    """Print the version number and exit."""
    click.echo(__version__)