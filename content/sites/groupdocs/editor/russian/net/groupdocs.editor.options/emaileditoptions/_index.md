---
title: EmailEditOptions
second_title: Справочник по API GroupDocs.Editor для .NET
description: Позволяет указать пользовательские параметры редактирования документов в различных форматах электронной почты email
type: docs
weight: 850
url: /ru/net/groupdocs.editor.options/emaileditoptions/
---
## EmailEditOptions class

Позволяет указать пользовательские параметры редактирования документов в различных форматах электронной почты (email)

```csharp
public sealed class EmailEditOptions : IEditOptions
```

## Конструкторы

| Имя | Описание |
| --- | --- |
| [EmailEditOptions](emaileditoptions#constructor)() | Инициализирует новый экземпляр[`EmailEditOptions`](../emaileditoptions) class, где для всех параметров установлены значения по умолчанию |
| [EmailEditOptions](emaileditoptions#constructor_1)(MailMessageOutput) | Инициализирует новый экземпляр[`EmailEditOptions`](../emaileditoptions) класс с[`MailMessageOutput`](./mailmessageoutput)параметр |

## Характеристики

| Имя | Описание |
| --- | --- |
| [MailMessageOutput](../../groupdocs.editor.options/emaileditoptions/mailmessageoutput) { get; set; } | Позволяет контролировать, какие части почтового сообщения должны быть доставлены на выход[`EditableDocument`](../../groupdocs.editor/editabledocument) а затем в испускаемый HTML |

### Смотрите также

* interface [IEditOptions](../ieditoptions)
* пространство имен [GroupDocs.Editor.Options](../../groupdocs.editor.options)
* сборка [GroupDocs.Editor](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Editor.dll -->
