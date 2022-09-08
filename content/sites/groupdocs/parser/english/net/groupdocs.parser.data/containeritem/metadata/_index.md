---
title: Metadata
second_title: GroupDocs.Parser for .NET API Reference
description: Gets the collection of metadata items.
type: docs
weight: 30
url: /net/groupdocs.parser.data/containeritem/metadata/
---
## ContainerItem.Metadata property

Gets the collection of metadata items.

```csharp
public IEnumerable<MetadataItem> Metadata { get; }
```

### Property Value

A collection of [`MetadataItem`](../../metadataitem) objects; empty if metadata isn't set.

### Remarks

These metadata refer to a container element itself, not a document. Depending on the container type metadata can contain the following items:

**Email Attachments**

**Name**

**Description**

**content-type**

The MIME type of the attachment content.

**ZIP Archives**

**Name**

**Description**

**date**

The time and date at which the file indicated by the Zip Entry was last modified.

**Outlook Storage**

**Name**

**Description**

**date**

The time and date at which the Outlook Storage item was last modified.

**email-sender**

The value of "sender" field.

**email-to**

The value of "to" field.

**subject**

The value of "subject" field.

### See Also

* class [MetadataItem](../../metadataitem)
* class [ContainerItem](../../containeritem)
* namespace [GroupDocs.Parser.Data](../../containeritem)
* assembly [GroupDocs.Parser](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.parser.dll -->