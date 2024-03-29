---
title: Index
second_title: GroupDocs..NET API 참조 검색
description: 의 새 인스턴스를 초기화합니다.Indexgroupdocs.search/index 메모리의 클래스.
type: docs
weight: 10
url: /ko/net/groupdocs.search/index/index/
---
## Index() {#constructor}

의 새 인스턴스를 초기화합니다.[`Index`](../../index) 메모리의 클래스.

```csharp
public Index()
```

### 예

이 예제는 파일을 디스크에 저장하지 않고 메모리에 인덱스를 만드는 방법을 보여줍니다.

```csharp
Index index = new Index(); 
```

### 또한보십시오

* class [Index](../../index)
* 네임스페이스 [GroupDocs.Search](../../index)
* 집회 [GroupDocs.Search](../../../)

---

## Index(IndexSettings) {#constructor_1}

의 새 인스턴스를 초기화합니다.[`Index`](../../index) 특정 인덱스 설정이 있는 메모리의 클래스.

```csharp
public Index(IndexSettings settings)
```

| 모수 | 유형 | 설명 |
| --- | --- | --- |
| settings | IndexSettings | 인덱스 설정 개체입니다. |

### 예

이 예는 특정 인덱스 설정으로 파일을 디스크에 저장하지 않고 메모리에 인덱스를 생성하는 방법을 보여줍니다.

```csharp
IndexSettings settings = new IndexSettings();
settings.IndexType = IndexType.CompactIndex;
Index index = new Index(settings);
```

### 또한보십시오

* class [IndexSettings](../../indexsettings)
* class [Index](../../index)
* 네임스페이스 [GroupDocs.Search](../../index)
* 집회 [GroupDocs.Search](../../../)

---

## Index(string) {#constructor_2}

의 새 인스턴스를 초기화합니다.[`Index`](../../index) class. 디스크에 새 인덱스를 생성하거나 기존 인덱스를 엽니다.

```csharp
public Index(string indexFolder)
```

| 모수 | 유형 | 설명 |
| --- | --- | --- |
| indexFolder | String | 인덱스 폴더 경로입니다. |

### 예

이 예제는 디스크에 인덱스를 생성하거나 기존 인덱스를 여는 방법을 보여줍니다.

```csharp
string indexFolder = @"c:\MyIndex\";
Index index = new Index(indexFolder); 
```

### 또한보십시오

* class [Index](../../index)
* 네임스페이스 [GroupDocs.Search](../../index)
* 집회 [GroupDocs.Search](../../../)

---

## Index(string, IndexSettings) {#constructor_4}

의 새 인스턴스를 초기화합니다.[`Index`](../../index) class. 특정 설정으로 새 인덱스를 생성하거나 디스크의 기존 인덱스를 엽니다.

```csharp
public Index(string indexFolder, IndexSettings settings)
```

| 모수 | 유형 | 설명 |
| --- | --- | --- |
| indexFolder | String | 인덱스 폴더 경로입니다. |
| settings | IndexSettings | 인덱스 설정 개체입니다. |

### 예

이 예는 특정 인덱스 설정으로 디스크에 인덱스를 만드는 방법을 보여줍니다.

```csharp
string indexFolder = @"c:\MyIndex\";
IndexSettings settings = new IndexSettings();
settings.IndexType = IndexType.CompactIndex;
Index index = new Index(indexFolder, settings);
```

### 또한보십시오

* class [IndexSettings](../../indexsettings)
* class [Index](../../index)
* 네임스페이스 [GroupDocs.Search](../../index)
* 집회 [GroupDocs.Search](../../../)

---

## Index(string, bool) {#constructor_3}

의 새 인스턴스를 초기화합니다.[`Index`](../../index) class. 다음과 같은 경우 디스크에서 기존 인덱스를 로드합니다.*overwriteIfExists* ~이다`거짓`; 그렇지 않으면 디스크에 새 인덱스를 생성합니다.

```csharp
public Index(string indexFolder, bool overwriteIfExists)
```

| 모수 | 유형 | 설명 |
| --- | --- | --- |
| indexFolder | String | 인덱스 폴더 경로입니다. |
| overwriteIfExists | Boolean | 색인 폴더를 덮어쓰는 플래그입니다. |

### 예

이 예는 이미 다른 색인이 포함된 폴더에 새 색인을 만드는 방법을 보여줍니다.

```csharp
string indexFolder = @"c:\MyIndex\";
Index index = new Index(indexFolder, true);
```

### 또한보십시오

* class [Index](../../index)
* 네임스페이스 [GroupDocs.Search](../../index)
* 집회 [GroupDocs.Search](../../../)

---

## Index(string, IndexSettings, bool) {#constructor_5}

의 새 인스턴스를 초기화합니다.[`Index`](../../index) class. 다음과 같은 경우 디스크에서 기존 인덱스를 로드합니다.*overwriteIfExists* ~이다`거짓` ; 그렇지 않으면 특정 색인 설정으로 디스크에 새 색인을 생성합니다.

```csharp
public Index(string indexFolder, IndexSettings settings, bool overwriteIfExists)
```

| 모수 | 유형 | 설명 |
| --- | --- | --- |
| indexFolder | String | 인덱스 폴더 경로입니다. |
| settings | IndexSettings | 인덱스 설정 개체입니다. |
| overwriteIfExists | Boolean | 색인 폴더를 덮어쓰는 플래그입니다. |

### 예

이 예는 특정 인덱스 설정으로 디스크에 인덱스를 만드는 방법을 보여줍니다.

```csharp
string indexFolder = @"c:\MyIndex\";
IndexSettings settings = new IndexSettings();
settings.IndexType = IndexType.CompactIndex;
Index index = new Index(indexFolder, settings, true);
```

### 또한보십시오

* class [IndexSettings](../../indexsettings)
* class [Index](../../index)
* 네임스페이스 [GroupDocs.Search](../../index)
* 집회 [GroupDocs.Search](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Search.dll -->
