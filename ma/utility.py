import json

def get_pretty_print(results):
    return json.dumps(
            results,
            sort_keys=True,
            indent=4,
            separators=(',', ': '))

def pretty_print(results):
    print(get_pretty_print(results))

def get_dict_from_named_tuple(nt):
    a = dir(nt)
    d = {
            k: getattr(nt, k)
            for k
            in a
            if k[0] != '_' \
                and k != 'count' \
                and k != 'index'
        }

    return d

def match_dict_keys_from_list(d, l):
    return [(k, d[k]) for k in l if k in d]
