---
title: IDocumentInfo
second_title: .NET API 참조용 GroupDocs.Editor
description: 모든 파일 메타데이터 wrappers 에 대한 공통 인터페이스
type: docs
weight: 740
url: /ko/net/groupdocs.editor.metadata/idocumentinfo/
---
## IDocumentInfo interface

모든 파일 메타데이터 wrappers 에 대한 공통 인터페이스

```csharp
public interface IDocumentInfo
```

## 속성

| 이름 | 설명 |
| --- | --- |
| [Format](../../groupdocs.editor.metadata/idocumentinfo/format) { get; } | 구현 형식에서 하나의 형식 패밀리를 나타내고 IDocumentFormat interface 에서 상속하는 형식의 단일 값으로 문서 형식을 반환해야 합니다. |
| [IsEncrypted](../../groupdocs.editor.metadata/idocumentinfo/isencrypted) { get; } | 특정 파일이 암호화되어 있고 열 때 암호가 필요한지 여부를 나타냅니다. 암호화할 수 없는 문서 유형의 경우(모든 텍스트 기반과 마찬가지로) 항상 'false'를 반환해야 합니다. |
| [PageCount](../../groupdocs.editor.metadata/idocumentinfo/pagecount) { get; } | 구현 유형에서 페이지 또는 기타 유사한 형식 종속 엔터티(탭, 슬라이드 등)의 수(숫자)를 반환해야 합니다. 1. |
| [Size](../../groupdocs.editor.metadata/idocumentinfo/size) { get; } | 바이트 단위의 문서 크기 |

### 또한보십시오

* 네임스페이스 [GroupDocs.Editor.Metadata](../../groupdocs.editor.metadata)
* 집회 [GroupDocs.Editor](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Editor.dll -->
