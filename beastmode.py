from patterns import generate_domains
from database import add_domains

import argparse

parser = argparse.ArgumentParser(description='generate and check a list of domains from patterns')
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('--file', type=str, help='import domains using a file with one pattern per line. mutually exclusive with --pattern')
group.add_argument('--pattern', "-p", type=str,  help='import domains from a single pattern string. mutually exclusive with --file')
parser.add_argument("--dryrun", "-n", action="store_true", help="process the patterns but dont actually write to the database or do any actual fetching")


def generate_from_pattern_file(filename, dryrun=False):
	with open(filename, "r") as patterns_file:
		for pattern in patterns_file.readlines():
			process_pattern(pattern, dryrun=dryrun)

def process_pattern(pattern, dryrun=False):
	pattern = pattern.strip()
	print("processing pattern: " + pattern)
	domains = generate_domains(pattern)

	for domain in domains:
		if not domain.has_valid_domain_name():
			print("invalid domain name: " + domain.domainname)
			return
	
	add_domains(domains, dryrun=dryrun)
	if dryrun:
		print("Would process " + str(len(domains)) + " domains")


if __name__ == "__main__":
	args = parser.parse_args()
	print(args)
	if args.file:
		generate_from_pattern_file(args.file, dryrun=args.dryrun)
	elif args.pattern:
		process_pattern(args.pattern, dryrun=args.dryrun)
