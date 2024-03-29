---
title: FromExtension
second_title: .NET API 참조용 GroupDocs.Watermark
description: 파일 확장자를 파일 유형에 매핑합니다.
type: docs
weight: 590
url: /ko/net/groupdocs.watermark.common/filetype/fromextension/
---
## FileType.FromExtension method

파일 확장자를 파일 유형에 매핑합니다.

```csharp
public static FileType FromExtension(string extension)
```

| 모수 | 유형 | 설명 |
| --- | --- | --- |
| extension | String | 파일 확장자(마침표 "." 포함). |

### 반환 값

파일 형식이 지원되면 반환하고 그렇지 않으면 기본값을 반환합니다.[`Unknown`](../unknown) 파일 형식.

### 예외

| 예외 | 상태 |
| --- | --- |
| ArgumentException | 발생하는 경우*extension* null이거나 빈 문자열입니다. |

### 또한보십시오

* class [FileType](../../filetype)
* 네임스페이스 [GroupDocs.Watermark.Common](../../filetype)
* 집회 [GroupDocs.Watermark](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Watermark.dll -->
