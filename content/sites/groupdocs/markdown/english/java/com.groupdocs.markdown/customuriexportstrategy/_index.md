---
title: CustomUriExportStrategy
second_title: GroupDocs.Markdown for Java API Reference
description: Implements a URI export strategy that lets you customize how resource URIs are written to Markdown.
type: docs
weight: 12
url: /java/com.groupdocs.markdown/customuriexportstrategy/
---
**Inheritance:**
java.lang.Object

**All Implemented Interfaces:**
[com.groupdocs.markdown.IUriExportStrategy](../../com.groupdocs.markdown/iuriexportstrategy)
```
public class CustomUriExportStrategy implements IUriExportStrategy
```

Implements a URI export strategy that lets you customize how resource URIs are written to Markdown.


Supply an [IUriSavingHandler](../../com.groupdocs.markdown.uriexport/iurisavinghandler) implementation to rewrite resource URIs
(for example, to prepend a CDN base URL).

**Example:**

````

 IUriSavingHandler handler = new CdnUriHandler();

 ConvertOptions options = new ConvertOptions();
 options.setUriExportStrategy(new CustomUriExportStrategy(handler));

 String markdown = MarkdownConverter.toMarkdown("document.docx", options);
 
````


## Constructors

| Constructor | Description |
| --- | --- |
| [CustomUriExportStrategy(IUriSavingHandler handler)](#CustomUriExportStrategy-com.groupdocs.markdown.uriexport.IUriSavingHandler-) | Initializes a new instance of the  CustomUriExportStrategy  class.
 |
## Methods

| Method | Description |
| --- | --- |
| [updateResourceUri(UriExportContext context)](#updateResourceUri-com.groupdocs.markdown.UriExportContext-) |  |
### CustomUriExportStrategy(IUriSavingHandler handler) {#CustomUriExportStrategy-com.groupdocs.markdown.uriexport.IUriSavingHandler-}
```
public CustomUriExportStrategy(IUriSavingHandler handler)
```


Initializes a new instance of the  CustomUriExportStrategy  class.


**Parameters:**
| Parameter | Type | Description |
| --- | --- | --- |
| handler | [IUriSavingHandler](../../com.groupdocs.markdown.uriexport/iurisavinghandler) | the handler that is called for each resource URI during conversion
 |

### updateResourceUri(UriExportContext context) {#updateResourceUri-com.groupdocs.markdown.UriExportContext-}
```
public void updateResourceUri(UriExportContext context)
```


Called for each resource URI that will be written to the Markdown output. Modify properties on  context  to customize the resulting URI.


**Parameters:**
| Parameter | Type | Description |
| --- | --- | --- |
| context | [UriExportContext](../../com.groupdocs.markdown/uriexportcontext) |  |

