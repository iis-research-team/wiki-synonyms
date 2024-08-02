import json
from typing import Optional, List, Dict

from src.paths import DATA_PATH


SynonymsList = List[Dict[str, List[str]]]


class DictWorker:

    SYNONYMS = 'synonyms'
    HYPERNYMS = 'hypernym'

    def __init__(self):
        self._data_dict = list()

        for fpath in DATA_PATH.iterdir():
            with open(fpath, 'r') as fin:
                data_dict = json.load(fin)
                self._data_dict.extend(data_dict)

    def get_element_by_synonym(self, synonym: str) -> Optional[dict]:
        for element in self._data_dict:
            if synonym in element[self.SYNONYMS]:
                return element

        return None

    @property
    def data_dict(self):
        return self._data_dict
