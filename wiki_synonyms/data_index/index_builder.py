import json
import logging
from collections import defaultdict
import time
from typing import Dict, List, Tuple, Set, Literal

from ..paths import DATA_PATH

ElementDict = Dict[str, List[str]]
IndexDict = Dict[str, Set[int]]
DictName = Literal['syn', 'hyp']


class IndexBuilder:
    SYNONYMS_FIELD = 'synonyms'
    HYPERNYM_FIELD = 'hypernym'

    def __init__(self) -> None:

        logging.info('Start building indices')

        self._data_dict = list()
        for fpath in DATA_PATH.iterdir():
            if fpath.suffix != '.json':
                continue
            with open(fpath, 'r', encoding='utf-8') as fin:
                data_dict = json.load(fin)
                self._data_dict.extend(data_dict)

        self._id2element = self._build_id2element()
        self._syn_text2id_element, self._hyp_text2id_element = self._build_text_index()

        del self._data_dict

    def get_elements(self, text: str, dict_name: DictName
                     ) -> List[ElementDict]:
        ids_element = []
        if dict_name == 'syn':
            ids_element = self._syn_text2id_element.get(text, None)
        elif dict_name == 'hyp':
            ids_element = self._hyp_text2id_element.get(text, None)

        elements = []
        if ids_element is not None:
            elements = [self._id2element[id] for id in ids_element]

        return elements

    def _build_id2element(self) -> Dict[int, ElementDict]:
        id2element = {i: element for i, element in enumerate(self._data_dict)}
        return id2element

    def _build_text_index(self) -> Tuple[IndexDict, IndexDict]:
        syn_text2id_element = defaultdict(set)
        hyp_text2id_element = defaultdict(set)

        t0 = time.time()
        for id, element in self._id2element.items():
            for text in element[self.SYNONYMS_FIELD]:
                syn_text2id_element[text].add(id)
            for text in element[self.HYPERNYM_FIELD]:
                hyp_text2id_element[text].add(id)
        t1 = time.time()

        logging.info(f'Built synonyms index with {len(syn_text2id_element)} elements')
        logging.info(f'Built hypernyms index with {len(hyp_text2id_element)} elements')
        logging.info(f'Built text indices for {t1 - t0} secs')

        return syn_text2id_element, hyp_text2id_element
