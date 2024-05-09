import sys
import os.path
import json
sys.stdin.reconfigure(encoding='utf-8')

def fill_template():
    template_file = input("Enter template filename: ")
    output_file = input("Enter output filename: ")
    fields_file = template_file + ".fields"

    with open(template_file, 'r', encoding='utf-8') as f:
        template = f.read()

    if os.path.isfile(fields_file):
        with open(fields_file, 'r', encoding='utf-8') as f:
            fields = json.loads(f.read())
    else:
        fields = {}

    while "{{" in template:
        start_idx = template.index("{{")
        end_idx = template.index("}}")
        field_name = template[start_idx+2 : end_idx]
        
        def_val_idx = field_name.find("=")
        if def_val_idx != -1:
            def_val = field_name[def_val_idx+1:].strip()
            field_name = field_name[:def_val_idx].strip()

        if field_name not in fields:
            if def_val_idx != -1:
                user_in = input(f"Enter value for '{field_name}', or press enter for default ({def_val}): ")
                user_in = user_in if user_in else def_val
            else:
                user_in = input(f"Enter value for '{field_name}': ")
            fields[field_name] = user_in
        else:
            user_in = fields[field_name]

        template = template[:start_idx] + user_in + template[end_idx+2:]

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(template)

fill_template()
