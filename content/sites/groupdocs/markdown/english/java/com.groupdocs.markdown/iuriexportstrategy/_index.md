---
title: IUriExportStrategy
second_title: GroupDocs.Markdown for Java API Reference
description: Defines a strategy for customizing resource URIs that are written into the Markdown output during conversion.
type: docs
weight: 33
url: /java/com.groupdocs.markdown/iuriexportstrategy/
---```
public interface IUriExportStrategy
```

Defines a strategy for customizing resource URIs that are written into the Markdown output during conversion.


Implement this interface to rewrite or transform the URIs that reference images or other external
resources in the generated Markdown. For example, you can prepend a CDN base URL or change
relative paths to absolute URLs.

**Example:**

````

 public class CdnUriExportStrategy implements IUriExportStrategy {
     @Override
     public void updateResourceUri(UriExportContext context) {
         context.setResourceFileUri(
             "https://cdn.example.com/assets/" + context.getResourceFileName()
         );
     }
 }
 
````


## Methods

| Method | Description |
| --- | --- |
| [updateResourceUri(UriExportContext context)](#updateResourceUri-com.groupdocs.markdown.UriExportContext-) | Called for each resource URI that will be written to the Markdown output.
 |
### updateResourceUri(UriExportContext context) {#updateResourceUri-com.groupdocs.markdown.UriExportContext-}
```
public abstract void updateResourceUri(UriExportContext context)
```


Called for each resource URI that will be written to the Markdown output. Modify properties on  context  to customize the resulting URI.


**Parameters:**
| Parameter | Type | Description |
| --- | --- | --- |
| context | [UriExportContext](../../com.groupdocs.markdown/uriexportcontext) | The URI export context. Set  resourceFileUri  to override the URI that appears in the Markdown output, or modify  resourceFileName  to change the resource file name.
 |

