Final Project Data Sphere 7B
This project aims to build a data pipeline using Airflow, Docker, MongoDB, Sentiment Analysis, and PostgreSQL for data extraction, transformation, and loading processes.

Setup and Requirements
Docker and Airflow Setup
Ensure Docker is installed on your system.
Clone this repository:
bash
Salin kode
git clone https://github.com/ahmadGalangLawendatu/sentimen_analisis_pipeline.git
cd sentimen_analisis_pipeline
Run Airflow using Docker Compose:
Salin kode
docker-compose up
This command will start Airflow along with PostgreSQL and other necessary services defined in docker-compose.yml.
Creating Plugins
Finnhub Loader Plugin
Implement a Python script to extract data from Finnhub API.
Configure Airflow to schedule and execute this script as a task.
MongoDB Loader Plugin
Develop Python code to load data into MongoDB.
Integrate this code into Airflow as a plugin to handle data loading tasks.
Sentiment Analysis Plugin
Create Python code for sentiment analysis using libraries like TextBlob or NLTK.
Integrate sentiment analysis tasks into Airflow for processing data.
PostgreSQL Loader Plugin
Implement Python code to load processed data into PostgreSQL.
Configure Airflow to run this code as part of the data pipeline.
Data Flow Process
Extract from Finnhub and Load to MongoDB:

Python code extracts financial news data from Finnhub API.
Data is stored in MongoDB for further processing.
Sentiment Analysis:

Python script reads data from MongoDB.
Performs sentiment analysis on the text data using NLP libraries.
Results of sentiment analysis are stored back in MongoDB.
Load Analyzed Data to PostgreSQL:

Python script retrieves analyzed data from MongoDB.
Loads the analyzed data into PostgreSQL database for storage and further analysis.
Running the Pipeline
Start Airflow using Docker Compose:
Salin kode
docker-compose up
Access Airflow UI at http://localhost:8080 and monitor task executions.
Trigger the pipeline manually or set up schedules for automated execution.
Contributing
Feel free to contribute by forking this repository, making improvements, and creating pull requests. For major changes, please open an issue first to discuss what you would like to change.
