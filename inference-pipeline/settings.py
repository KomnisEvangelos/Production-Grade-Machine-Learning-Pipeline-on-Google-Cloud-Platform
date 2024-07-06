from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Project settings
PROJECT_ID = os.getenv('PROJECT_ID')
BIGQUERY_CREDENTIALS = os.getenv('BIGQUERY_CREDENTIALS')
CLOUD_STORAGE_CREDENTIALS = os.getenv('CLOUD_STORAGE_CREDENTIALS')

# BigQuery settings
BQ_FEATURE_STORE_DATASET = "STORE"
BQ_PREDICTIONS_DATASET = "DATASET"

# GCP Locations
DATASET_LOCATION = 'LOCATION'

# Cloud Storage settings
GCS_BUCKET_NAME = os.getenv('GCS_BUCKET_NAME')