---
title: Sanitize
second_title: Справочник по API GroupDocs.Metadata для .NET
description: Удаляет доступные для записи свойства метаданных из всех обнаруженных пакетов или целых пакетов если это возможно. Операция является рекурсивной поэтому она также влияет на все вложенные пакеты.
type: docs
weight: 100
url: /ru/net/groupdocs.metadata/metadata/sanitize/
---
## Metadata.Sanitize method

Удаляет доступные для записи свойства метаданных из всех обнаруженных пакетов или целых пакетов, если это возможно. Операция является рекурсивной, поэтому она также влияет на все вложенные пакеты.

```csharp
public int Sanitize()
```

### Возвращаемое значение

Количество затронутых свойств.

### Примечания

**Учить больше**

* [Чистые метаданные](https://docs.groupdocs.com/display/metadatanet/Clean+metadata)

### Примеры

В этом примере показано, как удалить все обнаруженные пакеты/свойства метаданных из файла.

```csharp
using (Metadata metadata = new Metadata(Constants.InputPdf))
{
    // Удалить обнаруженные пакеты метаданных
    var affected = metadata.Sanitize();
    Console.WriteLine("Properties removed: {0}", affected);

    metadata.Save(Constants.OutputPdf);
}
```

### Смотрите также

* class [Metadata](../../metadata)
* пространство имен [GroupDocs.Metadata](../../metadata)
* сборка [GroupDocs.Metadata](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Metadata.dll -->