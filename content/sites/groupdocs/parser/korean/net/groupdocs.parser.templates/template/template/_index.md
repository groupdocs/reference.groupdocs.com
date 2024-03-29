---
title: Template
second_title: .NET API 참조용 GroupDocs.Parser
description: 의 새 인스턴스를 초기화합니다.Templategroupdocs.parser.templates/template 클래스.
type: docs
weight: 10
url: /ko/net/groupdocs.parser.templates/template/template/
---
## Template constructor

의 새 인스턴스를 초기화합니다.[`Template`](../../template) 클래스.

```csharp
public Template(IEnumerable<TemplateItem> items)
```

| 모수 | 유형 | 설명 |
| --- | --- | --- |
| items | IEnumerable`1 | 컬렉션[`TemplateItem`](../../templateitem)사물. |

### 예

용법:

```csharp
// 템플릿 필드의 배열 생성
TemplateItem[] fields = new TemplateItem[]
{
   new TemplateField(new TemplateRegexPosition("From"), "From", 0),
   new TemplateField(
       new TemplateLinkedPosition("From", new Size(100, 10), new TemplateLinkedPositionEdges(false, false, false, true)),
       "FromCompany",
       0),
   new TemplateField(
       new TemplateLinkedPosition("FromCompany", new Size(100, 30), new TemplateLinkedPositionEdges(false, false, false, true)),
       "FromAddress",
       0)
};

// 문서 템플릿 생성
Template template = new Template(fields);
```

### 또한보십시오

* class [TemplateItem](../../templateitem)
* class [Template](../../template)
* 네임스페이스 [GroupDocs.Parser.Templates](../../template)
* 집회 [GroupDocs.Parser](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Parser.dll -->
