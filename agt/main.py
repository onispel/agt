import click
from agt import __version__

import agt.version

@click.group
def main_cli() -> None:
    pass

main_cli.add_command(agt.version.version)

if __name__ == '__main__':
    main_cli()