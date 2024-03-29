---
title: CmsSigner
second_title: GroupDocs.Metadata for .NET API リファレンス
description: 署名者ごとの CMS 情報を表します
type: docs
weight: 3010
url: /ja/net/groupdocs.metadata.standards.pkcs/cmssigner/
---
## CmsSigner class

署名者ごとの CMS 情報を表します。

```csharp
public class CmsSigner : CustomPackage
```

## プロパティ

| 名前 | 説明 |
| --- | --- |
| [Count](../../groupdocs.metadata.common/metadatapackage/count) { get; } | メタデータ プロパティの数を取得します。 |
| [DigestAlgorithm](../../groupdocs.metadata.standards.pkcs/cmssigner/digestalgorithm) { get; } | 署名者が使用するメッセージ ダイジェスト アルゴリズムと関連するパラメーターを取得します。 |
| [Item](../../groupdocs.metadata.common/metadatapackage/item) { get; } | を取得します[`MetadataProperty`](../../groupdocs.metadata.common/metadataproperty)指定された名前で. |
| [Keys](../../groupdocs.metadata.common/metadatapackage/keys) { get; } | メタデータ プロパティ名のコレクションを取得します。 |
| [MetadataType](../../groupdocs.metadata.common/metadatapackage/metadatatype) { get; } | メタデータ タイプを取得します。 |
| [PropertyDescriptors](../../groupdocs.metadata.common/metadatapackage/propertydescriptors) { get; } | GroupDocs.Metadata 検索エンジンを介してアクセス可能なプロパティに関する情報を含む記述子のコレクションを取得します。 |
| [SignatureAlgorithm](../../groupdocs.metadata.standards.pkcs/cmssigner/signaturealgorithm) { get; } | 署名者がデジタル署名を生成するために使用する署名アルゴリズムと関連するパラメーターを取得します。 |
| [SignatureValue](../../groupdocs.metadata.standards.pkcs/cmssigner/signaturevalue) { get; } | メッセージ ダイジェストと署名者の秘密鍵を使用して、デジタル署名生成の結果を取得します。 |
| [SignedAttributes](../../groupdocs.metadata.standards.pkcs/cmssigner/signedattributes) { get; } | 署名された属性のコレクションを取得します。 |
| [SignerIdentifier](../../groupdocs.metadata.standards.pkcs/cmssigner/signeridentifier) { get; } | 署名者の証明書 (および署名者の公開鍵) の生データを取得します。 |
| [SigningTime](../../groupdocs.metadata.standards.pkcs/cmssigner/signingtime) { get; } | 署名者が (意図的に) 署名プロセスを実行した時刻を取得します。 |
| [UnsignedAttributes](../../groupdocs.metadata.standards.pkcs/cmssigner/unsignedattributes) { get; } | 署名されていない属性のコレクションを取得します。 |

## メソッド

| 名前 | 説明 |
| --- | --- |
| [AddProperties](../../groupdocs.metadata.common/metadatapackage/addproperties)(Func&lt;MetadataProperty, bool&gt;, PropertyValue) | 指定された述語を満たす既知のメタデータ プロパティを追加します。 操作は再帰的であるため、ネストされたすべてのパッケージにも影響します。 |
| [Contains](../../groupdocs.metadata.common/metadatapackage/contains)(string) | 指定した名前のメタデータ プロパティがパッケージに含まれているかどうかを判断します。 |
| virtual [FindProperties](../../groupdocs.metadata.common/metadatapackage/findproperties)(Func&lt;MetadataProperty, bool&gt;) | 指定された述語を満たすメタデータ プロパティを検索します。 検索は再帰的であるため、ネストされたすべてのパッケージにも影響します。 |
| [GetEnumerator](../../groupdocs.metadata.common/metadatapackage/getenumerator)() | コレクションを反復処理する列挙子を返します。 |
| virtual [RemoveProperties](../../groupdocs.metadata.common/metadatapackage/removeproperties)(Func&lt;MetadataProperty, bool&gt;) | 指定された述語を満たすメタデータ プロパティを削除します。 |
| virtual [Sanitize](../../groupdocs.metadata.common/metadatapackage/sanitize)() | 書き込み可能なメタデータ プロパティをパッケージから削除します。 操作は再帰的であるため、ネストされたすべてのパッケージにも影響します。 |
| [SetProperties](../../groupdocs.metadata.common/metadatapackage/setproperties)(Func&lt;MetadataProperty, bool&gt;, PropertyValue) | 指定された述語を満たす既知のメタデータ プロパティを設定します。 操作は再帰的であるため、ネストされたすべてのパッケージにも影響します。 このメソッドは、[`AddProperties`](../../groupdocs.metadata.common/metadatapackage/addproperties)と[`UpdateProperties`](../../groupdocs.metadata.common/metadatapackage/updateproperties) 既存のプロパティが述語を満たす場合、その値が更新されます。 述語を満たす既知のプロパティがパッケージにない場合、それがパッケージに追加されます。 |
| [UpdateProperties](../../groupdocs.metadata.common/metadatapackage/updateproperties)(Func&lt;MetadataProperty, bool&gt;, PropertyValue) | 指定された述語を満たす既知のメタデータ プロパティを更新します。 操作は再帰的であるため、ネストされたすべてのパッケージにも影響します。 |

### 関連項目

* class [CustomPackage](../../groupdocs.metadata.common/custompackage)
* 名前空間 [GroupDocs.Metadata.Standards.Pkcs](../../groupdocs.metadata.standards.pkcs)
* 組み立て [GroupDocs.Metadata](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Metadata.dll -->
