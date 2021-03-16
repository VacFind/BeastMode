from patterns import generate_domains
from database import add_domains

import argparse

parser = argparse.ArgumentParser(description='generate and check a list of domains from patterns')
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('--patternfile', type=str)
group.add_argument('--pattern', "-p", type=str)
parser.add_argument("--dryrun", "-n", action="store_true")


def generate_from_pattern_file(filename, dryrun=False):
	with open(filename, "r") as patterns_file:
		for pattern in patterns_file.readlines():
			process_pattern(pattern, dryrun=dryrun)

def process_pattern(pattern, dryrun=False):
	pattern = pattern.strip()
	print("processing pattern: " + pattern)
	domains = generate_domains(pattern)
	if not dryrun:
		try:
			add_domains(names)
		except exc.SQLAlchemyError as e:
			print("An error occurred. skipping this pattern")
			print(e)
	else:
		print("Would process " + str(len(domains)) + " domains")


