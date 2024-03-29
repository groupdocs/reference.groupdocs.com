---
title: IPreviewOptions
second_title: .NET API 참조용 GroupDocs.Merger
description: 미리보기 옵션용 인터페이스.
type: docs
weight: 290
url: /ko/net/groupdocs.merger.domain.options/ipreviewoptions/
---
## IPreviewOptions interface

미리보기 옵션용 인터페이스.

```csharp
public interface IPreviewOptions : IPageOptions
```

## 속성

| 이름 | 설명 |
| --- | --- |
| [CreateStream](../../groupdocs.merger.domain.options/ipreviewoptions/createstream) { get; } | 출력 페이지 미리보기 스트림을 생성하는 방법을 정의하는 대리자. |
| [Height](../../groupdocs.merger.domain.options/ipreviewoptions/height) { get; set; } | 미리보기 높이. |
| [Mode](../../groupdocs.merger.domain.options/ipreviewoptions/mode) { get; } | 미리보기 모드를 가져옵니다. |
| [ReleaseStream](../../groupdocs.merger.domain.options/ipreviewoptions/releasestream) { get; } | 출력 페이지 미리 보기 스트림을 해제하는 방법을 정의하는 대리자입니다. |
| [Width](../../groupdocs.merger.domain.options/ipreviewoptions/width) { get; set; } | 미리보기 너비. |

## 행동 양식

| 이름 | 설명 |
| --- | --- |
| [GetPathByPageNumber](../../groupdocs.merger.domain.options/ipreviewoptions/getpathbypagenumber)(int, string) | 확장자가 정의된 페이지 번호로 미리 본 문서의 전체 파일 경로를 가져옵니다. |
| [Validate](../../groupdocs.merger.domain.options/ipreviewoptions/validate)(FileType) | 분할 옵션을 확인합니다. |

### 또한보십시오

* interface [IPageOptions](../ipageoptions)
* 네임스페이스 [GroupDocs.Merger.Domain.Options](../../groupdocs.merger.domain.options)
* 집회 [GroupDocs.Merger](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Merger.dll -->
