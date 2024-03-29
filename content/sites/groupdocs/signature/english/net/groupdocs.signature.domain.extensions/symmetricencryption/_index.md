---
title: SymmetricEncryption
second_title: GroupDocs.Signature for .NET API Reference
description: Implements standard symmetric algorithms for data encryption with single key and passphrase salt.
type: docs
weight: 540
url: /net/groupdocs.signature.domain.extensions/symmetricencryption/
---
## SymmetricEncryption class

Implements standard symmetric algorithms for data encryption with single key and passphrase (salt).

```csharp
public sealed class SymmetricEncryption : IDataEncryption
```

## Constructors

| Name | Description |
| --- | --- |
| [SymmetricEncryption](symmetricencryption#constructor)(SymmetricAlgorithmType, string) | Creates symmetric encryption algorithm with default passphrase |
| [SymmetricEncryption](symmetricencryption#constructor_1)(SymmetricAlgorithmType, string, string) | Creates symmetric encryption algorithm with parameters. |

## Properties

| Name | Description |
| --- | --- |
| [AlgorithmType](../../groupdocs.signature.domain.extensions/symmetricencryption/algorithmtype) { get; set; } | Gets or sets type of symmetric algorithm. |
| [Key](../../groupdocs.signature.domain.extensions/symmetricencryption/key) { get; set; } | Gets or sets key of encryption algorithm. |
| [Salt](../../groupdocs.signature.domain.extensions/symmetricencryption/salt) { get; set; } | Gets or sets passphrase of encryption algorithm. |

## Methods

| Name | Description |
| --- | --- |
| [Decode](../../groupdocs.signature.domain.extensions/symmetricencryption/decode)(string) | Decrypts string based on provided algorithm type, key and salt parameters |
| [Encode](../../groupdocs.signature.domain.extensions/symmetricencryption/encode)(string) | Encrypts string based on provided algorithm type, key and salt parameters |

### See Also

* interface [IDataEncryption](../idataencryption)
* namespace [GroupDocs.Signature.Domain.Extensions](../../groupdocs.signature.domain.extensions)
* assembly [GroupDocs.Signature](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.signature.dll -->
