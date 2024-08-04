# Repycler

Repycler is a command-line tool for filling out UTF-8 text templates.

## Installation

Repycler isn't currently in any package managers (including pip).

To run it you only need Python 3.x.

## Usage

To use Repycler, write whatever template you need using `{{fields}}` and `{{default_value_fields=VALUE}}` along with an optional `.fields` file for automatically inserting the json-formatted values instead of prompting the user for each one. Here's a quick example:

### template.txt

```
Hey, {{username}}!
I see you're using {{tool=Repycler}} to fill out this template :3
```

### template.txt.fields (optional)

```json
{
    "username": "cycle",
}
```

With everything ready, run the script:

```bash
python repycler.py
```

After specifying the template/field filenames and filling out the fields the user is prompted for, the program quits and outputs a filled out file.

## Planned features

- **Batch `.fields` file support**: Generating a bunch of files based on multiple field files. (this might end up being a change to how the field files work and relying on bash scripting instead)
- **More template control**: Repeating and incrementing segments, alternating the structure.
- **Expressions/scripting**: Variables, fixes for duplicate fields, basic ability to use external data sources for input values.
- **Live mode/editor**: Simple live editor for templates, instead of having to edit them in another program.
- **Segment libraries**: Templates and template groups that can later be used in another template or in the live editor.
