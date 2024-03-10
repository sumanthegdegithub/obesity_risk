from typing import Any, List, Optional
import datetime

from pydantic import BaseModel
from model_training.processing.validation import DataInputSchema


class PredictionResults(BaseModel):
    errors: Optional[Any]
    version: str
    #predictions: Optional[List[int]]
    predictions: Optional[int]


class MultipleDataInputs(BaseModel):
    inputs: List[DataInputSchema]

    class Config:
        schema_extra = {
            "example": {
                "inputs": [
                    {
                    'Gender':'Male',
                    'Age':24.443011,
                    'Height': 1.699998,
                    'Weight': 81.66995,
                    'family_history_with_overweight': 'yes',
                    'FAVC': 'yes',
                    'FCVC': 2,
                    'NCP': 2.983297,
                    'CAEC': 'Sometimes',
                    'SMOKE': 'no',
                    'CH2O': 2.763573,
                    'SCC': 'no',
                    'FAF': 0,
                    'TUE': 0.976473,
                    'CALC': 'Sometimes',
                    'MTRANS' : 'Public_Transportation',
                    }
                ]
            }
        }
