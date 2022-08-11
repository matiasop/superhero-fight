from decouple import config
from requests import get, Response
from typing import Any, Optional


class SuperheroAPICaller:
    @staticmethod
    def get_response(url: str) -> dict[str, Any]:
        response: Response = get(url)
        data: dict[str, Any] = response.json()
        return data

    @staticmethod
    def get_name(id: int) -> str:
        url: str = f"{config('API_URL')}{config('ACCESS_TOKEN')}/{id}"
        data: dict[str, Any] = SuperheroAPICaller.get_response(url)
        name: str = data["name"]

        return name

    @staticmethod
    def get_powerstats(id: int) -> Optional[dict[str, int]]:
        url: str = f"{config('API_URL')}{config('ACCESS_TOKEN')}/{id}/powerstats"
        data: dict[str, Any] = SuperheroAPICaller.get_response(url)

        for key in ["response", "id", "name"]:
            data.pop(key)

        if "null" in data.values():
            return None

        powerstats: dict[str, int] = {power: int(data[power]) for power in data}

        return powerstats

    @staticmethod
    def get_alignment(id) -> Optional[str]:
        url: str = f"{config('API_URL')}{config('ACCESS_TOKEN')}/{id}/biography"
        data: dict[str, Any] = SuperheroAPICaller.get_response(url)
        alignment = data["alignment"]

        if alignment not in ["good", "bad"]:
            return None

        return alignment
