---
title: SplitHeadingLevel
second_title: Справочник по API GroupDocs.Editor для .NET
description: Указывает максимальный уровень заголовков на котором можно разделить файл ePub. Значение по умолчанию2 . Установка на0 отключит разделение поэтому все содержимое электронной книги будет объединено в единый пакет внутри ePub.
type: docs
weight: 30
url: /ru/net/groupdocs.editor.options/epubsaveoptions/splitheadinglevel/
---
## EpubSaveOptions.SplitHeadingLevel property

Указывает максимальный уровень заголовков, на котором можно разделить файл ePub. Значение по умолчанию`2` . Установка на`0` отключит разделение, поэтому все содержимое электронной книги будет объединено в единый пакет внутри ePub.

```csharp
public int SplitHeadingLevel { get; set; }
```

### Примечания

Если для этого свойства задано значение от 1 до 9, документ будет разбит на абзацы, отформатированные с помощью .**Заголовок 1** ,**Заголовок 2** ,**Заголовок 3** и т. д. стили до указанного уровня заголовка.

По умолчанию только**Заголовок 1** и**Заголовок 2** абзацы приводят к разделению документа. Установка этого свойства в ноль приведет к тому, что документ вообще не будет разделен на абзацы заголовков.

### Смотрите также

* class [EpubSaveOptions](../../epubsaveoptions)
* пространство имен [GroupDocs.Editor.Options](../../epubsaveoptions)
* сборка [GroupDocs.Editor](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Editor.dll -->
