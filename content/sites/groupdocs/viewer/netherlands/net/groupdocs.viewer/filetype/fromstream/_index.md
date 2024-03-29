---
title: FromStream
second_title: GroupDocs.Viewer voor .NET API-referentie
description: Detecteert het bestandstype door de bestandshandtekening te lezen.
type: docs
weight: 1950
url: /nl/net/groupdocs.viewer/filetype/fromstream/
---
## FromStream(Stream) {#fromstream}

Detecteert het bestandstype door de bestandshandtekening te lezen.

```csharp
public static FileType FromStream(Stream stream)
```

| Parameter | Type | Beschrijving |
| --- | --- | --- |
| stream | Stream | De bestandsstroom. |

### Zie ook

* class [FileType](../../filetype)
* naamruimte [GroupDocs.Viewer](../../filetype)
* montage [GroupDocs.Viewer](../../../)

---

## FromStream(Stream, string) {#fromstream_2}

Detecteert het bestandstype door de bestandshandtekening te lezen.

```csharp
public static FileType FromStream(Stream stream, string password)
```

| Parameter | Type | Beschrijving |
| --- | --- | --- |
| stream | Stream | De bestandsstroom. |
| password | String | Het wachtwoord om het bestand te openen. |

### Zie ook

* class [FileType](../../filetype)
* naamruimte [GroupDocs.Viewer](../../filetype)
* montage [GroupDocs.Viewer](../../../)

---

## FromStream(Stream, ILogger) {#fromstream_1}

Detecteert het bestandstype door de bestandshandtekening te lezen.

```csharp
public static FileType FromStream(Stream stream, ILogger logger)
```

| Parameter | Type | Beschrijving |
| --- | --- | --- |
| stream | Stream | De bestandsstroom. |
| logger | ILogger | De logger. |

### Winstwaarde

Retourneert het bestandstype in het geval dat het met succes is gedetecteerd, anders wordt de standaardwaarde geretourneerd[`Unknown`](../unknown) bestandstype.

### Zie ook

* interface [ILogger](../../../groupdocs.viewer.logging/ilogger)
* class [FileType](../../filetype)
* naamruimte [GroupDocs.Viewer](../../filetype)
* montage [GroupDocs.Viewer](../../../)

---

## FromStream(Stream, string, ILogger) {#fromstream_3}

Detecteert het bestandstype door de bestandshandtekening te lezen.

```csharp
public static FileType FromStream(Stream stream, string password, ILogger logger)
```

| Parameter | Type | Beschrijving |
| --- | --- | --- |
| stream | Stream | De bestandsstroom. |
| password | String | Het wachtwoord om het bestand te openen. |
| logger | ILogger | De logger. |

### Winstwaarde

Retourneert het bestandstype in het geval dat het met succes is gedetecteerd, anders wordt de standaardwaarde geretourneerd[`Unknown`](../unknown) bestandstype.

### Zie ook

* interface [ILogger](../../../groupdocs.viewer.logging/ilogger)
* class [FileType](../../filetype)
* naamruimte [GroupDocs.Viewer](../../filetype)
* montage [GroupDocs.Viewer](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Viewer.dll -->
