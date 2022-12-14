---
title: Annotator
second_title: GroupDocs.Annotation for .NET API Reference
description: Represents main class that controls document annotating process.
type: docs
weight: 10
url: /net/groupdocs.annotation/annotator/
---
## Annotator class

Represents main class that controls document annotating process.

```csharp
public class Annotator : IDisposable
```

## Constructors

| Name | Description |
| --- | --- |
| [Annotator](annotator#constructor)(Stream) | Initialise annotator class which accept document stream |
| [Annotator](annotator#constructor_4)(string) | Initialise annotator class which accept document path |
| [Annotator](annotator#constructor_1)(Stream, AnnotatorSettings) | Initialise annotator class which accept document stream |
| [Annotator](annotator#constructor_2)(Stream, LoadOptions) | Initialise annotator class which accept document stream |
| [Annotator](annotator#constructor_5)(string, AnnotatorSettings) | Initialise annotator class which accept document path |
| [Annotator](annotator#constructor_6)(string, LoadOptions) | Initialise annotator class which accept document path |
| [Annotator](annotator#constructor_3)(Stream, LoadOptions, AnnotatorSettings) | Initialise annotator class which accept document stream |
| [Annotator](annotator#constructor_7)(string, LoadOptions, AnnotatorSettings) | Initialise annotator class which accept document path |

## Properties

| Name | Description |
| --- | --- |
| [Document](../../groupdocs.annotation/annotator/document) { get; } | Document |
| [ProcessPages](../../groupdocs.annotation/annotator/processpages) { get; set; } | Document pages |
| [Rotation](../../groupdocs.annotation/annotator/rotation) { get; set; } | Document Rotation |

## Methods

| Name | Description |
| --- | --- |
| [Add](../../groupdocs.annotation/annotator/add#add)(AnnotationBase) | Adds annotation to document |
| [Add](../../groupdocs.annotation/annotator/add#add_1)(List&lt;AnnotationBase&gt;) | Adds collection of annotations to a document. |
| [Dispose](../../groupdocs.annotation/annotator/dispose)() | Dispose |
| [ExportAnnotationsFromXMLFile](../../groupdocs.annotation/annotator/exportannotationsfromxmlfile)(string) | Export annotations from XML file. |
| [Get](../../groupdocs.annotation/annotator/get#get)() | Gets collections of document annotations. |
| [Get](../../groupdocs.annotation/annotator/get#get_1)(AnnotationType) | Gets collection of document annotations by annotation type. |
| [GetVersion](../../groupdocs.annotation/annotator/getversion)(object) | Get annotations from versions. |
| [GetVersionsList](../../groupdocs.annotation/annotator/getversionslist)() | Get versions. |
| [ImportAnnotationsFromDocument](../../groupdocs.annotation/annotator/importannotationsfromdocument)(string) | Import annotations from document to XML file. |
| [Remove](../../groupdocs.annotation/annotator/remove#remove)(AnnotationBase) | Removes annotation from document. |
| [Remove](../../groupdocs.annotation/annotator/remove#remove_1)(int) | Removes annotation from document by Id. |
| [Remove](../../groupdocs.annotation/annotator/remove#remove_2)(List&lt;AnnotationBase&gt;) | Removes collection of annotations from document. |
| [Remove](../../groupdocs.annotation/annotator/remove#remove_3)(List&lt;int&gt;) | Removes collection of annotations from document by provided annotation ids. |
| [Save](../../groupdocs.annotation/annotator/save#save)() | Saves document after adding, updating or removing annotations. |
| [Save](../../groupdocs.annotation/annotator/save#save_1)(SaveOptions) | Saves document after adding, updating or removing annotations. |
| [Save](../../groupdocs.annotation/annotator/save#save_2)(Stream) | Saves document after adding, updating or removing annotations. |
| [Save](../../groupdocs.annotation/annotator/save#save_4)(string) | Saves document after adding, updating or removing annotations. |
| [Save](../../groupdocs.annotation/annotator/save#save_3)(Stream, SaveOptions) | Saves document after adding, updating or removing annotations. |
| [Save](../../groupdocs.annotation/annotator/save#save_5)(string, SaveOptions) | Saves document after adding, updating or removing annotations. |
| [Update](../../groupdocs.annotation/annotator/update#update)(AnnotationBase) | Updates document annotation. |
| [Update](../../groupdocs.annotation/annotator/update#update_1)(List&lt;AnnotationBase&gt;) | Updates collection of document annotations. |

### See Also

* namespace [GroupDocs.Annotation](../../groupdocs.annotation)
* assembly [GroupDocs.Annotation](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Annotation.dll -->
