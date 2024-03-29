---
title: MarkdownImageLoadingAction
second_title: Справочник по API GroupDocs.Editor для .NET
description: Определяет режим загрузки изображения при открытии для редактирования файла в формате Markdown
type: docs
weight: 980
url: /ru/net/groupdocs.editor.options/markdownimageloadingaction/
---
## MarkdownImageLoadingAction enumeration

Определяет режим загрузки изображения при открытии для редактирования файла в формате Markdown

```csharp
public enum MarkdownImageLoadingAction : byte
```

### Ценности

| Имя | Ценность | Описание |
| --- | --- | --- |
| Default | `0` | GroupDocs.Editor загрузит этот ресурс как обычно |
| Skip | `1` | GroupDocs.Editor пропустит загрузку этого изображения |
| UserProvided | `2` | GroupDocs.Editor будет использовать массив байтов, предоставленный пользователем в[`SetData`](../markdownimageloadargs/setdata) как изображение data |

### Смотрите также

* пространство имен [GroupDocs.Editor.Options](../../groupdocs.editor.options)
* сборка [GroupDocs.Editor](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Editor.dll -->
