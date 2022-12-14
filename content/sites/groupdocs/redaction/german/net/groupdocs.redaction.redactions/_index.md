---
title: GroupDocs.Redaction.Redactions
second_title: GroupDocs.Redaction für .NET-API-Referenz
description: DieRedactions Namespace bietet Klassen für verschiedene Arten von Schwärzungen.
type: docs
weight: 70
url: /de/net/groupdocs.redaction.redactions/
---
DieRedactions Namespace bietet Klassen für verschiedene Arten von Schwärzungen.

## Klassen

| Klasse | Beschreibung |
| --- | --- |
| [AnnotationRedaction](./annotationredaction) | Stellt eine Schwärzung dar, die Anmerkungstext (Kommentare usw.) ersetzt, der einem bestimmten regulären Ausdruck entspricht. |
| [CellColumnRedaction](./cellcolumnredaction) | Stellt eine Textschwärzung dar, die Text in Tabellenkalkulationsdokumenten (CSV, Excel usw.) ersetzt. |
| [CellFilter](./cellfilter) | Bietet eine Option zum Einschränken des Bereichs von a[`CellColumnRedaction`](../groupdocs.redaction.redactions/cellcolumnredaction) zu einem Arbeitsblatt und einer Spalte. |
| [DeleteAnnotationRedaction](./deleteannotationredaction) | Stellt eine Textschwärzung dar, die Anmerkungen löscht, wenn der Text mit dem angegebenen regulären Ausdruck übereinstimmt (löscht optional alle Anmerkungen). |
| [EraseMetadataRedaction](./erasemetadataredaction) | Stellt eine Metadatenschwärzung dar, die alle Metadaten oder Metadaten, die mit bestimmten Metadatenfiltern übereinstimmen, aus dem Dokument löscht. |
| [ExactPhraseRedaction](./exactphraseredaction) | Stellt eine Textschwärzung dar, die den genauen Ausdruck im Text des Dokuments ersetzt, standardmäßig ohne Berücksichtigung der Groß-/Kleinschreibung. |
| [ImageAreaRedaction](./imagearearedaction) | Stellt eine Schwärzung dar, die ein farbiges Rechteck in einem bestimmten Bereich eines Bilddokuments platziert. |
| [MetadataRedaction](./metadataredaction) | Repräsentiert eine abstrakte Basisklasse für das Schwärzen von Dokumentmetadaten. |
| [MetadataSearchRedaction](./metadatasearchredaction) | Stellt eine Metadatenschwärzung dar, die Metadaten mithilfe von regulären Ausdrücken, übereinstimmenden Schlüsseln und/oder Werten sucht und schwärzt. |
| [RedactionDescription](./redactiondescription) | Stellt eine einzelne Änderungsaktionsinformation dar, die während des Schwärzungsvorgangs durchgeführt wurde. |
| [RegexRedaction](./regexredaction) | Stellt eine Textschwärzung dar, die Text im Dokument sucht und ersetzt, indem sie den bereitgestellten regulären Ausdruck abgleicht. |
| [RegionReplacementOptions](./regionreplacementoptions) | Repräsentiert Farb- und Bereichsparameter zum Ersetzen von Bildbereichen. Sehen[`ImageAreaRedaction`](../groupdocs.redaction.redactions/imagearearedaction) . |
| [RemovePageRedaction](./removepageredaction) | Stellt eine Schwärzung dar, die eine Seite (Folie, Arbeitsblatt usw.) aus einem Dokument entfernt. |
| [ReplacementOptions](./replacementoptions) | Repräsentiert Optionen zum Ersetzen von übereinstimmendem Text. |
| [TextRedaction](./textredaction) | Repräsentiert eine abstrakte Basisklasse für das Schwärzen von Dokumenttext. |
| [TextReplacement](./textreplacement) | Stellt eine Textersatzinformation dar. |
## Schnittstellen

| Schnittstelle | Beschreibung |
| --- | --- |
| [IRedactionCallback](./iredactioncallback) | Definiert Methoden, die erforderlich sind, um Informationen zu jeder Schwärzungsänderung zu erhalten und optional zu verhindern. |
## Aufzählung

| Aufzählung | Beschreibung |
| --- | --- |
| [MetadataFilters](./metadatafilters) | Stellt eine Liste der häufigsten Arten von Dokumentmetadaten dar. |
| [PageSeekOrigin](./pageseekorigin) | Stellt die Felder bereit, die Bezugspunkte in einem Dokument zum Suchen darstellen. |
| [RedactionActionType](./redactionactiontype) | Stellt Aktionen dar, die zum Schwärzen durchgeführt werden können. |
| [RedactionType](./redactiontype) | Stellt einen Typ von Dokumentdaten dar, die von der Schwärzung betroffen sind. |
| [ReplacementType](./replacementtype) | Repräsentiert einen Ersetzungstyp für den abgeglichenen Text. |

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Redaction.dll -->
