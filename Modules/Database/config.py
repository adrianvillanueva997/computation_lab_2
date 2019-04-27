from sqlalchemy import create_engine

ip = '51.15.59.15/proyecto_computacion?charset=utf8mb4'
username = 'proy_comp'
password = 'teoguapo'
engine = create_engine(f"mysql+mysqldb://{username}:{password}@{ip}", encoding='utf-8')
