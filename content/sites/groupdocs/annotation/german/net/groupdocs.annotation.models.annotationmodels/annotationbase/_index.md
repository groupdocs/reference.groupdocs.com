---
title: AnnotationBase
second_title: GroupDocs.Annotation für .NET-API-Referenz
description: Basisklasse für alle Annotationstypen
type: docs
weight: 190
url: /de/net/groupdocs.annotation.models.annotationmodels/annotationbase/
---
## AnnotationBase class

Basisklasse für alle Annotationstypen

```csharp
public abstract class AnnotationBase : ICloneable, IEquatable<AnnotationBase>
```

## Eigenschaften

| Name | Beschreibung |
| --- | --- |
| [CreatedOn](../../groupdocs.annotation.models.annotationmodels/annotationbase/createdon) { get; set; } | Ruft das Erstellungsdatum der Anmerkung ab oder legt es fest |
| [Id](../../groupdocs.annotation.models.annotationmodels/annotationbase/id) { get; set; } | Ruft die eindeutige Kennung der Anmerkung ab oder legt sie fest |
| [Message](../../groupdocs.annotation.models.annotationmodels/annotationbase/message) { get; set; } | Ruft Anmerkungsmeldung ab oder legt sie fest |
| [PageNumber](../../groupdocs.annotation.models.annotationmodels/annotationbase/pagenumber) { get; set; } | Ruft die zu kommentierende Seitennummer ab oder legt sie fest |
| [Replies](../../groupdocs.annotation.models.annotationmodels/annotationbase/replies) { get; set; } | Stellt die Sammlung von Anmerkungsantworten dar |
| [Type](../../groupdocs.annotation.models.annotationmodels/annotationbase/type) { get; set; } | Ruft den Anmerkungstyp ab oder legt ihn fest |
| [User](../../groupdocs.annotation.models.annotationmodels/annotationbase/user) { get; set; } | Ruft Anmerkungsersteller ab oder legt sie fest |

## Methoden

| Name | Beschreibung |
| --- | --- |
| virtual [Clone](../../groupdocs.annotation.models.annotationmodels/annotationbase/clone)() | Gibt eine neue Instanz mit denselben Werten zurück |
| [Equals](../../groupdocs.annotation.models.annotationmodels/annotationbase/equals#equals)(AnnotationBase) | Vergleicht Basisanmerkungen mithilfe der IEquatable-Equals-Methode |
| override [Equals](../../groupdocs.annotation.models.annotationmodels/annotationbase/equals#equals_1)(object) | Vergleicht Basisanmerkungen mithilfe der Standardobjekt-Equals-Methode |
| override [GetHashCode](../../groupdocs.annotation.models.annotationmodels/annotationbase/gethashcode)() | Gibt HashCode von AnnotationBase Message, PageNumber und Type Properties zurück |

### Siehe auch

* namensraum [GroupDocs.Annotation.Models.AnnotationModels](../../groupdocs.annotation.models.annotationmodels)
* Montage [GroupDocs.Annotation](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Annotation.dll -->