import os
import json

all_data = []
for f_path in os.listdir('data'):
    with open('data/' + f_path, 'r', encoding='utf-8') as f:
        json_data = json.loads(f.read())
        all_data.extend(json_data)

with open('all_data.json', 'w', encoding='utf-8') as f:
    json.dump(all_data, f, indent=3)