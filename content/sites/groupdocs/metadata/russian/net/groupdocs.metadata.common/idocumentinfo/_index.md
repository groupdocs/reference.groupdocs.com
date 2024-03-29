---
title: IDocumentInfo
second_title: Справочник по API GroupDocs.Metadata для .NET
description: Предоставляет общую информацию о загруженном документе.
type: docs
weight: 90
url: /ru/net/groupdocs.metadata.common/idocumentinfo/
---
## IDocumentInfo interface

Предоставляет общую информацию о загруженном документе.

```csharp
public interface IDocumentInfo
```

## Характеристики

| Имя | Описание |
| --- | --- |
| [FileType](../../groupdocs.metadata.common/idocumentinfo/filetype) { get; } | Получает тип файла загруженного документа. |
| [IsEncrypted](../../groupdocs.metadata.common/idocumentinfo/isencrypted) { get; } | Получает значение, указывающее, зашифрован ли документ и требует ли пароль для открытия. |
| [PageCount](../../groupdocs.metadata.common/idocumentinfo/pagecount) { get; } | Получает количество страниц (слайдов, листов и т.д.) в загруженном документе. |
| [Pages](../../groupdocs.metadata.common/idocumentinfo/pages) { get; } | Получает коллекцию объектов, представляющих общую информацию о страницах документа (слайды, рабочие листы и т. д.). |
| [Size](../../groupdocs.metadata.common/idocumentinfo/size) { get; } | Получает размер загруженного документа в байтах. |

### Примечания

**Узнать больше**

* [Получить информацию о документе](https://docs.groupdocs.com/display/metadatanet/Get+document+info)

### Примеры

В этом примере показано, как извлечь основную информацию о формате из файла.

```csharp
using (Metadata metadata = new Metadata(Constants.InputXlsx))
{
    if (metadata.FileFormat != FileFormat.Unknown)
    {
        IDocumentInfo info = metadata.GetDocumentInfo();

        Console.WriteLine("File format: {0}", info.FileType.FileFormat);
        Console.WriteLine("File extension: {0}", info.FileType.Extension);
        Console.WriteLine("MIME Type: {0}", info.FileType.MimeType);
        Console.WriteLine("Number of pages: {0}", info.PageCount);
        Console.WriteLine("Document size: {0} bytes", info.Size);
        Console.WriteLine("Is document encrypted: {0}", info.IsEncrypted);
    }
}
```

### Смотрите также

* пространство имен [GroupDocs.Metadata.Common](../../groupdocs.metadata.common)
* сборка [GroupDocs.Metadata](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Metadata.dll -->
