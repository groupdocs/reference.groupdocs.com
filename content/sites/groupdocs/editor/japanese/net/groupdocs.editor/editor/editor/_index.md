---
title: Editor
second_title: GroupDocs.Editor for .NET API リファレンス
description: 指定された入力ドキュメントで新しい Editor インスタンスを初期化します ストリームとして
type: docs
weight: 10
url: /ja/net/groupdocs.editor/editor/editor/
---
## Editor(Func&lt;Stream&gt;) {#constructor}

指定された入力ドキュメントで新しい Editor インスタンスを初期化します (ストリームとして)

```csharp
public Editor(Func<Stream> document)
```

| パラメータ | タイプ | 説明 |
| --- | --- | --- |
| document | Func`1 | ドキュメント コンテンツを含むストリームを返すデリゲート。 NULL であってはなりません。 |

### 備考

**もっと詳しく知る**

* GroupDocs.Editor でサポートされているファイル タイプの詳細: [GroupDocs.Editor がサポートするドキュメント形式](https://docs.groupdocs.com/display/editornet/Supported+Document+Formats)
* GroupDocs.Editor for .NET 機能の詳細: [開発者ガイド](https://docs.groupdocs.com/display/editornet/Developer+Guide)

### 関連項目

* class [Editor](../../editor)
* 名前空間 [GroupDocs.Editor](../../editor)
* 組み立て [GroupDocs.Editor](../../../)

---

## Editor(Func&lt;Stream&gt;, Func&lt;ILoadOptions&gt;) {#constructor_1}

指定された入力ドキュメント (ストリームとして) を使用して新しい Editor インスタンスを初期化し、そのロード オプションを使用します

```csharp
public Editor(Func<Stream> document, Func<ILoadOptions> loadOptions)
```

| パラメータ | タイプ | 説明 |
| --- | --- | --- |
| document | Func`1 | ドキュメント コンテンツを含むストリームを返すデリゲート。 NULL であってはなりません。 |
| loadOptions | Func`1 | ドキュメントの読み込みオプションを返すデリゲート。 NULL の可能性があり、null - を返す可能性があります。その場合、ドキュメント タイプが自動的に検出され、そのタイプのデフォルトの読み込みオプションが適用されます。 |

### 備考

**もっと詳しく知る**

* GroupDocs.Editor でサポートされているファイル タイプの詳細: [GroupDocs.Editor がサポートするドキュメント形式](https://docs.groupdocs.com/display/editornet/Supported+Document+Formats)
* GroupDocs.Editor for .NET 機能の詳細: [開発者ガイド](https://docs.groupdocs.com/display/editornet/Developer+Guide)
* パスワードで保護されたドキュメントと別のストレージのドキュメントを開いて編集する方法の詳細: [GroupDocs.Editor を使用してドキュメントを読み込んで編集する](https://docs.groupdocs.com/display/editornet/Load+document)

### 関連項目

* interface [ILoadOptions](../../../groupdocs.editor.options/iloadoptions)
* class [Editor](../../editor)
* 名前空間 [GroupDocs.Editor](../../editor)
* 組み立て [GroupDocs.Editor](../../../)

---

## Editor(string) {#constructor_2}

指定された入力ドキュメント (完全なファイル パスとして) で新しい Editor インスタンスを初期化します

```csharp
public Editor(string filePath)
```

| パラメータ | タイプ | 説明 |
| --- | --- | --- |
| filePath | String | ファイルへのフル パス。 NULL であってはなりません。有効で、ファイルが存在する必要があります。 |

### 備考

**もっと詳しく知る**

* GroupDocs.Editor でサポートされているファイル タイプの詳細: [GroupDocs.Editor がサポートするドキュメント形式](https://docs.groupdocs.com/display/editornet/Supported+Document+Formats)
* GroupDocs.Editor for .NET 機能の詳細: [開発者ガイド](https://docs.groupdocs.com/display/editornet/Developer+Guide)

### 関連項目

* class [Editor](../../editor)
* 名前空間 [GroupDocs.Editor](../../editor)
* 組み立て [GroupDocs.Editor](../../../)

---

## Editor(string, Func&lt;ILoadOptions&gt;) {#constructor_3}

指定された入力ドキュメント (完全なファイル パスとして) を使用して新しいエディター インスタンスを初期化し、その読み込みオプションを使用します

```csharp
public Editor(string filePath, Func<ILoadOptions> loadOptions)
```

| パラメータ | タイプ | 説明 |
| --- | --- | --- |
| filePath | String | ファイルへのフル パス。 NULL であってはなりません。有効で、ファイルが存在する必要があります。 |
| loadOptions | Func`1 | ドキュメントの読み込みオプションを返すデリゲート。 NULL の可能性があり、null - を返す可能性があります。その場合、ドキュメント タイプが自動的に検出され、そのタイプのデフォルトの読み込みオプションが適用されます。 |

### 備考

**もっと詳しく知る**

* GroupDocs.Editor でサポートされているファイル タイプの詳細: [GroupDocs.Editor がサポートするドキュメント形式](https://docs.groupdocs.com/display/editornet/Supported+Document+Formats)
* GroupDocs.Editor for .NET 機能の詳細: [開発者ガイド](https://docs.groupdocs.com/display/editornet/Developer+Guide)
* パスワードで保護されたドキュメントと別のストレージのドキュメントを開いて編集する方法の詳細: [GroupDocs.Editor を使用してドキュメントを読み込んで編集する](https://docs.groupdocs.com/display/editornet/Load+document)

### 関連項目

* interface [ILoadOptions](../../../groupdocs.editor.options/iloadoptions)
* class [Editor](../../editor)
* 名前空間 [GroupDocs.Editor](../../editor)
* 組み立て [GroupDocs.Editor](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Editor.dll -->
