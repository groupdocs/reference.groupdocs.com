---
title: Save
second_title: GroupDocs.Redaction for .NET API Reference
description: Saves the document to a file with the following options AddSuffix  true RasterizeToPDF  true.
type: docs
weight: 60
url: /net/groupdocs.redaction/redactor/save/
---
## Save() {#save}

Saves the document to a file with the following options: AddSuffix = true, RasterizeToPDF = true.

```csharp
public string Save()
```

### Return Value

Path to redacted document

### See Also

* class [Redactor](../../redactor)
* namespace [GroupDocs.Redaction](../../../groupdocs.redaction)
* assembly [GroupDocs.Redaction](../../../)

---

## Save(SaveOptions) {#save_1}

Saves the document to a file.

```csharp
public string Save(SaveOptions saveOptions)
```

| Parameter | Type | Description |
| --- | --- | --- |
| saveOptions | SaveOptions | Options to add suffix or rasterize |

### Return Value

Path to redacted document

### Examples

The following example demonstrates how to save a document using SaveOptions.

```csharp
    using (Redactor redactor = new Redactor(@"C:\sample.pdf"))
    {
       // Document redaction goes here
       // ...
    
       // Save the document with default options (convert pages into images, save as PDF)
       redactor.Save();
    
       // Save the document in original format overwriting original file
       redactor.Save(new SaveOptions() { AddSuffix = false, RasterizeToPDF = false });
    
       // Save the document to "*_Redacted.*" file in original format
       redactor.Save(new SaveOptions() { AddSuffix = true, RasterizeToPDF = false });
    
       // Save the document to "*_AnyText.*" (e.g. timestamp instead of "AnyText") in its file name without rasterization
       redactor.Save(new SaveOptions(false, "AnyText"));
    }    
```

### See Also

* class [SaveOptions](../../../groupdocs.redaction.options/saveoptions)
* class [Redactor](../../redactor)
* namespace [GroupDocs.Redaction](../../../groupdocs.redaction)
* assembly [GroupDocs.Redaction](../../../)

---

## Save(Stream, RasterizationOptions) {#save_2}

Saves the document to a stream, including custom location.

```csharp
public void Save(Stream document, RasterizationOptions rasterizationOptions)
```

| Parameter | Type | Description |
| --- | --- | --- |
| document | Stream | Target stream |
| rasterizationOptions | RasterizationOptions | Options to rasterize or not and to specify pages for rasterization |

### Examples

The following example demonstrates how to set options for the rasterization process.

```csharp
    using (var redactor = new Redactor("SomePresentation.pptx"))
    {
        // redact sensitive data on the first slide 
    
        var rasterizationOptions = new RasterizationOptions();
        rasterizationOptions.PageIndex = 0;
        rasterizationOptions.PageCount = 1;
        rasterizationOptions.Compliance = PdfComplianceLevel.PdfA1a;
        using (var stream = File.Open(Path.Combine(@"C:\Temp", "PresentationFirstSlide.pdf")))
        {
            redactor.Save(stream, rasterizationOptions);
        }
    }      
```

### See Also

* class [RasterizationOptions](../../../groupdocs.redaction.options/rasterizationoptions)
* class [Redactor](../../redactor)
* namespace [GroupDocs.Redaction](../../../groupdocs.redaction)
* assembly [GroupDocs.Redaction](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.redaction.dll -->
