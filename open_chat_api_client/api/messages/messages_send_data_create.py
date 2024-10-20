from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.message import Message
from ...models.send_data_message import SendDataMessage
from ...types import Response


def _get_kwargs(
    chat_uuid: str,
    *,
    body: SendDataMessage,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": f"/api/messages/{chat_uuid}/send_data/",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Message]:
    if response.status_code == HTTPStatus.OK:
        response_200 = Message.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Message]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    chat_uuid: str,
    *,
    client: AuthenticatedClient,
    body: SendDataMessage,
) -> Response[Message]:
    """Simple Viewset messages CREATE, LIST, UPDATE, DELETE

    Args:
        chat_uuid (str):
        body (SendDataMessage):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Message]
    """

    kwargs = _get_kwargs(
        chat_uuid=chat_uuid,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    chat_uuid: str,
    *,
    client: AuthenticatedClient,
    body: SendDataMessage,
) -> Optional[Message]:
    """Simple Viewset messages CREATE, LIST, UPDATE, DELETE

    Args:
        chat_uuid (str):
        body (SendDataMessage):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Message
    """

    return sync_detailed(
        chat_uuid=chat_uuid,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    chat_uuid: str,
    *,
    client: AuthenticatedClient,
    body: SendDataMessage,
) -> Response[Message]:
    """Simple Viewset messages CREATE, LIST, UPDATE, DELETE

    Args:
        chat_uuid (str):
        body (SendDataMessage):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Message]
    """

    kwargs = _get_kwargs(
        chat_uuid=chat_uuid,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    chat_uuid: str,
    *,
    client: AuthenticatedClient,
    body: SendDataMessage,
) -> Optional[Message]:
    """Simple Viewset messages CREATE, LIST, UPDATE, DELETE

    Args:
        chat_uuid (str):
        body (SendDataMessage):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Message
    """

    return (
        await asyncio_detailed(
            chat_uuid=chat_uuid,
            client=client,
            body=body,
        )
    ).parsed
