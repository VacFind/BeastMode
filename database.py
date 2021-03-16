from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Domain

engine = create_engine('sqlite:///domains.db', echo=False)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()


def add_domains(domains):
	session.add_all(domains)
	session.commit()

