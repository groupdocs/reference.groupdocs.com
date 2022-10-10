---
title: WordProcessingLockType
second_title: GroupDocs.Watermark for .NET API Reference
description: Specifies watermark lock type in Word document.
type: docs
weight: 2290
url: /net/groupdocs.watermark.options.wordprocessing/wordprocessinglocktype/
---
## WordProcessingLockType enumeration

Specifies watermark lock type in Word document.

```csharp
public enum WordProcessingLockType
```

### Values

| Name | Value | Description |
| --- | --- | --- |
| AllowOnlyRevisions | `0` | User can only add revision marks to the document. |
| AllowOnlyComments | `1` | User can only modify comments in the document. |
| AllowOnlyFormFields | `2` | User can only enter data in the form fields in the document. |
| ReadOnly | `3` | The entire document is read-only. |
| ReadOnlyWithEditableContent | `4` | The document is read-only, but all the content except of the watermark is marked as editable. |
| NoLock | `-1` | Disable any lock on watermark and document. |

### See Also

* namespace [GroupDocs.Watermark.Options.WordProcessing](../../groupdocs.watermark.options.wordprocessing)
* assembly [GroupDocs.Watermark](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.watermark.dll -->