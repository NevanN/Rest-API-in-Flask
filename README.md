# CPSC 449 - Assignment 1

### Developing a REST API in Flask for CPSC 449 Web Backend Engineering

## Usage

1. Clone the repository

   - `$ git clone https://github.com/alexislayvu/cpsc449-assignment1.git`

2. Navigate to the directory

   - `$ cd cpsc449-assignment1`

3. Create and activate a virtual environment

   - `$ python -m venv .venv`
   - `$ source .venv/bin/activate`

4. Install dependencies

   - `$ pip install -r requirements.txt`

5. Set up MySQL database

   - Log into MySQL
     - `$ mysql -u root -p`
   - Create database and tables
     - `mysql> source schema.sql`

6. Provide your MySQL password

   - Open `example.env` and replace `your_mysql_password` with your MySQL password
   - Rename `example.env` to `.env`

7. Run the Flask application

   - `python main.py`
