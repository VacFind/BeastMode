# BeastMode

This repository intends to create an open-source tool that is similarin functionality to namecheap's "beast mode" domain name search tool.

This repository was originally created to help [vacfind.org](https://vacfind.org) find state and local covid-related tools by checking all domain names of a similar pattern, such as [vaccinateca.com](https://vaccinateca.com) and [vaccinatema.com](https://vaccinatema.com)

## Environment Variables

`DB_CONNECTION_STRING` - specify a DB connection string. defaults to `sqlite:///domains.db`.



## How to generate domain names with this script

1. generate a list of the domains you want to check via your favorite method. If theres enough interest I can make a python script to make this easier.
2. use a bulk WHOIS tool like [this](https://www.bulkseotools.com/bulk-whois-lookup.php) to look up who registered the domains
   - you may want to copy this into a spreadsheet when its done
3. Filter out anything that is not registered. you may want to set them aside in case they become registered in future
4. ~~if theres a lot of links, you can paste them into a [bulk URL opening tool](https://www.10bestseo.com/url-opener/). *NOTE*, this may make your screen flash as it opens the webpages, especially if you use dark mode.~~ https://httpstatus.io/ is a good way to check the status and/or redirects of a link. and it automatically handles www and non-www
5. go through each of the opened pages to see which ones are available. Generally you get one of three results:
	- the webpage is unable to connect (this can mean many things, but can be considered the same as "unregistered" for this purpose)
	- you see a domain registrar holding page (this could mean the domain was recently registered, or registered and never pointed at anything. these could be interpereted as "coming soon")
	- an actual webpage (sometimes this is a generic coming soon page)
6. possibly repeat with another domain name format
