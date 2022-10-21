---
title: ApeV2
second_title: Справочник по API GroupDocs.Metadata для .NET
description: Получает метаданные APE v2.
type: docs
weight: 10
url: /ru/net/groupdocs.metadata.formats.audio/mp3rootpackage/apev2/
---
## MP3RootPackage.ApeV2 property

Получает метаданные APE v2.

```csharp
public ApePackage ApeV2 { get; }
```

### Стоимость имущества

Метаданные APE v2.

### Примеры

В этом примере показано, как читать тег APEv2 в файле MP3.

```csharp
using (Metadata metadata = new Metadata(Constants.MP3WithApe))
{
    var root = metadata.GetRootPackage<MP3RootPackage>();

    if (root.ApeV2 != null)
    {
        Console.WriteLine(root.ApeV2.Album);
        Console.WriteLine(root.ApeV2.Title);
        Console.WriteLine(root.ApeV2.Artist);
        Console.WriteLine(root.ApeV2.Composer);
        Console.WriteLine(root.ApeV2.Copyright);
        Console.WriteLine(root.ApeV2.Genre);
        Console.WriteLine(root.ApeV2.Language);

        // ...
    }
}
```

### Смотрите также

* class [ApePackage](../../apepackage)
* class [MP3RootPackage](../../mp3rootpackage)
* пространство имен [GroupDocs.Metadata.Formats.Audio](../../mp3rootpackage)
* сборка [GroupDocs.Metadata](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Metadata.dll -->