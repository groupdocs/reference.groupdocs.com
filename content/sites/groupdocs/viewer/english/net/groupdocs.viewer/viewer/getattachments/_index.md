---
title: GetAttachments
second_title: GroupDocs.Viewer for .NET API Reference
description: Returns attachments contained by the document.
type: docs
weight: 40
url: /net/groupdocs.viewer/viewer/getattachments/
---
## GetAttachments() {#getattachments}

Returns attachments contained by the document.

```csharp
public IList<Attachment> GetAttachments()
```

### Return Value

Attachments contained by the document.

### Exceptions

| exception | condition |
| --- | --- |
| [PasswordRequiredException](../../../groupdocs.viewer.exceptions/passwordrequiredexception) | Thrown when password is required to open the document. |
| [IncorrectPasswordException](../../../groupdocs.viewer.exceptions/incorrectpasswordexception) | Thrown when password that was specified is incorrect. |

### Remarks

**Learn more**

* Learn more about getting document attachments in C#: [How to get list of document attachments using GroupDocs.Viewer](https://docs.groupdocs.com/display/viewernet/Get+attachments)
* Learn more about saving document attachments in C#: [How to save document attachments using GroupDocs.Viewer](https://docs.groupdocs.com/display/viewernet/Save+attachments)

### See Also

* class [Attachment](../../../groupdocs.viewer.results/attachment)
* class [Viewer](../../viewer)
* namespace [GroupDocs.Viewer](../../../groupdocs.viewer)
* assembly [GroupDocs.Viewer](../../../)

---

## GetAttachments(CancellationToken) {#getattachments_1}

Returns attachments contained by the document.

```csharp
public IList<Attachment> GetAttachments(CancellationToken cancellationToken)
```

| Parameter | Type | Description |
| --- | --- | --- |
| cancellationToken | CancellationToken | Cancellation token. |

### Return Value

Attachments contained by the document.

### Exceptions

| exception | condition |
| --- | --- |
| [PasswordRequiredException](../../../groupdocs.viewer.exceptions/passwordrequiredexception) | Thrown when password is required to open the document. |
| [IncorrectPasswordException](../../../groupdocs.viewer.exceptions/incorrectpasswordexception) | Thrown when password that was specified is incorrect. |

### Remarks

**Learn more**

* Learn more about getting document attachments in C#: [How to get list of document attachments using GroupDocs.Viewer](https://docs.groupdocs.com/display/viewernet/Get+attachments)
* Learn more about saving document attachments in C#: [How to save document attachments using GroupDocs.Viewer](https://docs.groupdocs.com/display/viewernet/Save+attachments)

### See Also

* class [Attachment](../../../groupdocs.viewer.results/attachment)
* class [Viewer](../../viewer)
* namespace [GroupDocs.Viewer](../../../groupdocs.viewer)
* assembly [GroupDocs.Viewer](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.viewer.dll -->
