import click

import agt
from agt import (
    version,
    vaults,
    jobs,
    archive,
    )


#read AccessKey and SecretKey from environment variables
# AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
# AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')


@click.group
def main_cli() -> None:
    """AWS Glacier Tools CLI"""

    pass

main_cli.add_command(version.version)
main_cli.add_command(vaults.vaults_grp)
main_cli.add_command(jobs.jobs_grp)
main_cli.add_command(archive.archive_grp)

if __name__ == '__main__':

    main_cli()