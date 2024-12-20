---
title: SetMeteredKey
second_title: GroupDocs.Redaction for .NET API Reference
description: Activates the product with Metered keys.
type: docs
weight: 20
url: /net/groupdocs.redaction/metered/setmeteredkey/
---
## Metered.SetMeteredKey method

Activates the product with Metered keys.

```csharp
public void SetMeteredKey(string publicKey, string privateKey)
```

| Parameter | Type | Description |
| --- | --- | --- |
| publicKey | String | The public key. |
| privateKey | String | The private key. |

### Examples

The following example demonstrates how to activate the product with Metered keys.

```csharp
string publicKey = "Public Key";
string privateKey = "Private Key";

Metered metered = new Metered();
metered.SetMeteredKey(publicKey, privateKey);
```

### See Also

* class [Metered](../../metered)
* namespace [GroupDocs.Redaction](../../../groupdocs.redaction)
* assembly [GroupDocs.Redaction](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.redaction.dll -->
