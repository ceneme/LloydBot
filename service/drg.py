import json
#from logging import Logger
import requests
from model.deepdives import DeepDives
from model.salutes import Salutes
from util.constants import (
    DRG_API_BASE_URL,
    DRG_API_VERSION,
    DRG_API_DEEPDIVES_ENDPOINT,
    DRG_API_SALUTES_ENDPOINT,
    DRG_API_TIMEOUT_SECONDS
    )


class DRGService():
    def __init__(self):
        #self.logger: Logger = logger.getChild('DRGService')
        self.base_url: str = DRG_API_BASE_URL
        self.version: str = DRG_API_VERSION
        self.deepdives_endpoint: str = DRG_API_DEEPDIVES_ENDPOINT
        self.salutes_endpoint: str = DRG_API_SALUTES_ENDPOINT
        self.timeout: int = DRG_API_TIMEOUT_SECONDS

    def get_deepdives(self) -> DeepDives:
        response = requests.get(url=f'{self.base_url}{self.version}{self.deepdives_endpoint}',
                                timeout=self.timeout)
        if response.status_code == 200:
            data = json.loads(response.text)
            return DeepDives.parse_obj(data)

        
        return None

    def get_salutes(self) -> Salutes:
        response = requests.get(url=f'{self.base_url}{self.version}{self.salutes_endpoint}',
                                timeout=self.timeout)
        if response.status_code == 200:
            data = json.loads(response.text)
            return Salutes.parse_obj(data)

        return None