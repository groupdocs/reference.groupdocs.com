---
title: ParserSettings
second_title: GroupDocs.Parser för .NET API-referens
description: Initierar en ny instans avParserSettingsgroupdocs.parser.options/parsersettings klass med loggern.
type: docs
weight: 10
url: /sv/net/groupdocs.parser.options/parsersettings/parsersettings/
---
## ParserSettings(ILogger) {#constructor_1}

Initierar en ny instans av[`ParserSettings`](../../parsersettings) klass med loggern.

```csharp
public ParserSettings(ILogger logger)
```

| Parameter | Typ | Beskrivning |
| --- | --- | --- |
| logger | ILogger | En instans av klass som implementerar[`ILogger`](../../ilogger) gränssnitt. |

### Se även

* interface [ILogger](../../ilogger)
* class [ParserSettings](../../parsersettings)
* namnutrymme [GroupDocs.Parser.Options](../../parsersettings)
* hopsättning [GroupDocs.Parser](../../../)

---

## ParserSettings(OcrConnectorBase) {#constructor_4}

Initierar en ny instans av[`ParserSettings`](../../parsersettings) klass med OCR Connector.

```csharp
public ParserSettings(OcrConnectorBase ocrConnector)
```

| Parameter | Typ | Beskrivning |
| --- | --- | --- |
| ocrConnector | OcrConnectorBase | En instans av klass som ärver[`OcrConnectorBase`](../../ocrconnectorbase) klass för att tillhandahålla OCR-funktionalitet. |

### Se även

* class [OcrConnectorBase](../../ocrconnectorbase)
* class [ParserSettings](../../parsersettings)
* namnutrymme [GroupDocs.Parser.Options](../../parsersettings)
* hopsättning [GroupDocs.Parser](../../../)

---

## ParserSettings(ExternalResourceHandler) {#constructor}

Initierar en ny instans av[`ParserSettings`](../../parsersettings) klass med den externa resurshanteraren.

```csharp
public ParserSettings(ExternalResourceHandler externalResourceHandler)
```

| Parameter | Typ | Beskrivning |
| --- | --- | --- |
| externalResourceHandler | ExternalResourceHandler | En instans av klass som ärver[`ExternalResourceHandler`](../../externalresourcehandler) klass för att ge kontroll över externa resurser. |

### Se även

* class [ExternalResourceHandler](../../externalresourcehandler)
* class [ParserSettings](../../parsersettings)
* namnutrymme [GroupDocs.Parser.Options](../../parsersettings)
* hopsättning [GroupDocs.Parser](../../../)

---

## ParserSettings(ILogger, OcrConnectorBase) {#constructor_2}

Initierar en ny instans av[`ParserSettings`](../../parsersettings) klass med logger och OCR Connector.

```csharp
public ParserSettings(ILogger logger, OcrConnectorBase ocrConnector)
```

| Parameter | Typ | Beskrivning |
| --- | --- | --- |
| logger | ILogger | En instans av klass som implementerar[`ILogger`](../../ilogger) gränssnitt. |
| ocrConnector | OcrConnectorBase | En instans av klass som ärver[`OcrConnectorBase`](../../ocrconnectorbase) klass för att tillhandahålla OCR-funktionalitet. |

### Se även

* interface [ILogger](../../ilogger)
* class [OcrConnectorBase](../../ocrconnectorbase)
* class [ParserSettings](../../parsersettings)
* namnutrymme [GroupDocs.Parser.Options](../../parsersettings)
* hopsättning [GroupDocs.Parser](../../../)

---

## ParserSettings(ILogger, OcrConnectorBase, ExternalResourceHandler) {#constructor_3}

Initierar en ny instans av[`ParserSettings`](../../parsersettings) class.

```csharp
public ParserSettings(ILogger logger, OcrConnectorBase ocrConnector, 
    ExternalResourceHandler externalResourceHandler)
```

| Parameter | Typ | Beskrivning |
| --- | --- | --- |
| logger | ILogger | En instans av klass som implementerar[`ILogger`](../../ilogger) gränssnitt. |
| ocrConnector | OcrConnectorBase | En instans av klass som ärver[`OcrConnectorBase`](../../ocrconnectorbase) klass för att tillhandahålla OCR-funktionalitet. |
| externalResourceHandler | ExternalResourceHandler | En instans av klass som ärver[`ExternalResourceHandler`](../../externalresourcehandler) klass för att ge kontroll över extern resursladdning. |

### Se även

* interface [ILogger](../../ilogger)
* class [OcrConnectorBase](../../ocrconnectorbase)
* class [ExternalResourceHandler](../../externalresourcehandler)
* class [ParserSettings](../../parsersettings)
* namnutrymme [GroupDocs.Parser.Options](../../parsersettings)
* hopsättning [GroupDocs.Parser](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Parser.dll -->
