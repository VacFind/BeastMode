import requests
import time

def get_whois_for_domain(domain, dryrun=False):
	body = "query=" + domain.domainname
	headers= {
		"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
		"Referer": "https://www.bulkseotools.com/bulk-whois-lookup.php"
	}
	if dryrun:
		print("would fetch whois for " + domain.domainname)
		return

	r = requests.post('https://www.bulkseotools.com/json/bulk-whois-lookup.php', data=body, headers=headers)

	if r.status_code == 200:
		return r.json()
	else:
		print("fetching whois for " + domain.domainname + " failed with code " + r.status_code)
		print("response received")
		print(vars(r))
		return

def get_whois_for_domain_list(domains, dryrun=False):
	for domain in domains:
		whois = get_whois_for_domain(domain, dryrun=dryrun)
		if whois:
			domain.set_whois_data(whois)
		
