---
title: DublinCorePackage
second_title: Справочник по API GroupDocs.Metadata для .NET
description: Получает пакет метаданных Dublin Core извлеченный из документа.
type: docs
weight: 20
url: /ru/net/groupdocs.metadata.formats.document/wordprocessingrootpackage/dublincorepackage/
---
## WordProcessingRootPackage.DublinCorePackage property

Получает пакет метаданных Dublin Core, извлеченный из документа.

```csharp
public DublinCorePackage DublinCorePackage { get; }
```

### Стоимость имущества

Пакет метаданных Dublin Core, извлеченный из документа.

### Примечания

**Узнать больше**

* [Работа с метаданными в документах WordProcessing](https://docs.groupdocs.com/display/metadatanet/Working+with+metadata+in+WordProcessing+documents)

### Примеры

В этом примере показано, как извлечь метаданные Dublin Core из документа WordProcessing.

```csharp
using (Metadata metadata = new Metadata(Constants.InputDocx))
{
    var root = metadata.GetRootPackage<WordProcessingRootPackage>();

    if (root.DublinCorePackage != null)
    {
        Console.WriteLine(root.DublinCorePackage.Format);
        Console.WriteLine(root.DublinCorePackage.Contributor);
        Console.WriteLine(root.DublinCorePackage.Coverage);
        Console.WriteLine(root.DublinCorePackage.Creator);
        Console.WriteLine(root.DublinCorePackage.Source);
        Console.WriteLine(root.DublinCorePackage.Description);

        // ...
    }
}
```

### Смотрите также

* class [DublinCorePackage](../../../groupdocs.metadata.standards.dublincore/dublincorepackage)
* class [WordProcessingRootPackage](../../wordprocessingrootpackage)
* пространство имен [GroupDocs.Metadata.Formats.Document](../../wordprocessingrootpackage)
* сборка [GroupDocs.Metadata](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Metadata.dll -->
