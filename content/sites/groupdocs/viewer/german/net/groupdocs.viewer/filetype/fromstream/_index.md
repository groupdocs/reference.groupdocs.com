---
title: FromStream
second_title: GroupDocs.Viewer für .NET-API-Referenz
description: Erkennt den Dateityp durch Lesen der Dateisignatur.
type: docs
weight: 1900
url: /de/net/groupdocs.viewer/filetype/fromstream/
---
## FromStream(Stream) {#fromstream}

Erkennt den Dateityp durch Lesen der Dateisignatur.

```csharp
public static FileType FromStream(Stream stream)
```

| Parameter | Typ | Beschreibung |
| --- | --- | --- |
| stream | Stream | Der Dateistream. |

### Siehe auch

* class [FileType](../../filetype)
* namensraum [GroupDocs.Viewer](../../filetype)
* Montage [GroupDocs.Viewer](../../../)

---

## FromStream(Stream, string) {#fromstream_2}

Erkennt den Dateityp durch Lesen der Dateisignatur.

```csharp
public static FileType FromStream(Stream stream, string password)
```

| Parameter | Typ | Beschreibung |
| --- | --- | --- |
| stream | Stream | Der Dateistream. |
| password | String | Das Passwort zum Öffnen der Datei. |

### Siehe auch

* class [FileType](../../filetype)
* namensraum [GroupDocs.Viewer](../../filetype)
* Montage [GroupDocs.Viewer](../../../)

---

## FromStream(Stream, ILogger) {#fromstream_1}

Erkennt den Dateityp durch Lesen der Dateisignatur.

```csharp
public static FileType FromStream(Stream stream, ILogger logger)
```

| Parameter | Typ | Beschreibung |
| --- | --- | --- |
| stream | Stream | Der Dateistream. |
| logger | ILogger | Der Logger. |

### Rückgabewert

Gibt den Dateityp zurück, falls er erfolgreich erkannt wurde, andernfalls gibt er den Standardwert zurück[`Unknown`](../unknown) Dateityp.

### Siehe auch

* interface [ILogger](../../../groupdocs.viewer.logging/ilogger)
* class [FileType](../../filetype)
* namensraum [GroupDocs.Viewer](../../filetype)
* Montage [GroupDocs.Viewer](../../../)

---

## FromStream(Stream, string, ILogger) {#fromstream_3}

Erkennt den Dateityp durch Lesen der Dateisignatur.

```csharp
public static FileType FromStream(Stream stream, string password, ILogger logger)
```

| Parameter | Typ | Beschreibung |
| --- | --- | --- |
| stream | Stream | Der Dateistream. |
| password | String | Das Passwort zum Öffnen der Datei. |
| logger | ILogger | Der Logger. |

### Rückgabewert

Gibt den Dateityp zurück, falls er erfolgreich erkannt wurde, andernfalls gibt er den Standardwert zurück[`Unknown`](../unknown) Dateityp.

### Siehe auch

* interface [ILogger](../../../groupdocs.viewer.logging/ilogger)
* class [FileType](../../filetype)
* namensraum [GroupDocs.Viewer](../../filetype)
* Montage [GroupDocs.Viewer](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Viewer.dll -->