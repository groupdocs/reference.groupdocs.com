---
title: MemoryCache
second_title: Справочник по API GroupDocs.Conversion для .NET
description: Кэширование памяти. Означает что кеш хранится в memory
type: docs
weight: 30
url: /ru/net/groupdocs.conversion.caching/memorycache/
---
## MemoryCache class

Кэширование памяти. Означает, что кеш хранится в memory

```csharp
public sealed class MemoryCache : ICache
```

## Конструкторы

| Имя | Описание |
| --- | --- |
| [MemoryCache](memorycache)() | Создает новый экземпляр MemoryCache class |

## Методы

| Имя | Описание |
| --- | --- |
| [GetKeys](../../groupdocs.conversion.caching/memorycache/getkeys)(string) | Возвращает все ключи, соответствующие фильтру. |
| [Set](../../groupdocs.conversion.caching/memorycache/set)(string, object) | Вставляет запись в кэш. |
| [TryGetValue](../../groupdocs.conversion.caching/memorycache/trygetvalue)(string, out object) | Получает запись, связанную с этим ключом, если он присутствует. |

### Примечания

**Узнать больше**

* Подробнее о кэшировании и оптимизации производительности процесса преобразования: [Кэширование результатов конвертации](https://docs.groupdocs.com/display/conversionnet/Caching)

### Смотрите также

* interface [ICache](../icache)
* пространство имен [GroupDocs.Conversion.Caching](../../groupdocs.conversion.caching)
* сборка [GroupDocs.Conversion](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Conversion.dll -->
