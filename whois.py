import requests
import time
import random
import logging

logger = logging.getLogger(__name__)

def get_whois_for_domain(domain, dryrun=False):
	body = "query=" + domain.domainname
	headers= {
		"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
		"Referer": "https://www.bulkseotools.com/bulk-whois-lookup.php"
	}
	if dryrun:
		logger.info("would fetch whois for " + domain.domainname)
		return

	r = requests.post('https://www.bulkseotools.com/json/bulk-whois-lookup.php', data=body, headers=headers)

	if r.status_code == 200:
		logger.info("successful WHOIS fetch for " + domain.domainname)
		return r.json()
	else:
		logger.error("fetching whois for " + domain.domainname + " failed with code " + r.status_code)
		logger.debug("response: " + vars(r))
		return

def get_whois_for_domain_list(domains, database=None):
	if len(domains) == 0:
		return
	
	dryrun = False if database else True
	for domain in domains:
		whois = get_whois_for_domain(domain, dryrun=dryrun)
		if whois and database:
			domain.set_whois_data(whois)
		sleeptime=random.uniform(1, 4)
		logger.info("sleeping for " + str(sleeptime))
		time.sleep(sleeptime)
	
	if database:
		database.commit()
