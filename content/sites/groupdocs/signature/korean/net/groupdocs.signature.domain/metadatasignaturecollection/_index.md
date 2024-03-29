---
title: MetadataSignatureCollection
second_title: .NET API 참조용 GroupDocs.Signature
description: 메타데이터 서명 개체 모음입니다.
type: docs
weight: 620
url: /ko/net/groupdocs.signature.domain/metadatasignaturecollection/
---
## MetadataSignatureCollection class

메타데이터 서명 개체 모음입니다.

```csharp
public class MetadataSignatureCollection : ICloneable, IEnumerable<MetadataSignature>
```

## 생성자

| 이름 | 설명 |
| --- | --- |
| [MetadataSignatureCollection](metadatasignaturecollection)() | 메타데이터 서명 컬렉션을 생성합니다. |

## 속성

| 이름 | 설명 |
| --- | --- |
| [Count](../../groupdocs.signature.domain/metadatasignaturecollection/count) { get; } | 컬렉션의 항목 수를 가져옵니다. |
| [Item](../../groupdocs.signature.domain/metadatasignaturecollection/item) { get; } | 속성 이름으로 MetadataSignature 개체를 반환합니다. (2 indexers) |

## 행동 양식

| 이름 | 설명 |
| --- | --- |
| [Add](../../groupdocs.signature.domain/metadatasignaturecollection/add)(MetadataSignature) | 컬렉션에 메타데이터 서명 개체를 추가합니다. |
| [AddRange](../../groupdocs.signature.domain/metadatasignaturecollection/addrange)(IEnumerable&lt;MetadataSignature&gt;) | 메타데이터 서명 컬렉션을 추가합니다. |
| [Clear](../../groupdocs.signature.domain/metadatasignaturecollection/clear)() | 컬렉션에서 모든 항목을 제거합니다. |
| [Clone](../../groupdocs.signature.domain/metadatasignaturecollection/clone)() | 메타데이터 서명 항목이 있는 복제 메타데이터 서명 컬렉션 클래스. |
| [Contains](../../groupdocs.signature.domain/metadatasignaturecollection/contains)(string) | 지정한 이름의 메타데이터가 컬렉션에 있으면 true를 반환합니다. |
| [GetEnumerator](../../groupdocs.signature.domain/metadatasignaturecollection/getenumerator)() | 열거자를 반환합니다. |
| [IndexOf](../../groupdocs.signature.domain/metadatasignaturecollection/indexof)(string) | 이름으로 속성의 인덱스를 가져옵니다. |
| [Remove](../../groupdocs.signature.domain/metadatasignaturecollection/remove)(string) | 컬렉션에서 지정된 이름을 가진 메타데이터 서명을 제거합니다. |
| [RemoveAt](../../groupdocs.signature.domain/metadatasignaturecollection/removeat)(int) | 지정된 인덱스에서 메타데이터 서명을 제거합니다. |

### 또한보십시오

* class [MetadataSignature](../metadatasignature)
* 네임스페이스 [GroupDocs.Signature.Domain](../../groupdocs.signature.domain)
* 집회 [GroupDocs.Signature](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Signature.dll -->
