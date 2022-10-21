---
title: FromExtension
second_title: Справочник по API GroupDocs.Editor для .NET
description: Возвращает экземплярTextualFormatsgroupdocs.editor.formats/textualformatsструктура связанная с указанным расширением имени файла или выдает исключение если расширение не может быть правильно проанализировано
type: docs
weight: 80
url: /ru/net/groupdocs.editor.formats/textualformats/fromextension/
---
## TextualFormats.FromExtension method

Возвращает экземпляр[`TextualFormats`](../../textualformats)структура, связанная с указанным расширением имени файла, или выдает исключение, если расширение не может быть правильно проанализировано

```csharp
public static TextualFormats FromExtension(string extension)
```

| Параметр | Тип | Описание |
| --- | --- | --- |
| extension | String | Расширение имени файла любого поддерживаемого текстового формата, с начальной точкой или без нее, независимо от регистра. Не может быть NULL или пустым, должно быть допустимым. |

### Возвращаемое значение

Экземпляр структуры TextualFormats в случае успеха или выброшенное исключение в случае сбоя

### Смотрите также

* struct [TextualFormats](../../textualformats)
* пространство имен [GroupDocs.Editor.Formats](../../textualformats)
* сборка [GroupDocs.Editor](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Editor.dll -->