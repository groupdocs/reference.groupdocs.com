---
title: RecognizeLists
second_title: GroupDocs.Editor für .NET-API-Referenz
description: Ermöglicht die Angabe wie nummerierte Listenelemente erkannt werden wenn ein Dokument aus dem NurTextFormat importiert wird. Der Standardwert ist true.
type: docs
weight: 60
url: /de/net/groupdocs.editor.options/texteditoptions/recognizelists/
---
## TextEditOptions.RecognizeLists property

Ermöglicht die Angabe, wie nummerierte Listenelemente erkannt werden, wenn ein Dokument aus dem Nur-Text-Format importiert wird. Der Standardwert ist true.

```csharp
public bool RecognizeLists { get; set; }
```

### Bemerkungen

Wenn diese Option auf „false“ gesetzt ist, erkennt der Listenerkennungsalgorithmus Listenabsätze, wenn Listennummern entweder mit einem Punkt, einer rechten Klammer oder einem Aufzählungszeichen (wie „•“, „*“, „-“ oder „o“) enden. Wenn diese Option auf „true“ gesetzt ist, werden Leerzeichen auch als Trennzeichen für Listennummern verwendet: Der Listenerkennungsalgorithmus für die Nummerierung im arabischen Stil (1., 1.1.2.) verwendet sowohl Leerzeichen als auch Punktsymbole („.“).

### Siehe auch

* class [TextEditOptions](../../texteditoptions)
* namensraum [GroupDocs.Editor.Options](../../texteditoptions)
* Montage [GroupDocs.Editor](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Editor.dll -->