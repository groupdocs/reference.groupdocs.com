---
title: WordProcessingTextSignatureImplementation
second_title: Справочник по API GroupDocs.Signature для .NET
description: Указывает тип реализации текстовой подписи для документов WordProcessing.
type: docs
weight: 1060
url: /ru/net/groupdocs.signature.domain/wordprocessingtextsignatureimplementation/
---
## WordProcessingTextSignatureImplementation enumeration

Указывает тип реализации текстовой подписи для документов WordProcessing.

```csharp
public enum WordProcessingTextSignatureImplementation
```

### Ценности

| Имя | Ценность | Описание |
| --- | --- | --- |
| TextStamp | `0` | Текстовая подпись как объект метки на странице Words. |
| TextAsImage | `1` | Текстовая подпись как объект изображения на странице Words. |
| TextToFormField | `2` | Текстовая подпись в виде текста в указанном поле формы. С этим типом реализации могут использоваться только параметры TextSignOptions.Text, TextSignOptions.FormTextFieldTitle и TextSignOptions.FormTextFieldType. |
| Watermark | `3` | Текстовая подпись в качестве водяного знака на странице Words. |

### Смотрите также

* пространство имен [GroupDocs.Signature.Domain](../../groupdocs.signature.domain)
* сборка [GroupDocs.Signature](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Signature.dll -->