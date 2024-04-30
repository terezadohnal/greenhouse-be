from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_PASSWORD = 'password'
SQLALCHEMY_DATABASE_URL = f'postgresql://default:fbcIm5DQ8lOu@ep-rough-mouse-a29jwiy8.eu-central-1.aws.neon.tech:5432/verceldb?sslmode=require'
DATABASE_NAME = 'greenhouse'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()