---
title: SetLicense
second_title: GroupDocs.Assembly for .NET API Reference
description: Licenses the component.
type: docs
weight: 30
url: /net/groupdocs.assembly/license/setlicense/
---
## SetLicense(string) {#setlicense_1}

Licenses the component.

```csharp
public void SetLicense(string licenseName)
```

| Parameter | Type | Description |
| --- | --- | --- |
| licenseName | String | Can be a full or short file name or name of an embedded resource. Use an empty string to switch to evaluation mode. |

### Remarks

Tries to find the license in the following locations:

1. Explicit path.

2. The folder that contains the GroupDocs component assembly.

3. The folder that contains the client's calling assembly.

4. The folder that contains the entry (startup) assembly.

5. An embedded resource in the client's calling assembly.

### See Also

* class [License](../../license)
* namespace [GroupDocs.Assembly](../../license)
* assembly [GroupDocs.Assembly](../../../)

---

## SetLicense(Stream) {#setlicense}

Licenses the component.

```csharp
public void SetLicense(Stream stream)
```

| Parameter | Type | Description |
| --- | --- | --- |
| stream | Stream | A stream that contains the license. |

### Remarks

Use this method to load a license from a stream.

### See Also

* class [License](../../license)
* namespace [GroupDocs.Assembly](../../license)
* assembly [GroupDocs.Assembly](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Assembly.dll -->