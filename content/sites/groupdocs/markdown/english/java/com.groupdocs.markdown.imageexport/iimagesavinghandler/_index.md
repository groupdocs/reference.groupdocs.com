---
title: IImageSavingHandler
second_title: GroupDocs.Markdown for Java API Reference
description: Callback interface invoked for each image encountered during conversion when using CustomImagesStrategy.
type: docs
weight: 10
url: /java/com.groupdocs.markdown.imageexport/iimagesavinghandler/
---```
public interface IImageSavingHandler
```

Callback interface invoked for each image encountered during conversion when using  CustomImagesStrategy .


Implement this interface to rename images, redirect output to a custom stream,
or apply other custom logic.

**Example:**

````

 public class RenameHandler implements IImageSavingHandler {
     private int index;

     @Override
     public void handle(CustomImageSavingArgs args) {
         args.setOutputImageFileName("img_" + index + "_" + args.getImageFileName());
         index++;
     }
 }
 
````


## Methods

| Method | Description |
| --- | --- |
| [handle(CustomImageSavingArgs args)](#handle-com.groupdocs.markdown.CustomImageSavingArgs-) | Called once for each image found in the source document during conversion.
 |
### handle(CustomImageSavingArgs args) {#handle-com.groupdocs.markdown.CustomImageSavingArgs-}
```
public abstract void handle(CustomImageSavingArgs args)
```


Called once for each image found in the source document during conversion.


**Parameters:**
| Parameter | Type | Description |
| --- | --- | --- |
| args | [CustomImageSavingArgs](../../com.groupdocs.markdown/customimagesavingargs) | Provides the default image file name and allows you to override the file name via [CustomImageSavingArgs.setOutputImageFileName(String)](../../com.groupdocs.markdown/customimagesavingargs#setOutputImageFileName-String-) or redirect the output via [CustomImageSavingArgs.setOutputStream(java.io.OutputStream)](../../com.groupdocs.markdown/customimagesavingargs#setOutputStream-java.io.OutputStream-).
 |

