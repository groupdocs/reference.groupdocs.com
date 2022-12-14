---
title: OnConversionCompleted
second_title: GroupDocs.Conversion für .NET-API-Referenz
description: Konvertierten Dokumentenstrom empfangen. Wird nur ausgelöst wenn Savestring oder SaveSaveDocumentStreamForFileType gesetzt ist.
type: docs
weight: 10
url: /de/net/groupdocs.conversion.fluent/iconversioncompleted/onconversioncompleted/
---
## IConversionCompleted.OnConversionCompleted method

Konvertierten Dokumentenstrom empfangen. Wird nur ausgelöst, wenn „Save(string)“ oder „Save(SaveDocumentStreamForFileType)“ gesetzt ist.

```csharp
public IConversionConvertOrCompress OnConversionCompleted(
    ConvertedDocumentStream convertedDocumentStream)
```

| Parameter | Typ | Beschreibung |
| --- | --- | --- |
| convertedDocumentStream | ConvertedDocumentStream | Konvertierter Dokument-Stream-Anbieter |

### Rückgabewert

Schnittstelle zum Fortsetzen des Umbaus

### Siehe auch

* interface [IConversionConvertOrCompress](../../iconversionconvertorcompress)
* delegate [ConvertedDocumentStream](../../../groupdocs.conversion.contracts/converteddocumentstream)
* interface [IConversionCompleted](../../iconversioncompleted)
* namensraum [GroupDocs.Conversion.Fluent](../../iconversioncompleted)
* Montage [GroupDocs.Conversion](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Conversion.dll -->
