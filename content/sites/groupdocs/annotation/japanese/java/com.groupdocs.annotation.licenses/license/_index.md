---
title: "ライセンス"
second_title: "GroupDocs.Annotation for Java API リファレンス"
description: "コンポーネントのライセンス付与のためのメソッドを提供します。"
type: docs
weight: 10
url: /ja/java/com.groupdocs.annotation.licenses/license/
---
**Inheritance:**
java.lang.Object
```
public class License
```

コンポーネントをライセンスするためのメソッドを提供します。ライセンスについての詳細は here を参照してください。

--------------------

 **Learn more** 

 *  
 *  
## コンストラクタ

| コンストラクタ | 説明 |
| --- | --- |
| [License()](#License--) |  |
## メソッド

| メソッド | 説明 |
| --- | --- |
| [isValidMeteredLicense()](#isValidMeteredLicense--) |  |
| [isValidLicense()](#isValidLicense--) | このインスタンスが有効なライセンスかどうかを示す値を取得します。 |
| [setLicense(InputStream licenseStream)](#setLicense-java.io.InputStream-) | コンポーネントにライセンスを付与します。 |
| [setLicenseInternal(System.IO.Stream licenseStream)](#setLicenseInternal-com.aspose.ms.System.IO.Stream-) |  |
| [setMeteredLicense()](#setMeteredLicense--) |  |
| [setLicense(Path licensePath)](#setLicense-java.nio.file.Path-) | コンポーネントにライセンスを付与します。 |
| [setLicense(String licensePath)](#setLicense-java.lang.String-) | コンポーネントにライセンスを付与します。 |
| [resetLicense()](#resetLicense--) |  |
### License() {#License--}
```
public License()
```


### isValidMeteredLicense() {#isValidMeteredLicense--}
```
public static boolean isValidMeteredLicense()
```




**Returns:**
boolean
### isValidLicense() {#isValidLicense--}
```
public static boolean isValidLicense()
```


このインスタンスが有効なライセンスかどうかを示す値を取得します。

値:  true  このインスタンスが有効なライセンスの場合は true、そうでない場合は false。

**Returns:**
boolean
### setLicense(InputStream licenseStream) {#setLicense-java.io.InputStream-}
```
public final void setLicense(InputStream licenseStream)
```


コンポーネントにライセンスを付与します。

**Parameters:**
| パラメーター | 型 | 説明 |
| --- | --- | --- |
| licenseStream | java.io.InputStream | ライセンスストリーム。 |

### setLicenseInternal(System.IO.Stream licenseStream) {#setLicenseInternal-com.aspose.ms.System.IO.Stream-}
```
public void setLicenseInternal(System.IO.Stream licenseStream)
```




**Parameters:**
| パラメーター | 型 | 説明 |
| --- | --- | --- |
| licenseStream | com.aspose.ms.System.IO.Stream |  |

### setMeteredLicense() {#setMeteredLicense--}
```
public final void setMeteredLicense()
```




### setLicense(Path licensePath) {#setLicense-java.nio.file.Path-}
```
public final void setLicense(Path licensePath)
```


コンポーネントにライセンスを付与します。

**Parameters:**
| パラメーター | 型 | 説明 |
| --- | --- | --- |
| licensePath | java.nio.file.Path | ライセンスパス。 |

### setLicense(String licensePath) {#setLicense-java.lang.String-}
```
public final void setLicense(String licensePath)
```


コンポーネントにライセンスを付与します。

**Parameters:**
| パラメーター | 型 | 説明 |
| --- | --- | --- |
| licensePath | java.lang.String | ライセンスパス。 |

### resetLicense() {#resetLicense--}
```
public static void resetLicense()
```




