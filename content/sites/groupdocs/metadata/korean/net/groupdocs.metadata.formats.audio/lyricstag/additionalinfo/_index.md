---
title: AdditionalInfo
second_title: .NET API 참조용 GroupDocs.Metadata
description: 추가 정보를 가져오거나 설정합니다. 이 값은 INF 필드로 표시됩니다.
type: docs
weight: 20
url: /ko/net/groupdocs.metadata.formats.audio/lyricstag/additionalinfo/
---
## LyricsTag.AdditionalInfo property

추가 정보를 가져오거나 설정합니다. 이 값은 INF 필드로 표시됩니다.

```csharp
public string AdditionalInfo { get; set; }
```

### 자산 가치

추가 정보입니다.

### 비고

v2.00에서는 항상 세(3)자 길이지만 향후 표준에서는 더 길어질 수 있습니다. 첫 번째 바이트는 날씨를 나타내며 가사 필드가 있는지 여부를 나타냅니다. 존재하는 경우 "1", 그렇지 않은 경우 "0". 두 번째 문자는 가사에 타임스탬프가 있는지 여부를 나타냅니다. 다시 "1"은 예이고 "0"은 아니오입니다. 세 번째 문자는 무작위 선택을 위해 트랙을 금지합니다. 금지된 경우 "1", 그렇지 않은 경우 "0"입니다.

### 또한보십시오

* class [LyricsTag](../../lyricstag)
* 네임스페이스 [GroupDocs.Metadata.Formats.Audio](../../lyricstag)
* 집회 [GroupDocs.Metadata](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Metadata.dll -->
