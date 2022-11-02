---
title: PdfSaveOptions
second_title: GroupDocs.Signature für .NET-API-Referenz
description: Speicheroptionen für PDFDokumente.
type: docs
weight: 1430
url: /de/net/groupdocs.signature.options/pdfsaveoptions/
---
## PdfSaveOptions class

Speicheroptionen für PDF-Dokumente.

```csharp
public class PdfSaveOptions : SaveOptions
```

## Konstrukteure

| Name | Beschreibung |
| --- | --- |
| [PdfSaveOptions](pdfsaveoptions#constructor)() | Initialisiert eine neue Instanz der PdfSaveOptions-Klasse mit Standardwerten. |
| [PdfSaveOptions](pdfsaveoptions#constructor_1)(bool) | Initialisiert eine neue Instanz der PdfSaveOptions-Klasse mit Überschreib-Flag. |
| [PdfSaveOptions](pdfsaveoptions#constructor_2)(PdfSaveFileFormat) | Initialisiert eine neue Instanz der PdfSaveOptions-Klasse mit dem angegebenen Ausgabedateiformat. |
| [PdfSaveOptions](pdfsaveoptions#constructor_3)(PdfSaveFileFormat, bool) | Initialisiert eine neue Instanz der PdfSaveOptions-Klasse mit dem angegebenen Ausgabedateiformat und dem Überschreib-Flag. |

## Eigenschaften

| Name | Beschreibung |
| --- | --- |
| [AddMissingExtenstion](../../groupdocs.signature.options/saveoptions/addmissingextenstion) { get; set; } | Ruft ein Flag ab oder setzt es, um eine Erweiterung automatisch hinzuzufügen, wenn sie im Pfad der Ausgabedatei fehlte Der Standardwert ist falsch. |
| [FileFormat](../../groupdocs.signature.options/pdfsaveoptions/fileformat) { get; set; } | Ruft das Dateiformat des signierten Dokuments ab oder legt es fest. |
| [OverwriteExistingFiles](../../groupdocs.signature.options/saveoptions/overwriteexistingfiles) { get; set; } | Ruft ab oder legt fest, ob eine vorhandene Datei mit einer neuen Ausgabedatei überschrieben werden soll. Andernfalls wird eine neue Datei mit einer Nummer als Suffix erstellt. Standardmäßig ist dieser Wert auf „true“ gesetzt, was bedeutet, dass die Datei überschrieben wird. |
| [Password](../../groupdocs.signature.options/saveoptions/password) { get; set; } | Ruft das Passwort ab oder legt es fest, um das signierte Dokument mit Passwortschutz zu speichern. Diese Eigenschaft wird für Bilddokumente nicht unterstützt. |
| [UseOriginalPassword](../../groupdocs.signature.options/saveoptions/useoriginalpassword) { get; set; } | Ruft ab oder legt fest, ob ein Kennwort von LoadOptions verwendet werden soll, um ein signiertes Dokument als geschützt zu speichern. Der Standardwert ist wahr. Diese Eigenschaft wird für Bilddokumente nicht unterstützt. |

### Siehe auch

* class [SaveOptions](../saveoptions)
* namensraum [GroupDocs.Signature.Options](../../groupdocs.signature.options)
* Montage [GroupDocs.Signature](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Signature.dll -->