from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date

import EnumAsInteger from enumtype
import Status from models

Base = declarative_base()

class Status(Enum):
    UNKNOWN = None
    PENDING = 1 # NEW
    UNREGISTERED = 2


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
	status = Column(EnumAsInteger(Status), nullable=True)
	parameters = Column(String)

	def __repr__(self):
		return "<Domain(domainname='%s', registrar='%s', expires='%s', params='%s')>" % (
							self.domainname, self.registrar, self.date_expires, self.parameters)