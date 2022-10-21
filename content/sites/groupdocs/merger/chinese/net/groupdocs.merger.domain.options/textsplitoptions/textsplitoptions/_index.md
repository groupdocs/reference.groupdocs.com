---
title: TextSplitOptions
second_title: GroupDocs.Merger for .NET API 参考
description: 初始化TextSplitOptionsgroupdocs.merger.domain.options/textsplitoptions类.
type: docs
weight: 10
url: /zh/net/groupdocs.merger.domain.options/textsplitoptions/textsplitoptions/
---
## TextSplitOptions(string, int[]) {#constructor_5}

初始化[`TextSplitOptions`](../../textsplitoptions)类.

```csharp
public TextSplitOptions(string filePathFormat, int[] lineNumbers)
```

| 范围 | 类型 | 描述 |
| --- | --- | --- |
| filePathFormat | String | 已定义扩展名的文件路径格式，例如“c:/split{0}.doc”或“c:/split{0}.{1}”。 |
| lineNumbers | Int32[] | 用于文本拆分的行号。 |

### 也可以看看

* class [TextSplitOptions](../../textsplitoptions)
* 命名空间 [GroupDocs.Merger.Domain.Options](../../textsplitoptions)
* 部件 [GroupDocs.Merger](../../../)

---

## TextSplitOptions(string, TextSplitMode, int[]) {#constructor_4}

初始化[`TextSplitOptions`](../../textsplitoptions)类.

```csharp
public TextSplitOptions(string filePathFormat, TextSplitMode mode, int[] lineNumbers)
```

| 范围 | 类型 | 描述 |
| --- | --- | --- |
| filePathFormat | String | 已定义扩展名的文件路径格式，例如“c:/split{0}.doc”或“c:/split{0}.{1}”。 |
| mode | TextSplitMode | 文本拆分模式。 |
| lineNumbers | Int32[] | 用于文本拆分的行号。 |

### 也可以看看

* enum [TextSplitMode](../../textsplitmode)
* class [TextSplitOptions](../../textsplitoptions)
* 命名空间 [GroupDocs.Merger.Domain.Options](../../textsplitoptions)
* 部件 [GroupDocs.Merger](../../../)

---

## TextSplitOptions(CreateSplitStream, int[]) {#constructor_3}

初始化[`TextSplitOptions`](../../textsplitoptions)类.

```csharp
public TextSplitOptions(CreateSplitStream createSplitStream, int[] lineNumbers)
```

| 范围 | 类型 | 描述 |
| --- | --- | --- |
| createSplitStream | CreateSplitStream | 实例化用于写入输出拆分数据的流的方法。 |
| lineNumbers | Int32[] | 用于文本拆分的行号。 |

### 也可以看看

* delegate [CreateSplitStream](../../../groupdocs.merger.domain.common/createsplitstream)
* class [TextSplitOptions](../../textsplitoptions)
* 命名空间 [GroupDocs.Merger.Domain.Options](../../textsplitoptions)
* 部件 [GroupDocs.Merger](../../../)

---

## TextSplitOptions(CreateSplitStream, TextSplitMode, int[]) {#constructor_2}

初始化[`TextSplitOptions`](../../textsplitoptions)类.

```csharp
public TextSplitOptions(CreateSplitStream createSplitStream, TextSplitMode mode, int[] lineNumbers)
```

| 范围 | 类型 | 描述 |
| --- | --- | --- |
| createSplitStream | CreateSplitStream | 实例化用于写入输出拆分数据的流的方法。 |
| mode | TextSplitMode | 文本拆分模式。 |
| lineNumbers | Int32[] | 用于文本拆分的行号。 |

### 也可以看看

* delegate [CreateSplitStream](../../../groupdocs.merger.domain.common/createsplitstream)
* enum [TextSplitMode](../../textsplitmode)
* class [TextSplitOptions](../../textsplitoptions)
* 命名空间 [GroupDocs.Merger.Domain.Options](../../textsplitoptions)
* 部件 [GroupDocs.Merger](../../../)

---

## TextSplitOptions(CreateSplitStream, ReleaseSplitStream, int[]) {#constructor_1}

初始化[`TextSplitOptions`](../../textsplitoptions)类.

```csharp
public TextSplitOptions(CreateSplitStream createSplitStream, ReleaseSplitStream releaseSplitStream, 
    int[] lineNumbers)
```

| 范围 | 类型 | 描述 |
| --- | --- | --- |
| createSplitStream | CreateSplitStream | 实例化用于写入输出拆分数据的流的方法。 |
| releaseSplitStream | ReleaseSplitStream | 释放由 createPageStream 方法创建的流的方法。 |
| lineNumbers | Int32[] | 用于文本拆分的行号。 |

### 也可以看看

* delegate [CreateSplitStream](../../../groupdocs.merger.domain.common/createsplitstream)
* delegate [ReleaseSplitStream](../../../groupdocs.merger.domain.common/releasesplitstream)
* class [TextSplitOptions](../../textsplitoptions)
* 命名空间 [GroupDocs.Merger.Domain.Options](../../textsplitoptions)
* 部件 [GroupDocs.Merger](../../../)

---

## TextSplitOptions(CreateSplitStream, ReleaseSplitStream, TextSplitMode, int[]) {#constructor}

初始化[`TextSplitOptions`](../../textsplitoptions)类.

```csharp
public TextSplitOptions(CreateSplitStream createSplitStream, ReleaseSplitStream releaseSplitStream, 
    TextSplitMode mode, int[] lineNumbers)
```

| 范围 | 类型 | 描述 |
| --- | --- | --- |
| createSplitStream | CreateSplitStream | 实例化用于写入输出拆分数据的流的方法。 |
| releaseSplitStream | ReleaseSplitStream | 释放由 createPageStream 方法创建的流的方法。 |
| mode | TextSplitMode | 文本拆分模式。 |
| lineNumbers | Int32[] | 用于文本拆分的行号。 |

### 也可以看看

* delegate [CreateSplitStream](../../../groupdocs.merger.domain.common/createsplitstream)
* delegate [ReleaseSplitStream](../../../groupdocs.merger.domain.common/releasesplitstream)
* enum [TextSplitMode](../../textsplitmode)
* class [TextSplitOptions](../../textsplitoptions)
* 命名空间 [GroupDocs.Merger.Domain.Options](../../textsplitoptions)
* 部件 [GroupDocs.Merger](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Merger.dll -->