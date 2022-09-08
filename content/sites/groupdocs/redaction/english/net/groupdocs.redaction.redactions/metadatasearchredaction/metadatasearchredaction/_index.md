---
title: MetadataSearchRedaction
second_title: GroupDocs.Redaction for .NET API Reference
description: Initializes a new instance of MetadataSearchRedaction class using value to match redacted items.
type: docs
weight: 10
url: /net/groupdocs.redaction.redactions/metadatasearchredaction/metadatasearchredaction/
---
## MetadataSearchRedaction(string, string) {#constructor}

Initializes a new instance of MetadataSearchRedaction class, using value to match redacted items.

```csharp
public MetadataSearchRedaction(string valuePattern, string replacement)
```

| Parameter | Type | Description |
| --- | --- | --- |
| valuePattern | String | Regular expression to search and replace |
| replacement | String | Textual replacement |

### See Also

* class [MetadataSearchRedaction](../../metadatasearchredaction)
* namespace [GroupDocs.Redaction.Redactions](../../metadatasearchredaction)
* assembly [GroupDocs.Redaction](../../../)

---

## MetadataSearchRedaction(string, string, string) {#constructor_1}

Initializes a new instance of MetadataSearchRedaction class, using item name and value to match redacted items.

```csharp
public MetadataSearchRedaction(string valuePattern, string replacement, string keyPattern)
```

| Parameter | Type | Description |
| --- | --- | --- |
| valuePattern | String | Regular expression to search and replace metadata item value |
| replacement | String | Textual replacement |
| keyPattern | String | Regular expression to search and replace metadata item name |

### See Also

* class [MetadataSearchRedaction](../../metadatasearchredaction)
* namespace [GroupDocs.Redaction.Redactions](../../metadatasearchredaction)
* assembly [GroupDocs.Redaction](../../../)

---

## MetadataSearchRedaction(Regex, string) {#constructor_2}

Initializes a new instance of MetadataSearchRedaction class, using value to match redacted items.

```csharp
public MetadataSearchRedaction(Regex valueRegex, string replacement)
```

| Parameter | Type | Description |
| --- | --- | --- |
| valueRegex | Regex | Regular expression to search and replace |
| replacement | String | Textual replacement |

### See Also

* class [MetadataSearchRedaction](../../metadatasearchredaction)
* namespace [GroupDocs.Redaction.Redactions](../../metadatasearchredaction)
* assembly [GroupDocs.Redaction](../../../)

---

## MetadataSearchRedaction(Regex, string, Regex) {#constructor_3}

Initializes a new instance of MetadataSearchRedaction class, using item name and value to match redacted items.

```csharp
public MetadataSearchRedaction(Regex valueRegex, string replacement, Regex keyRegex)
```

| Parameter | Type | Description |
| --- | --- | --- |
| valueRegex | Regex | Regular expression to search and replace metadata item value |
| replacement | String | Textual replacement |
| keyRegex | Regex | Regular expression to search and replace metadata item name |

### See Also

* class [MetadataSearchRedaction](../../metadatasearchredaction)
* namespace [GroupDocs.Redaction.Redactions](../../metadatasearchredaction)
* assembly [GroupDocs.Redaction](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.redaction.dll -->