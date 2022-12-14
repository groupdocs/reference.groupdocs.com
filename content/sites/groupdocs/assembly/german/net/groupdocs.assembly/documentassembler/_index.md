---
title: DocumentAssembler
second_title: GroupDocs.Assembly für .NET-API-Referenz
description: Bietet Routinen zum Füllen von Vorlagendokumenten mit Daten und eine Reihe von Einstellungen zum Steuern dieser Routinen.
type: docs
weight: 200
url: /de/net/groupdocs.assembly/documentassembler/
---
## DocumentAssembler class

Bietet Routinen zum Füllen von Vorlagendokumenten mit Daten und eine Reihe von Einstellungen zum Steuern dieser Routinen.

```csharp
public class DocumentAssembler
```

## Konstrukteure

| Name | Beschreibung |
| --- | --- |
| [DocumentAssembler](documentassembler)() | Initialisiert eine neue Instanz dieser Klasse. |

## Eigenschaften

| Name | Beschreibung |
| --- | --- |
| [BarcodeSettings](../../groupdocs.assembly/documentassembler/barcodesettings) { get; } | Ruft eine Reihe von Einstellungen ab, die die Barcode-Erzeugung beim Zusammenstellen eines Dokuments steuern. |
| [KnownTypes](../../groupdocs.assembly/documentassembler/knowntypes) { get; } | Ruft eine ungeordnete Menge (d. h. eine Sammlung eindeutiger Elemente) ab, die Folgendes enthältType Objekte , deren vollständig oder teilweise qualifizierte Namen in Dokumentvorlagen verwendet werden können, die von dieser -Assembler-Instanz verarbeitet werden, um die statischen Member der entsprechenden Typen aufzurufen, Typumwandlungen durchzuführen usw. |
| [Options](../../groupdocs.assembly/documentassembler/options) { get; set; } | Erhält oder setzt eine Reihe von Flags, die das Verhalten davon steuern[`DocumentAssembler`](../documentassembler) Instanz beim Zusammenstellen eines Dokuments. |
| static [UseReflectionOptimization](../../groupdocs.assembly/documentassembler/usereflectionoptimization) { get; set; } | Ruft einen Wert ab oder legt einen Wert fest, der angibt, ob Aufrufe benutzerdefinierter Typmember, die über die Reflektions-API ausgeführt werden, mit dynamischer Klassengenerierung optimiert werden oder nicht. Der Standardwert ist true. |

## Methoden

| Name | Beschreibung |
| --- | --- |
| [AssembleDocument](../../groupdocs.assembly/documentassembler/assembledocument#assembledocument)(Stream, Stream, params DataSourceInfo[]) | Lädt ein Vorlagendokument aus dem angegebenen Quellstream, füllt das Vorlagendokument mit Daten aus den angegebenen einzelnen oder mehreren Quellen und speichert das Ergebnisdokument im Zielstream unter Verwendung von default [`LoadSaveOptions`](../loadsaveoptions) . |
| [AssembleDocument](../../groupdocs.assembly/documentassembler/assembledocument#assembledocument_2)(string, string, params DataSourceInfo[]) | Lädt ein Vorlagendokument aus dem angegebenen Quellpfad, füllt das Vorlagendokument mit Daten aus den angegebenen einzelnen oder mehreren Quellen und speichert das Ergebnisdokument unter Verwendung von default im Zielpfad.[`LoadSaveOptions`](../loadsaveoptions) . |
| [AssembleDocument](../../groupdocs.assembly/documentassembler/assembledocument#assembledocument_1)(Stream, Stream, LoadSaveOptions, params DataSourceInfo[]) | Lädt ein Vorlagendokument aus dem angegebenen Quellstream, füllt das Vorlagendokument mit Daten aus den angegebenen einzelnen oder mehreren Quellen und speichert das Ergebnisdokument im Zielstream unter Verwendung des angegebenen [`LoadSaveOptions`](../loadsaveoptions) . |
| [AssembleDocument](../../groupdocs.assembly/documentassembler/assembledocument#assembledocument_3)(string, string, LoadSaveOptions, params DataSourceInfo[]) | Lädt ein Vorlagendokument aus dem angegebenen Quellpfad, füllt das Vorlagendokument mit Daten aus den angegebenen einzelnen oder mehreren Quellen und speichert das Ergebnisdokument unter Verwendung des angegebenen im Zielpfad.[`LoadSaveOptions`](../loadsaveoptions) . |

### Siehe auch

* namensraum [GroupDocs.Assembly](../../groupdocs.assembly)
* Montage [GroupDocs.Assembly](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Assembly.dll -->
