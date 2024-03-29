---
title: License
second_title: GroupDocs.Redaction for .NET API リファレンス
description: ライセンスを適用する方法を提供します
type: docs
weight: 260
url: /ja/net/groupdocs.redaction/license/
---
## License class

ライセンスを適用する方法を提供します。

```csharp
public class License
```

## コンストラクター

| 名前 | 説明 |
| --- | --- |
| [License](license)() | License クラスのインスタンスを初期化します。 |

## メソッド

| 名前 | 説明 |
| --- | --- |
| [SetLicense](../../groupdocs.redaction/license/setlicense#setlicense)(Stream) | ストリームから GroupDocs.Redaction ライセンスを設定します。 |
| [SetLicense](../../groupdocs.redaction/license/setlicense#setlicense_1)(string) | ファイル パスから GroupDocs.Redaction ライセンスを設定します。 |

### 備考

**もっと詳しく知る**

* ライセンスの詳細: [GroupDocs ライセンスに関するよくある質問](https://purchase.groupdocs.com/faqs/licensing)
* 詳細について**GroupDocs.Redaction**ライセンス: [評価の制限とライセンス](https://docs.groupdocs.com/redaction/net/evaluation-limitations-and-licensing/)

### 例

次の例は、GroupDocs.Redaction. のライセンスを設定する方法を示しています。

```csharp
GroupDocs.Redaction.License license = new GroupDocs.Redaction.License();
// 別の方法として、ストリームを使用できます:
license.SetLicense(licensePath);
```

### 関連項目

* 名前空間 [GroupDocs.Redaction](../../groupdocs.redaction)
* 組み立て [GroupDocs.Redaction](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Redaction.dll -->
