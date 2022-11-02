---
title: FolderFontSource
second_title: GroupDocs.Viewer für .NET-API-Referenz
description: Initialisiert eine neue Instanz vonFolderFontSourcegroupdocs.viewer.fonts/folderfontsource Klasse.
type: docs
weight: 10
url: /de/net/groupdocs.viewer.fonts/folderfontsource/folderfontsource/
---
## FolderFontSource constructor

Initialisiert eine neue Instanz von[`FolderFontSource`](../../folderfontsource) Klasse.

```csharp
public FolderFontSource(string folderPath, SearchOption searchOption)
```

| Parameter | Typ | Beschreibung |
| --- | --- | --- |
| folderPath | String | Pfad zu dem Ordner, der TrueType-Schriftarten enthält. |
| searchOption | SearchOption | Gibt an, ob der aktuelle Ordner oder der aktuelle Ordner und alle Unterordner durchsucht werden sollen. |

### Ausnahmen

| Ausnahme | Bedingung |
| --- | --- |
| ArgumentNullException | Wann geworfen*folderPath* ist Null. |
| DirectoryNotFoundException | Wird ausgelöst, wenn der Pfad in angegeben ist*folderPath* kann nicht lokalisiert werden. |

### Siehe auch

* enum [SearchOption](../../searchoption)
* class [FolderFontSource](../../folderfontsource)
* namensraum [GroupDocs.Viewer.Fonts](../../folderfontsource)
* Montage [GroupDocs.Viewer](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Viewer.dll -->