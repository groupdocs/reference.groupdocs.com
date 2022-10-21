---
title: ProcessCompleteEventHandler
second_title: Справочник по API GroupDocs.Signature для .NET
description: Представляет делегат метода который будет обрабатывать процессы полных событий для подписания проверки и поиска.
type: docs
weight: 1740
url: /ru/net/groupdocs.signature/processcompleteeventhandler/
---
## ProcessCompleteEventHandler delegate

Представляет делегат метода, который будет обрабатывать процессы полных событий для подписания, проверки и поиска.

```csharp
public delegate void ProcessCompleteEventHandler(Signature signature, 
    ProcessCompleteEventArgs args);
```

| Параметр | Тип | Описание |
| --- | --- | --- |
| signature | Signature | Объект подписи |
| args | ProcessCompleteEventArgs | Аргументы[`ProcessCompleteEventArgs`](../processcompleteeventargs)которые определяют свойства события Completed. |

### Смотрите также

* class [Signature](../signature)
* class [ProcessCompleteEventArgs](../processcompleteeventargs)
* пространство имен [GroupDocs.Signature](../../groupdocs.signature)
* сборка [GroupDocs.Signature](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Signature.dll -->