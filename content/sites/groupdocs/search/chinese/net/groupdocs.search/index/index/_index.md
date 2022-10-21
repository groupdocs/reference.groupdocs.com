---
title: Index
second_title: GroupDocs.Search for .NET API 参考
description: 初始化Indexgroupdocs.search/index内存中的类
type: docs
weight: 10
url: /zh/net/groupdocs.search/index/index/
---
## Index() {#constructor}

初始化[`Index`](../../index)内存中的类。

```csharp
public Index()
```

### 例子

该示例演示了如何在内存中创建索引而不将文件保存到磁盘。

```csharp
Index index = new Index(); 
```

### 也可以看看

* class [Index](../../index)
* 命名空间 [GroupDocs.Search](../../index)
* 部件 [GroupDocs.Search](../../../)

---

## Index(IndexSettings) {#constructor_1}

初始化[`Index`](../../index)具有特定索引设置的内存类。

```csharp
public Index(IndexSettings settings)
```

| 范围 | 类型 | 描述 |
| --- | --- | --- |
| settings | IndexSettings | 索引设置对象。 |

### 例子

该示例演示了如何在内存中创建索引，而不使用特定索引设置将文件保存到磁盘。

```csharp
IndexSettings settings = new IndexSettings();
settings.IndexType = IndexType.CompactIndex;
Index index = new Index(settings);
```

### 也可以看看

* class [IndexSettings](../../indexsettings)
* class [Index](../../index)
* 命名空间 [GroupDocs.Search](../../index)
* 部件 [GroupDocs.Search](../../../)

---

## Index(string) {#constructor_2}

初始化[`Index`](../../index) class. 在磁盘上创建新索引或打开现有索引。

```csharp
public Index(string indexFolder)
```

| 范围 | 类型 | 描述 |
| --- | --- | --- |
| indexFolder | String | 索引文件夹路径。 |

### 例子

该示例演示如何在磁盘上创建索引或打开现有索引。

```csharp
string indexFolder = @"c:\MyIndex\";
Index index = new Index(indexFolder); 
```

### 也可以看看

* class [Index](../../index)
* 命名空间 [GroupDocs.Search](../../index)
* 部件 [GroupDocs.Search](../../../)

---

## Index(string, IndexSettings) {#constructor_4}

初始化[`Index`](../../index) class. 使用特定设置创建新索引或打开磁盘上的现有索引。

```csharp
public Index(string indexFolder, IndexSettings settings)
```

| 范围 | 类型 | 描述 |
| --- | --- | --- |
| indexFolder | String | 索引文件夹路径。 |
| settings | IndexSettings | 索引设置对象。 |

### 例子

该示例演示了如何在具有特定索引设置的磁盘上创建索引。

```csharp
string indexFolder = @"c:\MyIndex\";
IndexSettings settings = new IndexSettings();
settings.IndexType = IndexType.CompactIndex;
Index index = new Index(indexFolder, settings);
```

### 也可以看看

* class [IndexSettings](../../indexsettings)
* class [Index](../../index)
* 命名空间 [GroupDocs.Search](../../index)
* 部件 [GroupDocs.Search](../../../)

---

## Index(string, bool) {#constructor_3}

初始化[`Index`](../../index) class. 从磁盘加载现有索引，如果*overwriteIfExists*是`错误的`; 否则在磁盘上创建一个新索引。

```csharp
public Index(string indexFolder, bool overwriteIfExists)
```

| 范围 | 类型 | 描述 |
| --- | --- | --- |
| indexFolder | String | 索引文件夹路径。 |
| overwriteIfExists | Boolean | 覆盖索引文件夹的标志。 |

### 例子

该示例演示了如何在已包含另一个索引的文件夹中创建新索引。

```csharp
string indexFolder = @"c:\MyIndex\";
Index index = new Index(indexFolder, true);
```

### 也可以看看

* class [Index](../../index)
* 命名空间 [GroupDocs.Search](../../index)
* 部件 [GroupDocs.Search](../../../)

---

## Index(string, IndexSettings, bool) {#constructor_5}

初始化[`Index`](../../index) class. 从磁盘加载现有索引，如果*overwriteIfExists*是`错误的` ; 在磁盘上创建一个具有特定索引设置的新索引。

```csharp
public Index(string indexFolder, IndexSettings settings, bool overwriteIfExists)
```

| 范围 | 类型 | 描述 |
| --- | --- | --- |
| indexFolder | String | 索引文件夹路径。 |
| settings | IndexSettings | 索引设置对象。 |
| overwriteIfExists | Boolean | 覆盖索引文件夹的标志。 |

### 例子

该示例演示了如何在具有特定索引设置的磁盘上创建索引。

```csharp
string indexFolder = @"c:\MyIndex\";
IndexSettings settings = new IndexSettings();
settings.IndexType = IndexType.CompactIndex;
Index index = new Index(indexFolder, settings, true);
```

### 也可以看看

* class [IndexSettings](../../indexsettings)
* class [Index](../../index)
* 命名空间 [GroupDocs.Search](../../index)
* 部件 [GroupDocs.Search](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Search.dll -->