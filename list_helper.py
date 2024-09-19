def shift_all_items_once(list_to_process: list, candidate_to_remove: str) -> list:
    if candidate_to_remove in list_to_process:
        list_to_process.remove(candidate_to_remove)

    return list_to_process