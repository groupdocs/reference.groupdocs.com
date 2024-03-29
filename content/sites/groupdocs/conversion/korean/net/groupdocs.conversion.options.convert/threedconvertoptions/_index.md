---
title: ThreeDConvertOptions
second_title: .NET API 참조용 GroupDocs.Conversion
description: 3D 유형으로 변환 옵션.
type: docs
weight: 1910
url: /ko/net/groupdocs.conversion.options.convert/threedconvertoptions/
---
## ThreeDConvertOptions class

3D 유형으로 변환 옵션.

```csharp
public class ThreeDConvertOptions : ConvertOptions<ThreeDFileType>, IPagedConvertOptions
```

## 생성자

| 이름 | 설명 |
| --- | --- |
| [ThreeDConvertOptions](threedconvertoptions)() | 의 새 인스턴스를 초기화합니다.[`ThreeDConvertOptions`](../threedconvertoptions) 클래스. |

## 속성

| 이름 | 설명 |
| --- | --- |
| [Format](../../groupdocs.conversion.options.convert/convertoptions-1/format) { get; set; } | 입력 문서를 변환해야 하는 원하는 파일 형식입니다. |
| virtual [Format](../../groupdocs.conversion.options.convert/convertoptions/format) { get; set; } | 입력 문서를 변환해야 하는 원하는 파일 형식입니다. |
| [PageNumber](../../groupdocs.conversion.options.convert/threedconvertoptions/pagenumber) { get; set; } | 변환을 시작할 페이지 번호입니다. |
| [PagesCount](../../groupdocs.conversion.options.convert/threedconvertoptions/pagescount) { get; set; } | 변환할 페이지 수`페이지 번호` . |

## 행동 양식

| 이름 | 설명 |
| --- | --- |
| [Clone](../../groupdocs.conversion.options.convert/convertoptions/clone)() | 현재 옵션 인스턴스를 복제합니다. |
| override [Equals](../../groupdocs.conversion.contracts/valueobject/equals)(object) | 두 개체 인스턴스가 같은지 여부를 결정합니다. |
| virtual [Equals](../../groupdocs.conversion.contracts/valueobject/equals)(ValueObject) | 두 개체 인스턴스가 같은지 여부를 결정합니다. |
| override [GetHashCode](../../groupdocs.conversion.contracts/valueobject/gethashcode)() | 기본 해시 함수 역할을 합니다. |

### 또한보십시오

* class [ConvertOptions&lt;TFileType&gt;](../convertoptions-1)
* class [ThreeDFileType](../../groupdocs.conversion.filetypes/threedfiletype)
* interface [IPagedConvertOptions](../ipagedconvertoptions)
* 네임스페이스 [GroupDocs.Conversion.Options.Convert](../../groupdocs.conversion.options.convert)
* 집회 [GroupDocs.Conversion](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Conversion.dll -->
