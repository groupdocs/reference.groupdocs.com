---
title: DigitalSignaturePackage
second_title: GroupDocs.Metadata for .NET API-referens
description: Hämtar metadatapaketet för digital signatur.
type: docs
weight: 10
url: /sv/net/groupdocs.metadata.formats.font/opentyperootpackage/digitalsignaturepackage/
---
## OpenTypeRootPackage.DigitalSignaturePackage property

Hämtar metadatapaketet för digital signatur.

```csharp
public CmsPackage DigitalSignaturePackage { get; }
```

### Fastighetsvärde

Det digitala signaturmetadatapaketet.

### Anmärkningar

**Läs mer**

* [Arbeta med OpenType-teckensnitt](https://docs.groupdocs.com/display/metadatanet/Working+with+OpenType+fonts)

### Exempel

Det här kodavsnittet visar hur man extraherar digitala signaturer associerade med ett OpenType-teckensnitt.

```csharp
public static void Run()
{
    using (Metadata metadata = new Metadata(Constants.InputTtf))
    {
        var root = metadata.GetRootPackage<OpenTypeRootPackage>();

        if (root.DigitalSignaturePackage != null)
        {
            Console.WriteLine(root.DigitalSignaturePackage.Flags);
            foreach (var signature in root.DigitalSignaturePackage.Signatures)
            {
                Console.WriteLine(signature.SignTime);
                if (signature.DigestAlgorithms != null)
                {
                    foreach (var signatureDigestAlgorithm in signature.DigestAlgorithms)
                    {
                        PrintOid(signatureDigestAlgorithm);
                    }
                }
                if (signature.EncapsulatedContent != null)
                {
                    PrintOid(signature.EncapsulatedContent.ContentType);
                    Console.WriteLine(signature.EncapsulatedContent.ContentRawData.Length);
                }
                if (signature.Certificates != null)
                {
                    foreach (var certificate in signature.Certificates)
                    {
                        Console.WriteLine(certificate.NotAfter);
                        Console.WriteLine(certificate.NotBefore);
                        Console.WriteLine(certificate.RawData.Length);
                    }
                }
                if (signature.Signers != null)
                {
                    foreach (var signerInfoEntry in signature.Signers)
                    {
                        Console.WriteLine(signerInfoEntry.SignatureValue);
                        PrintOid(signerInfoEntry.DigestAlgorithm);
                        PrintOid(signerInfoEntry.SignatureAlgorithm);
                        Console.WriteLine(signerInfoEntry.SigningTime);
                        PrintAttributes(signerInfoEntry.SignedAttributes);
                        PrintAttributes(signerInfoEntry.UnsignedAttributes);
                    }
                }
            }
        }
    }
}

private static void PrintOid(Oid oid)
{
    // Visa egenskapens namn och värde för OID
    if (oid != null)
    {
        Console.WriteLine(oid.FriendlyName);
        Console.WriteLine(oid.Value);
    }
}

private static void PrintAttributes(CmsAttribute[] attributes)
{
    //Visa CmsAttributes för en OID
    if (attributes != null)
    {
        foreach (CmsAttribute attribute in attributes)
        {
            PrintOid(attribute.Oid);
            Console.WriteLine(attribute.Value);
        }
    }
}
```

### Se även

* class [CmsPackage](../../../groupdocs.metadata.standards.pkcs/cmspackage)
* class [OpenTypeRootPackage](../../opentyperootpackage)
* namnutrymme [GroupDocs.Metadata.Formats.Font](../../opentyperootpackage)
* hopsättning [GroupDocs.Metadata](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Metadata.dll -->
