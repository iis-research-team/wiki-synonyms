import unittest

from src.dict_worker import DictWorker


class DictWorkerTest(unittest.TestCase):

    def setUp(self):
        self._dict_worker = DictWorker()

    def test_dict_worker(self):
        self.assertIsNotNone(self._dict_worker)
        self.assertTrue(len(self._dict_worker.data_dict) > 0)

        element = self._dict_worker.get_element_by_synonym('великолепия амберсонов')
        true_element = {
            "synonyms": [
                "великолепия амберсонов",
                "великолепные эмберсоны"
            ],
            "hypernym": [
                "художественный фильм"
            ]
        }

        self.assertTrue(element == true_element)
