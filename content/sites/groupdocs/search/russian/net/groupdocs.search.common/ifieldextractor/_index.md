---
title: IFieldExtractor
second_title: GroupDocs.Search для справочника API .NET
description: Предоставляет методы для извлечения полей из документа.
type: docs
weight: 190
url: /ru/net/groupdocs.search.common/ifieldextractor/
---
## IFieldExtractor interface

Предоставляет методы для извлечения полей из документа.

```csharp
public interface IFieldExtractor
```

## Характеристики

| Имя | Описание |
| --- | --- |
| [Extensions](../../groupdocs.search.common/ifieldextractor/extensions) { get; } | Получает поддерживаемые расширения. |

## Методы

| Имя | Описание |
| --- | --- |
| [GetFields](../../groupdocs.search.common/ifieldextractor/getfields#getfields)(Stream) | Извлекает все поля из указанного документа. |
| [GetFields](../../groupdocs.search.common/ifieldextractor/getfields#getfields_1)(string) | Извлекает все поля из указанного документа. |

### Примечания

**Узнать больше**

* [Пользовательские экстракторы текста](https://docs.groupdocs.com/display/searchnet/Custom+text+extractors)

### Примеры

Пример демонстрирует, как реализовать интерфейс[`IFieldExtractor`](../ifieldextractor) .

```csharp
public class LogExtractor : IFieldExtractor
{
    private readonly string[] extensions = new string[] { ".log" };

    public string[] Extensions
    {
        get { return extensions; }
    }

    public DocumentField[] GetFields(string filePath)
    {
        FileInfo fileInfo = new FileInfo(filePath);
        DocumentField[] fields = new DocumentField[]
        {
            new DocumentField("FileName", fileInfo.FullName),
            new DocumentField("CreationDate", fileInfo.CreationTime.ToString(CultureInfo.InvariantCulture)),
            new DocumentField("Content", ExtractContent(filePath)),
        };
        return fields;
    }

    private string ExtractContent(string filePath)
    {
        StringBuilder result = new StringBuilder();
        using (StreamReader streamReader = File.OpenText(filePath))
        {
            string line = streamReader.ReadLine();
            string processedLine = line.Remove(0, 12);
            result.AppendLine(processedLine);
        }
        return result.ToString();
    }
}
```

Пример демонстрирует, как использовать экстрактор custorm для индексации.

```csharp
string indexFolder = @"c:\MyIndex\"; // Указываем путь к папке индекса
string documentsFolder = @"c:\MyDocuments\"; // Указываем путь к папке с документами для поиска

Index index = new Index(indexFolder); // Создание или загрузка индекса

index.IndexSettings.CustomExtractors.Add(new LogExtractor()); // Добавление пользовательского экстрактора текста в настройки индекса

index.Add(documentsFolder); // Индексация документов из указанной папки
```

### Смотрите также

* пространство имен [GroupDocs.Search.Common](../../groupdocs.search.common)
* сборка [GroupDocs.Search](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Search.dll -->
