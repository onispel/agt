import click

from agt import client

def list_jobs(vault_name: str) -> dict:
    """List all jobs"""
    response = client.list_jobs(vaultName=vault_name)['JobList']
    return response

def describe_job(vault_name: str, job_id: str) -> dict:
    """Describe a job"""
    response = client.describe_job(vaultName=vault_name, jobId=job_id)
    return response

def initiate_job_inventory_retrieval(vault_name: str, job_type: str = 'inventory-retrieval') -> dict:
    """Initiate a job"""
    description = f'Inventory retrieval for vault {vault_name}'
    response = client.initiate_job(
        vaultName=vault_name,
        jobParameters={
            'Type': job_type,
            'Description': description,
        }
    )
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

@jobs_grp.command(name='retrieve')
@click.argument('vault_name', required=True)
@click.option('--inventory', 'job_type', flag_value='inventory-retrieval', default=True, help='Retrieve inventory (default)')
@click.option('--archive', 'job_type', flag_value='archive-retrieval', help='Retrieve archive')
def initiate_retrieve_job_cli(vault_name: str, job_type: str) -> None:
    """Initiate a retrieval job"""
    response = initiate_job_inventory_retrieval(vault_name, job_type)
    click.echo(response)