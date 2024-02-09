# QUORUM-TEST-ARIANN

## Description
    This is a test project that follows the Quorum specifications. 
    This projects displays the bills and the numbers of supporters and opposers of each bill, and also displays the legislators and the bill they supported and opposed.

## Stack
    - Django Rest Framework
    - ReactJS
    - SQLite

## Installation
### Backend
    - Activate the virtual environment:
        ```
        source quorum-env/bin/activate
        ```
    - Install the requirements:
        ```
        pip install -r requirements.txt
        ```
    - Run the server:
        ```
        python manage.py runserver
        ```

### Frontend
    - Install the dependencies:
        ```
        npm install
        ```
    - Run the server:
        ```
        npm start
        ```

## Usage
### Backend
    - Open the browser and go to the following URL:
        ```
        http://localhost:8000/
        ```
    - The API will be displayed.
    - The bills, legislators, votes and votes_results can be accessed through the following URLs:
        ```
        http://localhost:8000/bill/
        http://localhost:8000/legislator/
        http://localhost:8000/vote/
        http://localhost:8000/vote/results/
        ```
    - The bills, legislators, votes and votes_results can be updated by sending a csv file through the following URLs:
        ```
        http://localhost:8000/bill/import-csv
        http://localhost:8000/legislator/import-csv
        http://localhost:8000/vote/import-csv
        http://localhost:8000/vote/results/import-csv
        ```
    - The bills details, and legislators details can be accessed through the following URLs:
        ```
        http://localhost:8000/bill/list
        http://localhost:8000/legislator/list-bills
        ``` 

### Frontend
    - Open the browser and go to the following URL:
        ```
        http://localhost:3000/
        ```
    - The bills and the legislators will be displayed through the routes:
        ```
        http://localhost:3000/bills
        http://localhost:3000/legislators
        ```
