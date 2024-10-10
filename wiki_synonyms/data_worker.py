from typing import List

from .data_index.index_builder import IndexBuilder, ElementDict


class DataWorker:

    SYNONIMS_DICT = 'syn'
    HYPERNYM_DICT = 'hyp'

    def __init__(self):
        self._index = IndexBuilder()

    def get_elements_by_synonym(self, synonym: str) -> List[ElementDict]:
        elements = self._index.get_elements(synonym, self.SYNONIMS_DICT)
        return elements

    def get_elements_by_hypernym(self, hypernym: str) -> List[ElementDict]:
        elements = self._index.get_elements(hypernym, self.HYPERNYM_DICT)
        return elements
