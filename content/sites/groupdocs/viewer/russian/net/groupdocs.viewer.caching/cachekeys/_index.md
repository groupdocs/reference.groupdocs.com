---
title: CacheKeys
second_title: Справочник по API GroupDocs.Viewer для .NET
description: Предоставляет методы для получения уникального идентификатора записи кэша.
type: docs
weight: 10
url: /ru/net/groupdocs.viewer.caching/cachekeys/
---
## CacheKeys class

Предоставляет методы для получения уникального идентификатора записи кэша.

```csharp
public static class CacheKeys
```

## Методы

| Имя | Описание |
| --- | --- |
| static [GetAttachmentKey](../../groupdocs.viewer.caching/cachekeys/getattachmentkey)(string) | Возвращает уникальный идентификатор записи кэша, представляющей вложенный файл. |
| static [GetAttachmentsKey](../../groupdocs.viewer.caching/cachekeys/getattachmentskey)() | Возвращает уникальный идентификатор записи кэша, представляющей набор[`Attachment`](../../groupdocs.viewer.results/attachment) объекты. |
| static [GetFileInfoKey](../../groupdocs.viewer.caching/cachekeys/getfileinfokey)() | Возвращает уникальный идентификатор записи кэша, представляющей[`ViewInfo`](../../groupdocs.viewer.results/viewinfo) объект. |
| static [GetFileKey](../../groupdocs.viewer.caching/cachekeys/getfilekey)(string) | Возвращает уникальный идентификатор записи кэша, представляющей файл. |
| static [GetPageKey](../../groupdocs.viewer.caching/cachekeys/getpagekey)(int, string) | Возвращает уникальный идентификатор записи кэша, представляющей файл подкачки. |
| static [GetResourceFilter](../../groupdocs.viewer.caching/cachekeys/getresourcefilter)(int) | Возвращает строку фильтра для поиска записей кэша, представляющих[`Resource`](../../groupdocs.viewer.results/resource) объекты. |
| static [GetResourceKey](../../groupdocs.viewer.caching/cachekeys/getresourcekey)(int, Resource) | Возвращает уникальный идентификатор записи кэша, представляющей[`Resource`](../../groupdocs.viewer.results/resource) объект. |
| static [GetViewInfoKey](../../groupdocs.viewer.caching/cachekeys/getviewinfokey)() | Возвращает уникальный идентификатор записи кэша, представляющей[`ViewInfo`](../../groupdocs.viewer.results/viewinfo) объект. |

### Смотрите также

* пространство имен [GroupDocs.Viewer.Caching](../../groupdocs.viewer.caching)
* сборка [GroupDocs.Viewer](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Viewer.dll -->