---
title: IptcPackage
second_title: Referencia de API de GroupDocs.Metadata para .NET
description: Obtiene o establece el paquete de metadatos IPTC.
type: docs
weight: 20
url: /es/net/groupdocs.metadata.formats.image/tiffrootpackage/iptcpackage/
---
## TiffRootPackage.IptcPackage property

Obtiene o establece el paquete de metadatos IPTC.

```csharp
public IptcRecordSet IptcPackage { get; set; }
```

### El valor de la propiedad

El paquete de metadatos IPTC.

### Observaciones

**Aprende más**

* [Trabajar con metadatos IPTC IIM](https://docs.groupdocs.com/display/metadatanet/Working+with+IPTC+IIM+metadata)

### Ejemplos

Este ejemplo muestra cómo extraer propiedades básicas de metadatos IPTC de una imagen TIFF.

```csharp
using (Metadata metadata = new Metadata(Constants.TiffWithIptc))
{
    var root = metadata.GetRootPackage<TiffRootPackage>();
    if (root.IptcPackage != null)
    {
        if (root.IptcPackage.EnvelopeRecord != null)
        {
            Console.WriteLine(root.IptcPackage.EnvelopeRecord.DateSent);
            Console.WriteLine(root.IptcPackage.EnvelopeRecord.Destination);
            Console.WriteLine(root.IptcPackage.EnvelopeRecord.FileFormat);
            Console.WriteLine(root.IptcPackage.EnvelopeRecord.FileFormatVersion);

            // ...
        }

        if (root.IptcPackage.ApplicationRecord != null)
        {
            Console.WriteLine(root.IptcPackage.ApplicationRecord.Headline);
            Console.WriteLine(root.IptcPackage.ApplicationRecord.ByLine);
            Console.WriteLine(root.IptcPackage.ApplicationRecord.ByLineTitle);
            Console.WriteLine(root.IptcPackage.ApplicationRecord.CaptionAbstract);
            Console.WriteLine(root.IptcPackage.ApplicationRecord.City);
            Console.WriteLine(root.IptcPackage.ApplicationRecord.DateCreated);
            Console.WriteLine(root.IptcPackage.ApplicationRecord.ReleaseDate);

            // ...
        }
    }
}
```

### Ver también

* class [IptcRecordSet](../../../groupdocs.metadata.standards.iptc/iptcrecordset)
* class [TiffRootPackage](../../tiffrootpackage)
* espacio de nombres [GroupDocs.Metadata.Formats.Image](../../tiffrootpackage)
* asamblea [GroupDocs.Metadata](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Metadata.dll -->