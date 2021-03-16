from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from helpers import squash_to_none, convert_to_date

from enumtype import EnumAsInteger 
from enum import Enum
import json

Base = declarative_base()

class Status(Enum):
	UNKNOWN = None
	PENDING = 1 # NEW
	UNREGISTERED = 2
	REGISTERED = 3


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
	parameters = Column(String, default="{}")

	def get_status(self):
		if self.registrar == None:
			return Status.UNKNOWN
		elif self.registrar == "Available":
			return Status.UNREGISTERED
		else:
			return Status.REGISTERED

	def set_whois_data(self, whois_data):
		self.registrar = squash_to_none(whois_data["registrar"])
		self.date_created = convert_to_date(whois_data["created"])
		self.date_expires = convert_to_date(whois_data["expires"])
		self.owner_name = squash_to_none(whois_data["owner_name"])
		self.owner_address = squash_to_none(whois_data["owner_address"])
		self.owner_email = squash_to_none(whois_data["owner_email"])
		self.owner_phone = squash_to_none(whois_data["owner_phone"])
		self.nameserver = squash_to_none(whois_data["nserver"])
	
	def get_json_parameters(self):
		return json.parses(self.parameters)

	def __repr__(self):
		return "<Domain(domainname='%s', registrar='%s', expires='%s', params='%s')>" % (
							self.domainname, self.registrar, self.date_expires, self.parameters)