---
title: GetBodyContent
second_title: GroupDocs.Editor for .NET API Reference
description: Returns a body of the HTML document content between opening and closing BODY tags without these tags as a string.
type: docs
weight: 120
url: /net/groupdocs.editor/editabledocument/getbodycontent/
---
## GetBodyContent() {#getbodycontent}

Returns a body of the HTML document (content between opening and closing BODY tags without these tags) as a string.

```csharp
public string GetBodyContent()
```

### Return Value

String, which contains the body of the HTML document

### Remarks

WYSIWYG editors operate with the body of the document and cannot correctly process its meta information from the HEAD block. This method is designed for such cases. This overload doesn't allow to adjust URIs for external resource requests.

### See Also

* class [EditableDocument](../../editabledocument)
* namespace [GroupDocs.Editor](../../editabledocument)
* assembly [GroupDocs.Editor](../../../)

---

## GetBodyContent(string) {#getbodycontent_1}

Returns a body of the HTML document (content between opening and closing BODY tags without these tags) as a string, where links to the external resources contain specified prefix.

```csharp
public string GetBodyContent(string externalImagesPrefix)
```

| Parameter | Type | Description |
| --- | --- | --- |
| externalImagesPrefix | String | Through this parameter used can specify a prefix, which will be added to the links to all external images in IMG elements, which will be present in the resultant HTML string. If NULL or empty, prefixes will not be added. |

### Return Value

String, which contains the body of the HTML document with links, adjusted to the external images

### Remarks

WYSIWYG editors operate with the body of the document and cannot correctly process its meta information from the HEAD block. This method is designed for such cases. This overload allows to adjust URIs for external resource requests.

### See Also

* class [EditableDocument](../../editabledocument)
* namespace [GroupDocs.Editor](../../editabledocument)
* assembly [GroupDocs.Editor](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Editor.dll -->