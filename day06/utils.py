def insert_in_str_at(index : int, to_be_modified : str, insert : str) -> str:
	modified = to_be_modified[:index] + insert + to_be_modified[index + 1:]
	return modified