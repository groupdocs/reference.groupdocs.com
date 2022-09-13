---
title: Save
second_title: GroupDocs.Metadata for .NET API Reference
description: Saves all changes made in the loaded document.
type: docs
weight: 110
url: /net/groupdocs.metadata/metadata/save/
---
## Save() {#save}

Saves all changes made in the loaded document.

```csharp
public void Save()
```

### Remarks

**Learn more**

* [Save a modified file to the original source](https://docs.groupdocs.com/display/metadatanet/Save+a+modified+file+to+the+original+source)
* [Save a modified file to a specified location](https://docs.groupdocs.com/display/metadatanet/Save+a+modified+file+to+a+specified+location)
* [Save a modified file to a stream](https://docs.groupdocs.com/display/metadatanet/Save+a+modified+file+to+a+stream)

### Examples

This example shows how to save the modified content to the underlying source.

```csharp
using (Metadata metadata = new Metadata(Constants.OutputPpt))
{
    // Edit or remove metadata here

    // Saves the document to the underlying source (stream or file)
    metadata.Save();
}
```

### See Also

* class [Metadata](../../metadata)
* namespace [GroupDocs.Metadata](../../metadata)
* assembly [GroupDocs.Metadata](../../../)

---

## Save(Stream) {#save_1}

Saves the document content into a stream.

```csharp
public void Save(Stream document)
```

| Parameter | Type | Description |
| --- | --- | --- |
| document | Stream | An output stream for the document. |

### Remarks

**Learn more**

* [Save a modified file to the original source](https://docs.groupdocs.com/display/metadatanet/Save+a+modified+file+to+the+original+source)
* [Save a modified file to a specified location](https://docs.groupdocs.com/display/metadatanet/Save+a+modified+file+to+a+specified+location)
* [Save a modified file to a stream](https://docs.groupdocs.com/display/metadatanet/Save+a+modified+file+to+a+stream)

### Examples

This example shows how to save a document to the specified stream.

```csharp
using (MemoryStream stream = new MemoryStream())
{
    using (Metadata metadata = new Metadata(Constants.InputPng))
    {
        // Edit or remove metadata here

        metadata.Save(stream);
    }
}
```

### See Also

* class [Metadata](../../metadata)
* namespace [GroupDocs.Metadata](../../metadata)
* assembly [GroupDocs.Metadata](../../../)

---

## Save(string) {#save_2}

Saves the document content to the specified file.

```csharp
public void Save(string filePath)
```

| Parameter | Type | Description |
| --- | --- | --- |
| filePath | String | The full name of the output file. |

### Remarks

**Learn more**

* [Save a modified file to the original source](https://docs.groupdocs.com/display/metadatanet/Save+a+modified+file+to+the+original+source)
* [Save a modified file to a specified location](https://docs.groupdocs.com/display/metadatanet/Save+a+modified+file+to+a+specified+location)
* [Save a modified file to a stream](https://docs.groupdocs.com/display/metadatanet/Save+a+modified+file+to+a+stream)

### Examples

This example shows how to save a document to the specified location.

```csharp
using (Metadata metadata = new Metadata(Constants.InputJpeg))
{
    // Edit or remove metadata here

    metadata.Save(Constants.OutputJpeg);
}
```

### See Also

* class [Metadata](../../metadata)
* namespace [GroupDocs.Metadata](../../metadata)
* assembly [GroupDocs.Metadata](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.metadata.dll -->