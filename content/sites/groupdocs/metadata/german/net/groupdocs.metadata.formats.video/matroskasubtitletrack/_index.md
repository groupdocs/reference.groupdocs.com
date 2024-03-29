---
title: MatroskaSubtitleTrack
second_title: GroupDocs.Metadata für .NET-API-Referenz
description: Stellt UntertitelMetadaten in einem MatroskaVideo dar.
type: docs
weight: 2520
url: /de/net/groupdocs.metadata.formats.video/matroskasubtitletrack/
---
## MatroskaSubtitleTrack class

Stellt Untertitel-Metadaten in einem Matroska-Video dar.

```csharp
public class MatroskaSubtitleTrack : MatroskaTrack
```

## Eigenschaften

| Name | Beschreibung |
| --- | --- |
| [CodecID](../../groupdocs.metadata.formats.video/matroskatrack/codecid) { get; } | Ruft eine ID ab, die dem Codec entspricht. |
| [CodecName](../../groupdocs.metadata.formats.video/matroskatrack/codecname) { get; } | Ruft eine für Menschen lesbare Zeichenfolge ab, die den Codec angibt. |
| [Count](../../groupdocs.metadata.common/metadatapackage/count) { get; } | Ruft die Anzahl der Metadateneigenschaften ab. |
| [DefaultDuration](../../groupdocs.metadata.formats.video/matroskatrack/defaultduration) { get; } | Ruft die Anzahl der Nanosekunden ab (nicht skaliert über[`TimecodeScale`](../matroskasegment/timecodescale) ) pro Frame. |
| [FlagEnabled](../../groupdocs.metadata.formats.video/matroskatrack/flagenabled) { get; } | Ruft das Enabled-Flag ab, wahr, wenn der Track verwendbar ist. |
| [Item](../../groupdocs.metadata.common/metadatapackage/item) { get; } | Ruft die ab[`MetadataProperty`](../../groupdocs.metadata.common/metadataproperty) mit dem angegebenen Namen. |
| [Keys](../../groupdocs.metadata.common/metadatapackage/keys) { get; } | Ruft eine Sammlung der Metadaten-Eigenschaftsnamen ab. |
| [Language](../../groupdocs.metadata.formats.video/matroskatrack/language) { get; } | Ruft die Sprache des Tracks im Matroska-Sprachenformat ab. Dieses Element MUSS ignoriert werden, wenn die[`LanguageIetf`](../matroskatrack/languageietf) Element wird im selben TrackEntry verwendet. |
| [LanguageIetf](../../groupdocs.metadata.formats.video/matroskatrack/languageietf) { get; } | Ruft die Sprache des Tracks gemäß BCP 47 und unter Verwendung der IANA Language Subtag Registry ab. Wenn dieses Element verwendet wird, dann beliebig[`Language`](../matroskatrack/language) Elemente, die im selben TrackEntry verwendet werden, MÜSSEN ignoriert werden. |
| [MetadataType](../../groupdocs.metadata.common/metadatapackage/metadatatype) { get; } | Ruft den Metadatentyp ab. |
| [Name](../../groupdocs.metadata.formats.video/matroskatrack/name) { get; } | Ruft den menschenlesbaren Spurnamen ab. |
| [PropertyDescriptors](../../groupdocs.metadata.common/metadatapackage/propertydescriptors) { get; } | Ruft eine Sammlung von Deskriptoren ab, die Informationen zu Eigenschaften enthalten, auf die über die Suchmaschine GroupDocs.Metadata zugegriffen werden kann. |
| [Subtitles](../../groupdocs.metadata.formats.video/matroskasubtitletrack/subtitles) { get; } | Ruft die Untertitel ab. |
| [TrackNumber](../../groupdocs.metadata.formats.video/matroskatrack/tracknumber) { get; } | Ruft die Spurnummer ab, wie sie im Block-Header verwendet wird. Die Verwendung von mehr als 127 Spuren wird nicht empfohlen, obwohl das Design eine unbegrenzte Anzahl zulässt. |
| [TrackType](../../groupdocs.metadata.formats.video/matroskatrack/tracktype) { get; } | Ruft den Typ des Tracks ab. |
| [TrackUid](../../groupdocs.metadata.formats.video/matroskatrack/trackuid) { get; } | Ruft die eindeutige ID ab, um den Track zu identifizieren. Diese SOLLTE gleich bleiben, wenn eine direkte Stream-Kopie des Tracks in eine andere Datei erstellt wird. |

## Methoden

| Name | Beschreibung |
| --- | --- |
| [AddProperties](../../groupdocs.metadata.common/metadatapackage/addproperties)(Func&lt;MetadataProperty, bool&gt;, PropertyValue) | Fügt bekannte Metadateneigenschaften hinzu, die das angegebene Prädikat erfüllen. Die Operation ist rekursiv, sodass sie sich auch auf alle verschachtelten Pakete auswirkt. |
| [Contains](../../groupdocs.metadata.common/metadatapackage/contains)(string) | Bestimmt, ob das Paket eine Metadateneigenschaft mit dem angegebenen Namen enthält. |
| virtual [FindProperties](../../groupdocs.metadata.common/metadatapackage/findproperties)(Func&lt;MetadataProperty, bool&gt;) | Findet die Metadateneigenschaften, die das angegebene Prädikat erfüllen. Die Suche ist rekursiv, sodass sie auch alle verschachtelten Pakete betrifft. |
| [GetEnumerator](../../groupdocs.metadata.common/metadatapackage/getenumerator)() | Gibt einen Enumerator zurück, der die Sammlung durchläuft. |
| virtual [RemoveProperties](../../groupdocs.metadata.common/metadatapackage/removeproperties)(Func&lt;MetadataProperty, bool&gt;) | Entfernt Metadateneigenschaften, die das angegebene Prädikat erfüllen. |
| virtual [Sanitize](../../groupdocs.metadata.common/metadatapackage/sanitize)() | Entfernt beschreibbare Metadateneigenschaften aus dem Paket. Der Vorgang ist rekursiv, sodass er sich auch auf alle verschachtelten Pakete auswirkt. |
| [SetProperties](../../groupdocs.metadata.common/metadatapackage/setproperties)(Func&lt;MetadataProperty, bool&gt;, PropertyValue) | Legt bekannte Metadateneigenschaften fest, die das angegebene Prädikat erfüllen. Die Operation ist rekursiv, sodass sie sich auch auf alle verschachtelten Pakete auswirkt. Diese Methode ist eine Kombination aus[`AddProperties`](../../groupdocs.metadata.common/metadatapackage/addproperties) Und[`UpdateProperties`](../../groupdocs.metadata.common/metadatapackage/updateproperties) Wenn eine vorhandene Eigenschaft das Prädikat erfüllt, wird ihr Wert aktualisiert. Wenn im Paket eine bekannte Eigenschaft fehlt, die das Prädikat erfüllt, wird sie dem Paket hinzugefügt. |
| [UpdateProperties](../../groupdocs.metadata.common/metadatapackage/updateproperties)(Func&lt;MetadataProperty, bool&gt;, PropertyValue) | Aktualisiert bekannte Metadateneigenschaften, die das angegebene Prädikat erfüllen. Die Operation ist rekursiv, sodass sie sich auch auf alle verschachtelten Pakete auswirkt. |

### Bemerkungen

**Erfahren Sie mehr**

* [Arbeiten mit Metadaten in Matroska-Dateien (MKV).](https://docs.groupdocs.com/display/metadatanet/Working+with+metadata+in+Matroska+%28MKV%29+files)

### Siehe auch

* class [MatroskaTrack](../matroskatrack)
* namensraum [GroupDocs.Metadata.Formats.Video](../../groupdocs.metadata.formats.video)
* Montage [GroupDocs.Metadata](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Metadata.dll -->
