---
title: VCardTextRecord
second_title: Riferimento API GroupDocs.Metadata per .NET
description: Rappresenta la classe di metadati del record di testo vCard.
type: docs
weight: 810
url: /it/net/groupdocs.metadata.formats.businesscard/vcardtextrecord/
---
## VCardTextRecord class

Rappresenta la classe di metadati del record di testo vCard.

```csharp
public class VCardTextRecord : VCardRecord
```

## Proprietà

| Nome | Descrizione |
| --- | --- |
| [AltIdParameter](../../groupdocs.metadata.formats.businesscard/vcardrecord/altidparameter) { get; } | Ottiene il valore del parametro delle rappresentazioni alternative. |
| [AnonymParameters](../../groupdocs.metadata.formats.businesscard/vcardrecord/anonymparameters) { get; } | Ottiene i parametri anonimi. |
| [CharsetParameter](../../groupdocs.metadata.formats.businesscard/vcardtextrecord/charsetparameter) { get; } | Ottiene il parametro charset. |
| override [ContentType](../../groupdocs.metadata.formats.businesscard/vcardtextrecord/contenttype) { get; } | Ottiene il tipo di contenuto del record. |
| [Count](../../groupdocs.metadata.common/metadatapackage/count) { get; } | Ottiene il numero di proprietà dei metadati. |
| [EncodingParameter](../../groupdocs.metadata.formats.businesscard/vcardrecord/encodingparameter) { get; } | Ottiene il valore del parametro di codifica. |
| [Group](../../groupdocs.metadata.formats.businesscard/vcardrecord/group) { get; } | Ottiene il valore di raggruppamento. |
| [IsQuotedPrintable](../../groupdocs.metadata.formats.businesscard/vcardtextrecord/isquotedprintable) { get; } | Ottiene un valore che indica se questa istanza è una stringa stampabile tra virgolette. |
| [Item](../../groupdocs.metadata.common/metadatapackage/item) { get; } | Ottiene il[`MetadataProperty`](../../groupdocs.metadata.common/metadataproperty) con il nome specificato. |
| [Keys](../../groupdocs.metadata.common/metadatapackage/keys) { get; } | Ottiene una raccolta dei nomi delle proprietà dei metadati. |
| [LanguageParameter](../../groupdocs.metadata.formats.businesscard/vcardrecord/languageparameter) { get; } | Ottiene il valore del parametro della lingua. |
| [MediaTypeParameter](../../groupdocs.metadata.formats.businesscard/vcardtextrecord/mediatypeparameter) { get; } | Ottiene il valore del parametro del tipo di supporto. |
| [MetadataType](../../groupdocs.metadata.common/metadatapackage/metadatatype) { get; } | Ottiene il tipo di metadati. |
| [PrefParameter](../../groupdocs.metadata.formats.businesscard/vcardrecord/prefparameter) { get; } | Ottiene il parametro preferito. |
| [PropertyDescriptors](../../groupdocs.metadata.common/metadatapackage/propertydescriptors) { get; } | Ottiene una raccolta di descrittori che contengono informazioni sulle proprietà accessibili tramite il motore di ricerca GroupDocs.Metadata. |
| [TypeName](../../groupdocs.metadata.formats.businesscard/vcardrecord/typename) { get; } | Ottiene il tipo di record. |
| [TypeParameters](../../groupdocs.metadata.formats.businesscard/vcardrecord/typeparameters) { get; } | Ottiene i valori del parametro di tipo. |
| [Value](../../groupdocs.metadata.formats.businesscard/vcardtextrecord/value) { get; } | Ottiene il valore del record. |
| [ValueParameters](../../groupdocs.metadata.formats.businesscard/vcardrecord/valueparameters) { get; } | Ottiene i parametri del valore. |

## Metodi

| Nome | Descrizione |
| --- | --- |
| [AddProperties](../../groupdocs.metadata.common/metadatapackage/addproperties)(Func&lt;MetadataProperty, bool&gt;, PropertyValue) | Aggiunge proprietà di metadati note che soddisfano il predicato specificato. L'operazione è ricorsiva quindi interessa anche tutti i pacchetti nidificati. |
| [Contains](../../groupdocs.metadata.common/metadatapackage/contains)(string) | Determina se il pacchetto contiene una proprietà di metadati con il nome specificato. |
| virtual [FindProperties](../../groupdocs.metadata.common/metadatapackage/findproperties)(Func&lt;MetadataProperty, bool&gt;) | Trova le proprietà dei metadati che soddisfano il predicato specificato. La ricerca è ricorsiva quindi interessa anche tutti i pacchetti nidificati. |
| [GetEnumerator](../../groupdocs.metadata.common/metadatapackage/getenumerator)() | Restituisce un enumeratore che scorre la raccolta. |
| [GetReadabilityValue](../../groupdocs.metadata.formats.businesscard/vcardtextrecord/getreadabilityvalue)(string) | Ottiene il valore di leggibilità. |
| virtual [RemoveProperties](../../groupdocs.metadata.common/metadatapackage/removeproperties)(Func&lt;MetadataProperty, bool&gt;) | Rimuove le proprietà dei metadati che soddisfano il predicato specificato. |
| virtual [Sanitize](../../groupdocs.metadata.common/metadatapackage/sanitize)() | Rimuove le proprietà dei metadati scrivibili dal pacchetto. L'operazione è ricorsiva quindi interessa anche tutti i pacchetti annidati. |
| [SetProperties](../../groupdocs.metadata.common/metadatapackage/setproperties)(Func&lt;MetadataProperty, bool&gt;, PropertyValue) | Imposta le proprietà dei metadati noti che soddisfano il predicato specificato. L'operazione è ricorsiva quindi interessa anche tutti i pacchetti nidificati. Questo metodo è una combinazione di[`AddProperties`](../../groupdocs.metadata.common/metadatapackage/addproperties) E[`UpdateProperties`](../../groupdocs.metadata.common/metadatapackage/updateproperties) Se una proprietà esistente soddisfa il predicato, il suo valore viene aggiornato. Se nel pacchetto manca una proprietà nota che soddisfa il predicato, viene aggiunta al pacchetto. |
| [UpdateProperties](../../groupdocs.metadata.common/metadatapackage/updateproperties)(Func&lt;MetadataProperty, bool&gt;, PropertyValue) | Aggiorna le proprietà dei metadati noti che soddisfano il predicato specificato. L'operazione è ricorsiva quindi interessa anche tutti i pacchetti nidificati. |

### Osservazioni

**Saperne di più**

* [Utilizzo dei metadati vCard](https://docs.groupdocs.com/display/metadatanet/Working+with+vCard+metadata)

### Guarda anche

* class [VCardRecord](../vcardrecord)
* spazio dei nomi [GroupDocs.Metadata.Formats.BusinessCard](../../groupdocs.metadata.formats.businesscard)
* assemblea [GroupDocs.Metadata](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Metadata.dll -->
