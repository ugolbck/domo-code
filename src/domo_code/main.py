import click
import json

from domo_code.parser import parse_start


@click.group()
def domo():
    """Domo helps you to manage your development environment switches."""
    pass


@domo.command()
@click.argument('filepath', type=click.Path(exists=True, readable=True))
def start(filepath: str = None, ):
    """Start a new development environment."""
    with open(filepath, 'r') as f:
        data = json.load(f)
    parse_start(data)


@domo.command()
@click.argument('file', type=click.Path(exists=True, readable=True))
def stop(file: str = None, ):
    """Stop a development environment."""
    click.echo('Hello, World!')


if __name__ == '__main__':
    domo()
