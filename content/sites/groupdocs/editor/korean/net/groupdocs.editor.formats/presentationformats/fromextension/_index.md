---
title: FromExtension
second_title: .NET API 참조용 GroupDocs.Editor
description: 인스턴스 반환PresentationFormatsgroupdocs.editor.formats/presentationformats 지정된 파일 이름 확장자와 연결된 구조이거나 확장자를 제대로 구문 분석할 수 없는 경우 예외가 발생합니다
type: docs
weight: 130
url: /ko/net/groupdocs.editor.formats/presentationformats/fromextension/
---
## PresentationFormats.FromExtension method

인스턴스 반환[`PresentationFormats`](../../presentationformats) 지정된 파일 이름 확장자와 연결된 구조이거나 확장자를 제대로 구문 분석할 수 없는 경우 예외가 발생합니다

```csharp
public static PresentationFormats FromExtension(string extension)
```

| 모수 | 유형 | 설명 |
| --- | --- | --- |
| extension | String | 파일 이름 확장자 단독 또는 지원 가능한 프리젠테이션 형식의 적절한 확장자가 있는 파일 이름, 선행 점 문자 포함 또는 제외, 대소문자 독립적. NULL이거나 비어 있을 수 없으며 유효해야 합니다. |

### 반환 값

대신에[`PresentationFormats`](../../presentationformats)성공 시 구조 또는 실패 시 예외 발생

### 또한보십시오

* struct [PresentationFormats](../../presentationformats)
* 네임스페이스 [GroupDocs.Editor.Formats](../../presentationformats)
* 집회 [GroupDocs.Editor](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Editor.dll -->
