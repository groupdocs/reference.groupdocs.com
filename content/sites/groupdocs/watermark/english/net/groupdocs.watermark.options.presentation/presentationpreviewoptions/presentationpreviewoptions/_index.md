---
title: PresentationPreviewOptions
second_title: GroupDocs.Watermark for .NET API Reference
description: Initializes a new instance of the PresentationPreviewOptionsgroupdocs.watermark.options.presentation/presentationpreviewoptions class causing the output stream to be closed.
type: docs
weight: 10
url: /net/groupdocs.watermark.options.presentation/presentationpreviewoptions/presentationpreviewoptions/
---
## PresentationPreviewOptions(CreatePageStream) {#constructor}

Initializes a new instance of the [`PresentationPreviewOptions`](../../presentationpreviewoptions) class causing the output stream to be closed.

```csharp
public PresentationPreviewOptions(CreatePageStream createPageStream)
```

| Parameter | Type | Description |
| --- | --- | --- |
| createPageStream | CreatePageStream | Creates a stream for a specific page preview. |

### See Also

* delegate [CreatePageStream](../../../groupdocs.watermark.options/createpagestream)
* class [PresentationPreviewOptions](../../presentationpreviewoptions)
* namespace [GroupDocs.Watermark.Options.Presentation](../../presentationpreviewoptions)
* assembly [GroupDocs.Watermark](../../../)

---

## PresentationPreviewOptions(CreatePageStream, ReleasePageStream) {#constructor_1}

Initializes a new instance of [`PresentationPreviewOptions`](../../presentationpreviewoptions) class causing the output stream to be returned to the client for further use.

```csharp
public PresentationPreviewOptions(CreatePageStream createPageStream, 
    ReleasePageStream releasePageStream)
```

| Parameter | Type | Description |
| --- | --- | --- |
| createPageStream | CreatePageStream | Creates a stream for a specific page preview. |
| releasePageStream | ReleasePageStream | Notifies that the page preview generation is done and gets the output stream. |

### See Also

* delegate [CreatePageStream](../../../groupdocs.watermark.options/createpagestream)
* delegate [ReleasePageStream](../../../groupdocs.watermark.options/releasepagestream)
* class [PresentationPreviewOptions](../../presentationpreviewoptions)
* namespace [GroupDocs.Watermark.Options.Presentation](../../presentationpreviewoptions)
* assembly [GroupDocs.Watermark](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.watermark.dll -->
