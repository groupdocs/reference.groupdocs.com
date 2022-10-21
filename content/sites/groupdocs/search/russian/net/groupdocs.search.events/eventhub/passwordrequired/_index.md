---
title: PasswordRequired
second_title: GroupDocs.Search для справочника API .NET
description: Происходит когда для открытия документа требуется пароль.
type: docs
weight: 60
url: /ru/net/groupdocs.search.events/eventhub/passwordrequired/
---
## EventHub.PasswordRequired event

Происходит, когда для открытия документа требуется пароль.

```csharp
public event EventHandler<PasswordRequiredEventArgs> PasswordRequired;
```

### Примеры

В примере показано, как использовать событие.

```csharp
string indexFolder = @"c:\MyIndex\";
string documentsFolder = @"c:\MyDocuments\";

// Создание индекса
Index index = new Index(indexFolder);

// Подписка на событие
index.Events.PasswordRequired += (sender, args) =>
{
    if (args.DocumentFullPath.EndsWith("ProtectedDocument.pdf", StringComparison.InvariantCultureIgnoreCase))
    {
        args.Password = "123456";
    }
};

// Индексация документов из указанной папки
index.Add(documentsFolder);
```

### Смотрите также

* class [PasswordRequiredEventArgs](../../passwordrequiredeventargs)
* class [EventHub](../../eventhub)
* пространство имен [GroupDocs.Search.Events](../../eventhub)
* сборка [GroupDocs.Search](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Search.dll -->