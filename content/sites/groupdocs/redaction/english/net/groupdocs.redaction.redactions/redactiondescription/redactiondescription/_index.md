---
title: RedactionDescription
second_title: GroupDocs.Redaction for .NET API Reference
description: Initializes a new instance of RedactionDescription class without replacement information.
type: docs
weight: 10
url: /net/groupdocs.redaction.redactions/redactiondescription/redactiondescription/
---
## RedactionDescription(RedactionType, RedactionActionType, string) {#constructor_1}

Initializes a new instance of RedactionDescription class without replacement information.

```csharp
public RedactionDescription(RedactionType redactionType, RedactionActionType actionType, 
    string originalText)
```

| Parameter | Type | Description |
| --- | --- | --- |
| redactionType | RedactionType | Type of data being redacted |
| actionType | RedactionActionType | Action to be performed on these data |
| originalText | String | Matched text, comment or annotation body |

### See Also

* enum [RedactionType](../../redactiontype)
* enum [RedactionActionType](../../redactionactiontype)
* class [RedactionDescription](../../redactiondescription)
* namespace [GroupDocs.Redaction.Redactions](../../redactiondescription)
* assembly [GroupDocs.Redaction](../../../)

---

## RedactionDescription(RedactionType, RedactionActionType, string, TextReplacement) {#constructor_2}

Initializes a new instance of RedactionDescription class with replacement information.

```csharp
public RedactionDescription(RedactionType redactionType, RedactionActionType actionType, 
    string originalText, TextReplacement replacement)
```

| Parameter | Type | Description |
| --- | --- | --- |
| redactionType | RedactionType | Type of data being redacted |
| actionType | RedactionActionType | Action to be performed on these data |
| originalText | String | Matched text, comment or annotation body |
| replacement | TextReplacement | Replacement text, matched text and its position within original string |

### See Also

* enum [RedactionType](../../redactiontype)
* enum [RedactionActionType](../../redactionactiontype)
* class [TextReplacement](../../textreplacement)
* class [RedactionDescription](../../redactiondescription)
* namespace [GroupDocs.Redaction.Redactions](../../redactiondescription)
* assembly [GroupDocs.Redaction](../../../)

---

## RedactionDescription(RedactionType, RedactionActionType, RegionReplacementOptions, string) {#constructor}

Initializes a new instance of RedactionDescription class with image area replacement information.

```csharp
public RedactionDescription(RedactionType redactionType, RedactionActionType actionType, 
    RegionReplacementOptions imageAreaReplacement, string imageDetails)
```

| Parameter | Type | Description |
| --- | --- | --- |
| redactionType | RedactionType | Type of data being redacted |
| actionType | RedactionActionType | Action to be performed on these data |
| imageAreaReplacement | RegionReplacementOptions | Image area replacement information |
| imageDetails | String | Image textual description, by default it is String.Empty |

### See Also

* enum [RedactionType](../../redactiontype)
* enum [RedactionActionType](../../redactionactiontype)
* class [RegionReplacementOptions](../../regionreplacementoptions)
* class [RedactionDescription](../../redactiondescription)
* namespace [GroupDocs.Redaction.Redactions](../../redactiondescription)
* assembly [GroupDocs.Redaction](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.redaction.dll -->