---
title: License
second_title: Справочник по API GroupDocs.Metadata для .NET
description: Представляет лицензию GroupDocs.Metadata. Класс лицензии должен применяться один раз для каждого AppDomain.
type: docs
weight: 2650
url: /ru/net/groupdocs.metadata/license/
---
## License class

Представляет лицензию GroupDocs.Metadata. Класс лицензии должен применяться один раз для каждого AppDomain.

```csharp
public sealed class License
```

## Конструкторы

| Имя | Описание |
| --- | --- |
| [License](license)() | Инициализирует новый экземпляр[`License`](../license) класс. |

## Методы

| Имя | Описание |
| --- | --- |
| [SetLicense](../../groupdocs.metadata/license/setlicense#setlicense)(Stream) | Лицензирует компонент. |
| [SetLicense](../../groupdocs.metadata/license/setlicense#setlicense_1)(string) | Лицензирует компонент. |

### Примеры

В этом примере показано, как настроить лицензию.

```csharp
// инициализируем класс лицензии
License license = new License();

// устанавливаем путь к .lic файлу
license.SetLicense(@"C:\\GroupDocs.Metadata.lic");
```

### Смотрите также

* пространство имен [GroupDocs.Metadata](../../groupdocs.metadata)
* сборка [GroupDocs.Metadata](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Metadata.dll -->