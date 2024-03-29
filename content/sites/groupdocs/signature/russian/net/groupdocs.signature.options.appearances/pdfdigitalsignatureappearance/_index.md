---
title: PdfDigitalSignatureAppearance
second_title: Справочник по API GroupDocs.Signature для .NET
description: Описывает внешний вид цифровой подписи в документах PDF.
type: docs
weight: 1210
url: /ru/net/groupdocs.signature.options.appearances/pdfdigitalsignatureappearance/
---
## PdfDigitalSignatureAppearance class

Описывает внешний вид цифровой подписи в документах PDF.

```csharp
public sealed class PdfDigitalSignatureAppearance : SignatureAppearance
```

## Конструкторы

| Имя | Описание |
| --- | --- |
| [PdfDigitalSignatureAppearance](pdfdigitalsignatureappearance)() | Создает объект внешнего вида подписи со значениями по умолчанию. |

## Характеристики

| Имя | Описание |
| --- | --- |
| [Background](../../groupdocs.signature.options.appearances/pdfdigitalsignatureappearance/background) { get; set; } | Получить или установить фоновый цвет подписи. По умолчанию значение равно SystemColors.Windows |
| [ContactInfoLabel](../../groupdocs.signature.options.appearances/pdfdigitalsignatureappearance/contactinfolabel) { get; set; } | Получает или задает метку контактной информации. Значение по умолчанию: "Контакт". если это значение пустое, то метка контакта не будет отображаться в области цифровой подписи. |
| [DateSignedAtLabel](../../groupdocs.signature.options.appearances/pdfdigitalsignatureappearance/datesignedatlabel) { get; set; } | Получает или задает метку с датой подписания. Значение по умолчанию: «Дата». |
| [DigitalSignedLabel](../../groupdocs.signature.options.appearances/pdfdigitalsignatureappearance/digitalsignedlabel) { get; set; } | Получает или задает метку с цифровой подписью. Значение по умолчанию: «С цифровой подписью». |
| [FontFamilyName](../../groupdocs.signature.options.appearances/pdfdigitalsignatureappearance/fontfamilyname) { get; set; } | Получает или задает имя семейства шрифтов для отображения меток. Значение по умолчанию — «Arial». |
| [FontSize](../../groupdocs.signature.options.appearances/pdfdigitalsignatureappearance/fontsize) { get; set; } | Получает или задает размер шрифта для отображения меток. Значение по умолчанию: 10. . |
| [Foreground](../../groupdocs.signature.options.appearances/pdfdigitalsignatureappearance/foreground) { get; set; } | Получить или установить цвет текста переднего плана для внешнего вида подписи. По умолчанию значение равно Color.FromArgb(76, 100, 255) |
| [LocationLabel](../../groupdocs.signature.options.appearances/pdfdigitalsignatureappearance/locationlabel) { get; set; } | Получает или задает метку местоположения. Значение по умолчанию: "Местоположение". если это значение пусто, то в области цифровой подписи не будет отображаться метка местоположения. |
| [ReasonLabel](../../groupdocs.signature.options.appearances/pdfdigitalsignatureappearance/reasonlabel) { get; set; } | Получает или задает метку причины. Значение по умолчанию: "Причина". если это значение пустое, то в области цифровой подписи не будет отображаться метка причины. |

### Примечания

**Узнать больше**

* Дополнительные простые примеры создания цифровых электронных подписей с помощью GroupDocs.Signature: [Расширенное подписание документа с помощью цифровых электронных подписей](https://docs.groupdocs.com/signature/net/sign-document-with-digital-signature-advanced/)
* См. дополнительные примеры настройки различных электронных подписей с помощью GroupDocs.Signature: [Расширенные свойства электронных подписей](https://docs.groupdocs.com/signature/net/sign-documents-with-extra-digital-signature-properties/)

### Смотрите также

* class [SignatureAppearance](../signatureappearance)
* пространство имен [GroupDocs.Signature.Options.Appearances](../../groupdocs.signature.options.appearances)
* сборка [GroupDocs.Signature](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Signature.dll -->
