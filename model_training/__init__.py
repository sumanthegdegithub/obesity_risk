import sys
from pathlib import Path
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

from model_training.config.core import PACKAGE_ROOT, config

__version__ = '0.0.1'