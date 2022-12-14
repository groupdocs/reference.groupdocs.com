---
title: SignatureSettings
second_title: Riferimento API GroupDocs.Signature per .NET
description: Definisce le impostazioni per la personalizzazioneSignature./signature comportamento.
type: docs
weight: 1810
url: /it/net/groupdocs.signature/signaturesettings/
---
## SignatureSettings class

Definisce le impostazioni per la personalizzazione[`Signature`](../signature) comportamento.

```csharp
public class SignatureSettings
```

## Costruttori

| Nome | Descrizione |
| --- | --- |
| [SignatureSettings](signaturesettings)() | Default_Costruttore |

## Proprietà

| Nome | Descrizione |
| --- | --- |
| [DefaultCulture](../../groupdocs.signature/signaturesettings/defaultculture) { get; set; } | Ottiene o imposta le impostazioni cultura predefinite da utilizzare durante l'elaborazione del documento. Il valore predefinito è "en-US". |
| [SaveDocumentOnEmptyDelete](../../groupdocs.signature/signaturesettings/savedocumentonemptydelete) { get; set; } | Ottiene o imposta il flag per salvare nuovamente il documento di origine quando il metodo Delete non ha firme interessate da rimuovere. Se questo flag è impostato su true (per impostazione predefinita), il documento verrà salvato con il registro del processo di cronologia corrispondente (data e tipo di operazione) anche se il metodo Delete non ha firme da rimuovere. Quando questo flat è impostato su false, il documento di origine non verrà modificato affatto. |
| [SaveDocumentOnEmptyUpdate](../../groupdocs.signature/signaturesettings/savedocumentonemptyupdate) { get; set; } | Ottiene o imposta il flag per salvare nuovamente il documento di origine quando il metodo di aggiornamento non ha firme da aggiornare. Se questo flag è impostato su true (per impostazione predefinita), il documento verrà salvato con il registro del processo della cronologia corrispondente (data e tipo di operazione) anche se il metodo di aggiornamento ha nessuna firma da aggiornare. Quando questo flat è impostato su false, il documento di origine non verrà modificato affatto. |
| [ShowDeletedSignaturesInfo](../../groupdocs.signature/signaturesettings/showdeletedsignaturesinfo) { get; set; } | Ottiene o imposta il flag che include le firme eliminate nel risultato Info documento. Ogni firma[`BaseSignature`](../../groupdocs.signature.domain/basesignature) ha il flag Eliminato[`Deleted`](../../groupdocs.signature.domain/basesignature/deleted) per rilevare se è stato eliminato. |

### Guarda anche

* spazio dei nomi [GroupDocs.Signature](../../groupdocs.signature)
* assemblea [GroupDocs.Signature](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Signature.dll -->
