---
title: RemoveApeV2
second_title: Referencia de API de GroupDocs.Metadata para .NET
description: Elimina la etiqueta de audio APEv2.
type: docs
weight: 70
url: /es/net/groupdocs.metadata.formats.audio/mp3rootpackage/removeapev2/
---
## MP3RootPackage.RemoveApeV2 method

Elimina la etiqueta de audio APEv2.

```csharp
public void RemoveApeV2()
```

### Observaciones

Esta función no está disponible en modo de prueba.

### Ejemplos

Este ejemplo muestra cómo eliminar la etiqueta APEv2 de un archivo MP3.

```csharp
using (Metadata metadata = new Metadata(Constants.MP3WithApe))
{
    var root = metadata.GetRootPackage<MP3RootPackage>();

    root.RemoveApeV2();

    metadata.Save(Constants.OutputMp3);
}
```

### Ver también

* class [MP3RootPackage](../../mp3rootpackage)
* espacio de nombres [GroupDocs.Metadata.Formats.Audio](../../mp3rootpackage)
* asamblea [GroupDocs.Metadata](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Metadata.dll -->
