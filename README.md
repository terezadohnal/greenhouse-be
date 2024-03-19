# README #

## Database
- run a local PostgreSQL instance on your computer
- create a new database 
  - in psql: `CREATE DATABASE greenhouse;`
- in `database.py` change **DATABASE_PASSWORD** to your password of the default user **postgres** 

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