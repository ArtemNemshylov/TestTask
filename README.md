# McDonald's Products API

This project consists of two files. The `parcer.py` file is responsible for scraping data from the McDonald's website and saving it in JSON format. The `main.py` file implements a simple web application using FastAPI to serve the data from the JSON file in JSON format.

## Description

### `parcer.py`

The `scraper.py` script scrapes product data from the McDonald's website for the Ukrainian market. It collects information such as product name, description, and nutrient facts, and saves it in a JSON file named `result.json`.

### `main.py`

The `main.py` script implements a basic API using FastAPI to serve the scraped product data. It provides three endpoints:
- `localhost:8000/`: Returns all product data.
- `localhost:8000/{name}`: Returns product data for a specific product by name.
- `localhost:8000/{name}/{key}`: Returns a specific value for a given product and key.

## Requirements

To run this project, you need to have Python installed, along with the following libraries:
- requests
- BeautifulSoup
- FastAPI
- uvicorn

You can install the required libraries using the following command:
`pip install -r requirements.txt`


## Usage

1. Clone the repository to your local machine.
2. Run the `parcer.py` script to scrape product data and generate the `result.json` file.
3. Run the `main.py` script to start the FastAPI server.`uvicorn main:app --reload`
4. Access the API endpoints to retrieve product data.
5. Use 127.0.0.1/docs to work with endpoints

## API Endpoints

- `GET /`: Returns all product data.
- `GET /{name}`: Returns product data for a specific product by name.
- `GET /{name}/{key}`: Returns a specific value for a given product and key.



