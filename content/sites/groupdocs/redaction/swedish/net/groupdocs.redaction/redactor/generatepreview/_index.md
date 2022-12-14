---
title: GeneratePreview
second_title: GroupDocs.Redaction för .NET API-referens
description: Genererar förhandsvisningsbilder av specifika sidor i ett givet bildformat.
type: docs
weight: 40
url: /sv/net/groupdocs.redaction/redactor/generatepreview/
---
## Redactor.GeneratePreview method

Genererar förhandsvisningsbilder av specifika sidor i ett givet bildformat.

```csharp
public void GeneratePreview(PreviewOptions previewOptions)
```

| Parameter | Typ | Beskrivning |
| --- | --- | --- |
| previewOptions | PreviewOptions | Bildegenskaper och inställningar för sidintervall |

### Exempel

Följande exempel visar hur man får en förhandsgranskning av ett dokument med hjälp av[`PreviewOptions`](../../../groupdocs.redaction.options/previewoptions) och båda delegaterna.

```csharp
    CreatePageStream createDelegate = delegate (int pageNumber)
    {
        var pagePath = System.IO.Path.Combine(@"C:\Temp", string.Format("page_{0}.png", pageNumber));
        return System.IO.File.Create(pagePath);
    };
    ReleasePageStream releaseDelegate = delegate (int pageNumber, System.IO.Stream pageStream)
    {
        // gör vad som helst med Stream, som innehåller sidförhandsgranskning
        pageStream.Close();
    };
    var previewOptions = new PreviewOptions(createDelegate, releaseDelegate);
    previewOptions.PreviewFormat = PreviewOptions.PreviewFormats.PNG;
    previewOptions.Height = 640;
    previewOptions.Width = 480;
    previewOptions.PageNumbers = new int[] { 1 };
    using (var redactor = new Redactor("C:\Temp\SourceFile.pdf"))
    {
        redactor.GeneratePreview(previewOptions);
    }
```

### Se även

* class [PreviewOptions](../../../groupdocs.redaction.options/previewoptions)
* class [Redactor](../../redactor)
* namnutrymme [GroupDocs.Redaction](../../redactor)
* hopsättning [GroupDocs.Redaction](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Redaction.dll -->
