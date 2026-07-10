def dict_depth(d, current_depth=0):
    if not isinstance(d, dict):
        return current_depth

    current_max = current_depth  # baza: ten poziom
    for v in d.values():
        child_depth = dict_depth(v, current_depth + 1)
        current_max = max(current_max, child_depth)
    return current_max