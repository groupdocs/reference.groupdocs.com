---
title: License
second_title: .NET API 참조용 GroupDocs.Redaction
description: 라이선스 적용 방법을 제공합니다.
type: docs
weight: 260
url: /ko/net/groupdocs.redaction/license/
---
## License class

라이선스 적용 방법을 제공합니다.

```csharp
public class License
```

## 생성자

| 이름 | 설명 |
| --- | --- |
| [License](license)() | 라이선스 클래스의 인스턴스를 초기화합니다. |

## 행동 양식

| 이름 | 설명 |
| --- | --- |
| [SetLicense](../../groupdocs.redaction/license/setlicense#setlicense)(Stream) | 스트림에서 GroupDocs.Redaction 라이선스를 설정합니다. |
| [SetLicense](../../groupdocs.redaction/license/setlicense#setlicense_1)(string) | 파일 경로에서 GroupDocs.Redaction 라이센스를 설정합니다. |

### 비고

**더 알아보기**

* 라이선스에 대한 추가 정보: [GroupDocs 라이센스 FAQ](https://purchase.groupdocs.com/faqs/licensing)
* 추가 정보**GroupDocs.Redaction** 라이선스: [평가 제한 및 라이선스](https://docs.groupdocs.com/redaction/net/evaluation-limitations-and-licensing/)

### 예

다음 예는 GroupDocs.Redaction. 에 대한 라이센스를 설정하는 방법을 보여줍니다.

```csharp
GroupDocs.Redaction.License license = new GroupDocs.Redaction.License();
// 대안으로 스트림을 사용할 수 있습니다.
license.SetLicense(licensePath);
```

### 또한보십시오

* 네임스페이스 [GroupDocs.Redaction](../../groupdocs.redaction)
* 집회 [GroupDocs.Redaction](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Redaction.dll -->
