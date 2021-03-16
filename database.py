from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker
from models import Base, Domain
import logging

class BeastModeDB:
	def __init__(self, connection_string):
		self.logger = logging.getLogger(__name__)
		self.session = self.new_session(connection_string=connection_string)

	def new_session(self, connection_string):
		engine = create_engine(connection_string, echo=False)
		Base.metadata.create_all(engine)
		Session = sessionmaker(bind=engine)
		return Session()

	def add_domains(self, domains):
		try:
			self.session.add_all(domains)
			self.session.commit()
		except SQLAlchemyError as e:
			session.rollback()
			self.logger.error("An error occurred while inserting into database")
			self.logger.error(e)
