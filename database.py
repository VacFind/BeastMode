from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker
from models import Base, Domain
import logging

logger = logging.getLogger(__name__)

def new_session(connection_string='sqlite:///domains.db'):
	engine = create_engine(connection_string, echo=False)
	Base.metadata.create_all(engine)
	Session = sessionmaker(bind=engine)
	return Session()



def add_domains(domains, dryrun=False):
	try:
		if not dryrun:
			session.add_all(domains)
			session.commit()
	except SQLAlchemyError as e:
		session.rollback()
		logger.error("An error occurred while inserting into database")
		logger.error(e)
