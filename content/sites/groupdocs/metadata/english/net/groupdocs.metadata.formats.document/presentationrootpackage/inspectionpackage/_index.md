---
title: InspectionPackage
second_title: GroupDocs.Metadata for .NET API Reference
description: Gets a metadata package containing inspection results for the document. The package contains information about document parts that can be considered as metadata in some cases.
type: docs
weight: 30
url: /net/groupdocs.metadata.formats.document/presentationrootpackage/inspectionpackage/
---
## PresentationRootPackage.InspectionPackage property

Gets a metadata package containing inspection results for the document. The package contains information about document parts that can be considered as metadata in some cases.

```csharp
public PresentationInspectionPackage InspectionPackage { get; }
```

### Property Value

A metadata package containing inspection results for the document.

### Remarks

**Learn more**

* [Working with metadata in Presentations](https://docs.groupdocs.com/display/metadatanet/Working+with+metadata+in+Presentations)

### Examples

This code sample demonstrates how to inspect a presentation.

```csharp
using (Metadata metadata = new Metadata(Constants.InputPpt))
{
     var root = metadata.GetRootPackage<PresentationRootPackage>();

     if (root.InspectionPackage.Comments != null)
     {
         foreach (var comment in root.InspectionPackage.Comments)
         {
             Console.WriteLine(comment.Author);
             Console.WriteLine(comment.Text);
             Console.WriteLine(comment.CreatedTime);
             Console.WriteLine(comment.SlideNumber);
         }
     }

     if (root.InspectionPackage.HiddenSlides != null)
     {
         foreach (var slide in root.InspectionPackage.HiddenSlides)
         {
             Console.WriteLine(slide.Name);
             Console.WriteLine(slide.Number);
             Console.WriteLine(slide.SlideId);
         }
     }
}
```

### See Also

* class [PresentationInspectionPackage](../../presentationinspectionpackage)
* class [PresentationRootPackage](../../presentationrootpackage)
* namespace [GroupDocs.Metadata.Formats.Document](../../presentationrootpackage)
* assembly [GroupDocs.Metadata](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.metadata.dll -->