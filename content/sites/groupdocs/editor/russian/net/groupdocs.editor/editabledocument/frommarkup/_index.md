---
title: FromMarkup
second_title: Справочник по API GroupDocs.Editor для .NET
description: Статическая фабрика которая создает экземпляр EditableDocument из указанной HTMLразметки и набора соответствующих связанных ресурсов
type: docs
weight: 20
url: /ru/net/groupdocs.editor/editabledocument/frommarkup/
---
## EditableDocument.FromMarkup method

Статическая фабрика, которая создает экземпляр EditableDocument из указанной HTML-разметки и набора соответствующих связанных ресурсов

```csharp
public static EditableDocument FromMarkup(string newHtmlContent, 
    IEnumerable<IHtmlResource> resources)
```

| Параметр | Тип | Описание |
| --- | --- | --- |
| newHtmlContent | String | Строка, содержащая необработанную HTML-разметку, которую необходимо проанализировать. Не может быть NULL, пустым или недействительным. |
| resources | IEnumerable`1 | Сбор всех ресурсов (изображений, таблиц стилей, шрифтов), которые используются в HTML-документе, указанном в*newHtmlContent* параметр. Может отсутствовать (NULL или пустая коллекция). |

### Возвращаемое значение

Новый ненулевой экземпляр EditableDocument

### Исключения

| исключение | условие |
| --- | --- |
| ArgumentException | Строка с входной необработанной HTML-разметкой не может быть нулевой или пустой |

### Смотрите также

* interface [IHtmlResource](../../../groupdocs.editor.htmlcss.resources/ihtmlresource)
* class [EditableDocument](../../editabledocument)
* пространство имен [GroupDocs.Editor](../../editabledocument)
* сборка [GroupDocs.Editor](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Editor.dll -->
