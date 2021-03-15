import itertools

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


