---
title: GetPackage
second_title: GroupDocs.Metadata für .NET-API-Referenz
description: Ruft Paket nach Namensraum uri ab.
type: docs
weight: 110
url: /de/net/groupdocs.metadata.standards.xmp/xmppacketwrapper/getpackage/
---
## XmpPacketWrapper.GetPackage method

Ruft Paket nach Namensraum uri ab.

```csharp
public XmpPackage GetPackage(string namespaceUri)
```

| Parameter | Typ | Beschreibung |
| --- | --- | --- |
| namespaceUri | String | Paketschema uri. |

### Rückgabewert

Angemessen[`XmpPackage`](../../xmppackage) wenn Paket gefunden von*namespaceUri*; sonst null.

### Ausnahmen

| Ausnahme | Bedingung |
| --- | --- |
| ArgumentNullException | Namespace-URI darf nicht null sein. |

### Siehe auch

* class [XmpPackage](../../xmppackage)
* class [XmpPacketWrapper](../../xmppacketwrapper)
* namensraum [GroupDocs.Metadata.Standards.Xmp](../../xmppacketwrapper)
* Montage [GroupDocs.Metadata](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Metadata.dll -->