import click

from agt import client
from agt.format import format_json

def list_jobs(vault_name: str) -> dict:
    """List all jobs of vault"""
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

def get_job_output(vault_name: str, job_id: str) -> dict:
    """Get job output"""
    response = client.get_job_output(vaultName=vault_name, jobId=job_id)
    return response

@click.group(name='jobs')
def jobs_grp() -> None:
    """Jobs"""
    pass

@jobs_grp.command(name='output')
@click.argument('vault_name', required=True)
@click.argument('job_id', required=True)
def get_job_output_cli(vault_name: str, job_id: str) -> None:
    """Get job output"""
    response = get_job_output(vault_name, job_id)
    body = response['body'].read()
    click.echo(body)

@jobs_grp.command(name='list')
@click.argument('vault_name', required=True)
def list_jobs_cli(vault_name: str) -> None:
    """List all jobs"""
    response = list_jobs(vault_name)
    click.echo(format_json(response))

@jobs_grp.command(name='retrieve')
@click.argument('vault_name', required=True)
@click.option('--inventory', 'job_type', flag_value='inventory-retrieval', default=True, help='Retrieve inventory (default)')
@click.option('--archive', 'job_type', flag_value='archive-retrieval', help='Retrieve archive')
def initiate_retrieve_job_cli(vault_name: str, job_type: str) -> None:
    """Initiate a retrieval job"""
    response = initiate_job_inventory_retrieval(vault_name, job_type)
    click.echo(response)