import os

from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv(verbose=True)
ip = os.getenv('IP')
username = os.getenv('USERNAME')
password = os.getenv('PASSWORD')
engine = create_engine(f"mysql+mysqldb://{username}:{password}@{ip}", encoding='utf-8')
