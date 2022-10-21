---
title: OleDiagramOptions
second_title: Справочник по API GroupDocs.Merge для .NET
description: Предоставляет параметры для импорта встроенного документа в Diagram через OLE.
type: docs
weight: 440
url: /ru/net/groupdocs.merger.domain.options/olediagramoptions/
---
## OleDiagramOptions class

Предоставляет параметры для импорта встроенного документа в Diagram через OLE.

```csharp
public class OleDiagramOptions : ImportDocumentOptions, IOleDiagramOptions
```

## Конструкторы

| Имя | Описание |
| --- | --- |
| [OleDiagramOptions](olediagramoptions#constructor_2)(string, int) | Инициализирует новый экземпляр[`OleDiagramOptions`](../olediagramoptions) класс. |
| [OleDiagramOptions](olediagramoptions#constructor_1)(string, byte[], int) | Инициализирует новый экземпляр[`OleDiagramOptions`](../olediagramoptions) класс. |
| [OleDiagramOptions](olediagramoptions#constructor)(byte[], byte[], string, int) | Инициализирует новый экземпляр[`OleDiagramOptions`](../olediagramoptions) класс. |

## Характеристики

| Имя | Описание |
| --- | --- |
| [Extension](../../groupdocs.merger.domain.options/importdocumentoptions/extension) { get; } | Расширение внедренного объекта. |
| [Height](../../groupdocs.merger.domain.options/olediagramoptions/height) { get; set; } | Высота формы внедренного объекта в дюймах. |
| [ImageData](../../groupdocs.merger.domain.options/olediagramoptions/imagedata) { get; } | Данные изображения внедренного объекта. |
| [ObjectData](../../groupdocs.merger.domain.options/importdocumentoptions/objectdata) { get; } | Данные внедренного объекта. |
| [PageNumber](../../groupdocs.merger.domain.options/importdocumentoptions/pagenumber) { get; } | Номер страницы для вставки встроенного объекта. |
| [Width](../../groupdocs.merger.domain.options/olediagramoptions/width) { get; set; } | Ширина формы внедренного объекта в дюймах. |
| [X](../../groupdocs.merger.domain.options/olediagramoptions/x) { get; set; } | Координата X булавки формы встроенного объекта (центр вращения) относительно страницы. |
| [Y](../../groupdocs.merger.domain.options/olediagramoptions/y) { get; set; } | Координата Y булавки формы внедренного объекта (центр вращения) относительно страницы. |

### Примечания

**Учить больше**

* Подробнее о добавлении документа в диаграмму через OLE: [Добавьте документ в диаграмму через OLE.](https://docs.groupdocs.com/merger/net/add-document-to-diagram-via-ole/)

### Смотрите также

* class [ImportDocumentOptions](../importdocumentoptions)
* interface [IOleDiagramOptions](../iolediagramoptions)
* пространство имен [GroupDocs.Merger.Domain.Options](../../groupdocs.merger.domain.options)
* сборка [GroupDocs.Merger](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Merger.dll -->