import requests
import json


class SchemaRegistryAPI:
    BASE_URL = "http://schemaregistry.example.com"
    HEADERS = {
        "Accept": "application/vnd.schemaregistry.v1+json, application/vnd.schemaregistry+json, application/json"
    }

    def __init__(self):
        pass

    def _handle_response(self, response):
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 404:
            raise Exception("Error code 40403 - Schema not found")
        elif response.status_code == 500:
            raise Exception("Error code 50001 - Error in the backend datastore")
        else:
            response.raise_for_status()

    def get_schema_by_id(self, id, subject=None):
        url = f"{self.BASE_URL}/schemas/ids/{id}"
        if subject:
            url += f"?subject={subject}"
        response = requests.get(url, headers=self.HEADERS)
        return self._handle_response(response)

    def get_only_schema_by_id(self, id, subject=None):
        url = f"{self.BASE_URL}/schemas/ids/{id}/schema"
        if subject:
            url += f"?subject={subject}"
        response = requests.get(url, headers=self.HEADERS)
        return self._handle_response(response)

    def get_schema_types(self):
        url = f"{self.BASE_URL}/schemas/types"
        response = requests.get(url, headers=self.HEADERS)
        return self._handle_response(response)

    def get_versions_by_id(self, id):
        url = f"{self.BASE_URL}/schemas/ids/{id}/versions"
        response = requests.get(url, headers=self.HEADERS)
        return self._handle_response(response)
