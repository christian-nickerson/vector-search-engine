import asyncio
from typing import List

from httpx import AsyncClient, Client, Response
from jinja2 import Environment, FileSystemLoader, Template
from pandas import isna

from src.config import settings
from src.data import NikeDataset


class APIClient:

    """Client for making requests to the vector engine API"""

    def __init__(self) -> None:
        self.jinja = Environment(loader=FileSystemLoader(settings.templates.dir))

    def _get_product_template(self) -> Template:
        """get add product graphql mutation template

        :return: add_product jinja template
        """
        return self.jinja.get_template(settings.templates.add_product)

    def _get_similarity_template(self) -> Template:
        """get similarity search graphql query template

        :return: similarity_search jinja template
        """
        return self.jinja.get_template(settings.templates.similarity_search)

    def _get_records(self) -> List[dict]:
        """Get records to populate database with"""
        data = []
        df_dict = NikeDataset().df.to_dict("records")
        for dict in df_dict:
            cleaned = {k: dict[k] for k in dict if not isna(dict[k])}
            data.append(cleaned)
        return data

    async def async_graphql_post(self, query_list: List[str]) -> List[Response]:
        """Async post calls to the GraphQL API.

        :param query_list: _description_
        :return: response
        """
        async with AsyncClient(base_url=settings.api.url) as client:
            tasks = [client.post("/graphql", json={"query": body}) for body in query_list]
            response_list = await asyncio.gather(*tasks)
        for response in response_list:
            print(response.json())
            if response.status_code != 200:
                raise response.raise_for_status()
        return response_list

    def build_db(self) -> None:
        """Build database records"""
        template = self._get_product_template()
        data = self._get_records()
        records = [template.render(**record) for record in data]
        asyncio.run(self.async_graphql_post(records))

    def search_query(self, text: str) -> Response:
        """search query request

        :param text: text to search vector db with
        :return: search response
        """
        template = self._get_similarity_template()
        query = template.render(text=text)
        with Client(base_url=settings.api.url) as client:
            response = client.post("/graphql", json={"query": query})
        if response.status_code == 200:
            return response.json()
        else:
            raise response.raise_for_status()
