---
title: IUriSavingHandler
second_title: GroupDocs.Markdown for Java API Reference
description: Callback interface invoked for each resource URI during conversion when using CustomUriExportStrategy.
type: docs
weight: 10
url: /java/com.groupdocs.markdown.uriexport/iurisavinghandler/
---```
public interface IUriSavingHandler
```

Callback interface invoked for each resource URI during conversion when using  CustomUriExportStrategy . Implement this interface to rewrite resource URIs in the Markdown output.

**Example:**

````

 public class CdnUriHandler implements IUriSavingHandler {
     @Override
     public void handle(UriSavingArgs args) {
         args.setResourceFileUri("https://cdn.example.com/" + args.getResourceFileName());
     }
 }
 
````


## Methods

| Method | Description |
| --- | --- |
| [handle(UriSavingArgs args)](#handle-com.groupdocs.markdown.UriSavingArgs-) | Called once for each resource URI that will be written to the Markdown output.
 |
### handle(UriSavingArgs args) {#handle-com.groupdocs.markdown.UriSavingArgs-}
```
public abstract void handle(UriSavingArgs args)
```


Called once for each resource URI that will be written to the Markdown output.


**Parameters:**
| Parameter | Type | Description |
| --- | --- | --- |
| args | [UriSavingArgs](../../com.groupdocs.markdown/urisavingargs) | Provides the default resource file name and URI, and allows you to override the URI via [UriSavingArgs.setResourceFileUri(String)](../../com.groupdocs.markdown/urisavingargs#setResourceFileUri-String-).
 |

