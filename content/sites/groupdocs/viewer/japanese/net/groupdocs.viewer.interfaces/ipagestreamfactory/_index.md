---
title: IPageStreamFactory
second_title: GroupDocs.Viewer for .NET API リファレンス
description: 出力ページ ストリームのインスタンス化と解放に必要なメソッドを定義します
type: docs
weight: 170
url: /ja/net/groupdocs.viewer.interfaces/ipagestreamfactory/
---
## IPageStreamFactory interface

出力ページ ストリームのインスタンス化と解放に必要なメソッドを定義します。

```csharp
public interface IPageStreamFactory
```

## メソッド

| 名前 | 説明 |
| --- | --- |
| [CreatePageStream](../../groupdocs.viewer.interfaces/ipagestreamfactory/createpagestream)(int) | 出力ページ データの書き込みに使用されるストリームを作成します。 |
| [ReleasePageStream](../../groupdocs.viewer.interfaces/ipagestreamfactory/releasepagestream)(int, Stream) | によって作成されたストリームを解放します[`CreatePageStream`](./createpagestream)method. |

### 関連項目

* 名前空間 [GroupDocs.Viewer.Interfaces](../../groupdocs.viewer.interfaces)
* 組み立て [GroupDocs.Viewer](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Viewer.dll -->
