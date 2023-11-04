import requests
import os
from typing import NewType
from typing import Any
import pandas

Json = NewType('Json', dict[str, Any])

class Concept2ApiManager(object):
    def __init__(self):
        self.auth_token = os.getenv('C2_TOKEN')
        self.base_url = 'https://log.concept2.com/api/'

    def __add_auth_header(self, headers: dict[str, str]) -> dict[str, str]:
        headers['Authorization'] = f'Bearer {self.auth_token}'
        return headers

    def get(self, endpoint: str) -> Json:
        headers = self.__add_auth_header(headers={})
        r = requests.get(self.base_url + endpoint, headers=headers)
        r.raise_for_status()
        return r.json()


def get_results_list(api_manager: Concept2ApiManager) -> Json:
    endpoint: str = 'users/me/results'
    results: Json = api_manager.get(endpoint)
    return results

def get_strokes_info(api_manager: Concept2ApiManager, result_id: int) -> Json:
    endpoint: str = f'users/me/results/{result_id}/strokes'
    strokes: Json = api_manager.get(endpoint)
    return strokes

if __name__ == '__main__':
    api_manager: Concept2ApiManager = Concept2ApiManager()
    results: Json = get_results_list(api_manager)
    df = pandas.DataFrame.from_dict(results['data'])
    pandas.options.display.max_columns = 999
    print(df.head())
