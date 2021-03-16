from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker
from models import Base, Domain
import logging

engine = create_engine('sqlite:///domains.db', echo=False)
logger = logging.getLogger(__name__)

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
		logger.error("An error occurred while inserting into database")
		logger.error(e)
