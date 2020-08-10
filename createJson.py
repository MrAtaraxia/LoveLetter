import json
# merged = {**dictA, **dictB}
# jsonMerged = {**json.loads(jsonStringA), **json.loads(jsonStringB)}
# asString = json.dumps(jsonMerged)


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
