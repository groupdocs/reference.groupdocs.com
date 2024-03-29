---
title: MetadataSearchRedaction
second_title: Справочник по API GroupDocs.Redaction для .NET
description: Представляет редактирование метаданных которое ищет и редактирует метаданные с использованием регулярных выражений соответствующих ключей и/или значений.
type: docs
weight: 540
url: /ru/net/groupdocs.redaction.redactions/metadatasearchredaction/
---
## MetadataSearchRedaction class

Представляет редактирование метаданных, которое ищет и редактирует метаданные с использованием регулярных выражений, соответствующих ключей и/или значений.

```csharp
public class MetadataSearchRedaction : MetadataRedaction
```

## Конструкторы

| Имя | Описание |
| --- | --- |
| [MetadataSearchRedaction](metadatasearchredaction#constructor_2)(Regex, string) | Инициализирует новый экземпляр класса MetadataSearchRedaction, используя значение для соответствия отредактированным элементам. |
| [MetadataSearchRedaction](metadatasearchredaction#constructor)(string, string) | Инициализирует новый экземпляр класса MetadataSearchRedaction, используя значение для соответствия отредактированным элементам. |
| [MetadataSearchRedaction](metadatasearchredaction#constructor_3)(Regex, string, Regex) | Инициализирует новый экземпляр класса MetadataSearchRedaction, используя имя и значение элемента для соответствия отредактированным элементам. |
| [MetadataSearchRedaction](metadatasearchredaction#constructor_1)(string, string, string) | Инициализирует новый экземпляр класса MetadataSearchRedaction, используя имя и значение элемента для соответствия отредактированным элементам. |

## Характеристики

| Имя | Описание |
| --- | --- |
| override [Description](../../groupdocs.redaction.redactions/metadatasearchredaction/description) { get; } | Возвращает строку, описывающую редактирование и его параметры. |
| [Filter](../../groupdocs.redaction.redactions/metadataredaction/filter) { get; set; } | Получает или задает фильтр, который используется для выбора всех или определенных метаданных, например автора или компании. |
| [KeyExpression](../../groupdocs.redaction.redactions/metadatasearchredaction/keyexpression) { get; } | Получает регулярное выражение для соответствия имени (ключу) элемента метаданных. |
| [Replacement](../../groupdocs.redaction.redactions/metadatasearchredaction/replacement) { get; } | Получает текстовое значение замены. |
| [ValueExpression](../../groupdocs.redaction.redactions/metadatasearchredaction/valueexpression) { get; } | Получает регулярное выражение для соответствия тексту значения элемента метаданных. |

## Методы

| Имя | Описание |
| --- | --- |
| override [ApplyTo](../../groupdocs.redaction.redactions/metadataredaction/applyto)(DocumentFormatInstance) | Применяет редактирование к заданному экземпляру формата. |

### Примечания

**Узнать больше**

* Подробнее о применении правок: [Основы редактирования](https://docs.groupdocs.com/redaction/net/redaction-basics/)
* Подробнее о редактировании метаданных документа: [Редакции метаданных](https://docs.groupdocs.com/redaction/net/metadata-redactions/)

### Примеры

В следующем примере показано, как искать и редактировать определенный текст в определенных метаданных.

```csharp
using (Redactor redactor = new Redactor(@"C:\sample.docx"))
{
   MetadataSearchRedaction redaction = new MetadataSearchRedaction("Company Ltd.", "--company--");
   // Если не установлено, применяется ко всем элементам метаданных
   redaction.Filter = MetadataFilters.Company;
   redactor.Apply(redaction);
   redactor.Save();
}
```

### Смотрите также

* class [MetadataRedaction](../metadataredaction)
* пространство имен [GroupDocs.Redaction.Redactions](../../groupdocs.redaction.redactions)
* сборка [GroupDocs.Redaction](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Redaction.dll -->
