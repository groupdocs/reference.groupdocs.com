---
title: Redactor
second_title: .NET API 참조용 GroupDocs.Redaction
description: 의 새 인스턴스를 초기화합니다.Redactorgroupdocs.redaction/redactor 파일 경로를 사용하는 클래스.
type: docs
weight: 10
url: /ko/net/groupdocs.redaction/redactor/redactor/
---
## Redactor(string) {#constructor_3}

의 새 인스턴스를 초기화합니다.[`Redactor`](../../redactor) 파일 경로를 사용하는 클래스.

```csharp
public Redactor(string filePath)
```

| 모수 | 유형 | 설명 |
| --- | --- | --- |
| filePath | String | 파일 경로 |

### 예

다음 예제는 교정을 위해 문서를 여는 방법을 보여줍니다.

```csharp
using (Redactor redactor = new Redactor(@"C:\sample.pdf"))
{
    // 여기에서 문서 인스턴스를 사용하여 교정을 수행할 수 있습니다.
}
```

### 또한보십시오

* class [Redactor](../../redactor)
* 네임스페이스 [GroupDocs.Redaction](../../redactor)
* 집회 [GroupDocs.Redaction](../../../)

---

## Redactor(Stream) {#constructor}

의 새 인스턴스를 초기화합니다.[`Redactor`](../../redactor) stream. 를 사용하는 클래스

```csharp
public Redactor(Stream document)
```

| 모수 | 유형 | 설명 |
| --- | --- | --- |
| document | Stream | 문서의 소스 스트림 |

### 예

다음 예제는 stream. 에서 문서를 여는 방법을 보여줍니다.

```csharp
using (Stream stream = File.Open(@"C:\\sample.pdf", FileMode.Open, FileAccess.ReadWrite))
{
    using (Redactor redactor = new Redactor(stream))
    {
        // 여기에서 문서 인스턴스를 사용하여 교정을 수행할 수 있습니다.
    }
}
```

### 또한보십시오

* class [Redactor](../../redactor)
* 네임스페이스 [GroupDocs.Redaction](../../redactor)
* 집회 [GroupDocs.Redaction](../../../)

---

## Redactor(string, LoadOptions) {#constructor_4}

의 새 인스턴스를 초기화합니다.[`Redactor`](../../redactor) path. 를 사용하는 암호로 보호된 문서의 클래스

```csharp
public Redactor(string filePath, LoadOptions loadOptions)
```

| 모수 | 유형 | 설명 |
| --- | --- | --- |
| filePath | String | 파일 경로. |
| loadOptions | LoadOptions | 비밀번호를 포함한 옵션. |

### 또한보십시오

* class [LoadOptions](../../../groupdocs.redaction.options/loadoptions)
* class [Redactor](../../redactor)
* 네임스페이스 [GroupDocs.Redaction](../../redactor)
* 집회 [GroupDocs.Redaction](../../../)

---

## Redactor(string, LoadOptions, RedactorSettings) {#constructor_5}

의 새 인스턴스를 초기화합니다.[`Redactor`](../../redactor) 경로와 설정을 사용하여 암호로 보호된 문서의 클래스.

```csharp
public Redactor(string filePath, LoadOptions loadOptions, RedactorSettings settings)
```

| 모수 | 유형 | 설명 |
| --- | --- | --- |
| filePath | String | 파일 경로. |
| loadOptions | LoadOptions | 암호를 포함한 파일 종속 옵션. |
| settings | RedactorSettings | 교정 프로세스의 기본 설정입니다. |

### 또한보십시오

* class [LoadOptions](../../../groupdocs.redaction.options/loadoptions)
* class [RedactorSettings](../../../groupdocs.redaction.options/redactorsettings)
* class [Redactor](../../redactor)
* 네임스페이스 [GroupDocs.Redaction](../../redactor)
* 집회 [GroupDocs.Redaction](../../../)

---

## Redactor(Stream, LoadOptions) {#constructor_1}

의 새 인스턴스를 초기화합니다.[`Redactor`](../../redactor) stream. 를 사용하는 암호로 보호된 문서의 클래스

```csharp
public Redactor(Stream document, LoadOptions loadOptions)
```

| 모수 | 유형 | 설명 |
| --- | --- | --- |
| document | Stream | 소스 입력 스트림. |
| loadOptions | LoadOptions | 비밀번호를 포함한 옵션. |

### 예

다음 예제에서는 LoadOptions를 사용하여 암호로 보호된 문서를 여는 방법을 보여줍니다.

```csharp
LoadOptions loadOptions = new LoadOptions("mypassword");
using (Redactor redactor = new Redactor(@"C:\sample.pdf", loadOptions))
{
    // 여기에서 문서 인스턴스를 사용하여 교정을 수행할 수 있습니다.
}
```

### 또한보십시오

* class [LoadOptions](../../../groupdocs.redaction.options/loadoptions)
* class [Redactor](../../redactor)
* 네임스페이스 [GroupDocs.Redaction](../../redactor)
* 집회 [GroupDocs.Redaction](../../../)

---

## Redactor(Stream, LoadOptions, RedactorSettings) {#constructor_2}

의 새 인스턴스를 초기화합니다.[`Redactor`](../../redactor)스트림 및 설정을 사용하여 암호로 보호된 문서에 대한 클래스입니다.

```csharp
public Redactor(Stream document, LoadOptions loadOptions, RedactorSettings settings)
```

| 모수 | 유형 | 설명 |
| --- | --- | --- |
| document | Stream | 소스 입력 스트림. |
| loadOptions | LoadOptions | 비밀번호를 포함한 옵션. |
| settings | RedactorSettings | 교정 프로세스의 기본 설정입니다. |

### 예

다음 예제에서는 LoadOptions를 사용하여 암호로 보호된 문서를 여는 방법을 보여줍니다.

```csharp
LoadOptions loadOptions = new LoadOptions("mypassword");
using (Redactor redactor = new Redactor(@"C:\sample.pdf", loadOptions))
{
    // 여기에서 문서 인스턴스를 사용하여 교정을 수행할 수 있습니다.
}
```

### 또한보십시오

* class [LoadOptions](../../../groupdocs.redaction.options/loadoptions)
* class [RedactorSettings](../../../groupdocs.redaction.options/redactorsettings)
* class [Redactor](../../redactor)
* 네임스페이스 [GroupDocs.Redaction](../../redactor)
* 집회 [GroupDocs.Redaction](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Redaction.dll -->
