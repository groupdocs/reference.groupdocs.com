---
title: GetBarcodes
second_title: GroupDocs.Parser for .NET API 参考
description: 从文档中提取条形码
type: docs
weight: 50
url: /zh/net/groupdocs.parser/parser/getbarcodes/
---
## GetBarcodes() {#getbarcodes}

从文档中提取条形码。

```csharp
public IEnumerable<PageBarcodeArea> GetBarcodes()
```

### 返回值

集合[`PageBarcodeArea`](../../../groupdocs.parser.data/pagebarcodearea)对象; `无效的`如果不支持条形码提取。

### 例子

以下示例显示如何从文档中提取条形码：

```csharp
// 创建 Parser 类的实例
using (Parser parser = new Parser(filePath))
{
    // 从文档中提取条形码。
    IEnumerable<PageBarcodeArea> barcodes = parser.GetBarcodes();

    // 遍历条码
    foreach(PageBarcodeArea barcode in barcodes)
    {
        // 打印页面索引
        Console.WriteLine("Page: " + barcode.Page.Index.ToString());
        // 打印条码值
        Console.WriteLine("Value: " + barcode.Value);
    }
}
```

### 也可以看看

* class [PageBarcodeArea](../../../groupdocs.parser.data/pagebarcodearea)
* class [Parser](../../parser)
* 命名空间 [GroupDocs.Parser](../../parser)
* 部件 [GroupDocs.Parser](../../../)

---

## GetBarcodes(int) {#getbarcodes_2}

从文档页面中提取条形码。

```csharp
public IEnumerable<PageBarcodeArea> GetBarcodes(int pageIndex)
```

| 范围 | 类型 | 描述 |
| --- | --- | --- |
| pageIndex | Int32 | 从零开始的页面索引。 |

### 返回值

集合[`PageBarcodeArea`](../../../groupdocs.parser.data/pagebarcodearea)对象; `无效的`如果不支持条形码提取。

### 例子

以下示例显示如何从文档页面中提取条形码：

```csharp
// 创建 Parser 类的实例
using (Parser parser = new Parser(filePath))
{
    // 从第二个文档页面中提取条形码。
    IEnumerable<PageBarcodeArea> barcodes = parser.GetBarcodes(1);

    // 遍历条码
    foreach(PageBarcodeArea barcode in barcodes)
    {
        // 打印页面索引
        Console.WriteLine("Page: " + barcode.Page.Index.ToString());
        // 打印条码值
        Console.WriteLine("Value: " + barcode.Value);
    }
}
```

### 也可以看看

* class [PageBarcodeArea](../../../groupdocs.parser.data/pagebarcodearea)
* class [Parser](../../parser)
* 命名空间 [GroupDocs.Parser](../../parser)
* 部件 [GroupDocs.Parser](../../../)

---

## GetBarcodes(PageAreaOptions) {#getbarcodes_1}

使用自定义选项 从文档中提取条形码（设置包含条形码的矩形区域）。

```csharp
public IEnumerable<PageBarcodeArea> GetBarcodes(PageAreaOptions options)
```

| 范围 | 类型 | 描述 |
| --- | --- | --- |
| options | PageAreaOptions | 条码提取的选项。 |

### 返回值

集合[`PageBarcodeArea`](../../../groupdocs.parser.data/pagebarcodearea)对象; `无效的`如果不支持条形码提取。

### 例子

以下示例显示如何从右上角提取条形码。

```csharp
// 创建 Parser 类的实例
using (Parser parser = new Parser(filePath))
{
    // 创建用于条码提取的选项
    PageAreaOptions options = new PageAreaOptions(new Rectangle(new Point(590, 80), new Size(150, 150)));
    // 从右上角提取条形码。
    IEnumerable<PageBarcodeArea> barcodes = parser.GetBarcodes(options);

    // 遍历条码
    foreach (PageBarcodeArea barcode in barcodes)
    {
        // 打印页面索引
        Console.WriteLine("Page: " + barcode.Page.Index.ToString());
        // 打印条码值
        Console.WriteLine("Value: " + barcode.Value);
    }
}
```

### 也可以看看

* class [PageBarcodeArea](../../../groupdocs.parser.data/pagebarcodearea)
* class [PageAreaOptions](../../../groupdocs.parser.options/pageareaoptions)
* class [Parser](../../parser)
* 命名空间 [GroupDocs.Parser](../../parser)
* 部件 [GroupDocs.Parser](../../../)

---

## GetBarcodes(int, PageAreaOptions) {#getbarcodes_3}

使用自定义选项 （设置包含条形码的矩形区域）从文档页面中提取条形码。

```csharp
public IEnumerable<PageBarcodeArea> GetBarcodes(int pageIndex, PageAreaOptions options)
```

| 范围 | 类型 | 描述 |
| --- | --- | --- |
| pageIndex | Int32 | 从零开始的页面索引。 |
| options | PageAreaOptions | 条码提取的选项。 |

### 返回值

集合[`PageBarcodeArea`](../../../groupdocs.parser.data/pagebarcodearea)对象; `无效的`如果不支持条形码提取。

### 也可以看看

* class [PageBarcodeArea](../../../groupdocs.parser.data/pagebarcodearea)
* class [PageAreaOptions](../../../groupdocs.parser.options/pageareaoptions)
* class [Parser](../../parser)
* 命名空间 [GroupDocs.Parser](../../parser)
* 部件 [GroupDocs.Parser](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Parser.dll -->