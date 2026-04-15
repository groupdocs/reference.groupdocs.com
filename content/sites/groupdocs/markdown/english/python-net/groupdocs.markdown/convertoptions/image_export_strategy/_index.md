---
title: image_export_strategy property
second_title: GroupDocs.Markdown for Python via .NET API References
description: 
type: docs
url: /markdown/python-net/groupdocs.markdown/convertoptions/image_export_strategy/
is_root: false
weight: 2030
---


## image_export_strategy property

The strategy for handling images during conversion. Default is [`ExportImagesAsBase64Strategy`](/markdown/python-net/groupdocs.markdown/exportimagesasbase64strategy/).

Built-in strategies:
- [`ExportImagesAsBase64Strategy`](/markdown/python-net/groupdocs.markdown/exportimagesasbase64strategy/) - Embeds images as Base64 strings (default)
- [`ExportImagesToFileSystemStrategy`](/markdown/python-net/groupdocs.markdown/exportimagestofilesystemstrategy/) - Saves images to a specified folder
- [`SkipImagesStrategy`](/markdown/python-net/groupdocs.markdown/skipimagesstrategy/) - Skips image saving
- [`CustomImagesStrategy`](/markdown/python-net/groupdocs.markdown/customimagesstrategy/) - Custom image saving handler

Or implement [`IImageExportStrategy`](/markdown/python-net/groupdocs.markdown/iimageexportstrategy/) for a fully custom strategy.

### Definition:
```python
@property
def image_export_strategy(self):
    ...
@image_export_strategy.setter
def image_export_strategy(self, value):
    ...
```

### See Also
* class [`ConvertOptions`](/markdown/python-net/groupdocs.markdown/convertoptions/)
