---
title: GetData
second_title: Справочник по API GroupDocs.Signature для .NET
description: Получить объект из значения подписи метаданных через десериализацию.
type: docs
weight: 70
url: /ru/net/groupdocs.signature.domain/metadatasignature/getdata/
---
## GetData&lt;T&gt;() {#getdata}

Получить объект из значения подписи метаданных через десериализацию.

```csharp
public T GetData<T>()
    where T : class
```

| Параметр | Описание |
| --- | --- |
| T | Тип объекта для десериализации из значения метаданных |

### Возвращаемое значение

Экземпляр объекта T

### Смотрите также

* class [MetadataSignature](../../metadatasignature)
* пространство имен [GroupDocs.Signature.Domain](../../metadatasignature)
* сборка [GroupDocs.Signature](../../../)

---

## GetData&lt;T&gt;(IDataEncryption) {#getdata_1}

Получить объект из текста подписи метаданных через десериализацию.

```csharp
public T GetData<T>(IDataEncryption dataEncryption)
    where T : class
```

| Параметр | Описание |
| --- | --- |
| T | Тип объекта для десериализации из значения метаданных |
| dataEncryption | Установить пользовательскую реализацию шифрования данных |

### Смотрите также

* interface [IDataEncryption](../../../groupdocs.signature.domain.extensions/idataencryption)
* class [MetadataSignature](../../metadatasignature)
* пространство имен [GroupDocs.Signature.Domain](../../metadatasignature)
* сборка [GroupDocs.Signature](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Signature.dll -->
