---
title: OperationFinished
second_title: GroupDocs.Search для справочника API .NET
description: Происходит после завершения операции с индексом.
type: docs
weight: 40
url: /ru/net/groupdocs.search.events/eventhub/operationfinished/
---
## EventHub.OperationFinished event

Происходит после завершения операции с индексом.

```csharp
public event EventHandler<OperationFinishedEventArgs> OperationFinished;
```

### Примеры

В примере показано, как использовать событие.

```csharp
string indexFolder = @"c:\MyIndex\";
string documentsFolder = @"c:\MyDocuments\";

// Создание индекса
Index index = new Index(indexFolder);

// Подписка на событие
index.Events.OperationFinished += (sender, args) =>
{
    Console.WriteLine("Operation finished: " + args.OperationType);
    Console.WriteLine("Message: " + args.Message);
    Console.WriteLine("Index folder: " + args.IndexFolder);
    Console.WriteLine("Time: " + args.Time);
};

// Индексация документов из указанной папки
index.Add(documentsFolder);
```

### Смотрите также

* class [OperationFinishedEventArgs](../../operationfinishedeventargs)
* class [EventHub](../../eventhub)
* пространство имен [GroupDocs.Search.Events](../../eventhub)
* сборка [GroupDocs.Search](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Search.dll -->