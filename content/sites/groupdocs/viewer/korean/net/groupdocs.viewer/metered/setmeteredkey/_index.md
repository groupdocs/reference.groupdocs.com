---
title: SetMeteredKey
second_title: .NET API 참조용 GroupDocs.Viewer
description: 측정된 키로 제품을 활성화합니다.
type: docs
weight: 20
url: /ko/net/groupdocs.viewer/metered/setmeteredkey/
---
## Metered.SetMeteredKey method

측정된 키로 제품을 활성화합니다.

```csharp
public void SetMeteredKey(string publicKey, string privateKey)
```

| 모수 | 유형 | 설명 |
| --- | --- | --- |
| publicKey | String | 공개 키입니다. |
| privateKey | String | 개인 키입니다. |

### 예

다음 예는 측정된 키로 제품을 활성화하는 방법을 보여줍니다.

```csharp
string publicKey = "Public Key";
string privateKey = "Private Key";

Metered metered = new Metered();
metered.SetMeteredKey(publicKey, privateKey);
```

### 또한보십시오

* class [Metered](../../metered)
* 네임스페이스 [GroupDocs.Viewer](../../metered)
* 집회 [GroupDocs.Viewer](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Viewer.dll -->
