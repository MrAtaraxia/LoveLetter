import json
# merged = {**dictA, **dictB}
# jsonMerged = {**json.loads(jsonStringA), **json.loads(jsonStringB)}
# asString = json.dumps(jsonMerged)

# # now we have two json STRINGS
# import json
# dictA = json.loads(jsonStringA)
# dictB = json.loads(jsonStringB)
#
# merged_dict = {key: value for (key, value) in (dictA.items() + dictB.items())}


def create_json():
    data = {}
    data['people'] = []
    data['people'].append({
        'name': 'Scott',
        'website': 'stackabuse.com',
        'from': 'Nebraska'
    })
    data['people'].append({
        'name': 'Larry',
        'website': 'google.com',
        'from': 'Michigan'
    })
    data['people'].append({
        'name': 'Tim',
        'website': 'apple.com',
        'from': 'Alabama'
    })

    with open('anotherJson.json', 'w') as outfile:
        json.dump(data, outfile, indent=4)


def merge_json(json1, json2):
    merged = {**json1, **json2}
    return merged




if __name__ == "__main__":
    create_json()
