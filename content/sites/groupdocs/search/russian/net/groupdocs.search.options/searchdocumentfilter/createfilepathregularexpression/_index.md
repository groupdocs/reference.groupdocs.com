---
title: CreateFilePathRegularExpression
second_title: GroupDocs.Search для справочника API .NET
description: Создает фильтр для пропуска документов не соответствующих регулярному выражению. Регулярное выражение применяется к полному пути документа.
type: docs
weight: 40
url: /ru/net/groupdocs.search.options/searchdocumentfilter/createfilepathregularexpression/
---
## CreateFilePathRegularExpression(string) {#createfilepathregularexpression}

Создает фильтр для пропуска документов, не соответствующих регулярному выражению. Регулярное выражение применяется к полному пути документа.

```csharp
public static ISearchDocumentFilter CreateFilePathRegularExpression(string pattern)
```

| Параметр | Тип | Описание |
| --- | --- | --- |
| pattern | String | Шаблон регулярного выражения. |

### Возвращаемое значение

Фильтр поиска документов по имени файла.

### Смотрите также

* interface [ISearchDocumentFilter](../../isearchdocumentfilter)
* class [SearchDocumentFilter](../../searchdocumentfilter)
* пространство имен [GroupDocs.Search.Options](../../searchdocumentfilter)
* сборка [GroupDocs.Search](../../../)

---

## CreateFilePathRegularExpression(string, RegexOptions) {#createfilepathregularexpression_1}

Создает фильтр для пропуска документов, не соответствующих регулярному выражению. Регулярное выражение применяется к полному пути документа.

```csharp
public static ISearchDocumentFilter CreateFilePathRegularExpression(string pattern, 
    RegexOptions options)
```

| Параметр | Тип | Описание |
| --- | --- | --- |
| pattern | String | Шаблон регулярного выражения. |
| options | RegexOptions | Параметры регулярного выражения. |

### Возвращаемое значение

Фильтр поиска документов по имени файла.

### Смотрите также

* interface [ISearchDocumentFilter](../../isearchdocumentfilter)
* class [SearchDocumentFilter](../../searchdocumentfilter)
* пространство имен [GroupDocs.Search.Options](../../searchdocumentfilter)
* сборка [GroupDocs.Search](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Search.dll -->
