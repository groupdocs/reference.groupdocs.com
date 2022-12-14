---
title: SetLicense
second_title: Справочник по API GroupDocs.Metadata для .NET
description: Лицензирует компонент.
type: docs
weight: 20
url: /ru/net/groupdocs.metadata/license/setlicense/
---
## SetLicense(string) {#setlicense_1}

Лицензирует компонент.

```csharp
public void SetLicense(string filePath)
```

| Параметр | Тип | Описание |
| --- | --- | --- |
| filePath | String | Абсолютный путь к файлу лицензии. |

### Примеры

В этом примере показано, как настроить лицензию.

```csharp
// инициализируем класс лицензии
License license = new License();

// устанавливаем путь к .lic файлу
license.SetLicense(@"C:\\GroupDocs.Metadata.lic");    
```

### Смотрите также

* class [License](../../license)
* пространство имен [GroupDocs.Metadata](../../license)
* сборка [GroupDocs.Metadata](../../../)

---

## SetLicense(Stream) {#setlicense}

Лицензирует компонент.

```csharp
public void SetLicense(Stream stream)
```

| Параметр | Тип | Описание |
| --- | --- | --- |
| stream | Stream | Лицензионный поток. |

### Смотрите также

* class [License](../../license)
* пространство имен [GroupDocs.Metadata](../../license)
* сборка [GroupDocs.Metadata](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Metadata.dll -->
