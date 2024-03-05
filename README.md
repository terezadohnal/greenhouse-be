# README #
### How to run Fast API server ###

## Requirements ##
- Python 3.x
- FastAPI
- uvicorn

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