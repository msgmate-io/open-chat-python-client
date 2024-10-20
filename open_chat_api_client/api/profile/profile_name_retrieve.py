from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.user_profile import UserProfile
from ...types import UNSET, Response, Unset


def _get_kwargs(
    username: str,
    *,
    reveal_secret: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["reveal_secret"] = reveal_secret

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/api/profile/name/{username}/",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[UserProfile]:
    if response.status_code == HTTPStatus.OK:
        response_200 = UserProfile.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[UserProfile]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    username: str,
    *,
    client: AuthenticatedClient,
    reveal_secret: Union[Unset, str] = UNSET,
) -> Response[UserProfile]:
    """
    Args:
        username (str):
        reveal_secret (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UserProfile]
    """

    kwargs = _get_kwargs(
        username=username,
        reveal_secret=reveal_secret,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    username: str,
    *,
    client: AuthenticatedClient,
    reveal_secret: Union[Unset, str] = UNSET,
) -> Optional[UserProfile]:
    """
    Args:
        username (str):
        reveal_secret (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UserProfile
    """

    return sync_detailed(
        username=username,
        client=client,
        reveal_secret=reveal_secret,
    ).parsed


async def asyncio_detailed(
    username: str,
    *,
    client: AuthenticatedClient,
    reveal_secret: Union[Unset, str] = UNSET,
) -> Response[UserProfile]:
    """
    Args:
        username (str):
        reveal_secret (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UserProfile]
    """

    kwargs = _get_kwargs(
        username=username,
        reveal_secret=reveal_secret,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    username: str,
    *,
    client: AuthenticatedClient,
    reveal_secret: Union[Unset, str] = UNSET,
) -> Optional[UserProfile]:
    """
    Args:
        username (str):
        reveal_secret (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UserProfile
    """

    return (
        await asyncio_detailed(
            username=username,
            client=client,
            reveal_secret=reveal_secret,
        )
    ).parsed
