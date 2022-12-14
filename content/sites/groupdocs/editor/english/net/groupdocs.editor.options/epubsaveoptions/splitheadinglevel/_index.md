---
title: SplitHeadingLevel
second_title: GroupDocs.Editor for .NET API Reference
description: Specifies the maximum level of headings at which to split the ePub file. Default value is 2. Setting it to 0 will disable splitting so all content of the eBook will be incorporarted into a single package inside the ePub.
type: docs
weight: 30
url: /net/groupdocs.editor.options/epubsaveoptions/splitheadinglevel/
---
## EpubSaveOptions.SplitHeadingLevel property

Specifies the maximum level of headings at which to split the ePub file. Default value is `2`. Setting it to `0` will disable splitting, so all content of the e-Book will be incorporarted into a single package inside the ePub.

```csharp
public int SplitHeadingLevel { get; set; }
```

### Remarks

When this property is set to a value from 1 to 9, the document will be split at paragraphs formatted using **Heading 1**, **Heading 2** , **Heading 3** etc. styles up to the specified heading level.

By default, only **Heading 1** and **Heading 2** paragraphs cause the document to be split. Setting this property to zero will cause the document not to be split at heading paragraphs at all.

### See Also

* class [EpubSaveOptions](../../epubsaveoptions)
* namespace [GroupDocs.Editor.Options](../../epubsaveoptions)
* assembly [GroupDocs.Editor](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.editor.dll -->
