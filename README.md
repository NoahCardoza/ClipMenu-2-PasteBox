# ClipMenu-2-PasteBox

Converts ClipMenu exports for the PasteBox app.

# Preface

[ClipMenu](https://www.clipmenu.com/) is no longer fully supported in macOS Montery. With no signs of any compatability updates by the developer, I found a good alternative in [PasteBox](https://apps.apple.com/us/app/pastebox/id928940999?mt=12).


# Usage

This script is compatiable with both Python 2.7 and 3.

First export your configuration from ClipMenu, then run the following:

```
python clip-2-paste.py <path/to/export.xml> <path/to/conversion.json>
```

Then in PasteBox, use the import option to import the newly converted file.

Voilà!