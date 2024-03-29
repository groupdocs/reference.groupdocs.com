---
title: IndexRepository
second_title: GroupDocs.Search для справочника API .NET
description: Представляет собой контейнер для объединения нескольких индексов и выполнения над ними общих операций.
type: docs
weight: 690
url: /ru/net/groupdocs.search/indexrepository/
---
## IndexRepository class

Представляет собой контейнер для объединения нескольких индексов и выполнения над ними общих операций.

```csharp
public class IndexRepository : IDisposable
```

## Конструкторы

| Имя | Описание |
| --- | --- |
| [IndexRepository](indexrepository)() | Инициализирует новый экземпляр[`IndexRepository`](../indexrepository) класс. |

## Характеристики

| Имя | Описание |
| --- | --- |
| [Events](../../groupdocs.search/indexrepository/events) { get; } | Получает концентратор событий для подписки на события. |
| [Indexes](../../groupdocs.search/indexrepository/indexes) { get; } | Получает индексы, содержащиеся в этом[`IndexRepository`](../indexrepository) . |

## Методы

| Имя | Описание |
| --- | --- |
| [AddToRepository](../../groupdocs.search/indexrepository/addtorepository#addtorepository)(Index) | Добавляет индекс в репозиторий индексов. |
| [AddToRepository](../../groupdocs.search/indexrepository/addtorepository#addtorepository_1)(string) | Открывает и добавляет индекс в репозиторий индексов. |
| [Create](../../groupdocs.search/indexrepository/create#create)() | Создает новый индекс в памяти. |
| [Create](../../groupdocs.search/indexrepository/create#create_1)(IndexSettings) | Создает новый индекс в памяти. |
| [Create](../../groupdocs.search/indexrepository/create#create_2)(string) | Создает новый индекс на диске. Папка индекса будет очищена перед созданием индекса. |
| [Create](../../groupdocs.search/indexrepository/create#create_3)(string, IndexSettings) | Создает новый индекс на диске. Папка индекса будет очищена перед созданием индекса. |
| [Dispose](../../groupdocs.search/indexrepository/dispose)() | Освобождает все ресурсы, используемые[`IndexRepository`](../indexrepository) . |
| [Search](../../groupdocs.search/indexrepository/search#search)(SearchQuery) | Поиск по всем индексам репозитория. |
| [Search](../../groupdocs.search/indexrepository/search#search_2)(string) | Поиск по всем индексам репозитория. |
| [Search](../../groupdocs.search/indexrepository/search#search_1)(SearchQuery, SearchOptions) | Поиск по всем индексам репозитория. |
| [Search](../../groupdocs.search/indexrepository/search#search_3)(string, SearchOptions) | Поиск по всем индексам репозитория. |
| [Update](../../groupdocs.search/indexrepository/update#update)() | Обновляет все индексы в репозитории. |
| [Update](../../groupdocs.search/indexrepository/update#update_1)(UpdateOptions) | Обновляет все индексы в репозитории. |

### Примечания

**Узнать больше**

* [Репозиторий поискового индекса](https://docs.groupdocs.com/display/searchnet/Search+index+repository)

### Примеры

Пример демонстрирует типичное использование класса.

```csharp
string indexFolder1 = @"c:\MyIndex\";
string indexFolder2 = @"c:\MyIndex\";
string query = "Einstein";

IndexRepository repository = new IndexRepository();
repository.AddToRepository(indexFolder1); // Загрузка существующего индекса
repository.AddToRepository(indexFolder2); // Загрузка другого существующего индекса

SearchResult result = repository.Search(query); // Поиск по индексам репозитория
```

### Смотрите также

* пространство имен [GroupDocs.Search](../../groupdocs.search)
* сборка [GroupDocs.Search](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Search.dll -->
