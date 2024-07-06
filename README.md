# End-to-End Machine Learning Pipeline on Google Cloud Platform:

## Automated Cryptocurrency Price Forecasting:
This repository showcases an automated cryptocurrency forecasting pipeline developed to predict future cryptocurrency prices. The project demonstrates the setup of a complete machine learning pipeline on Google Cloud Platform (GCP).

## Project Architecture

![Project Architecture](https://github.com/michailchionidis/gcp-ml-pipeline/assets/104796421/0d537e37-8d93-4fd2-b06b-fcb83f463db9)

## Skills Demonstrated

- **Data Pipelines:**
  - **Data Extraction:** Utilizes a Cloud Function to extract raw cryptocurrency data from CoinAPI and store it in BigQuery and Cloud Storage.

- **Machine Learning Pipeline:**
  - **Feature Engineering:** Implements a Cloud Function to process raw data into meaningful features stored in BigQuery.
  - **Model Training:** Automates the training process using a Cloud Function. This includes feature extraction from BigQuery, model training with XGBoost, and storing the trained model and scaler in Cloud Storage, effectively using it as a model registry.
  - **Inference:** Deploys a Cloud Function to use the trained models for generating hourly predictions of future cryptocurrency prices.

- **Job Orchestration and Automation:**
  - **Cloud Workflows:** Orchestrates the sequential execution of data fetching, feature engineering, training, and inference pipelines.
  - **Cloud Scheduler:** Automates the execution schedule, ensuring the pipeline runs hourly and the model is retrained daily.

- **Data Visualization:**
  - **Looker Studio:** Visualizes predictions in an interactive dashboard, providing up-to-date data on cryptocurrency prices.

## Technologies Used

- **Python**
- **Google Cloud Platform:** Cloud Functions, Cloud Storage, BigQuery, Cloud Workflows, Cloud Scheduler, Looker Studio
- **Machine Learning Libraries:** scikit-learn, XGBoost

## Acknowledgments

This project is provided by [DataProjects.io](https://dataprojects.io), a platform that helps data professionals build a portfolio of real-world, end-to-end projects on the cloud.

## License

This project is licensed under the Mozilla Public License 2.0 - see the LICENSE file for details.
