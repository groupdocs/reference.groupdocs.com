---
title: SignatureSettings
second_title: Справочник по API GroupDocs.Signature для .NET
description: Определяет параметры для настройкиSignature./signature поведение.
type: docs
weight: 1890
url: /ru/net/groupdocs.signature/signaturesettings/
---
## SignatureSettings class

Определяет параметры для настройки[`Signature`](../signature) поведение.

```csharp
public class SignatureSettings
```

## Конструкторы

| Имя | Описание |
| --- | --- |
| [SignatureSettings](signaturesettings#constructor)() | Создает экземпляр SignatureSettings по умолчанию со значениями по умолчанию. |
| [SignatureSettings](signaturesettings#constructor_1)(ILogger) | Создает экземпляр SignatureSettings по умолчанию с реализацией Logger. |

## Характеристики

| Имя | Описание |
| --- | --- |
| [DefaultCulture](../../groupdocs.signature/signaturesettings/defaultculture) { get; set; } | Получает или задает язык и региональные параметры по умолчанию, которые будут использоваться при обработке документа. Значение по умолчанию — "en-US". |
| [IncludeStandardMetadataSignatures](../../groupdocs.signature/signaturesettings/includestandardmetadatasignatures) { get; set; } | Получает или устанавливает флаг для включения в список метаданных встроенных стандартных подписей метаданных документа, таких как автор, владелец, дата создания документа, дата изменения и т. д. Если для этого флага установлено значение false (по умолчанию), GetDocumentInfo не будет включать эти метаданные подписи. Если для этого флага установлено значение true, информация о документе будет включать эти стандартные подписи метаданных. |
| [Logger](../../groupdocs.signature/signaturesettings/logger) { get; } | Реализация регистратора, используемая для ведения журнала (ошибки, предупреждения, трассировки).[`ILogger`](../../groupdocs.signature.logging/ilogger) . |
| [LogLevel](../../groupdocs.signature/signaturesettings/loglevel) { get; set; } | Уровень логирования для ограничения сообщений (Все, Трассировки, Предупреждения, Ошибки).[`LogLevel`](./loglevel) . ПО умолчанию установлен тип All level. |
| [SaveDocumentOnEmptyDelete](../../groupdocs.signature/signaturesettings/savedocumentonemptydelete) { get; set; } | Получает или устанавливает флаг для повторного сохранения исходного документа, когда метод Delete не имеет затронутых подписей для удаления. У метода удаления нет подписей для удаления. Если для этой квартиры установлено значение false, исходный документ вообще не будет изменен. |
| [SaveDocumentOnEmptyUpdate](../../groupdocs.signature/signaturesettings/savedocumentonemptyupdate) { get; set; } | Получает или устанавливает флаг для повторного сохранения исходного документа, когда метод обновления не имеет сигнатур для обновления. у метода нет сигнатур для обновления. Если для этой квартиры задано значение false, исходный документ вообще не будет изменен. |
| [ShowDeletedSignaturesInfo](../../groupdocs.signature/signaturesettings/showdeletedsignaturesinfo) { get; set; } | Получает или устанавливает флаг, который включает удаленные подписи в результат сведений о документе. Каждая подпись[`BaseSignature`](../../groupdocs.signature.domain/basesignature) имеет удаленный флаг[`Deleted`](../../groupdocs.signature.domain/basesignature/deleted) чтобы определить, был ли он удален. |

### Смотрите также

* пространство имен [GroupDocs.Signature](../../groupdocs.signature)
* сборка [GroupDocs.Signature](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Signature.dll -->
