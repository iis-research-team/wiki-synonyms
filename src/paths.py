from pathlib import Path


file_path = Path(__file__)


PROJECT_PATH = file_path.parent.parent.resolve()
DATA_PATH = PROJECT_PATH / 'data'
INDEX_PATH = PROJECT_PATH / 'index'
