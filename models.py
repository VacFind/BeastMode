from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date

Base = declarative_base()

class Domain(Base):
	__tablename__ = 'domains'

	id = Column(Integer, primary_key=True)
	domainname = Column(String, unique=True)
	registrar = Column(String)
	date_created = Column(Date)
	date_expires = Column(Date)
	owner_name = Column(String)
	owner_address = Column(String)
	owner_email = Column(String)
	owner_phone = Column(String)
	nameserver = Column(String)
	parameters = Column(String)

	def __repr__(self):
		return "<Domain(domainname='%s', registrar='%s', expires='%s', params='%s')>" % (
							self.domainname, self.registrar, self.date_expires, self.parameters)