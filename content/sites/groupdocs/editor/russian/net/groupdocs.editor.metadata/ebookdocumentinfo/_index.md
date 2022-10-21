---
title: EbookDocumentInfo
second_title: Справочник по API GroupDocs.Editor для .NET
description: Представляет метаданные одной электронной книги document
type: docs
weight: 560
url: /ru/net/groupdocs.editor.metadata/ebookdocumentinfo/
---
## EbookDocumentInfo structure

Представляет метаданные одной электронной книги document

```csharp
public struct EbookDocumentInfo : IDocumentInfo, IEquatable<EbookDocumentInfo>
```

## Характеристики

| Имя | Описание |
| --- | --- |
| [Format](../../groupdocs.editor.metadata/ebookdocumentinfo/format) { get; } | Возвращает формат этой электронной книги |
| [IsEncrypted](../../groupdocs.editor.metadata/ebookdocumentinfo/isencrypted) { get; } | Поскольку документы электронной книги не могут быть зашифрованы паролем, это свойство всегда возвращает «false» |
| [PageCount](../../groupdocs.editor.metadata/ebookdocumentinfo/pagecount) { get; } | Возвращает количество страниц в случае MOBI или AZW3 или количество глав в случае ePub. |
| [Size](../../groupdocs.editor.metadata/ebookdocumentinfo/size) { get; } | Возвращает размер этой электронной книги в байтах document |

## Методы

| Имя | Описание |
| --- | --- |
| [Equals](../../groupdocs.editor.metadata/ebookdocumentinfo/equals#equals)(EbookDocumentInfo) | Определяет, равен ли этот экземпляр другому указанному EbookDocumentInfo instance |

### Смотрите также

* interface [IDocumentInfo](../idocumentinfo)
* пространство имен [GroupDocs.Editor.Metadata](../../groupdocs.editor.metadata)
* сборка [GroupDocs.Editor](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Editor.dll -->