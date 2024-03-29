---
title: DigitalVerifyOptions
second_title: Справочник по API GroupDocs.Signature для .NET
description: Сохраняет параметры для проверки цифровой подписи документа.
type: docs
weight: 1350
url: /ru/net/groupdocs.signature.options/digitalverifyoptions/
---
## DigitalVerifyOptions class

Сохраняет параметры для проверки цифровой подписи документа.

```csharp
public class DigitalVerifyOptions : VerifyOptions
```

## Конструкторы

| Имя | Описание |
| --- | --- |
| [DigitalVerifyOptions](digitalverifyoptions#constructor)() | Создает вариант цифровой проверки со значениями по умолчанию. |
| [DigitalVerifyOptions](digitalverifyoptions#constructor_1)(Stream) | Создает вариант цифровой проверки с заданным потоком сертификата. |
| [DigitalVerifyOptions](digitalverifyoptions#constructor_2)(string) | Создает опцию цифровой проверки с заданным путем к файлу цифрового сертификата. |

## Характеристики

| Имя | Описание |
| --- | --- |
| [AllPages](../../groupdocs.signature.options/verifyoptions/allpages) { get; set; } | Флаг для проверки каждой страницы документа. По умолчанию значение равно true. |
| [Certificate](../../groupdocs.signature.options/digitalverifyoptions/certificate) { get; } | Получить сертификат X509Certificate2 из сертификата FilePath или Stream. |
| [CertificateFilePath](../../groupdocs.signature.options/digitalverifyoptions/certificatefilepath) { get; set; } | Путь к файлу цифрового сертификата. |
| [CertificateStream](../../groupdocs.signature.options/digitalverifyoptions/certificatestream) { get; set; } | Поток цифрового сертификата. |
| [Comments](../../groupdocs.signature.options/digitalverifyoptions/comments) { get; set; } | Комментарии цифровой подписи для проверки. |
| [Contact](../../groupdocs.signature.options/digitalverifyoptions/contact) { get; set; } | Подпись Контакт для подтверждения. |
| [Extensions](../../groupdocs.signature.options/verifyoptions/extensions) { get; set; } | Дополнительные расширения для проверки альтернативных вариантов подписи. |
| [IssuerName](../../groupdocs.signature.options/digitalverifyoptions/issuername) { get; set; } | Имя издателя сертификата для проверки. Значение чувствительно к регистру. Если это свойство установлено, проверка проверит, содержит ли имя издателя подписи переданное значение или равно ему |
| [IsValid](../../groupdocs.signature.options/verifyoptions/isvalid) { get; } | Флаг действительного свойства. |
| [Location](../../groupdocs.signature.options/digitalverifyoptions/location) { get; set; } | Местоположение подписи для проверки. |
| virtual [PageNumber](../../groupdocs.signature.options/verifyoptions/pagenumber) { get; set; } | Номер страницы документа для проверки. Если свойство не установлено, все страницы документа будут проверяться на первое вхождение. Минимальное значение 1. |
| virtual [PagesSetup](../../groupdocs.signature.options/verifyoptions/pagessetup) { get; set; } | Параметры страницы для указания проверяемых страниц. |
| [Password](../../groupdocs.signature.options/digitalverifyoptions/password) { get; set; } | Пароль цифрового сертификата, если требуется. |
| [Reason](../../groupdocs.signature.options/digitalverifyoptions/reason) { get; set; } | Причина проверки цифровой подписи. |
| [SignDateTimeFrom](../../groupdocs.signature.options/digitalverifyoptions/signdatetimefrom) { get; set; } | Дата и диапазон времени проверки цифровой подписи. Значение, допускающее значение NULL, будет проигнорировано. |
| [SignDateTimeTo](../../groupdocs.signature.options/digitalverifyoptions/signdatetimeto) { get; set; } | Дата и диапазон времени проверки цифровой подписи. Значение, допускающее значение NULL, будет проигнорировано. |
| [SubjectName](../../groupdocs.signature.options/digitalverifyoptions/subjectname) { get; set; } | Отличительное имя субъекта сертификата для проверки. Значение чувствительно к регистру. Если это свойство установлено, проверка проверит, содержит ли имя субъекта подписи переданное значение или равно ему |

### Примечания

**Узнать больше**

* Базовое использование проверки ЭЦП с помощью GroupDocs.Signature: [ Электронная проверка цифровой подписи в документе](https://docs.groupdocs.com/display/signaturenet/Verify+Digital+signatures+in+the+document)
* Расширенное использование настроек проверки ЭЦП с GroupDocs.Signature: [Расширенное использование цифровых подписей eVerification в документе и дополнительные настройки]()

### Смотрите также

* class [VerifyOptions](../verifyoptions)
* пространство имен [GroupDocs.Signature.Options](../../groupdocs.signature.options)
* сборка [GroupDocs.Signature](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Signature.dll -->
