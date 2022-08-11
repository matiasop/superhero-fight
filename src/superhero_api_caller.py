from requests import get, Response
from typing import Any, Optional


class SuperheroAPICaller:
    api_url = "https://www.superheroapi.com/api/"
    access_token = "2183127771827858"

    @classmethod
    def get_response(cls, url: str) -> dict[str, Any]:
        response: Response = get(url)
        data: dict[str, Any] = response.json()
        return data

    @classmethod
    def get_name(cls, id: int) -> str:
        url: str = f"{cls.api_url}{cls.access_token}/{id}"
        data: dict[str, Any] = SuperheroAPICaller.get_response(url)
        name: str = data["name"]

        return name

    @classmethod
    def get_powerstats(cls, id: int) -> Optional[dict[str, int]]:
        url: str = f"{cls.api_url}{cls.access_token}/{id}/powerstats"
        data: dict[str, Any] = SuperheroAPICaller.get_response(url)

        for key in ["response", "id", "name"]:
            data.pop(key)

        if "null" in data.values():
            return None

        powerstats: dict[str, int] = {power: int(data[power]) for power in data}

        return powerstats

    @classmethod
    def get_alignment(cls, id) -> Optional[str]:
        url: str = f"{cls.api_url}{cls.access_token}/{id}/biography"
        data: dict[str, Any] = SuperheroAPICaller.get_response(url)
        alignment = data["alignment"]

        if alignment not in ["good", "bad"]:
            return None

        return alignment
