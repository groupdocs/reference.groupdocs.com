---
title: DocumentFilter
second_title: GroupDocs.Search для справочника API .NET
description: Получает или задает фильтр документа. DocumentFiltergroupdocs.search/indexsettings/documentfilter работает по логике включения. ИспользуйтеDocumentFiltergroupdocs.search.options/documentfilter класс для создания экземпляров фильтра документов. Значение по умолчаниюнулевой  что означает что все добавленные документы проиндексированы.
type: docs
weight: 40
url: /ru/net/groupdocs.search/indexsettings/documentfilter/
---
## IndexSettings.DocumentFilter property

Получает или задает фильтр документа. `DocumentFilter` работает по логике включения. Используйте[`DocumentFilter`](../../../groupdocs.search.options/documentfilter) класс для создания экземпляров фильтра документов. Значение по умолчанию:`нулевой` , что означает, что все добавленные документы проиндексированы.

```csharp
public DocumentFilter DocumentFilter { get; set; }
```

### Стоимость имущества

Фильтр документов.

### Примеры

В примере показано, как настроить фильтр документов.

```csharp
string indexFolder = @"c:\MyIndex\";
string documentsFolder = @"c:\MyDocuments\";

// Создание фильтра, пропускающего документы с расширениями '.doc', '.docx', '.rtf'
IndexSettings settings = new IndexSettings();
DocumentFilter fileExtensionFilter = DocumentFilter.CreateFileExtension(".doc", ".docx", ".rtf"); // Создание фильтра расширения файла
DocumentFilter invertedFilter = DocumentFilter.CreateNot(fileExtensionFilter); // Инвертирование фильтра расширения файла
settings.DocumentFilter = invertedFilter;

// Создание индекса в указанной папке
Index index = new Index(indexFolder, settings);

// Индексация документов
index.Add(documentsFolder);

// Идет поиск
SearchResult result = index.Search("Einstein");
```

### Смотрите также

* class [DocumentFilter](../../../groupdocs.search.options/documentfilter)
* class [IndexSettings](../../indexsettings)
* пространство имен [GroupDocs.Search](../../indexsettings)
* сборка [GroupDocs.Search](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Search.dll -->