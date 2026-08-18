---
title: Metered
second_title: GroupDocs.Markdown for Java API Reference
description: Provides methods for applying Metered license.
type: docs
weight: 28
url: /java/com.groupdocs.markdown/metered/
---
**Inheritance:**
java.lang.Object
```
public class Metered
```

Provides methods for applying Metered license.

## Constructors

| Constructor | Description |
| --- | --- |
| [Metered()](#Metered--) |  |
## Methods

| Method | Description |
| --- | --- |
| [setMeteredKey(String publicKey, String privateKey)](#setMeteredKey-java.lang.String-java.lang.String-) | Activates product with Metered keys.
 |
| [getConsumptionQuantity()](#getConsumptionQuantity--) | Retrieves amount of MBs processed.
 |
| [getConsumptionCredit()](#getConsumptionCredit--) | Retrieves count of credits consumed.
 |
### Metered() {#Metered--}
```
public Metered()
```


### setMeteredKey(String publicKey, String privateKey) {#setMeteredKey-java.lang.String-java.lang.String-}
```
public void setMeteredKey(String publicKey, String privateKey)
```


Activates product with Metered keys.


**Parameters:**
| Parameter | Type | Description |
| --- | --- | --- |
| publicKey | java.lang.String | the public key
 |
| privateKey | java.lang.String | the private key
 |

### getConsumptionQuantity() {#getConsumptionQuantity--}
```
public static Double getConsumptionQuantity()
```


Retrieves amount of MBs processed.


**Returns:**
java.lang.Double - processed MB count

### getConsumptionCredit() {#getConsumptionCredit--}
```
public static Double getConsumptionCredit()
```


Retrieves count of credits consumed.


**Returns:**
java.lang.Double - consumed credits count

