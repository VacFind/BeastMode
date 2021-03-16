from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker
from models import Base, Domain

engine = create_engine('sqlite:///domains.db', echo=False)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()


def add_domains(domains, dryrun=False):
	try:
		if not dryrun:
			session.add_all(domains)
			session.commit()
	except SQLAlchemyError as e:
		session.rollback()
		print("An error occurred while inserting into database")
		print(e)
