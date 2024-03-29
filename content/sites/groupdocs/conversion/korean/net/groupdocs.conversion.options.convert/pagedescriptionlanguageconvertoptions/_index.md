---
title: PageDescriptionLanguageConvertOptions
second_title: .NET API 참조용 GroupDocs.Conversion
description: 페이지 설명 언어 파일 형식으로 변환하기 위한 옵션입니다.
type: docs
weight: 1700
url: /ko/net/groupdocs.conversion.options.convert/pagedescriptionlanguageconvertoptions/
---
## PageDescriptionLanguageConvertOptions class

페이지 설명 언어 파일 형식으로 변환하기 위한 옵션입니다.

```csharp
public class PageDescriptionLanguageConvertOptions : 
    CommonConvertOptions<PageDescriptionLanguageFileType>
```

## 생성자

| 이름 | 설명 |
| --- | --- |
| [PageDescriptionLanguageConvertOptions](pagedescriptionlanguageconvertoptions)() | 의 새 인스턴스를 초기화합니다.[`PageDescriptionLanguageFileType`](../../groupdocs.conversion.filetypes/pagedescriptionlanguagefiletype) 클래스. |

## 속성

| 이름 | 설명 |
| --- | --- |
| [Format](../../groupdocs.conversion.options.convert/convertoptions-1/format) { get; set; } | 입력 문서를 변환해야 하는 원하는 파일 형식입니다. |
| virtual [Format](../../groupdocs.conversion.options.convert/convertoptions/format) { get; set; } | 입력 문서를 변환해야 하는 원하는 파일 형식입니다. |
| [PageNumber](../../groupdocs.conversion.options.convert/commonconvertoptions-1/pagenumber) { get; set; } | 변환을 시작할 페이지 번호입니다. |
| [Pages](../../groupdocs.conversion.options.convert/commonconvertoptions-1/pages) { get; set; } | 변환할 페이지 인덱스 목록입니다. 특정 페이지를 변환하려면 지정해야 합니다. |
| [PagesCount](../../groupdocs.conversion.options.convert/commonconvertoptions-1/pagescount) { get; set; } | 변환할 페이지 수`페이지 번호` . |
| [Watermark](../../groupdocs.conversion.options.convert/commonconvertoptions-1/watermark) { get; set; } | 워터마크별 options |

## 행동 양식

| 이름 | 설명 |
| --- | --- |
| [Clone](../../groupdocs.conversion.options.convert/convertoptions/clone)() | 현재 옵션 인스턴스를 복제합니다. |
| override [Equals](../../groupdocs.conversion.contracts/valueobject/equals)(object) | 두 개체 인스턴스가 같은지 여부를 결정합니다. |
| virtual [Equals](../../groupdocs.conversion.contracts/valueobject/equals)(ValueObject) | 두 개체 인스턴스가 같은지 여부를 결정합니다. |
| override [GetHashCode](../../groupdocs.conversion.contracts/valueobject/gethashcode)() | 기본 해시 함수 역할을 합니다. |

### 또한보십시오

* class [CommonConvertOptions&lt;TFileType&gt;](../commonconvertoptions-1)
* class [PageDescriptionLanguageFileType](../../groupdocs.conversion.filetypes/pagedescriptionlanguagefiletype)
* 네임스페이스 [GroupDocs.Conversion.Options.Convert](../../groupdocs.conversion.options.convert)
* 집회 [GroupDocs.Conversion](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Conversion.dll -->
