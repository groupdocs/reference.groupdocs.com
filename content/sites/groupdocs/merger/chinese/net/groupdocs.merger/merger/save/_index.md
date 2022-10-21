---
title: Save
second_title: GroupDocs.Merger for .NET API 参考
description: 将结果文档保存到流中document.
type: docs
weight: 150
url: /zh/net/groupdocs.merger/merger/save/
---
## Save(Stream) {#save}

将结果文档保存到流中*document*.

```csharp
public void Save(Stream document)
```

| 范围 | 类型 | 描述 |
| --- | --- | --- |
| document | Stream | 文档流。 |

### 例外

| 例外 | （健康）状况 |
| --- | --- |
| ArgumentNullException | 何时抛出*document*一片空白。 |

### 也可以看看

* class [Merger](../../merger)
* 命名空间 [GroupDocs.Merger](../../merger)
* 部件 [GroupDocs.Merger](../../../)

---

## Save(string) {#save_1}

将结果文档文件保存到*filePath*.

```csharp
public void Save(string filePath)
```

| 范围 | 类型 | 描述 |
| --- | --- | --- |
| filePath | String | 文件名或完整文件路径。 |

### 例外

| 例外 | （健康）状况 |
| --- | --- |
| ArgumentNullException | 何时抛出*filePath*为空或为空。 |

### 也可以看看

* class [Merger](../../merger)
* 命名空间 [GroupDocs.Merger](../../merger)
* 部件 [GroupDocs.Merger](../../../)

---

## Save(string, bool) {#save_2}

将结果文档文件保存到*filePath*.

```csharp
public void Save(string filePath, bool useDefaultDirectory)
```

| 范围 | 类型 | 描述 |
| --- | --- | --- |
| filePath | String | 默认目录使用情况下的文件路径或名称。 |
| useDefaultDirectory | Boolean | 使用设置中的默认目录。 |

### 例外

| 例外 | （健康）状况 |
| --- | --- |
| ArgumentNullException | 何时抛出*filePath*为空或为空。 |

### 也可以看看

* class [Merger](../../merger)
* 命名空间 [GroupDocs.Merger](../../merger)
* 部件 [GroupDocs.Merger](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Merger.dll -->