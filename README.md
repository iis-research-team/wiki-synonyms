# wiki-synonyms

This tool allows to search for the synonyms in Russian.

## Installation

To install with pip run:
```commandline
pip install wiki-synonyms
```

## Use cases

Firstly, initialize the DictWorker:

```python
from wiki_synonyms import DataWorker

dw = DataWorker()
```

To search for the synonyms:

```python
synonyms = dw.get_elements_by_synonym('машинное обучение')
```

To search for the hypernyms:
```python
hypernyms = dw.get_elements_by_hypernym('художественный фильм')
```

## Contact
You can contact us via e-mail: bruches@bk.ru
