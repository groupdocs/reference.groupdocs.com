---
title: InputControlsClassName
second_title: .NET API 참조용 GroupDocs.Editor
description: 입력 WordProcessing 문서의 일부 필드를 나타내는 모든 HTML 요소의 class 특성에 배치될 클래스 이름을 지정할 수 있습니다. 기본적으로 NULL  class 특성이 적용되지 않습니다.
type: docs
weight: 60
url: /ko/net/groupdocs.editor.options/wordprocessingeditoptions/inputcontrolsclassname/
---
## WordProcessingEditOptions.InputControlsClassName property

입력 WordProcessing 문서의 일부 필드를 나타내는 모든 HTML 요소의 'class' 특성에 배치될 클래스 이름을 지정할 수 있습니다. 기본적으로 NULL - 'class' 특성이 적용되지 않습니다.

```csharp
public string InputControlsClassName { get; set; }
```

### 비고

WordProcessing 형식 계열의 거의 모든 형식에는 사용자로부터 입력 데이터를 얻을 수 있는 특정 문서 엔터티인 필드가 포함되어 있습니다. 텍스트 상자, 체크 상자, 콤보 상자, 드롭다운 목록, 버튼, 날짜/시간 선택기 등 다양한 필드가 있습니다. 입력한 사용자를 유지하면서 모든 항목이 가장 적합한 HTML 구조 및 요소로 변환됩니다. 데이터(입력 문서에 있는 경우). 특정 사용 사례에서는 전체 문서 내용을 편집하는 대신 클라이언트 측에서 입력된 데이터만 수집하면 됩니다. 이러한 경우 클라이언트 측에서 데이터와 함께 입력 컨트롤을 가져오기 위해 어떤 방식으로든 입력 컨트롤을 식별해야 합니다. 이 속성을 사용하면 HTML 마크업의 모든 입력 컨트롤에 적용되는 클래스 이름을 지정할 수 있으므로 클라이언트 코드는 HTML 문서 구조를 통과하고 데이터를 수집할 수 있습니다.

### 또한보십시오

* class [WordProcessingEditOptions](../../wordprocessingeditoptions)
* 네임스페이스 [GroupDocs.Editor.Options](../../wordprocessingeditoptions)
* 집회 [GroupDocs.Editor](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Editor.dll -->
