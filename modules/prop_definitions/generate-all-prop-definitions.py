import os

prop_definitions_folder = './'

# Create or update the all_prop_definitions.yml file
with open(os.path.join(prop_definitions_folder, 'all_prop_definitions.yml'), 'w') as f:
    f.write('id: https://example.org/all_prop_definitions\n')
    f.write('name: AllPropDefinitions\n')
    f.write('version: 1.0.0\n')
    f.write('imports:\n')
    for filename in os.listdir(prop_definitions_folder):
        if filename.endswith('.yml') and filename != 'ALL_PROP_DEFINITIONS.yml':
            f.write(f'  - ./{filename}\n')