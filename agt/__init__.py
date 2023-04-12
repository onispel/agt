import importlib.metadata
import boto3

__version__ = importlib.metadata.version('agt')

client:boto3.client = boto3.client('glacier')
