import json

def pretty_print(results):
    print(json.dumps(
            results, 
            sort_keys=True,
            indent=4, 
            separators=(',', ': ')))

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
