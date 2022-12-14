---
title: CreateResourceStream
second_title: Справочник по API GroupDocs.Viewer для .NET
description: Представляет метод который создает экземпляр потока используемого для записи выходных данных HTMLресурса.
type: docs
weight: 140
url: /ru/net/groupdocs.viewer.interfaces/createresourcestream/
---
## CreateResourceStream delegate

Представляет метод, который создает экземпляр потока, используемого для записи выходных данных HTML-ресурса.

```csharp
public delegate Stream CreateResourceStream(int pageNumber, Resource resource);
```

| Параметр | Тип | Описание |
| --- | --- | --- |
| pageNumber | Int32 | Номер страницы. |
| resource | Resource | Ресурс HTML, такой как шрифт, стиль, изображение или графика. |

### Возвращаемое значение

Поток, используемый для записи выходных данных ресурса HTML.

### Смотрите также

* class [Resource](../../groupdocs.viewer.results/resource)
* пространство имен [GroupDocs.Viewer.Interfaces](../../groupdocs.viewer.interfaces)
* сборка [GroupDocs.Viewer](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Viewer.dll -->
