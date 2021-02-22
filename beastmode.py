
state_postal_codes = ["al", "ak", "az", "ar", "ca", "co", "ct", "de", "fl", "ga", "hi", "id", "il", "in", "ia", "ks", "ky", "la", "me", "md", "ma", "mi", "mn", "ms", "mo", "mt", "ne", "nv", "nh", "nj", "nm", "ny", "nc", "nd", "oh", "ok", "or", "pa", "ri", "sc", "sd", "tn", "tx", "ut", "vt", "va", "wa", "wv", "wi", "wy", "dc", "as", "gu", "mp", "pr", "vi"]

tlds = ["com", "net", "org"]

for tld in tlds:
	for x in state_postal_codes:
		print( x + "vaccinate" + "." + tld )

