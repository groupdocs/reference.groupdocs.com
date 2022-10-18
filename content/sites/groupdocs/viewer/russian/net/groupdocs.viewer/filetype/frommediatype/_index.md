---
title: FromMediaType
second_title: Справочник по API GroupDocs.Viewer для .NET
description: Сопоставляет тип носителя файла с типом файла например application/pdf будет сопоставлен сPDFgroupdocs.viewer/filetype/pdf .
type: docs
weight: 1890
url: /ru/net/groupdocs.viewer/filetype/frommediatype/
---
## FileType.FromMediaType method

Сопоставляет тип носителя файла с типом файла, например, «application/pdf» будет сопоставлен с[`PDF`](../pdf) .

```csharp
public static FileType FromMediaType(string mediaType)
```

| Параметр | Тип | Описание |
| --- | --- | --- |
| mediaType | String | Тип носителя файла, например, application/pdf. |

### Возвращаемое значение

Возвращает соответствующий тип носителя, если он найден, в противном случае возвращает значение по умолчанию.[`Unknown`](../unknown) тип файла.

### Смотрите также

* class [FileType](../../filetype)
* пространство имен [GroupDocs.Viewer](../../filetype)
* сборка [GroupDocs.Viewer](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Viewer.dll -->