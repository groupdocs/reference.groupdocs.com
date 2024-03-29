---
title: ImageAnnotation
second_title: GroupDocs.Annotation voor .NET API-referentie
description: Vertegenwoordigt afbeelding annotatieeigenschappen
type: docs
weight: 250
url: /nl/net/groupdocs.annotation.models.annotationmodels/imageannotation/
---
## ImageAnnotation class

Vertegenwoordigt afbeelding annotatie-eigenschappen

```csharp
public class ImageAnnotation : AnnotationBase, IAngle, IBox, IEquatable<ImageAnnotation>, IOpacity
```

## Constructeurs

| Naam | Beschrijving |
| --- | --- |
| [ImageAnnotation](imageannotation)() | Initialiseert nieuw exemplaar van[`ImageAnnotation`](../imageannotation) klasse. |

## Eigenschappen

| Naam | Beschrijving |
| --- | --- |
| [Angle](../../groupdocs.annotation.models.annotationmodels/imageannotation/angle) { get; set; } | Krijgt of stelt annotatierotatiehoek in |
| [Box](../../groupdocs.annotation.models.annotationmodels/imageannotation/box) { get; set; } | Krijgt of stelt annotatiepositie in |
| [CreatedOn](../../groupdocs.annotation.models.annotationmodels/annotationbase/createdon) { get; set; } | Aanmaakdatum annotatie ophalen of instellen |
| [Id](../../groupdocs.annotation.models.annotationmodels/annotationbase/id) { get; set; } | Krijgt of stelt annotatie unieke identifier in |
| [ImageExtension](../../groupdocs.annotation.models.annotationmodels/imageannotation/imageextension) { get; set; } | Krijgt of stelt afbeeldingsgegevens in |
| [ImagePath](../../groupdocs.annotation.models.annotationmodels/imageannotation/imagepath) { get; set; } | Haalt of stelt afbeeldingspad in |
| [Message](../../groupdocs.annotation.models.annotationmodels/annotationbase/message) { get; set; } | Krijgt of stelt annotatiebericht in |
| [Opacity](../../groupdocs.annotation.models.annotationmodels/imageannotation/opacity) { get; set; } | Krijgt of stelt afbeeldingsdekking in |
| [PageNumber](../../groupdocs.annotation.models.annotationmodels/annotationbase/pagenumber) { get; set; } | Krijgt of stelt paginanummer in om te annoteren |
| [Replies](../../groupdocs.annotation.models.annotationmodels/annotationbase/replies) { get; set; } | Vertegenwoordigt verzameling annotatieantwoorden |
| [Type](../../groupdocs.annotation.models.annotationmodels/annotationbase/type) { get; set; } | Krijgt of stelt annotatietype in |
| [User](../../groupdocs.annotation.models.annotationmodels/annotationbase/user) { get; set; } | Krijgt of stelt annotatie maker in |
| [ZIndex](../../groupdocs.annotation.models.annotationmodels/imageannotation/zindex) { get; set; } | Haalt of stelt z-index in. Standaardwaarde is 0 |

## methoden

| Naam | Beschrijving |
| --- | --- |
| override [Clone](../../groupdocs.annotation.models.annotationmodels/imageannotation/clone)() | Retourneert een nieuwe instantie met dezelfde waarden |
| [Equals](../../groupdocs.annotation.models.annotationmodels/annotationbase/equals)(AnnotationBase) | Vergelijkt basisannotaties met behulp van de methode IEquatable Equals |
| [Equals](../../groupdocs.annotation.models.annotationmodels/imageannotation/equals#equals_1)(ImageAnnotation) | Vergelijkt beeldannotaties met behulp van de methode IEquatable Equals |
| override [Equals](../../groupdocs.annotation.models.annotationmodels/imageannotation/equals#equals_2)(object) | Vergelijkt beeldannotaties met behulp van standaardobject Equals-methode |
| override [GetHashCode](../../groupdocs.annotation.models.annotationmodels/imageannotation/gethashcode)() | Retourneert hashcode van afbeeldingsannotatie |
| [GetImage](../../groupdocs.annotation.models.annotationmodels/imageannotation/getimage)() | Krijgt afbeelding object |

### Opmerkingen

**Kom meer te weten**

* Meer over annotatietypen en het annoteren van PDF- en Microsoft Word-documenten, Excel-spreadsheets en PowerPoint-presentaties: [Documenten annoteren met GroupDocs.Annotation voor .NET](https://docs.groupdocs.com/display/annotationnet/Add+annotation+to+the+document)
* Meer informatie over het toevoegen van beeldannotaties aan documenten van verschillende typen: [Annotaties aan afbeeldingen toevoegen in C#](https://docs.groupdocs.com/display/annotationnet/Add+image+annotation)

### Zie ook

* class [AnnotationBase](../annotationbase)
* interface [IAngle](../../groupdocs.annotation.models.annotationmodels.interfaces.properties/iangle)
* interface [IBox](../../groupdocs.annotation.models.annotationmodels.interfaces.properties/ibox)
* interface [IOpacity](../../groupdocs.annotation.models.annotationmodels.interfaces.properties/iopacity)
* naamruimte [GroupDocs.Annotation.Models.AnnotationModels](../../groupdocs.annotation.models.annotationmodels)
* montage [GroupDocs.Annotation](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Annotation.dll -->
