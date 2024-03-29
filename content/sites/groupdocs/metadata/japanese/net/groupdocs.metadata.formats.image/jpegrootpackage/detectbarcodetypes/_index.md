---
title: DetectBarcodeTypes
second_title: GroupDocs.Metadata for .NET API リファレンス
description: 画像に表示されているバーコードの種類を抽出します
type: docs
weight: 60
url: /ja/net/groupdocs.metadata.formats.image/jpegrootpackage/detectbarcodetypes/
---
## JpegRootPackage.DetectBarcodeTypes method

画像に表示されているバーコードの種類を抽出します。

```csharp
public string[] DetectBarcodeTypes()
```

### 戻り値

バーコード タイプの配列。

### 備考

**もっと詳しく知る**

* [JPEG 画像のメタデータの操作](https://docs.groupdocs.com/display/metadatanet/Working+with+metadata+in+JPEG+images)

### 例

このコード スニペットは、JPEG 画像内のバーコードを検出する方法を示しています。

```csharp
using (Metadata metadata = new Metadata(Constants.JpegWithBarcodes))
{
    var root = metadata.GetRootPackage<JpegRootPackage>();

    var barcodeTypes = root.DetectBarcodeTypes();

    foreach (var barcodeType in barcodeTypes)
    {
        Console.WriteLine(barcodeType);
    }
}
```

### 関連項目

* class [JpegRootPackage](../../jpegrootpackage)
* 名前空間 [GroupDocs.Metadata.Formats.Image](../../jpegrootpackage)
* 組み立て [GroupDocs.Metadata](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Metadata.dll -->
