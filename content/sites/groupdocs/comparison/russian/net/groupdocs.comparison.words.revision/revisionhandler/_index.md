---
title: RevisionHandler
second_title: Справочник по API GroupDocs.Comparison для .NET
description: Представляет основной класс управляющий обработкой редакций.
type: docs
weight: 460
url: /ru/net/groupdocs.comparison.words.revision/revisionhandler/
---
## RevisionHandler class

Представляет основной класс, управляющий обработкой редакций.

```csharp
public class RevisionHandler : IDisposable
```

## Конструкторы

| Имя | Описание |
| --- | --- |
| [RevisionHandler](revisionhandler#constructor)(Stream) | Инициализирует новый экземпляр[`RevisionHandler`](../revisionhandler) class с файловым потоком с ревизиями. |
| [RevisionHandler](revisionhandler#constructor_1)(string) | Инициализирует новый экземпляр[`RevisionHandler`](../revisionhandler) class с указанием пути к файлу с ревизиями. |

## Методы

| Имя | Описание |
| --- | --- |
| [ApplyRevisionChanges](../../groupdocs.comparison.words.revision/revisionhandler/applyrevisionchanges#applyrevisionchanges)(ApplyRevisionOptions) | Обрабатывает изменения в ревизиях и применяет их к тому же файлу, из которого были взяты ревизии. |
| [ApplyRevisionChanges](../../groupdocs.comparison.words.revision/revisionhandler/applyrevisionchanges#applyrevisionchanges_1)(Stream, ApplyRevisionOptions) | Обрабатывает изменения в ревизиях, и результат записывается в поток документов. |
| [ApplyRevisionChanges](../../groupdocs.comparison.words.revision/revisionhandler/applyrevisionchanges#applyrevisionchanges_2)(string, ApplyRevisionOptions) | Обрабатывает изменения в ревизиях, и результат записывается в указанный файл по пути. |
| [Dispose](../../groupdocs.comparison.words.revision/revisionhandler/dispose)() | Освобождает ресурсы. |
| [GetRevisions](../../groupdocs.comparison.words.revision/revisionhandler/getrevisions)() | Получает список всех ревизий. |

### Смотрите также

* пространство имен [GroupDocs.Comparison.Words.Revision](../../groupdocs.comparison.words.revision)
* сборка [GroupDocs.Comparison](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Comparison.dll -->
