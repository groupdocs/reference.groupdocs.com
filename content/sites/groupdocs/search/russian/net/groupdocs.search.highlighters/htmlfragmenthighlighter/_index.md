---
title: HtmlFragmentHighlighter
second_title: GroupDocs.Search для справочника API .NET
description: Представляет средство выделения результатов поиска которое выделяет результаты поиска во фрагментах текста в формате HTML.
type: docs
weight: 630
url: /ru/net/groupdocs.search.highlighters/htmlfragmenthighlighter/
---
## HtmlFragmentHighlighter class

Представляет средство выделения результатов поиска, которое выделяет результаты поиска во фрагментах текста в формате HTML.

```csharp
public class HtmlFragmentHighlighter : Highlighter
```

## Конструкторы

| Имя | Описание |
| --- | --- |
| [HtmlFragmentHighlighter](htmlfragmenthighlighter)() | Инициализирует новый экземпляр[`HtmlFragmentHighlighter`](../htmlfragmenthighlighter) класс. |

## Методы

| Имя | Описание |
| --- | --- |
| [GetResult](../../groupdocs.search.highlighters/htmlfragmenthighlighter/getresult)() | Получает массив результирующих контейнеров фрагментов. |

### Примечания

**Учить больше**

* [Выделение результатов поиска](https://docs.groupdocs.com/display/searchnet/Highlighting+search+results)

### Примеры

Пример демонстрирует типичное использование класса.

```csharp
string indexFolder = @"c:\MyIndex\";
string documentsFolder = @"c:\MyDocuments\";

// Создание индекса
Index index = new Index(indexFolder);

// Индексация документов из указанной папки
index.Add(documentsFolder);

// Поиск слова «Эйнштейн»
SearchResult result = index.Search("Einstein");

// Назначение параметров выделения
HighlightOptions options = new HighlightOptions();
options.TermsBefore = 5;
options.TermsAfter = 5;
options.TermsTotal = 15;

// Подсветка найденных слов в тексте документа
FoundDocument document = result.GetFoundDocument(0);
HtmlFragmentHighlighter highlighter = new HtmlFragmentHighlighter();
index.Highlight(document, highlighter, options);

// Получение результата
FragmentContainer[] fragmentContainers = highlighter.GetResult();
for (int i = 0; i < fragmentContainers.Length; i++)
{
    FragmentContainer container = fragmentContainers[i];
    string[] fragments = container.GetFragments();
    if (fragments.Length > 0)
    {
        Console.WriteLine(container.FieldName);
        Console.WriteLine();
        for (int j = 0; j < fragments.Length; j++)
        {
            // Вывод HTML-разметки на консоль
            Console.WriteLine(fragments[j]);
            Console.WriteLine();
        }
    }
}
```

### Смотрите также

* class [Highlighter](../highlighter)
* пространство имен [GroupDocs.Search.Highlighters](../../groupdocs.search.highlighters)
* сборка [GroupDocs.Search](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Search.dll -->