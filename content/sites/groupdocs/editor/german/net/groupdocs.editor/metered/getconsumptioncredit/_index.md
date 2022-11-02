---
title: GetConsumptionCredit
second_title: GroupDocs.Editor für .NET-API-Referenz
description: Ruft die Anzahl der verbrauchten Credits ab.
type: docs
weight: 30
url: /de/net/groupdocs.editor/metered/getconsumptioncredit/
---
## Metered.GetConsumptionCredit method

Ruft die Anzahl der verbrauchten Credits ab.

```csharp
public static decimal GetConsumptionCredit()
```

### Rückgabewert

Anzahl der bereits verbrauchten Credits

### Beispiele

Das folgende Beispiel zeigt, wie die Anzahl der verbrauchten Credits abgerufen wird.

```csharp
string publicKey = "Public Key";
string privateKey = "Private Key";

Metered metered = new Metered();
metered.SetMeteredKey(publicKey, privateKey);

decimal creditsConsumed = Metered.GetConsumptionCredit();
```

### Siehe auch

* class [Metered](../../metered)
* namensraum [GroupDocs.Editor](../../metered)
* Montage [GroupDocs.Editor](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Editor.dll -->