import sys
from pathlib import Path
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

from sklearn.preprocessing import LabelEncoder,OneHotEncoder, StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.compose import make_column_selector
from xgboost import XGBClassifier
import numpy as np

from model_training.config.core import config

preprocess = ColumnTransformer([
    ("onehot", OneHotEncoder(handle_unknown="ignore"), make_column_selector(dtype_include=object)),
    ("scale", StandardScaler(), make_column_selector(dtype_include=np.number)),
])

obesity_risk_pipeline = Pipeline([
    ('preprocess', preprocess), ('xgb', XGBClassifier(objective='multi:softmax', num_class=7, random_state=42))
    ], verbose = True)
