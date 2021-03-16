from patterns import generate_domains
from database import BeastModeDB

import argparse, logging
from dotenv import load_dotenv
import os

load_dotenv()

logger = logging.getLogger(__name__)

parser = argparse.ArgumentParser(description='generate and check a list of domains from patterns')
group = parser.add_mutually_exclusive_group()
group.add_argument('--file', type=str, help='import domains using a file with one pattern per line. mutually exclusive with --pattern')
group.add_argument('--pattern', "-p", type=str,  help='import domains from a single pattern string. mutually exclusive with --file')
parser.add_argument("--whois", nargs='?', const=25, type=int, default=0, help="process WHOIS data for new domains (this can take a lot of time). Optionally specify a batch size")
parser.add_argument("--dryrun", "-n", action="store_true", help="process the patterns but dont actually write to the database or do any actual fetching")
parser.add_argument('-v', '--verbose', action='count', default=0)


def generate_from_pattern_file(filename, database=None):
	with open(filename, "r") as patterns_file:
		for pattern in patterns_file.readlines():
			if not pattern.strip().startswith("#") and len(pattern.strip()) > 0:
				process_pattern(pattern, database=database)

def process_pattern(pattern, database=None):
	pattern = pattern.strip()
	logger.info("processing pattern: " + pattern)
	domains = generate_domains(pattern)

	for domain in domains:
		if not domain.has_valid_domain_name():
			logger.warn("invalid domain name: " + domain.domainname)
			return
	
	if database:
		database.add_domains(domains, dryrun=dryrun)
	else:
		logger.info("Would process " + str(len(domains)) + " domains")


if __name__ == "__main__":
	args = parser.parse_args()

	# set up logging
	loglevel = logging.WARNING # default loglevel
	if args.verbose == 1:
		loglevel = logging.INFO
	elif args.verbose >= 2:
		loglevel = logging.DEBUG

	logging.basicConfig(level=loglevel)
	logger.info("starting up")
	connection_str = os.environ.get("DB_CONNECTION_STRING", "sqlite:///domains.db")
	database = BeastModeDB(connection_string=connection_str)
	db_to_pass = database if not args.dryrun else None

	if args.file:
		logger.info("detected pattern file")
		generate_from_pattern_file(args.file, database=db_to_pass)
	elif args.pattern:
		logger.info("detected pattern parameter")
		process_pattern(args.pattern, database=db_to_pass)
