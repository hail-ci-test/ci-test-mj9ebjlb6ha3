import typer
import hailtop

from .auth import cli as auth_cli
from .batch import cli as batch_cli
from .config import cli as config_cli
from .curl import curl
from .describe import describe
from .dataproc import cli as dataproc_cli
from .dev import cli as dev_cli
from .hdinsight import cli as hdinsight_cli


app = typer.Typer(help='Manage and monitor hail deployments.', no_args_is_help=True)

for cli in (
    auth_cli.app,
    batch_cli.app,
    config_cli.app,
    dataproc_cli.app,
    dev_cli.app,
    hdinsight_cli.app,
):
    app.add_typer(cli)


@app.command()
def version():
    '''Print version information and exit.'''
    print(hailtop.version())


app.command(help='Issue authenticated curl requests to Hail infrastructure.')(curl)


app.command(help='Describe Hail Matrix Table and Table files.')(describe)


def main():
    app()
