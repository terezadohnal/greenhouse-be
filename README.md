# README #

## Database
1. **run a local PostgreSQL instance on your computer**
   - if you have postgresql already installed on your computer, go to step 2
   - install PostgreSQL on your computer [link](https://www.postgresql.org/download/) and go to step 2
   - OR run PostgreSQL in docker `docker run --rm --name postgres -p 5433:5432 -e POSTGRES_PASSWORD=123 postgres`
      - you may need to change the command a bit
      - then you need to add port to database.py after `localhost`, e.g. `localhost:5433`
2. **create a new database**
   - in psql console: `CREATE DATABASE greenhouse;`
3. in `database.py` change **DATABASE_PASSWORD** to your password of the user **postgres** 

## Installation ##
1. Clone this repository and navigate to the directory:
```sh
git clone https://github.com/terezadohnal/greenhouse-be.git
```

2. Create a virtual environment:
```sh
python3 -m venv venv
source venv/bin/activate
```

2. Install dependencies:
```sh
pip install -r requirements.txt
```

2. Start the server:

```sh
uvicorn main:app --port 3000 --reload
```


## Security Considerations ##

- Ensure that your API key is kept private and not shared with unauthorized users.

## Performance Considerations ##

- Consider using a load balancer or scaling up the number of worker processes to handle high traffic loads.