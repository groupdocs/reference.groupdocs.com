---
title: MetadataRedaction
second_title: Справочник по API GroupDocs.Redaction для .NET
description: Представляет базовый абстрактный класс для редактирования метаданных документа.
type: docs
weight: 520
url: /ru/net/groupdocs.redaction.redactions/metadataredaction/
---
## MetadataRedaction class

Представляет базовый абстрактный класс для редактирования метаданных документа.

```csharp
public abstract class MetadataRedaction : Redaction
```

## Характеристики

| Имя | Описание |
| --- | --- |
| virtual [Description](../../groupdocs.redaction/redaction/description) { get; } | Возвращает строку, описывающую редактирование и его параметры. |
| [Filter](../../groupdocs.redaction.redactions/metadataredaction/filter) { get; set; } | Получает или задает фильтр, который используется для выбора всех или определенных метаданных, например автора или компании. |

## Методы

| Имя | Описание |
| --- | --- |
| override [ApplyTo](../../groupdocs.redaction.redactions/metadataredaction/applyto)(DocumentFormatInstance) | Применяет редактирование к заданному экземпляру формата. |

### Примечания

**Учить больше**

* Подробнее о редактировании метаданных документа: [Редакции метаданных](https://docs.groupdocs.com/redaction/net/metadata-redactions/)

### Смотрите также

* class [Redaction](../../groupdocs.redaction/redaction)
* пространство имен [GroupDocs.Redaction.Redactions](../../groupdocs.redaction.redactions)
* сборка [GroupDocs.Redaction](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Redaction.dll -->