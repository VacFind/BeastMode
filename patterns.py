import itertools
from models import Domain

patterns = {
	"state_code": ["al", "ak", "az", "ar", "ca", "co", "ct", "de", "fl", "ga", "hi", "id", "il", "in", "ia", "ks", "ky", "la", "me", "md", "ma", "mi", "mn", "ms", "mo", "mt", "ne", "nv", "nh", "nj", "nm", "ny", "nc", "nd", "oh", "ok", "or", "pa", "ri", "sc", "sd", "tn", "tx", "ut", "vt", "va", "wa", "wv", "wi", "wy", "dc", "as", "gu", "mp", "pr", "vi"],
	"state_name": ["alabama", "alaska", "arizona", "arkansas", "california", "colorado", "connecticut", "delaware", "florida", "georgia", "hawaii", "idaho", "illinois", "indiana", "iowa", "kansas", "kentucky", "louisiana", "maine", "maryland", "massachusetts", "michigan", "minnesota", "mississippi", "missouri", "montana", "nebraska", "nevada", "new hampshire", "new jersey", "new mexico", "new york", "north carolina", "north dakota", "ohio", "oklahoma", "oregon", "pennsylvania", "rhode island", "south carolina", "south dakota", "tennessee", "texas", "utah", "vermont", "virginia", "washington", "west virginia", "wisconsin", "wyoming", "district of columbia", "american samoa", "guam", "northern mariana islands", "puerto rico", "virgin islands"],
	"tld": ["com", "net", "org"]
}

def get_tokens(pattern_string):
	# split on the opening curlybrace to mark the start of the token
	token_locations = pattern_string.split("{")
	del token_locations[0]
	tokens = []
	for tokenchunk in token_locations:
		# split on the closing curlybrace to separate the end of the token from the rest (which we dont care about for the purposes of this function)
		token = tokenchunk.split("}")[0]
		tokens.append(token.strip())
	return tokens

def get_iterations(tokens):
	values = []
	for token in tokens:
		if patterns[token] is not None:
			values.append(patterns[token])
		else:
			values.append([])
	return list(itertools.product(*values))

def sanitize_domain(domain):
	return domain.replace(" ", "")

def sanitize_pattern_value(value):
	return value.replace(" ", "").replace(".", "").lower()


def generate_substitutions_for_pattern(pattern_string):
	tokens = get_tokens(pattern_string)
	iterations = get_iterations(tokens)
	return [dict_from_kv(tokens, iteration, lambda x:sanitize_pattern_value(x)) for iteration in iterations]

def dict_from_kv(keys, values, value_filter=lambda x: x):
	return dict([(keys[i], value_filter(values[i])) for i in range(0,len(keys))])

def generate_domains(pattern_string):
	substitutions = generate_substitutions_for_pattern(pattern_string)
	domains = []
	for substitution in substitutions:
		domain = sanitize_domain(pattern_string.format(**substitution))
		parameters = {}
		state_code = get_state_code_from_substitution_value(substitution)
		if substitution:
			parameters = { "state": state_code }
		domains.append(Domain(domainname=domain, parameters=parameters))

	return domains
		
# this is a bad function with lots of assumptions that is only here for temporary use searching through and generating coronavirus-related domain names for 
def get_state_code_from_substitution_value(substitution_dict):
	for key in substitution_dict.keys():
		if key == 'state_code':
			# return the state code
			return substitution_dict[key]
		elif key == 'state_name':
			# TODO: remove assumption that the state name and code dicts are in the same order
			return cross_match(substitution_dict[key], patterns[key], patterns['state_code'])
	return

# gets a matching value in the target list using the ksy's index in the source list
def cross_match(key, source_list, target_list):

	source_value_index = source_list.index(key) if key in source_list else None
	if not source_value_index:
		source_value_index = source_list.index(sanitize_pattern_value(key)) if key in source_list else None

	if not source_value_index:
		return None
		
	return target_list[source_value_index]
