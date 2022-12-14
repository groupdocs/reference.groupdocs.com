---
title: PageCount
second_title: Справочник по API GroupDocs.Editor для .NET
description: Возвращает количество страниц в случае MOBI или AZW3 или количество глав в случае ePub.
type: docs
weight: 30
url: /ru/net/groupdocs.editor.metadata/ebookdocumentinfo/pagecount/
---
## EbookDocumentInfo.PageCount property

Возвращает количество страниц в случае MOBI или AZW3 или количество глав в случае ePub.

```csharp
public int PageCount { get; }
```

### Примечания

Документы электронной книги обычно не имеют фиксированных страниц и, следовательно, количества страниц. В случае ePub можно рассчитать количество глав. Однако форматы MOBI и AZW3 также не имеют глав, поэтому это число рассчитывается на основе стандартного размера страницы, установленного на A4 в книжной ориентации.

### Смотрите также

* struct [EbookDocumentInfo](../../ebookdocumentinfo)
* пространство имен [GroupDocs.Editor.Metadata](../../ebookdocumentinfo)
* сборка [GroupDocs.Editor](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Editor.dll -->
