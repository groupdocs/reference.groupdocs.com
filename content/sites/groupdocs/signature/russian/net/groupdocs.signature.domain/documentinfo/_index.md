---
title: DocumentInfo
second_title: Справочник по API GroupDocs.Signature для .NET
description: Определяет свойства описания документа.
type: docs
weight: 150
url: /ru/net/groupdocs.signature.domain/documentinfo/
---
## DocumentInfo class

Определяет свойства описания документа.

```csharp
public class DocumentInfo : IDocumentInfo
```

## Конструкторы

| Имя | Описание |
| --- | --- |
| [DocumentInfo](documentinfo)() | Инициализирует новый экземпляр[`DocumentInfo`](../documentinfo) класс. |

## Характеристики

| Имя | Описание |
| --- | --- |
| [BarcodeSignatures](../../groupdocs.signature.domain/documentinfo/barcodesignatures) { get; } | Коллекция подписей штрихкодов документов, добавленная или обновленная[`Signature`](../../groupdocs.signature/signature) методы. |
| [DigitalSignatures](../../groupdocs.signature.domain/documentinfo/digitalsignatures) { get; } | Коллекция цифровых подписей документов, добавленная или обновленная[`Signature`](../../groupdocs.signature/signature) методы. |
| [FileType](../../groupdocs.signature.domain/documentinfo/filetype) { get; set; } | Тип формата файла. |
| [FormFields](../../groupdocs.signature.domain/documentinfo/formfields) { get; } | Коллекция всех существующих поддерживаемых полей формы в документе. Это свойство поддерживается только для типов документов Pdf и Word Processing. |
| [FormFieldSignatures](../../groupdocs.signature.domain/documentinfo/formfieldsignatures) { get; } | Коллекция подписей полей формы документа, добавленных или обновленных[`Signature`](../../groupdocs.signature/signature) методы. |
| [ImageSignatures](../../groupdocs.signature.domain/documentinfo/imagesignatures) { get; } | Коллекция подписей изображений документов, добавленных или обновленных[`Signature`](../../groupdocs.signature/signature) методы. |
| [MaxPageHeight](../../groupdocs.signature.domain/documentinfo/maxpageheight) { get; set; } | Определяет максимальную высоту страницы. |
| [PageCount](../../groupdocs.signature.domain/documentinfo/pagecount) { get; set; } | Количество страниц документа. |
| [Pages](../../groupdocs.signature.domain/documentinfo/pages) { get; set; } | Коллекция описаний страниц документа. |
| [ProcessLogs](../../groupdocs.signature.domain/documentinfo/processlogs) { get; } | Коллекция процессов истории документа, таких как Sign, Update, Delete. |
| [QrCodeSignatures](../../groupdocs.signature.domain/documentinfo/qrcodesignatures) { get; } | Коллекция подписей QR-кода документа, добавленная или обновленная[`Signature`](../../groupdocs.signature/signature) методы. |
| [Signatures](../../groupdocs.signature.domain/documentinfo/signatures) { get; } | Сбор подписей всех типов документов[`BaseSignature`](../basesignature) . |
| [Size](../../groupdocs.signature.domain/documentinfo/size) { get; set; } | Размер документа в байтах. |
| [TextSignatures](../../groupdocs.signature.domain/documentinfo/textsignatures) { get; } | Сбор подписей текста документа. |
| [WidthForMaxHeight](../../groupdocs.signature.domain/documentinfo/widthformaxheight) { get; set; } | Указывает ширину для максимальной высоты страницы. |

### Смотрите также

* interface [IDocumentInfo](../idocumentinfo)
* пространство имен [GroupDocs.Signature.Domain](../../groupdocs.signature.domain)
* сборка [GroupDocs.Signature](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Signature.dll -->