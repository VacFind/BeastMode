from patterns import generate_domains
from database import add_domains

def generate_from_pattern_file(filename):
	with open(filename, "r") as patterns_file:
		for pattern in patterns_file.readlines():
			process_pattern(pattern)

def process_pattern(pattern):
	pattern = pattern.strip()
	print("processing pattern: " + pattern)
	domains = generate_domains(pattern)
	try:
		add_domains(names)
	except exc.SQLAlchemyError as e:
		print("An error occurred. skipping this pattern")
		print(e)


