---
title: PreviewOptions
second_title: GroupDocs.Parser för .NET API-referens
description: Initierar en ny instans avPreviewOptionsgroupdocs.parser.options/previewoptions klass som gör att utgångsströmmen stängs.
type: docs
weight: 10
url: /sv/net/groupdocs.parser.options/previewoptions/previewoptions/
---
## PreviewOptions(CreatePageStream) {#constructor}

Initierar en ny instans av[`PreviewOptions`](../../previewoptions) klass som gör att utgångsströmmen stängs.

```csharp
public PreviewOptions(CreatePageStream createPageStream)
```

| Parameter | Typ | Beskrivning |
| --- | --- | --- |
| createPageStream | CreatePageStream | Skapar en ström för en specifik förhandsvisning av sidan. |

### Se även

* delegate [CreatePageStream](../../createpagestream)
* class [PreviewOptions](../../previewoptions)
* namnutrymme [GroupDocs.Parser.Options](../../previewoptions)
* hopsättning [GroupDocs.Parser](../../../)

---

## PreviewOptions(CreatePageStream, ReleasePageStream) {#constructor_1}

Initierar en ny instans av[`PreviewOptions`](../../previewoptions) klass som gör att utdataströmmen returneras till klienten för vidare användning.

```csharp
public PreviewOptions(CreatePageStream createPageStream, ReleasePageStream releasePageStream)
```

| Parameter | Typ | Beskrivning |
| --- | --- | --- |
| createPageStream | CreatePageStream | Skapar en ström för en specifik förhandsvisning av sidan |
| releasePageStream | ReleasePageStream | Meddelar att genereringen av sidförhandsgranskningen är klar och hämtar utdataströmmen. |

### Se även

* delegate [CreatePageStream](../../createpagestream)
* delegate [ReleasePageStream](../../releasepagestream)
* class [PreviewOptions](../../previewoptions)
* namnutrymme [GroupDocs.Parser.Options](../../previewoptions)
* hopsättning [GroupDocs.Parser](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Parser.dll -->
