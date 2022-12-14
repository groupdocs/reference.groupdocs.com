---
title: StatusChanged
second_title: GroupDocs.Search для справочника API .NET
description: Происходит при изменении состояния индекса.
type: docs
weight: 80
url: /ru/net/groupdocs.search.events/eventhub/statuschanged/
---
## EventHub.StatusChanged event

Происходит при изменении состояния индекса.

```csharp
public event EventHandler<BaseIndexEventArgs> StatusChanged;
```

### Примеры

В примере показано, как использовать событие.

```csharp
string indexFolder = @"c:\MyIndex\";
string documentsFolder = @"c:\MyDocuments\";

// Создание индекса
Index index = new Index(indexFolder);

// Подписка на событие
index.Events.StatusChanged += (sender, args) =>
{
    if (args.Status != IndexStatus.InProgress)
    {
        // Здесь должно быть уведомление о завершении операции
    }
};

// Установка флага для асинхронного индексирования
IndexingOptions options = new IndexingOptions();
options.IsAsync = true;

// Асинхронное индексирование документов из указанной папки
// Метод завершается до завершения операции
index.Add(documentsFolder, options);
```

### Смотрите также

* class [BaseIndexEventArgs](../../baseindexeventargs)
* class [EventHub](../../eventhub)
* пространство имен [GroupDocs.Search.Events](../../eventhub)
* сборка [GroupDocs.Search](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Search.dll -->
