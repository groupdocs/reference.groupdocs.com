---
title: ForRenderingByWidthAndHeight
second_title: .NET API 참조용 GroupDocs.Viewer
description: 의 새 인스턴스를 초기화합니다.CadOptionsgroupdocs.viewer.options/cadoptions 너비와 높이로 렌더링하기 위한 클래스.
type: docs
weight: 40
url: /ko/net/groupdocs.viewer.options/cadoptions/forrenderingbywidthandheight/
---
## CadOptions.ForRenderingByWidthAndHeight method

의 새 인스턴스를 초기화합니다.[`CadOptions`](../../cadoptions) 너비와 높이로 렌더링하기 위한 클래스.

```csharp
public static CadOptions ForRenderingByWidthAndHeight(int width, int height)
```

| 모수 | 유형 | 설명 |
| --- | --- | --- |
| width | Int32 | 출력 결과의 너비는 픽셀 단위입니다. |
| height | Int32 | 출력 결과의 높이(픽셀)입니다. |

### 반환 값

새 인스턴스[`CadOptions`](../../cadoptions)너비와 높이로 렌더링하기 위한 클래스입니다.

### 예외

| 예외 | 상태 |
| --- | --- |
| ArgumentException | 언제 던져*width* 0보다 작거나 같습니다. |
| ArgumentException | 언제 던져*height* 0보다 작거나 같습니다. |

### 또한보십시오

* class [CadOptions](../../cadoptions)
* 네임스페이스 [GroupDocs.Viewer.Options](../../cadoptions)
* 집회 [GroupDocs.Viewer](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Viewer.dll -->
