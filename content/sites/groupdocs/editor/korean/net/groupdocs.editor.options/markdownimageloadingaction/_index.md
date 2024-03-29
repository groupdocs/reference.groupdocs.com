---
title: MarkdownImageLoadingAction
second_title: .NET API 참조용 GroupDocs.Editor
description: Markdown format 에서 파일을 편집하기 위해 여는 동안 이미지 로드 모드를 정의합니다.
type: docs
weight: 980
url: /ko/net/groupdocs.editor.options/markdownimageloadingaction/
---
## MarkdownImageLoadingAction enumeration

Markdown format 에서 파일을 편집하기 위해 여는 동안 이미지 로드 모드를 정의합니다.

```csharp
public enum MarkdownImageLoadingAction : byte
```

### 가치

| 이름 | 값 | 설명 |
| --- | --- | --- |
| Default | `0` | GroupDocs.Editor는 평소와 같이 이 리소스를 로드합니다 |
| Skip | `1` | GroupDocs.Editor는 이 image 의 로드를 건너뜁니다. |
| UserProvided | `2` | GroupDocs.Editor는 다음에서 사용자가 제공한 바이트 배열을 사용합니다.[`SetData`](../markdownimageloadargs/setdata) 이미지 data 로 |

### 또한보십시오

* 네임스페이스 [GroupDocs.Editor.Options](../../groupdocs.editor.options)
* 집회 [GroupDocs.Editor](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Editor.dll -->
