import json

def pretty_print(results):
    print(json.dumps(
            results, 
            sort_keys=True,
            indent=4, 
            separators=(',', ': ')))
