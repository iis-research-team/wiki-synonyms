import shutil
import unittest

from wiki_synonyms.data_worker import DataWorker
from wiki_synonyms.paths import INDEX_PATH


class TestDataWorker(unittest.TestCase):

    def setUp(self):
        self._data_worker = DataWorker()

    def test_extract_elements(self):
        synonym = 'великолепия амберсонов'
        elements = self._data_worker.get_elements_by_synonym(synonym)
        self.assertTrue(len(elements) == 1)

        hypernym = 'художественный фильм'
        elements = self._data_worker.get_elements_by_hypernym(hypernym)
        self.assertTrue(len(elements) == 2)

    def tearDown(self):
        shutil.rmtree(INDEX_PATH)
