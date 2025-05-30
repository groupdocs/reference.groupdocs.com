---
title: AcceptRedaction
second_title: GroupDocs.Redaction for .NET API Reference
description: This call is triggered right before applying any redaction to the document and allows to log or forbid it.
type: docs
weight: 10
url: /net/groupdocs.redaction.redactions/iredactioncallback/acceptredaction/
---
## IRedactionCallback.AcceptRedaction method

This call is triggered right before applying any redaction to the document and allows to log or forbid it.

```csharp
public bool AcceptRedaction(RedactionDescription description)
```

| Parameter | Type | Description |
| --- | --- | --- |
| description | RedactionDescription | Contains information about particular match type, criteria, text and position |

### Return Value

Return true to accept or false to decline particular match redaction

### See Also

* class [RedactionDescription](../../redactiondescription)
* interface [IRedactionCallback](../../iredactioncallback)
* namespace [GroupDocs.Redaction.Redactions](../../../groupdocs.redaction.redactions)
* assembly [GroupDocs.Redaction](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.redaction.dll -->
