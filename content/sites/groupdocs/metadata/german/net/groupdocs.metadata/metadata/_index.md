---
title: Metadata
second_title: GroupDocs.Metadata für .NET-API-Referenz
description: Stellt die Hauptklasse für den Zugriff auf Metadaten in allen unterstützten Formaten bereit.
type: docs
weight: 2660
url: /de/net/groupdocs.metadata/metadata/
---
## Metadata class

Stellt die Hauptklasse für den Zugriff auf Metadaten in allen unterstützten Formaten bereit.

```csharp
public sealed class Metadata : IDisposable
```

## Konstrukteure

| Name | Beschreibung |
| --- | --- |
| [Metadata](metadata#constructor)(Stream) | Initialisiert eine neue Instanz von[`Metadata`](../metadata) Klasse. |
| [Metadata](metadata#constructor_2)(string) | Initialisiert eine neue Instanz von[`Metadata`](../metadata) Klasse. |
| [Metadata](metadata#constructor_1)(Stream, LoadOptions) | Initialisiert eine neue Instanz von[`Metadata`](../metadata) Klasse. |
| [Metadata](metadata#constructor_3)(string, LoadOptions) | Initialisiert eine neue Instanz von[`Metadata`](../metadata) Klasse. |

## Eigenschaften

| Name | Beschreibung |
| --- | --- |
| [FileFormat](../../groupdocs.metadata/metadata/fileformat) { get; } | Ruft den Typ der geladenen Datei ab (sofern erkannt). |

## Methoden

| Name | Beschreibung |
| --- | --- |
| [AddProperties](../../groupdocs.metadata/metadata/addproperties)(Func&lt;MetadataProperty, bool&gt;, PropertyValue) | Fügt bekannte Metadateneigenschaften hinzu, die das angegebene Prädikat erfüllen. Die Operation ist rekursiv, sodass sie sich auch auf alle verschachtelten Pakete auswirkt. |
| [Dispose](../../groupdocs.metadata/metadata/dispose)() | Führt anwendungsdefinierte Aufgaben aus, die mit dem Freigeben, Freigeben oder Zurücksetzen nicht verwalteter Ressourcen verbunden sind. |
| [FindProperties](../../groupdocs.metadata/metadata/findproperties)(Func&lt;MetadataProperty, bool&gt;) | Findet die Metadateneigenschaften, die das angegebene Prädikat erfüllen. Die Suche ist rekursiv, sodass sie auch alle verschachtelten Pakete betrifft. |
| [GeneratePreview](../../groupdocs.metadata/metadata/generatepreview)(PreviewOptions) | Erstellt Vorschaubilder für bestimmte Seiten. |
| [GetDocumentInfo](../../groupdocs.metadata/metadata/getdocumentinfo)() | Ruft allgemeine Informationen über das geladene Dokument ab. |
| [GetRootPackage](../../groupdocs.metadata/metadata/getrootpackage#getrootpackage)() | Ruft das Stammpaket ab, das Zugriff auf alle Metadateneigenschaften bietet, die aus der Datei extrahiert wurden. |
| [GetRootPackage&lt;TRoot&gt;](../../groupdocs.metadata/metadata/getrootpackage#getrootpackage_1)() | Ruft das Stammpaket ab, das Zugriff auf alle Metadateneigenschaften bietet, die aus der Datei extrahiert wurden. |
| [RemoveProperties](../../groupdocs.metadata/metadata/removeproperties)(Func&lt;MetadataProperty, bool&gt;) | Entfernt Metadateneigenschaften, die das angegebene Prädikat erfüllen. |
| [Sanitize](../../groupdocs.metadata/metadata/sanitize)() | Entfernt beschreibbare Metadateneigenschaften von allen erkannten Paketen oder ganzen Paketen, falls möglich. Die Operation ist rekursiv, sodass sie sich auch auf alle verschachtelten Pakete auswirkt. |
| [Save](../../groupdocs.metadata/metadata/save#save)() | Speichert alle im geladenen Dokument vorgenommenen Änderungen. |
| [Save](../../groupdocs.metadata/metadata/save#save_1)(Stream) | Speichert den Dokumentinhalt in einem Stream. |
| [Save](../../groupdocs.metadata/metadata/save#save_2)(string) | Speichert den Dokumentinhalt in der angegebenen Datei. |
| [SetProperties](../../groupdocs.metadata/metadata/setproperties)(Func&lt;MetadataProperty, bool&gt;, PropertyValue) | Legt bekannte Metadateneigenschaften fest, die das angegebene Prädikat erfüllen. Die Operation ist rekursiv, sodass sie sich auch auf alle verschachtelten Pakete auswirkt. Diese Methode ist eine Kombination aus[`AddProperties`](./addproperties) Und[`UpdateProperties`](./updateproperties) . Wenn eine vorhandene Eigenschaft das Prädikat erfüllt, wird ihr Wert aktualisiert. Wenn in einem Paket eine bekannte Eigenschaft fehlt, die das Prädikat erfüllt, wird sie dem Paket hinzugefügt. |
| [UpdateProperties](../../groupdocs.metadata/metadata/updateproperties)(Func&lt;MetadataProperty, bool&gt;, PropertyValue) | Aktualisiert bekannte Metadateneigenschaften, die das angegebene Prädikat erfüllen. Die Operation ist rekursiv, sodass sie sich auch auf alle verschachtelten Pakete auswirkt. |

### Siehe auch

* namensraum [GroupDocs.Metadata](../../groupdocs.metadata)
* Montage [GroupDocs.Metadata](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Metadata.dll -->
