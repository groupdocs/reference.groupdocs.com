---
title: XmpPackage
second_title: Справочник по API GroupDocs.Metadata для .NET
description: Получает или задает пакет метаданных XMP.
type: docs
weight: 50
url: /ru/net/groupdocs.metadata.formats.image/jpegrootpackage/xmppackage/
---
## JpegRootPackage.XmpPackage property

Получает или задает пакет метаданных XMP.

```csharp
public XmpPacketWrapper XmpPackage { get; set; }
```

### Стоимость имущества

Пакет метаданных XMP.

### Примечания

**Учить больше**

* [Работа с метаданными XMP](https://docs.groupdocs.com/display/metadatanet/Working+with+XMP+metadata)

### Примеры

В этом примере показано, как извлечь метаданные XMP из файла.

```csharp
using (Metadata metadata = new Metadata(Constants.JpegWithXmp))
{
    var root = metadata.GetRootPackage<JpegRootPackage>();
    if (root.XmpPackage != null)
    {
        if (root.XmpPackage.Schemes.XmpBasic != null)
        {
            Console.WriteLine(root.XmpPackage.Schemes.XmpBasic.CreatorTool);
            Console.WriteLine(root.XmpPackage.Schemes.XmpBasic.CreateDate);
            Console.WriteLine(root.XmpPackage.Schemes.XmpBasic.ModifyDate);
            Console.WriteLine(root.XmpPackage.Schemes.XmpBasic.Label);
            Console.WriteLine(root.XmpPackage.Schemes.XmpBasic.Nickname);

            // ...
        }

        if (root.XmpPackage.Schemes.DublinCore != null)
        {
            Console.WriteLine(root.XmpPackage.Schemes.DublinCore.Format);
            Console.WriteLine(root.XmpPackage.Schemes.DublinCore.Coverage);
            Console.WriteLine(root.XmpPackage.Schemes.DublinCore.Identifier);
            Console.WriteLine(root.XmpPackage.Schemes.DublinCore.Source);

            // ...
        }

        if (root.XmpPackage.Schemes.Photoshop != null)
        {
            Console.WriteLine(root.XmpPackage.Schemes.Photoshop.ColorMode);
            Console.WriteLine(root.XmpPackage.Schemes.Photoshop.IccProfile);
            Console.WriteLine(root.XmpPackage.Schemes.Photoshop.Country);
            Console.WriteLine(root.XmpPackage.Schemes.Photoshop.City);
            Console.WriteLine(root.XmpPackage.Schemes.Photoshop.DateCreated);

            // ... 
        }

        // ...
    }
}
```

### Смотрите также

* class [XmpPacketWrapper](../../../groupdocs.metadata.standards.xmp/xmppacketwrapper)
* class [JpegRootPackage](../../jpegrootpackage)
* пространство имен [GroupDocs.Metadata.Formats.Image](../../jpegrootpackage)
* сборка [GroupDocs.Metadata](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Metadata.dll -->