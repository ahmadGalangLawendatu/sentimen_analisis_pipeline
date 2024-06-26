# Final Project Data Sphere 7B

This project aims to build a data pipeline using Airflow, Docker, MongoDB, Sentiment Analysis, and PostgreSQL for data extraction, transformation, and loading processes.

## Setup and Requirements

### Docker and Airflow Setup

1. Ensure Docker is installed on your system.
2. Clone this repository:
3. Run Airflow using Docker Compose:

### Creating Plugins

#### Finnhub Loader Plugin

1. Implement a Python script to extract data from Finnhub API.
2. Configure Airflow to schedule and execute this script as a task.

#### MongoDB Loader Plugin

1. Develop Python code to load data into MongoDB.
2. Integrate this code into Airflow as a plugin to handle data loading tasks.

#### Sentiment Analysis Plugin

1. Create Python code for sentiment analysis using libraries like TextBlob or NLTK.
2. Integrate sentiment analysis tasks into Airflow for processing data.

#### PostgreSQL Loader Plugin

1. Implement Python code to load processed data into PostgreSQL.
2. Configure Airflow to run this code as part of the data pipeline.

## Data Flow Process

1. **Extract from Finnhub and Load to MongoDB:**
- Python code extracts financial news data from Finnhub API.
- Data is stored in MongoDB for further processing.

2. **Sentiment Analysis:**
- Python script reads data from MongoDB.
- Performs sentiment analysis on the text data using NLP libraries.
- Results of sentiment analysis are stored back in MongoDB.

3. **Load Analyzed Data to PostgreSQL:**
- Python script retrieves analyzed data from MongoDB.
- Loads the analyzed data into PostgreSQL database for storage and further analysis.

## Running the Pipeline

1. Start Airflow using Docker Compose:
2. Access Airflow UI at `http://localhost:8080` and monitor task executions.
3. Trigger the pipeline manually or set up schedules for automated execution.
