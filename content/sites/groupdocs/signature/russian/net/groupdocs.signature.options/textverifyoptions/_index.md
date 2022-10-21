---
title: TextVerifyOptions
second_title: Справочник по API GroupDocs.Signature для .NET
description: Сохраняет параметры для проверки текстовой подписи документа.
type: docs
weight: 1660
url: /ru/net/groupdocs.signature.options/textverifyoptions/
---
## TextVerifyOptions class

Сохраняет параметры для проверки текстовой подписи документа.

```csharp
public class TextVerifyOptions : VerifyOptions
```

## Конструкторы

| Имя | Описание |
| --- | --- |
| [TextVerifyOptions](textverifyoptions#constructor)() | Инициализирует новый экземпляр TextVerifyOptions со значениями по умолчанию. |
| [TextVerifyOptions](textverifyoptions#constructor_1)(string) | Инициализирует новый экземпляр TextVerifyOptions с проверочным текстом. |
| [TextVerifyOptions](textverifyoptions#constructor_2)(string, TextSignatureImplementation) | Инициализирует новый экземпляр TextVerifyOptions со свойством Text для проверки и реализации подписи. |

## Характеристики

| Имя | Описание |
| --- | --- |
| [AllPages](../../groupdocs.signature.options/verifyoptions/allpages) { get; set; } | Флаг для проверки каждой страницы документа. По умолчанию значение равно true. |
| [Extensions](../../groupdocs.signature.options/verifyoptions/extensions) { get; set; } | Дополнительные расширения для проверки альтернативных вариантов подписи. |
| [FormTextFieldTitle](../../groupdocs.signature.options/textverifyoptions/formtextfieldtitle) { get; set; } | Получает или задает заголовок поля формы для его проверки. Если это свойство устанавливает текст, он будет найден только в текстовых полях формы. |
| [FormTextFieldType](../../groupdocs.signature.options/textverifyoptions/formtextfieldtype) { get; set; } | Получает или задает тип поля формы для его проверки. Если это свойство устанавливает текст, он будет найден только в текстовых полях формы. |
| [IsValid](../../groupdocs.signature.options/verifyoptions/isvalid) { get; } | Флаг действительного свойства. |
| [MatchType](../../groupdocs.signature.options/textverifyoptions/matchtype) { get; set; } | Получает или задает проверку типа совпадения текста. |
| virtual [PageNumber](../../groupdocs.signature.options/verifyoptions/pagenumber) { get; set; } | Номер страницы документа для проверки. Если свойство не установлено, все страницы документа будут проверяться на первое вхождение. Минимальное значение 1. |
| virtual [PagesSetup](../../groupdocs.signature.options/verifyoptions/pagessetup) { get; set; } | Параметры страницы для указания проверяемых страниц. |
| [SignatureID](../../groupdocs.signature.options/textverifyoptions/signatureid) { get; set; } | Укажите идентификатор текстовой подписи больше нуля, если он должен быть проверен. Это свойство поддерживается только для документов Pdf |
| [SignatureImplementation](../../groupdocs.signature.options/textverifyoptions/signatureimplementation) { get; set; } | Тип подписи для проверки. |
| [Text](../../groupdocs.signature.options/textverifyoptions/text) { get; set; } | Укажите текст подписи, если он должен быть проверен. |

### Примечания

**Учить больше**

* Основное использование проверки электронной подписи штрих-кода с помощью GroupDocs.Signature: [ Как eVerification подписи штрих-кода в документе](https://docs.groupdocs.com/display/signaturenet/Verify+Text+signatures+in+the+document)
* Расширенное использование настроек проверки электронной подписи штрих-кода с помощью GroupDocs.Signature: [Расширенное использование подписей eVerification Barcode в документе и дополнительные настройки](https://docs.groupdocs.com/display/signaturenet/Verify+Text+signatures)

### Смотрите также

* class [VerifyOptions](../verifyoptions)
* пространство имен [GroupDocs.Signature.Options](../../groupdocs.signature.options)
* сборка [GroupDocs.Signature](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Signature.dll -->