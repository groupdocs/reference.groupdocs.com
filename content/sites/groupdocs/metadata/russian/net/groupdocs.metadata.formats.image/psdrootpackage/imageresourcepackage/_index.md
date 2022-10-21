---
title: ImageResourcePackage
second_title: Справочник по API GroupDocs.Metadata для .NET
description: Получает пакет метаданных Photoshop Image Resource. Блоки ресурсов изображения являются основной структурной единицей собственного формата файлов Photoshop.
type: docs
weight: 20
url: /ru/net/groupdocs.metadata.formats.image/psdrootpackage/imageresourcepackage/
---
## PsdRootPackage.ImageResourcePackage property

Получает пакет метаданных Photoshop Image Resource. Блоки ресурсов изображения являются основной структурной единицей собственного формата файлов Photoshop.

```csharp
public ImageResourcePackage ImageResourcePackage { get; }
```

### Стоимость имущества

Пакет метаданных ресурса изображения.

### Примечания

**Учить больше**

* [Работа с метаданными в изображениях PSD](https://docs.groupdocs.com/display/metadatanet/Working+with+metadata+in+PSD+images)

### Примеры

В приведенном ниже примере кода показано, как извлечь блоки ресурсов изображения (строительные блоки формата файла Photoshop) из изображения PSD.

```csharp
using (Metadata metadata = new Metadata(Constants.PsdWithIrb))
{
    var root = metadata.GetRootPackage<PsdRootPackage>();

    if (root.ImageResourcePackage != null)
    {
        foreach (var block in root.ImageResourcePackage.ToList())
        {
            Console.WriteLine(block.Signature);
            Console.WriteLine(block.ID);
            Console.WriteLine(block.Name);
            Console.WriteLine(block.Data);
        }
    }
}
```

### Смотрите также

* class [ImageResourcePackage](../../imageresourcepackage)
* class [PsdRootPackage](../../psdrootpackage)
* пространство имен [GroupDocs.Metadata.Formats.Image](../../psdrootpackage)
* сборка [GroupDocs.Metadata](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Metadata.dll -->