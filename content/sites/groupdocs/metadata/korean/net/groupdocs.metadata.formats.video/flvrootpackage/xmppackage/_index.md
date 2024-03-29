---
title: XmpPackage
second_title: .NET API 참조용 GroupDocs.Metadata
description: XMP 메타데이터 패키지를 가져오거나 설정합니다.
type: docs
weight: 20
url: /ko/net/groupdocs.metadata.formats.video/flvrootpackage/xmppackage/
---
## FlvRootPackage.XmpPackage property

XMP 메타데이터 패키지를 가져오거나 설정합니다.

```csharp
public XmpPacketWrapper XmpPackage { get; set; }
```

### 자산 가치

XMP 메타데이터 패키지.

### 비고

**더 알아보기**

* [XMP 메타데이터 작업](https://docs.groupdocs.com/display/metadatanet/Working+with+XMP+metadata)

### 예

이 예는 파일에서 XMP 메타데이터를 추출하는 방법을 보여줍니다.

```csharp
using (Metadata metadata = new Metadata(Constants.FlvWithXmp))
{
    var root = metadata.GetRootPackage<FlvRootPackage>();
    if (root.XmpPackage != null)
    {
        if (root.XmpPackage.Schemes.XmpBasic != null)
        {
            Console.WriteLine(root.XmpPackage.Schemes.XmpBasic.CreatorTool);
            Console.WriteLine(root.XmpPackage.Schemes.XmpBasic.CreateDate);
            Console.WriteLine(root.XmpPackage.Schemes.XmpBasic.ModifyDate);
            Console.WriteLine(root.XmpPackage.Schemes.XmpBasic.Label);
            Console.WriteLine(root.XmpPackage.Schemes.XmpBasic.Nickname);

            // ...
        }

        if (root.XmpPackage.Schemes.DublinCore != null)
        {
            Console.WriteLine(root.XmpPackage.Schemes.DublinCore.Format);
            Console.WriteLine(root.XmpPackage.Schemes.DublinCore.Coverage);
            Console.WriteLine(root.XmpPackage.Schemes.DublinCore.Identifier);
            Console.WriteLine(root.XmpPackage.Schemes.DublinCore.Source);

            // ...
        }

        if (root.XmpPackage.Schemes.Photoshop != null)
        {
            Console.WriteLine(root.XmpPackage.Schemes.Photoshop.ColorMode);
            Console.WriteLine(root.XmpPackage.Schemes.Photoshop.IccProfile);
            Console.WriteLine(root.XmpPackage.Schemes.Photoshop.Country);
            Console.WriteLine(root.XmpPackage.Schemes.Photoshop.City);
            Console.WriteLine(root.XmpPackage.Schemes.Photoshop.DateCreated);

            // ... 
        }

        // ...
    }
}
```

### 또한보십시오

* class [XmpPacketWrapper](../../../groupdocs.metadata.standards.xmp/xmppacketwrapper)
* class [FlvRootPackage](../../flvrootpackage)
* 네임스페이스 [GroupDocs.Metadata.Formats.Video](../../flvrootpackage)
* 집회 [GroupDocs.Metadata](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Metadata.dll -->
