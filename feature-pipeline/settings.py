from dotenv import load_dotenv
import os
from datetime import datetime, timedelta, timezone

# Load environment variables from .env file
load_dotenv()

# Project settings
PROJECT_ID = os.getenv('PROJECT_ID')
BIGQUERY_CREDENTIALS = os.getenv('BIGQUERY_CREDENTIALS')

# BigQuery settings
BQ_SOURCE_DATASET = "DATASET"
BQ_FEATURE_STORE_DATASET = "DATASET"

# GCP Locations
DATASET_LOCATION = 'LOCATION'