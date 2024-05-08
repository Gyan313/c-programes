# Data Ingestion -----> refers to "reading data" from a source which can be anything.
# All the code for dividing data into train and test dataset for training ML model purpose.
# All the code for that we will be writing over here in this file.

import os

# importing sys to use the CustomException module we created.
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split

from dataclasses import dataclass
