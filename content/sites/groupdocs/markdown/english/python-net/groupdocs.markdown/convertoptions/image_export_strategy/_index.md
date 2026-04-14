---
title: image_export_strategy property
second_title: GroupDocs.Markdown for Python via .NET API References
description: 
type: docs
url: /python-net/groupdocs.markdown/convertoptions/image_export_strategy/
is_root: false
weight: 2030
---


## image_export_strategy property

The strategy for handling images during conversion. The default is [`ExportImagesAsBase64Strategy`](/python-net/groupdocs.markdown/exportimagesasbase64strategy/).

Built-in strategies:
- [`ExportImagesAsBase64Strategy`](/python-net/groupdocs.markdown/exportimagesasbase64strategy/) - Embeds images as Base64 strings (default)
- [`ExportImagesToFileSystemStrategy`](/python-net/groupdocs.markdown/exportimagestofilesystemstrategy/) - Saves images to a specified folder
- [`SkipImagesStrategy`](/python-net/groupdocs.markdown/skipimagesstrategy/) - Skips image saving
- [`CustomImagesStrategy`](/python-net/groupdocs.markdown/customimagesstrategy/) - Custom image saving handler

Or implement `IImageExportStrategy` for a fully custom strategy.

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
* class [`ConvertOptions`](/python-net/groupdocs.markdown/convertoptions/)
