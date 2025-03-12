from pathlib import Path

SRC_DIR = Path(__file__).parent.resolve()
ROOT_DIR = SRC_DIR.parent.resolve()
DATA_DIR = SRC_DIR.joinpath('./data').resolve()
