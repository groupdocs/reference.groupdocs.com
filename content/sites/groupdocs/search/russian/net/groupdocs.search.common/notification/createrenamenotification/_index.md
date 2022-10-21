---
title: CreateRenameNotification
second_title: GroupDocs.Search для справочника API .NET
description: Создает объект уведомления для переименования проиндексированного документа который был переименован и не нуждается в переиндексации. Переименованный документ не будет переиндексирован во время следующей операции обновления даже если его содержимое было изменено.
type: docs
weight: 10
url: /ru/net/groupdocs.search.common/notification/createrenamenotification/
---
## Notification.CreateRenameNotification method

Создает объект уведомления для переименования проиндексированного документа, который был переименован и не нуждается в переиндексации. Переименованный документ не будет переиндексирован во время следующей операции обновления, даже если его содержимое было изменено.

```csharp
public static Notification CreateRenameNotification(string oldPath, string newPath)
```

| Параметр | Тип | Описание |
| --- | --- | --- |
| oldPath | String | Старый путь к проиндексированному документу. |
| newPath | String | Новый путь к проиндексированному документу. |

### Возвращаемое значение

Новый объект уведомления о переименовании.

### Смотрите также

* class [Notification](../../notification)
* пространство имен [GroupDocs.Search.Common](../../notification)
* сборка [GroupDocs.Search](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Search.dll -->