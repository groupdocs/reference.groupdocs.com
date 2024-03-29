---
title: FontSize
second_title: .NET API 참조용 GroupDocs.Editor
description: 글꼴의 크기를 지정하는 특수 단위 또는 길이 값으로 글꼴 크기를 나타냅니다이전에는 대문자 M의 너비.
type: docs
weight: 290
url: /ko/net/groupdocs.editor.htmlcss.css.properties/fontsize/
---
## FontSize structure

글꼴의 크기를 지정하는 특수 단위 또는 길이 값으로 글꼴 크기를 나타냅니다(이전에는 대문자 "M"의 너비).

```csharp
public struct FontSize : IEquatable<FontSize>
```

## 속성

| 이름 | 설명 |
| --- | --- |
| [IsAbsoluteSize](../../groupdocs.editor.htmlcss.css.properties/fontsize/isabsolutesize) { get; } | 이 font-size가 사용자의 기본 글꼴 크기(중간)를 기준으로 절대 크기를 키워드로 사용하여 정의되는지 여부를 나타냅니다. |
| [IsInitial](../../groupdocs.editor.htmlcss.css.properties/fontsize/isinitial) { get; } | 이 글꼴 크기가 초기 값(중간)인지 여부를 나타냅니다. |
| [IsLengthDefined](../../groupdocs.editor.htmlcss.css.properties/fontsize/islengthdefined) { get; } | 이 글꼴 크기가[`Length`](../../groupdocs.editor.htmlcss.css.datatypes/length) 값 |
| [IsRelativeSize](../../groupdocs.editor.htmlcss.css.properties/fontsize/isrelativesize) { get; } | 이 font-size가 상대 크기를 키워드로 정의되었는지 여부를 나타냅니다. 글꼴은 절대 크기 키워드를 구분하는 데 사용되는 대략적인 비율로 부모 요소의 글꼴 크기에 비해 크거나 작습니다. |
| [Length](../../groupdocs.editor.htmlcss.css.properties/fontsize/length) { get; } | 이 글꼴 크기가 정의된 경우 길이 값이거나 그렇지 않으면 예외가 발생했습니다 |
| [Value](../../groupdocs.editor.htmlcss.css.properties/fontsize/value) { get; } | 이 글꼴 크기의 값을 string 로 반환합니다. |

## 행동 양식

| 이름 | 설명 |
| --- | --- |
| static [FromLength](../../groupdocs.editor.htmlcss.css.properties/fontsize/fromlength)(Length) | 지정된 길이 에서 글꼴 크기를 만듭니다. |
| [Equals](../../groupdocs.editor.htmlcss.css.properties/fontsize/equals#equals)(FontSize) | 이 글꼴 크기 인스턴스가 specified 와 같은지 여부를 결정합니다. |
| override [Equals](../../groupdocs.editor.htmlcss.css.properties/fontsize/equals#equals_1)(object) | 이 글꼴 크기 인스턴스가 지정된 uncasted 와 같은지 여부를 결정합니다. |
| override [GetHashCode](../../groupdocs.editor.htmlcss.css.properties/fontsize/gethashcode)() | 이 instance 에 대한 해시 코드를 반환합니다. |
| static [TryParse](../../groupdocs.editor.htmlcss.css.properties/fontsize/tryparse)(string, out FontSize) | 지정된 키워드를 'font-size'의 적절한 키워드 값으로 인식하고 성공 시 반환하거나 실패 시 NULL을 반환합니다. |
| [operator ==](../../groupdocs.editor.htmlcss.css.properties/fontsize/op_equality) | 두 개의 "FontSize" 값이 같은지 확인합니다 |
| [operator !=](../../groupdocs.editor.htmlcss.css.properties/fontsize/op_inequality) | 두 개의 "FontSize" 값이 같지 않은지 확인합니다 |

## 필드

| 이름 | 설명 |
| --- | --- |
| static readonly [Large](../../groupdocs.editor.htmlcss.css.properties/fontsize/large) | 일반적으로 큰 절대 크기 |
| static readonly [Larger](../../groupdocs.editor.htmlcss.css.properties/fontsize/larger) | 더 큰 상대 크기 - 글꼴은 위의 절대 크기 키워드를 구분하는 데 사용되는 대략적인 비율로 상위 요소의 글꼴 크기에 상대적으로 더 커집니다. |
| static readonly [Medium](../../groupdocs.editor.htmlcss.css.properties/fontsize/medium) | 중간 크기. 초기값. |
| static readonly [Small](../../groupdocs.editor.htmlcss.css.properties/fontsize/small) | 일반적으로 작은 절대 크기 |
| static readonly [Smaller](../../groupdocs.editor.htmlcss.css.properties/fontsize/smaller) | 더 작은 상대적 크기 - 글꼴은 상위 요소의 글꼴 크기에 비해 상대적으로 더 작아지며 대략 위의 절대 크기 키워드를 구분하는 데 사용되는 비율만큼 작아집니다. |
| static readonly [XLarge](../../groupdocs.editor.htmlcss.css.properties/fontsize/xlarge) | 평범한 큰 절대 크기 |
| static readonly [XSmall](../../groupdocs.editor.htmlcss.css.properties/fontsize/xsmall) | 평범한 작은 절대 크기 |
| static readonly [XxLarge](../../groupdocs.editor.htmlcss.css.properties/fontsize/xxlarge) | 매우 큰 절대 크기 |
| static readonly [XxSmall](../../groupdocs.editor.htmlcss.css.properties/fontsize/xxsmall) | 아주 작은 절대 크기 |

### 또한보십시오

* 네임스페이스 [GroupDocs.Editor.HtmlCss.Css.Properties](../../groupdocs.editor.htmlcss.css.properties)
* 집회 [GroupDocs.Editor](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Editor.dll -->
