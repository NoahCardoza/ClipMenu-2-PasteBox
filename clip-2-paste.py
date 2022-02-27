import json
import sys
import xml.etree.ElementTree as ET

if len(sys.argv) != 3:
    print('usage: python clip-2-paste.py <input.xml> <output.json>')
    exit(1)

tree = ET.parse(sys.argv[1])

root = tree.getroot()

folder_map = {}
folders = {}

for child in root:
    node_type = child.attrib.get('type')
    if node_type == 'FOLDER':
        for folder_child in child:
            if folder_child.attrib['name'] == "title":
                folder_map[child.attrib['id']] = folder_child.text

for title in folder_map.values():
    folders[title] = []

title = ''
content = ''
folder = ''

for child in root:
    node_type = child.attrib.get('type')
    if node_type == 'SNIPPET':
        for folder_child in child:
            name = folder_child.attrib['name']
            if name == "title":
                title = folder_child.text
            elif name == "content":
                content = folder_child.text
            elif name == "folder":
                folder = folder_child.attrib['idrefs']
            
        folders[folder_map[folder]].append({
            "name" : title,
            "content" : content
        })

json.dump(
    {
        "snippets": 
        [
            {
                "name": key,
                "snippets": value
            } for key, value in folders.items()
        ],
        "version" : 1
    }, open(sys.argv[2], 'w'), indent=2)
