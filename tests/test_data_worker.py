import unittest

from src.data_worker import DataWorker


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
