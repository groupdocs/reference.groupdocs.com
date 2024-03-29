---
title: InsertAsNewSlide
second_title: GroupDocs.Editor voor .NET API-referentie
description: Booleaanse vlag die specificeert of de bewerkte dia de bestaande dia in de oorspronkelijke presentatie moet vervangen op de positie die is opgegeven door deSlideNumbergroupdocs.editor.options/presentationsaveoptions/slidenumber eigenschap of het moet worden geïnjecteerd tussen de bestaande dia en de vorige zonder de inhoud ervan te vervangen. Standaard is dit onwaar  de bestaande dia wordt vervangen. Deze eigenschap wordt genegeerd als de waarde vanSlideNumbergroupdocs.editor.options/presentationsaveoptions/slidenumber eigenschap is ingesteld op 0.
type: docs
weight: 20
url: /nl/net/groupdocs.editor.options/presentationsaveoptions/insertasnewslide/
---
## PresentationSaveOptions.InsertAsNewSlide property

Booleaanse vlag, die specificeert of de bewerkte dia de bestaande dia in de oorspronkelijke presentatie moet vervangen op de positie die is opgegeven door de[`SlideNumber`](../slidenumber) eigenschap, of het moet worden geïnjecteerd tussen de bestaande dia en de vorige, zonder de inhoud ervan te vervangen. Standaard is dit onwaar — de bestaande dia wordt vervangen. Deze eigenschap wordt genegeerd als de waarde van[`SlideNumber`](../slidenumber) eigenschap is ingesteld op '0'.

```csharp
public bool InsertAsNewSlide { get; set; }
```

### Opmerkingen

Standaard wordt dia vervangen. Dit betekent dat als een gegeven presentatie 5 dia's heeft, en[`SlideNumber`](../slidenumber) =4, dan wordt de 4e dia vervangen door de nieuwe bewerkte dia, terwijl het totale aantal dia's in presentatie (5) ongewijzigd blijft. Als de waarde van deze eigenschap echter is ingesteld opWAAR, wordt de nieuwe bewerkte dia ingevoegd als 4e dia en worden alle volgende dia's naar het einde verschoven: "oude" 4e dia wordt 5e en 5e wordt 6e, en het totale aantal dia's in de presentatie wordt verhoogd met één en gelijk aan 6.

### Zie ook

* class [PresentationSaveOptions](../../presentationsaveoptions)
* naamruimte [GroupDocs.Editor.Options](../../presentationsaveoptions)
* montage [GroupDocs.Editor](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Editor.dll -->
