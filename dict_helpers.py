def find_max_length_sublist(dict_to_process: dict) -> int:
    #we expect a dict with keys as int and values as lists
    max_length = 0

    for key, value in dict_to_process.items():
        if len(value) > max_length:
            max_length = len(value)

    return max_length