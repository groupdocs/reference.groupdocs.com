---
title: Header
second_title: .NET API 참조용 GroupDocs.Metadata
description: AVI 헤더 패키지를 가져옵니다.
type: docs
weight: 10
url: /ko/net/groupdocs.metadata.formats.video/avirootpackage/header/
---
## AviRootPackage.Header property

AVI 헤더 패키지를 가져옵니다.

```csharp
public AviHeader Header { get; }
```

### 자산 가치

AVI 헤더 패키지.

### 비고

**더 알아보기**

* [AVI 파일의 메타데이터 작업](https://docs.groupdocs.com/display/metadatanet/Working+with+metadata+in+AVI+files)

### 예

이 코드 조각은 AVI 헤더 속성을 읽는 방법을 보여줍니다.

```csharp
using (Metadata metadata = new Metadata(Constants.InputAvi))
{
    var root = metadata.GetRootPackage<AviRootPackage>();

    Console.WriteLine(root.Header.AviHeaderFlags);
    Console.WriteLine(root.Header.Height);
    Console.WriteLine(root.Header.Width);
    Console.WriteLine(root.Header.TotalFrames);
    Console.WriteLine(root.Header.InitialFrames);
    Console.WriteLine(root.Header.MaxBytesPerSec);
    Console.WriteLine(root.Header.PaddingGranularity);
    Console.WriteLine(root.Header.Streams);

    // ...
}
```

### 또한보십시오

* class [AviHeader](../../aviheader)
* class [AviRootPackage](../../avirootpackage)
* 네임스페이스 [GroupDocs.Metadata.Formats.Video](../../avirootpackage)
* 집회 [GroupDocs.Metadata](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Metadata.dll -->
