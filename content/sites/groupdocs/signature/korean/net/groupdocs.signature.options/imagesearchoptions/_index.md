---
title: ImageSearchOptions
second_title: .NET API 참조용 GroupDocs.Signature
description: 이미지 서명에 대한 검색 옵션을 나타냅니다.
type: docs
weight: 1410
url: /ko/net/groupdocs.signature.options/imagesearchoptions/
---
## ImageSearchOptions class

이미지 서명에 대한 검색 옵션을 나타냅니다.

```csharp
public class ImageSearchOptions : SearchOptions
```

## 생성자

| 이름 | 설명 |
| --- | --- |
| [ImageSearchOptions](imagesearchoptions)() | 기본값으로 ImageSearchOptions 클래스의 새 인스턴스를 초기화합니다. |

## 속성

| 이름 | 설명 |
| --- | --- |
| [AllPages](../../groupdocs.signature.options/searchoptions/allpages) { get; set; } | 각 문서 페이지에서 검색할 플래그입니다. 기본적으로 이 값은 true로 설정됩니다. |
| [MaxContentSize](../../groupdocs.signature.options/imagesearchoptions/maxcontentsize) { get; set; } | 0이 아닌 값의 경우 이 플래그는 검색 기준에 대한 이미지의 최대 크기를 지정합니다. 기본적으로 이 플래그는 0으로 설정되며 검색 결과에 영향을 주지 않습니다. |
| [MinContentSize](../../groupdocs.signature.options/imagesearchoptions/mincontentsize) { get; set; } | 0이 아닌 값의 경우 이 플래그는 검색 기준에 대한 이미지의 최소 크기를 지정합니다. 기본적으로 이 플래그는 0으로 설정되며 검색 결과에 영향을 주지 않습니다. |
| [PageNumber](../../groupdocs.signature.options/searchoptions/pagenumber) { get; set; } | 검색할 문서 페이지 번호를 가져오거나 설정합니다. 값은 선택 사항입니다. |
| [PagesSetup](../../groupdocs.signature.options/searchoptions/pagessetup) { get; set; } | 서명 검색을 위한 페이지 지정 옵션. |
| [ReturnContent](../../groupdocs.signature.options/imagesearchoptions/returncontent) { get; set; } | 문서 페이지에서 서명의 이미지 내용을 가져오도록 플래그를 가져오거나 설정합니다. 이 플래그가 true로 설정되면 이미지 서명 내용은 필요한 형식으로 원시 이미지 데이터를 유지합니다.[`ReturnContentType`](./returncontenttype) . 기본적으로 이 옵션은 비활성화되어 있습니다. |
| [ReturnContentType](../../groupdocs.signature.options/imagesearchoptions/returncontenttype) { get; set; } | ReturnContent 속성이 활성화된 경우 이미지 서명의 반환된 콘텐츠 파일 형식을 지정합니다. 기본적으로 Null로 설정됩니다. 이는 이미지 콘텐츠를 원본 형식으로 반환하는 것을 의미합니다. 이 이미지 형식은 다음에 지정됩니다.[`Format`](../../groupdocs.signature.domain/imagesignature/format) 가능한 지원 값은 FileType.JPEG, FileType.PNG, FileType.BMP입니다. 제공된 형식이 지원되지 않는 경우 원본 형식의 이미지 콘텐츠가 반환됩니다. |
| [SkipExternal](../../groupdocs.signature.options/searchoptions/skipexternal) { get; set; } | IsSignature로 표시된 서명만 반환하는 플래그입니다. 기본 값은 지정된 기준과 일치하는 모든 서명을 반환함을 나타내는 false입니다. |

### 비고

**더 알아보기**

* GroupDocs.Signature에 의한 이미지 전자 서명 검색의 기본 사용법: [ 문서에서 이미지 서명을 eSearch하는 방법](https://docs.groupdocs.com/display/signaturenet/Search+for+Image+e-signatures)
* GroupDocs.Signature를 사용한 이미지 전자 서명 검색 설정의 고급 사용: [문서 및 추가 설정에서 eSearch 이미지 서명의 고급 사용](https://docs.groupdocs.com/display/signaturenet/Advanced+search+for+Image+signatures)

### 또한보십시오

* class [SearchOptions](../searchoptions)
* 네임스페이스 [GroupDocs.Signature.Options](../../groupdocs.signature.options)
* 집회 [GroupDocs.Signature](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Signature.dll -->
