---
title: EmailContent
second_title: Riferimento API GroupDocs.Watermark per .NET
description: Rappresenta un messaggio di posta elettronica.
type: docs
weight: 330
url: /it/net/groupdocs.watermark.contents.email/emailcontent/
---
## EmailContent class

Rappresenta un messaggio di posta elettronica.

```csharp
public sealed class EmailContent : Content
```

## Proprietà

| Nome | Descrizione |
| --- | --- |
| [Attachments](../../groupdocs.watermark.contents.email/emailcontent/attachments) { get; } | Ottiene la raccolta di tutti gli allegati del messaggio di posta elettronica. |
| [Bcc](../../groupdocs.watermark.contents.email/emailcontent/bcc) { get; } | Ottiene la raccolta dei destinatari BCC (copia nascosta) del messaggio di posta elettronica. |
| [Body](../../groupdocs.watermark.contents.email/emailcontent/body) { get; set; } | Ottiene o imposta la rappresentazione in testo normale del corpo del messaggio. |
| [BodyType](../../groupdocs.watermark.contents.email/emailcontent/bodytype) { get; } | Ottiene il tipo di corpo del messaggio di posta elettronica. |
| [Cc](../../groupdocs.watermark.contents.email/emailcontent/cc) { get; } | Ottiene la raccolta dei destinatari CC (copia carbone) del messaggio di posta elettronica. |
| [EmbeddedObjects](../../groupdocs.watermark.contents.email/emailcontent/embeddedobjects) { get; } | Ottiene la raccolta di tutti gli oggetti incorporati del messaggio di posta elettronica. |
| [From](../../groupdocs.watermark.contents.email/emailcontent/from) { get; } | Ottiene l'indirizzo del mittente del messaggio di posta elettronica. |
| [HtmlBody](../../groupdocs.watermark.contents.email/emailcontent/htmlbody) { get; set; } | Ottiene o imposta la rappresentazione html del corpo del messaggio. |
| [Subject](../../groupdocs.watermark.contents.email/emailcontent/subject) { get; set; } | Recupera o imposta l'oggetto del messaggio di posta elettronica. |
| [To](../../groupdocs.watermark.contents.email/emailcontent/to) { get; } | Ottiene la raccolta dei destinatari del messaggio di posta elettronica. |

## Metodi

| Nome | Descrizione |
| --- | --- |
| [Dispose](../../groupdocs.watermark.contents/content/dispose)() | Elimina l'istanza corrente. |
| [FindImages](../../groupdocs.watermark.contents/contentpart/findimages)() | Trova tutte le immagini nel contenuto. La ricerca viene condotta negli oggetti specificati in[`SearchableObjects`](../../groupdocs.watermark/watermarker/searchableobjects) . |
| [FindImages](../../groupdocs.watermark.contents/contentpart/findimages)(ImageSearchCriteria) | Trova le immagini in base ai criteri di ricerca specificati. La ricerca viene eseguita negli oggetti specificati in[`SearchableObjects`](../../groupdocs.watermark/watermarker/searchableobjects) . |
| [Search](../../groupdocs.watermark.contents/contentpart/search)() | Trova tutte le possibili filigrane nel contenuto. La ricerca viene condotta negli oggetti specificati in[`SearchableObjects`](../../groupdocs.watermark/watermarker/searchableobjects) . |
| [Search](../../groupdocs.watermark.contents/contentpart/search)(SearchCriteria) | Trova filigrane possibili in base ai criteri di ricerca specificati. La ricerca viene eseguita negli oggetti specificati in[`SearchableObjects`](../../groupdocs.watermark/watermarker/searchableobjects) . |

### Osservazioni

**Saperne di più:**

* [Aggiungi filigrane agli allegati e-mail](https://docs.groupdocs.com/display/watermarknet/Add+watermarks+to+email+attachments)
* [Allegati e-mail](https://docs.groupdocs.com/display/watermarknet/Email+attachments)
* [Messaggi di posta elettronica](https://docs.groupdocs.com/display/watermarknet/Email+messages)

### Guarda anche

* class [Content](../../groupdocs.watermark.contents/content)
* spazio dei nomi [GroupDocs.Watermark.Contents.Email](../../groupdocs.watermark.contents.email)
* assemblea [GroupDocs.Watermark](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Watermark.dll -->
