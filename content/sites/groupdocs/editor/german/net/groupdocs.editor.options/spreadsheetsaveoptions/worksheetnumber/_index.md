---
title: WorksheetNumber
second_title: GroupDocs.Editor für .NET-API-Referenz
description: Ermöglicht das Einfügen eines bearbeiteten Arbeitsblatts in eine Kopie einer vorhandenen Tabelle anstatt eine neue Tabelle mit einem einzelnen Arbeitsblatt zu erstellen Standardverhalten. WorksheetNumber ist eine auf 1 basierende Nummer eines Arbeitsblatts in der Tabelle die in die EditorKlasse geladen wird. Wenn es 0 ist Standardwert wird das neue Arbeitsblatt mit einem einzigen bearbeiteten Arbeitsblatt erstellt. Wenn es größer oder kleiner als null ist und es ein gültiges Arbeitsblatt gibt das in der EditorKlasse geladen ist wird das bearbeitete Arbeitsblatt dargestellt durch input EditableDocumentInstanz wird in diese Tabelle eingefügt.
type: docs
weight: 50
url: /de/net/groupdocs.editor.options/spreadsheetsaveoptions/worksheetnumber/
---
## SpreadsheetSaveOptions.WorksheetNumber property

Ermöglicht das Einfügen eines bearbeiteten Arbeitsblatts in eine Kopie einer vorhandenen Tabelle, anstatt eine neue Tabelle mit einem einzelnen Arbeitsblatt zu erstellen (Standardverhalten). WorksheetNumber ist eine auf 1 basierende Nummer eines Arbeitsblatts in der Tabelle, die in die Editor-Klasse geladen wird. Wenn es 0 ist (Standardwert), wird das neue Arbeitsblatt mit einem einzigen bearbeiteten Arbeitsblatt erstellt. Wenn es größer oder kleiner als null ist und es ein gültiges Arbeitsblatt gibt, das in der Editor-Klasse geladen ist, wird das bearbeitete Arbeitsblatt dargestellt durch input EditableDocument-Instanz, wird in diese Tabelle eingefügt.

```csharp
public int WorksheetNumber { get; set; }
```

### Bemerkungen

ArbeitsblattnummerGanzzahl-Eigenschaft, wenn sie sich nicht im Standardzustand befindet (reservierter Wert „0“), stellt eine Arbeitsblattnummer dar, beginnt also bei 1 und nicht bei null, und ihr Maximalwert ist die Anzahl aller vorhandenen Folien in einer Präsentation. Wenn der angegebene Wert jedoch größer ist als die Anzahl aller Folien, passt GroupDocs.Editor ihn an, um das letzte Arbeitsblatt zu markieren. Negative Werte sind ebenfalls erlaubt und zählen Arbeitsblätter von Ende. Zum Beispiel impliziert "-1" das letzte Arbeitsblatt in einer Tabelle, "-2" — das vorletzte, usw. Wie bei positiven Werten, wenn die negative Arbeitsblattnummer die Gesamtzahl der Arbeitsblätter in der angegebenen Tabelle überschreitet, wird sie angepasst das erste Arbeitsblatt. Die[`InsertAsNewWorksheet`](../insertasnewworksheet) Die boolesche Eigenschaft ist eng mit dieser gekoppelt.

### Beispiele

Die gegebene Tabelle hat 5 Arbeitsblätter: WorksheetNumber = 0; — gegebenes Arbeitsblatt ignorieren, neues Arbeitsblatt erstellen und bearbeitetes Arbeitsblatt darin einfügen. WorksheetNumber = 1; — Ersetzen Sie das erste Arbeitsblatt mit edit WorksheetNumber = 2; — Ersetzen Sie das zweite Arbeitsblatt mit edit WorksheetNumber = 5; — Ersetzen Sie das letzte (5.) Arbeitsblatt mit edit WorksheetNumber = 6; — Ersetzen Sie das letzte (5.) Arbeitsblatt durch bearbeitet, da 6 größer als 5 ist und somit adjustiert WorksheetNumber = -1 ist; — Ersetzen Sie das letzte (5.) Arbeitsblatt durch bearbeitet, da "-1" "zuletzt vorhanden" bedeutet WorksheetNumber = -2; — Ersetzen Sie das 4. Arbeitsblatt mit edit WorksheetNumber = -3; — Ersetzen Sie das 3. Arbeitsblatt mit edit WorksheetNumber = -4; — Ersetzen Sie das 2. Arbeitsblatt mit edit WorksheetNumber = -5; — Ersetzen Sie das erste Arbeitsblatt mit edit WorksheetNumber = -6; — Ersetzen Sie das erste Arbeitsblatt durch bearbeitet, da "-6" größer als 5 ist und daher angepasst ist

### Siehe auch

* class [SpreadsheetSaveOptions](../../spreadsheetsaveoptions)
* namensraum [GroupDocs.Editor.Options](../../spreadsheetsaveoptions)
* Montage [GroupDocs.Editor](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Editor.dll -->
