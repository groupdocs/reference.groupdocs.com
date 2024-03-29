---
title: ConvertOptions
second_title: .NET API 참조용 GroupDocs.Conversion
description: 일반 변환 옵션 클래스.
type: docs
weight: 1460
url: /ko/net/groupdocs.conversion.options.convert/convertoptions/
---
## ConvertOptions class

일반 변환 옵션 클래스.

```csharp
public abstract class ConvertOptions : ValueObject, ICloneable, IConvertOptions
```

## 속성

| 이름 | 설명 |
| --- | --- |
| virtual [Format](../../groupdocs.conversion.options.convert/convertoptions/format) { get; set; } | 입력 문서를 변환해야 하는 원하는 파일 형식입니다. |

## 행동 양식

| 이름 | 설명 |
| --- | --- |
| [Clone](../../groupdocs.conversion.options.convert/convertoptions/clone)() | 현재 옵션 인스턴스를 복제합니다. |
| override [Equals](../../groupdocs.conversion.contracts/valueobject/equals)(object) | 두 개체 인스턴스가 같은지 여부를 결정합니다. |
| virtual [Equals](../../groupdocs.conversion.contracts/valueobject/equals)(ValueObject) | 두 개체 인스턴스가 같은지 여부를 결정합니다. |
| override [GetHashCode](../../groupdocs.conversion.contracts/valueobject/gethashcode)() | 기본 해시 함수 역할을 합니다. |

### 또한보십시오

* class [ValueObject](../../groupdocs.conversion.contracts/valueobject)
* interface [IConvertOptions](../iconvertoptions)
* 네임스페이스 [GroupDocs.Conversion.Options.Convert](../../groupdocs.conversion.options.convert)
* 집회 [GroupDocs.Conversion](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Conversion.dll -->
