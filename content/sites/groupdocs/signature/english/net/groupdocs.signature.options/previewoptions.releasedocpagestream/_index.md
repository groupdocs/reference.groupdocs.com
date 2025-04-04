---
title: PreviewOptions.ReleaseDocPageStream
second_title: GroupDocs.Signature for .NET API Reference
description: Delegate that defines method to release output document page preview stream.
type: docs
weight: 1840
url: /net/groupdocs.signature.options/previewoptions.releasedocpagestream/
---
## PreviewOptions.ReleaseDocPageStream delegate

Delegate that defines method to release output document page preview stream.

```csharp
public delegate void ReleaseDocPageStream(PreviewPageData pageData, Stream pageStream);
```

| Parameter | Type | Description |
| --- | --- | --- |
| pageData | PreviewPageData | Page previewed data. |
| pageStream | Stream | The page stream to release. |

### See Also

* class [PreviewPageData](../previewpagedata)
* class [PreviewOptions](../previewoptions)
* namespace [GroupDocs.Signature.Options](../../groupdocs.signature.options)
* assembly [GroupDocs.Signature](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.signature.dll -->
