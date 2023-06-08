import os
from typing import List, Optional
from typing_extensions import Annotated as Ann

from typer import Argument as Arg


def curl(
    namespace: str,
    service: str,
    path: str,
    curl_args: Ann[Optional[List[str]], Arg()] = None,
):
    from hailtop.auth import hail_credentials  # pylint: disable=import-outside-toplevel
    from hailtop.config import get_deploy_config  # pylint: disable=import-outside-toplevel
    from hailtop.utils import async_to_blocking  # pylint: disable=import-outside-toplevel

    curl_args = curl_args or []
    headers_dict = async_to_blocking(hail_credentials(namespace=namespace).auth_headers())
    headers = [x for k, v in headers_dict.items() for x in ['-H', f'{k}: {v}']]
    path = get_deploy_config().url(service, path)
    os.execvp('curl', ['curl', *headers, *curl_args, path])
