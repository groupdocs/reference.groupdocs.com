---
title: CadViewInfo
second_title: GroupDocs.Viewer för .NET API-referens
description: Initierar ny instans avCadViewInfogroupdocs.viewer.results/cadviewinfo class.
type: docs
weight: 10
url: /sv/net/groupdocs.viewer.results/cadviewinfo/cadviewinfo/
---
## CadViewInfo constructor

Initierar ny instans av[`CadViewInfo`](../../cadviewinfo) class.

```csharp
public CadViewInfo(FileType fileType, IList<Page> pages, IList<Layer> layers, IList<Layout> layouts)
```

| Parameter | Typ | Beskrivning |
| --- | --- | --- |
| fileType | FileType | Typen av fil. |
| pages | IList`1 | Listan över sidor att visa. |
| layers | IList`1 | Listan över lager som ingår i CAD-ritningen. |
| layouts | IList`1 | Listan över lager som ingår i CAD-ritningen. |

### Undantag

| undantag | skick |
| --- | --- |
| ArgumentNullException | Kastas när*fileType* är inget. |
| ArgumentNullException | Kastas när*pages* är inget. |
| ArgumentNullException | Kastas när*layers* är inget. |
| ArgumentNullException | Kastas när*layouts* är inget. |

### Se även

* class [FileType](../../../groupdocs.viewer/filetype)
* class [Page](../../page)
* class [Layer](../../layer)
* class [Layout](../../layout)
* class [CadViewInfo](../../cadviewinfo)
* namnutrymme [GroupDocs.Viewer.Results](../../cadviewinfo)
* hopsättning [GroupDocs.Viewer](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Viewer.dll -->
