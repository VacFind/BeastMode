import datetime

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
