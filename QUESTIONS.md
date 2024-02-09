## QUESTIONS

### 1. Discuss your strategy and decisions implementing the application.Please,consider time complexity, effort cost, technologies used and any other variable that you understand important on your development process.

I used the following technologies:
- Python
- Django
- Django Rest Framework
- JavaScript
- ReactJS
- SQLite

I chose these technologies because I have experience with them and I believe they are the best for this project, as using them we can create a project from the ground-up pretty fast. I used Django Rest Framework to create the API and ReactJS to create the frontend. I used SQLite as the database because it is easy to use and it is the default database for Django.

I created the following models:
- Bill
- Legislator
- Vote
- VoteResult

I created the endpoints to access the models and to import the data from the csv files. I also created the endpoints to access the bills details and the legislators details.

I chose to import the data from the csv files to the database because it can perform the query faster than reading the csv file every time the user wants to access the data. The time complexity of importing the data from the csv file is O(n), where n is the number of rows in the csv file. The time complexity of reading the csv file every time the user wants to access the data is O(n*m), where n is the number of rows in the csv file and m is the number of times the user wants to access the data.

### 2. How would you change your solution to account for future columns that might be requested, such as “Bill Voted On Date” or “Co-Sponsors”?

I would change the solution to account for future columns by adding the new columns to the models and to the csv files. I would also add the new columns to the serializers and to the views. I would also add the new columns to the frontend.

The solution is well structured and it is easy to add new columns to the models and to the csv files.

### 3. How would you change your solution if instead of receiving CSVs of data,you were given a list of legislators or bills that you should generate a CSV for?

I would add the new endpoints to receive the list of legislators or bills, then add a new endpoint to generate the csv file. I would also add options to the frontend, to facilitate the user to access the new endpoints.

### 4. How long did you spend working on the assignment?

I spent close to 6 hours working on the assignment.