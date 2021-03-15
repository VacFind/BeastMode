# this script parses the data from the existing CSV into the database
# this script is not currently used as it was only needed one time and is here for future reference. it has been placed in this `tools` folder so it is clearly separate
# in order to work it needs to be moved out of this folder due to issues with the imports

from patterns import generate_names
from database import session
from models import Domain
import csv, json
import datetime
print(generate_names("covid{state_name}.{tld}"))

def squash_to_none(value):
	if value in ['-', 'null', '']:
		return None
	else:
		return value

def convert_to_date(value):
	str_date = squash_to_none(value)
	if str_date is None:
		return str_date
	parts = str_date.split("-")
	for part in range(0, len(parts)):
		parts[part] = int(parts[part])
	return datetime.date(*parts)

def clean_domains(value):
	if value.startswith("http://"):
		return value[7:]
	elif value.startswith("https://"):
		return value[8:]
	else:
		return value

# def add

# existing = session.query(Domain).filter(Domain.domainname=='example.com').one_or_none()

csv_header = []

with open('data2.csv', newline='') as f:
	reader = csv.reader(f)
	# print(reader[0])
	for row in reader:
		if csv_header == []:
			csv_header = row
		else:
			dict_form = dict([(csv_header[i], row[i]) for i in range(0,len(csv_header))])
			# print(dict_form)

			params = { 'state': dict_form["State"] }

			domainEntry = Domain(
				domainname=clean_domains(dict_form["domainname"]),
				registrar=squash_to_none(dict_form["Registrar"]),
				date_created=convert_to_date(dict_form["Date Created"]),
				date_expires=convert_to_date(dict_form["Date Expires"]),
				owner_name=squash_to_none(dict_form["Owner Name"]),
				owner_address=squash_to_none(dict_form["Owner Address"]),
				owner_email=squash_to_none(dict_form["Owner Email"]),
				owner_phone=squash_to_none(dict_form["Owner Phone"]),
				nameserver=squash_to_none(dict_form["Nameserver"]),
				parameters=json.dumps(params)
				)
			# {'State': 'U.S. Virgin Islands', 'domainname': 'covidvirginislands.org', 'Registrar': '', 'Date Created': '2020-03-30', 'Date Expires': '', 'Owner Name': '', 'Owner Address': '', 'Owner Email': '', 'Owner Phone': '', 'Nameserver': ''}
			# print(domainEntry)
			session.add(domainEntry)
	session.commit()



# if not existing:
	# print("no record exists")
# test_domain = Domain(domainname="example.com")
# 