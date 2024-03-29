---
title: GetRootPackage
second_title: GroupDocs.Metadata for .NET API リファレンス
description: ファイルから抽出されたすべてのメタデータ プロパティへのアクセスを提供するルート パッケージを取得します
type: docs
weight: 80
url: /ja/net/groupdocs.metadata/metadata/getrootpackage/
---
## GetRootPackage() {#getrootpackage}

ファイルから抽出されたすべてのメタデータ プロパティへのアクセスを提供するルート パッケージを取得します。

```csharp
public RootMetadataPackage GetRootPackage()
```

### 戻り値

ファイルから抽出されたすべてのメタデータ プロパティへのアクセスを提供するルート パッケージ。

### 備考

**もっと詳しく知る**

* [メタデータ ツリー全体をトラバースする](https://docs.groupdocs.com/display/metadatanet/Traverse+a+whole+metadata+tree)

### 例

この例では、形式に関係なく、特定のファイルのメタデータ ツリー全体をトラバースする方法を示します。

```csharp
public static void Run()
{
    using (Metadata metadata = new Metadata(Constants.JpegWithXmp))
    {
        DisplayMetadataTree(metadata.GetRootPackage(), 0);
    }
}

private static void DisplayMetadataTree(MetadataPackage package, int indent)
{
    if (package != null)
    {
        var stringMetadataType = package.MetadataType.ToString();
        Console.WriteLine(stringMetadataType.PadLeft(stringMetadataType.Length + indent));
        foreach (MetadataProperty property in package)
        {
            string stringPropertyRepresentation = string.Format("Name: {0}, Value: {1}", property.Name, property.Value);
            Console.WriteLine(stringPropertyRepresentation.PadLeft(stringPropertyRepresentation.Length + indent + 1));
            if (property.Value != null)
            {
                switch (property.Value.Type)
                {
                    case MetadataPropertyType.Metadata:
                        DisplayMetadataTree(property.Value.ToClass<MetadataPackage>(), indent + 2);
                    break;
                    case MetadataPropertyType.MetadataArray:
                        DisplayMetadataTree(property.Value.ToArray<MetadataPackage>(), indent + 2);
                    break;
                }
            }
        }
    }
}

private static void DisplayMetadataTree(MetadataPackage[] packages, int indent)
{
    if (packages != null)
    {
        foreach (var package in packages)
        {
            DisplayMetadataTree(package, indent);
        }
    }
}
```

### 関連項目

* class [RootMetadataPackage](../../../groupdocs.metadata.common/rootmetadatapackage)
* class [Metadata](../../metadata)
* 名前空間 [GroupDocs.Metadata](../../metadata)
* 組み立て [GroupDocs.Metadata](../../../)

---

## GetRootPackage&lt;TRoot&gt;() {#getrootpackage_1}

ファイルから抽出されたすべてのメタデータ プロパティへのアクセスを提供するルート パッケージを取得します。

```csharp
public TRoot GetRootPackage<TRoot>()
    where TRoot : RootMetadataPackage
```

| パラメータ | 説明 |
| --- | --- |
| TRoot | ルート パッケージの正確なタイプ。 |

### 戻り値

ファイルから抽出されたすべてのメタデータ プロパティへのアクセスを提供するルート パッケージ。

### 備考

**もっと詳しく知る**

* [メタデータ ツリー全体をトラバースする](https://docs.groupdocs.com/display/metadatanet/Traverse+a+whole+metadata+tree)

### 関連項目

* class [RootMetadataPackage](../../../groupdocs.metadata.common/rootmetadatapackage)
* class [Metadata](../../metadata)
* 名前空間 [GroupDocs.Metadata](../../metadata)
* 組み立て [GroupDocs.Metadata](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Metadata.dll -->
