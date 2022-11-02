---
title: PdfRecognitionMode
second_title: GroupDocs.Conversion für .NET-API-Referenz
description: Ermöglicht die Steuerung wie ein PDFDokument in ein Textverarbeitungsdokument konvertiert wird.
type: docs
weight: 1640
url: /de/net/groupdocs.conversion.options.convert/pdfrecognitionmode/
---
## PdfRecognitionMode class

Ermöglicht die Steuerung, wie ein PDF-Dokument in ein Textverarbeitungsdokument konvertiert wird.

```csharp
public sealed class PdfRecognitionMode : Enumeration
```

## Konstrukteure

| Name | Beschreibung |
| --- | --- |
| [PdfRecognitionMode](pdfrecognitionmode)() | Serialisierungskonstruktor |

## Methoden

| Name | Beschreibung |
| --- | --- |
| [CompareTo](../../groupdocs.conversion.contracts/enumeration/compareto)(object) | Vergleicht aktuelles Objekt mit anderem. |
| virtual [Equals](../../groupdocs.conversion.contracts/enumeration/equals)(Enumeration) | Bestimmt, ob zwei Objektinstanzen gleich sind. |
| override [Equals](../../groupdocs.conversion.contracts/enumeration/equals)(object) | Bestimmt, ob zwei Objektinstanzen gleich sind. |
| override [GetHashCode](../../groupdocs.conversion.contracts/enumeration/gethashcode)() | Dient als Standard-Hash-Funktion. |
| override [ToString](../../groupdocs.conversion.contracts/enumeration/tostring)() | Gibt eine Zeichenfolge zurück, die das aktuelle Objekt darstellt. |

## Felder

| Name | Beschreibung |
| --- | --- |
| static readonly [Flow](../../groupdocs.conversion.options.convert/pdfrecognitionmode/flow) | Vollständiger Erkennungsmodus, die Engine führt eine Gruppierung und mehrstufige Analyse durch , um die Absicht des ursprünglichen Dokumentautors wiederherzustellen und ein maximal bearbeitbares Dokument zu erstellen. Der Nachteil ist, dass das Ausgabedokument möglicherweise anders aussieht als die ursprüngliche PDF-Datei. |
| static readonly [Textbox](../../groupdocs.conversion.options.convert/pdfrecognitionmode/textbox) | Dieser Modus ist schnell und gut, um das ursprüngliche Aussehen der PDF -Datei maximal beizubehalten, aber die Bearbeitbarkeit des resultierenden Dokuments könnte eingeschränkt sein. Jeder visuell gruppierte Textblock in der ursprünglichen PDF-Datei wird im resultierenden Dokument in ein Textfeld umgewandelt. Dadurch wird eine maximale Ähnlichkeit des -Ausgabedokuments mit der ursprünglichen PDF-Datei erreicht. Das Ausgabedokument sieht gut aus, aber es besteht ausschließlich aus Textfeldern und kann die weitere Bearbeitung des Dokuments in Microsoft Word ziemlich erschweren. Dies ist der Standardmodus. |

### Siehe auch

* class [Enumeration](../../groupdocs.conversion.contracts/enumeration)
* namensraum [GroupDocs.Conversion.Options.Convert](../../groupdocs.conversion.options.convert)
* Montage [GroupDocs.Conversion](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Conversion.dll -->