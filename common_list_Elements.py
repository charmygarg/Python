def _unique_common_elements_sample_ed2_(a, b):
    common = []
    for items in a:
        if items in b:
            common.append(items)
    if not common:
        return None
    unique = []
    for items in common[:]:
        if items not in unique:
            unique.append(items)
    return sorted(unique)