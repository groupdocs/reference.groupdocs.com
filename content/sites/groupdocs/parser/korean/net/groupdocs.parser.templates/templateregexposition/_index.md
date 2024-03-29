---
title: TemplateRegexPosition
second_title: .NET API 참조용 GroupDocs.Parser
description: 정규식을 사용하는 템플릿 필드 위치를 제공합니다.
type: docs
weight: 730
url: /ko/net/groupdocs.parser.templates/templateregexposition/
---
## TemplateRegexPosition class

정규식을 사용하는 템플릿 필드 위치를 제공합니다.

```csharp
public sealed class TemplateRegexPosition : TemplatePosition
```

## 생성자

| 이름 | 설명 |
| --- | --- |
| [TemplateRegexPosition](templateregexposition#constructor)(string) | 의 새 인스턴스를 초기화합니다.[`TemplateRegexPosition`](../templateregexposition) 클래스. |
| [TemplateRegexPosition](templateregexposition#constructor_1)(string, bool) | 의 새 인스턴스를 초기화합니다.[`TemplateRegexPosition`](../templateregexposition) 클래스. |

## 속성

| 이름 | 설명 |
| --- | --- |
| [Expression](../../groupdocs.parser.templates/templateregexposition/expression) { get; } | 정규식을 가져옵니다. |
| [MatchCase](../../groupdocs.parser.templates/templateregexposition/matchcase) { get; } | 텍스트 대소문자가 무시되지 않는지 여부를 나타내는 값을 가져옵니다. |

### 예

다음 예는 문서에 "송장 번호 INV-12345"가 포함된 상황 를 보여 주며 템플릿 필드는 다음과 같은 방식으로 정의할 수 있습니다.

이 경우 전체 문자열이 값으로 추출됩니다. 문자열의 일부만 추출하려면 정규식 그룹 "값"이 사용됩니다.

이 경우 값으로 "INV-3337" 문자열이 추출됩니다.

```csharp
// "InvoiceNumber" 이름으로 정규식 템플릿 필드 생성
TemplateField templateField = new TemplateField(
    new TemplateRegexPosition("Invoice Number\\s+[A-Z0-9\\-]+"),
    "InvoiceNumber");
```

```csharp
// "value" 그룹이 있는 "InvoiceNumber" 이름의 정규식 템플릿 필드를 만듭니다.
TemplateField templateField = new TemplateField(
    new TemplateRegexPosition("Invoice Number\\s+(?<value>[A-Z0-9\\-]+)"),
    "InvoiceNumber");
```

### 또한보십시오

* class [TemplatePosition](../templateposition)
* 네임스페이스 [GroupDocs.Parser.Templates](../../groupdocs.parser.templates)
* 집회 [GroupDocs.Parser](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Parser.dll -->
