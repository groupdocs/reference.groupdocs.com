---
title: GetViewInfo
second_title: GroupDocs.Viewer für .NET-API-Referenz
description: Gibt Informationen zu ansichts und dokumentspezifischen Informationen zurück.
type: docs
weight: 50
url: /de/net/groupdocs.viewer/viewer/getviewinfo/
---
## GetViewInfo(ViewInfoOptions) {#getviewinfo}

Gibt Informationen zu ansichts- und dokumentspezifischen Informationen zurück.

```csharp
public ViewInfo GetViewInfo(ViewInfoOptions options)
```

| Parameter | Typ | Beschreibung |
| --- | --- | --- |
| options | ViewInfoOptions | Die Optionen zum Anzeigen von Informationen. |

### Rückgabewert

Informationen zu ansichts- und dokumentspezifischen Informationen.

### Ausnahmen

| Ausnahme | Bedingung |
| --- | --- |
| ArgumentNullException | Wann geworfen*options* ist Null. |
| [PasswordRequiredException](../../../groupdocs.viewer.exceptions/passwordrequiredexception) | Wird ausgelöst, wenn zum Öffnen des Dokuments ein Kennwort erforderlich ist. |
| [IncorrectPasswordException](../../../groupdocs.viewer.exceptions/incorrectpasswordexception) | Wird ausgelöst, wenn das angegebene Kennwort falsch ist. |

### Bemerkungen

**Mehr erfahren**

* Erfahren Sie mehr über Dokumente – Dateityp, Seitenanzahl und andere formatspezifische Eigenschaften: [So erhalten Sie Dateiinformationen mit GroupDocs.Viewer](https://docs.groupdocs.com/display/viewernet/Get+file+information)

### Siehe auch

* class [ViewInfo](../../../groupdocs.viewer.results/viewinfo)
* class [ViewInfoOptions](../../../groupdocs.viewer.options/viewinfooptions)
* class [Viewer](../../viewer)
* namensraum [GroupDocs.Viewer](../../viewer)
* Montage [GroupDocs.Viewer](../../../)

---

## GetViewInfo(ViewInfoOptions, CancellationToken) {#getviewinfo_1}

Gibt Informationen zu ansichts- und dokumentspezifischen Informationen zurück.

```csharp
public ViewInfo GetViewInfo(ViewInfoOptions options, CancellationToken cancellationToken)
```

| Parameter | Typ | Beschreibung |
| --- | --- | --- |
| options | ViewInfoOptions | Die Optionen zum Anzeigen von Informationen. |
| cancellationToken | CancellationToken | Stornierungstoken. |

### Rückgabewert

Informationen zu ansichts- und dokumentspezifischen Informationen.

### Ausnahmen

| Ausnahme | Bedingung |
| --- | --- |
| ArgumentNullException | Wann geworfen*options* ist Null. |
| [PasswordRequiredException](../../../groupdocs.viewer.exceptions/passwordrequiredexception) | Wird ausgelöst, wenn zum Öffnen des Dokuments ein Kennwort erforderlich ist. |
| [IncorrectPasswordException](../../../groupdocs.viewer.exceptions/incorrectpasswordexception) | Wird ausgelöst, wenn das angegebene Kennwort falsch ist. |

### Bemerkungen

**Mehr erfahren**

* Erfahren Sie mehr über Dokumente – Dateityp, Seitenanzahl und andere formatspezifische Eigenschaften: [So erhalten Sie Dateiinformationen mit GroupDocs.Viewer](https://docs.groupdocs.com/display/viewernet/Get+file+information)

### Siehe auch

* class [ViewInfo](../../../groupdocs.viewer.results/viewinfo)
* class [ViewInfoOptions](../../../groupdocs.viewer.options/viewinfooptions)
* class [Viewer](../../viewer)
* namensraum [GroupDocs.Viewer](../../viewer)
* Montage [GroupDocs.Viewer](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Viewer.dll -->