---
title: PresentationInspectionPackage
second_title: GroupDocs.Metadata für .NET-API-Referenz
description: Enthält Informationen zu Präsentationsteilen die teilweise als Metadaten angesehen werden können.
type: docs
weight: 1080
url: /de/net/groupdocs.metadata.formats.document/presentationinspectionpackage/
---
## PresentationInspectionPackage class

Enthält Informationen zu Präsentationsteilen, die teilweise als Metadaten angesehen werden können.

```csharp
public sealed class PresentationInspectionPackage : CustomPackage
```

## Eigenschaften

| Name | Beschreibung |
| --- | --- |
| [Comments](../../groupdocs.metadata.formats.document/presentationinspectionpackage/comments) { get; } | Ruft ein Array der Kommentare ab. |
| [Count](../../groupdocs.metadata.common/metadatapackage/count) { get; } | Ruft die Anzahl der Metadateneigenschaften ab. |
| [HiddenSlides](../../groupdocs.metadata.formats.document/presentationinspectionpackage/hiddenslides) { get; } | Ruft ein Array der ausgeblendeten Folien ab. |
| [Item](../../groupdocs.metadata.common/metadatapackage/item) { get; } | Ruft die ab[`MetadataProperty`](../../groupdocs.metadata.common/metadataproperty) mit dem angegebenen Namen. |
| [Keys](../../groupdocs.metadata.common/metadatapackage/keys) { get; } | Ruft eine Sammlung der Metadaten-Eigenschaftsnamen ab. |
| [MetadataType](../../groupdocs.metadata.common/metadatapackage/metadatatype) { get; } | Ruft den Metadatentyp ab. |
| [PropertyDescriptors](../../groupdocs.metadata.common/metadatapackage/propertydescriptors) { get; } | Ruft eine Sammlung von Deskriptoren ab, die Informationen zu Eigenschaften enthalten, auf die über die Suchmaschine GroupDocs.Metadata zugegriffen werden kann. |

## Methoden

| Name | Beschreibung |
| --- | --- |
| [AddProperties](../../groupdocs.metadata.common/metadatapackage/addproperties)(Func&lt;MetadataProperty, bool&gt;, PropertyValue) | Fügt bekannte Metadateneigenschaften hinzu, die das angegebene Prädikat erfüllen. Die Operation ist rekursiv, sodass sie sich auch auf alle verschachtelten Pakete auswirkt. |
| [ClearComments](../../groupdocs.metadata.formats.document/presentationinspectionpackage/clearcomments)() | Entfernt alle erkannten Benutzerkommentare aus der Präsentation. |
| [ClearHiddenSlides](../../groupdocs.metadata.formats.document/presentationinspectionpackage/clearhiddenslides)() | Entfernt alle erkannten ausgeblendeten Folien aus der Präsentation. |
| [Contains](../../groupdocs.metadata.common/metadatapackage/contains)(string) | Bestimmt, ob das Paket eine Metadateneigenschaft mit dem angegebenen Namen enthält. |
| virtual [FindProperties](../../groupdocs.metadata.common/metadatapackage/findproperties)(Func&lt;MetadataProperty, bool&gt;) | Findet die Metadateneigenschaften, die das angegebene Prädikat erfüllen. Die Suche ist rekursiv, sodass sie auch alle verschachtelten Pakete betrifft. |
| [GetEnumerator](../../groupdocs.metadata.common/metadatapackage/getenumerator)() | Gibt einen Enumerator zurück, der die Sammlung durchläuft. |
| override [RemoveProperties](../../groupdocs.metadata.formats.document/presentationinspectionpackage/removeproperties)(Func&lt;MetadataProperty, bool&gt;) | Entfernt Metadateneigenschaften, die das angegebene Prädikat erfüllen. |
| override [Sanitize](../../groupdocs.metadata.formats.document/presentationinspectionpackage/sanitize)() | Entfernt beschreibbare Metadateneigenschaften aus dem Paket. Der Vorgang ist rekursiv, sodass er sich auch auf alle verschachtelten Pakete auswirkt. |
| [SetProperties](../../groupdocs.metadata.common/metadatapackage/setproperties)(Func&lt;MetadataProperty, bool&gt;, PropertyValue) | Legt bekannte Metadateneigenschaften fest, die das angegebene Prädikat erfüllen. Die Operation ist rekursiv, sodass sie sich auch auf alle verschachtelten Pakete auswirkt. Diese Methode ist eine Kombination aus[`AddProperties`](../../groupdocs.metadata.common/metadatapackage/addproperties) und[`UpdateProperties`](../../groupdocs.metadata.common/metadatapackage/updateproperties) Wenn eine vorhandene Eigenschaft das Prädikat erfüllt, wird ihr Wert aktualisiert. Wenn im Paket eine bekannte Eigenschaft fehlt, die das Prädikat erfüllt, wird sie dem Paket hinzugefügt. |
| [UpdateProperties](../../groupdocs.metadata.common/metadatapackage/updateproperties)(Func&lt;MetadataProperty, bool&gt;, PropertyValue) | Aktualisiert bekannte Metadateneigenschaften, die das angegebene Prädikat erfüllen. Die Operation ist rekursiv, sodass sie sich auch auf alle verschachtelten Pakete auswirkt. |

### Bemerkungen

**Mehr erfahren**

* [Arbeiten mit Metadaten in Präsentationen](https://docs.groupdocs.com/display/metadatanet/Working+with+metadata+in+Presentations)

### Beispiele

Dieses Codebeispiel zeigt, wie Inspektionseigenschaften in einer Präsentation bereinigt werden.

```csharp
using (Metadata metadata = new Metadata(Constants.InputPpt))
{
    var root = metadata.GetRootPackage<PresentationRootPackage>();

    root.InspectionPackage.ClearComments();
    root.InspectionPackage.ClearHiddenSlides();

    metadata.Save(Constants.OutputPpt);
}
```

### Siehe auch

* class [CustomPackage](../../groupdocs.metadata.common/custompackage)
* namensraum [GroupDocs.Metadata.Formats.Document](../../groupdocs.metadata.formats.document)
* Montage [GroupDocs.Metadata](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Metadata.dll -->