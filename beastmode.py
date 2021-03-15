from patterns import generate_names
from database import add_from_name_list

names = generate_names("coronavirus{state_name}.{tld}")

add_from_name_list(names)

