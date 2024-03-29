---
title: VerificationResult
second_title: .NET API 참조용 GroupDocs.Signature
description: 검증 프로세스 결과를 보관할 인스턴스입니다.
type: docs
weight: 1050
url: /ko/net/groupdocs.signature.domain/verificationresult/
---
## VerificationResult class

검증 프로세스 결과를 보관할 인스턴스입니다.

```csharp
public class VerificationResult : IResult
```

## 속성

| 이름 | 설명 |
| --- | --- |
| [DestinDocumentSize](../../groupdocs.signature.domain/verificationresult/destindocumentsize) { get; } | 대상 문서 크기를 반환합니다. 확인을 위해 이 변수는 항상 0을 포함합니다. |
| [IsValid](../../groupdocs.signature.domain/verificationresult/isvalid) { get; } | 확인 프로세스가 성공적이면 true를 반환하고 그렇지 않으면 false를 반환합니다. |
| [ProcessingTime](../../groupdocs.signature.domain/verificationresult/processingtime) { get; } | 프로세스의 실행 시간을 밀리초 단위로 반환합니다. |
| [SourceDocumentSize](../../groupdocs.signature.domain/verificationresult/sourcedocumentsize) { get; } | 소스 문서 크기를 바이트 단위로 반환합니다. |
| [Succeeded](../../groupdocs.signature.domain/verificationresult/succeeded) { get; } | 성공적으로 확인된 서명 목록[`BaseSignature`](../basesignature) . |
| [TotalSignatures](../../groupdocs.signature.domain/verificationresult/totalsignatures) { get; } | 처리된 총 서명을 반환합니다 |

### 또한보십시오

* interface [IResult](../iresult)
* 네임스페이스 [GroupDocs.Signature.Domain](../../groupdocs.signature.domain)
* 집회 [GroupDocs.Signature](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Signature.dll -->
