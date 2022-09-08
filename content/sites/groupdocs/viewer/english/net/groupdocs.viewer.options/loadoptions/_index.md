---
title: LoadOptions
second_title: GroupDocs.Viewer for .NET API Reference
description: Provides options that used to open the file.
type: docs
weight: 370
url: /net/groupdocs.viewer.options/loadoptions/
---
## LoadOptions class

Provides options that used to open the file.

```csharp
public class LoadOptions
```

## Constructors

| Name | Description |
| --- | --- |
| [LoadOptions](loadoptions#constructor)() | Initializes new instance of [`LoadOptions`](../loadoptions) class. |
| [LoadOptions](loadoptions#constructor_1)(FileType) | Initializes new instance of [`LoadOptions`](../loadoptions) class. |

## Properties

| Name | Description |
| --- | --- |
| [Encoding](../../groupdocs.viewer.options/loadoptions/encoding) { get; set; } | The encoding used when opening text-based files or email messages such as [`CSV`](../../groupdocs.viewer/filetype/csv), [`TXT`](../../groupdocs.viewer/filetype/txt), and [`MSG`](../../groupdocs.viewer/filetype/msg). Default value is Default. |
| [FileType](../../groupdocs.viewer.options/loadoptions/filetype) { get; set; } | The type of the file to open. |
| [Password](../../groupdocs.viewer.options/loadoptions/password) { get; set; } | The password for opening encrypted file. |
| [ResourceLoadingTimeout](../../groupdocs.viewer.options/loadoptions/resourceloadingtimeout) { get; set; } | The external resources e.g. graphics loading timeout. The default value is 30 seconds. This option is supported for Word Processing documents that contain external resources. |

### See Also

* namespace [GroupDocs.Viewer.Options](../../groupdocs.viewer.options)
* assembly [GroupDocs.Viewer](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.viewer.dll -->