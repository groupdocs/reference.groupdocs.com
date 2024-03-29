---
title: Woff2Font
second_title: GroupDocs.Editor per Riferimento API .NET
description: Rappresenta un font nel formato WOFF2 Web Open Font Format
type: docs
weight: 410
url: /it/net/groupdocs.editor.htmlcss.resources.fonts/woff2font/
---
## Woff2Font class

Rappresenta un font nel formato WOFF2 (Web Open Font Format)

```csharp
public sealed class Woff2Font : FontResourceBase
```

## Costruttori

| Nome | Descrizione |
| --- | --- |
| [Woff2Font](woff2font#constructor)(string, Stream) | Crea una nuova classe Woff2Font dal contenuto, rappresentato come flusso di byte e con il nome specificato |
| [Woff2Font](woff2font#constructor_1)(string, string) | Crea una nuova classe Woff2Font dal contenuto, rappresentata come stringa con codifica base64 e con il nome specificato |

## Proprietà

| Nome | Descrizione |
| --- | --- |
| [ByteContent](../../groupdocs.editor.htmlcss.resources.fonts/fontresourcebase/bytecontent) { get; } | Restituisce il contenuto di questo carattere come flusso di byte |
| [FilenameWithExtension](../../groupdocs.editor.htmlcss.resources.fonts/fontresourcebase/filenamewithextension) { get; } | Restituisce il nome file corretto di questa risorsa font, che consiste in nome ed estensione. Teoricamente può differire dal nome. |
| [IsDisposed](../../groupdocs.editor.htmlcss.resources.fonts/fontresourcebase/isdisposed) { get; } | Determina se questo carattere è eliminato o meno |
| [Name](../../groupdocs.editor.htmlcss.resources.fonts/fontresourcebase/name) { get; } | Restituisce il nome di questa risorsa font. Di solito non contiene l'estensione del nome file e teoricamente può differire dal nome file. |
| [TextContent](../../groupdocs.editor.htmlcss.resources.fonts/fontresourcebase/textcontent) { get; } | Restituisce il contenuto di questo font come stringa con codifica Base64. Questo valore viene memorizzato nella cache dopo la prima chiamata. |
| override [Type](../../groupdocs.editor.htmlcss.resources.fonts/woff2font/type) { get; } | Restituisce FontType.Woff2 |

## Metodi

| Nome | Descrizione |
| --- | --- |
| [Dispose](../../groupdocs.editor.htmlcss.resources.fonts/fontresourcebase/dispose)() | Elimina questa risorsa font, eliminandone il contenuto e rendendo la maggior parte dei metodi e delle proprietà non funzionanti |
| [Equals](../../groupdocs.editor.htmlcss.resources.fonts/fontresourcebase/equals)(FontResourceBase) | Controlla questa istanza con la risorsa font specificata su reference equality |
| [Equals](../../groupdocs.editor.htmlcss.resources.fonts/fontresourcebase/equals)(IHtmlResource) | Controlla questa istanza con la risorsa HTML specificata sull'uguaglianza di riferimento |
| [Save](../../groupdocs.editor.htmlcss.resources.fonts/fontresourcebase/save)(string) | Salva questo font nel file specificato |
| static [IsValid](../../groupdocs.editor.htmlcss.resources.fonts/woff2font/isvalid#isvalid)(Stream) | Controlla se il flusso specificato è un font WOFF2 valido |
| static [IsValid](../../groupdocs.editor.htmlcss.resources.fonts/woff2font/isvalid#isvalid_1)(string) | Controlla se la stringa con codifica Base64 specificata è un font WOFF2 valido |

## Campi

| Nome | Descrizione |
| --- | --- |
| const [RequiredHeaderSize](../../groupdocs.editor.htmlcss.resources.fonts/woff2font/requiredheadersize) | Dimensione dell'intestazione WOFF2 (in byte), necessaria per la sua convalida |

## Eventi

| Nome | Descrizione |
| --- | --- |
| event [Disposed](../../groupdocs.editor.htmlcss.resources.fonts/fontresourcebase/disposed) | Evento che si verifica quando questo font viene eliminato |

### Guarda anche

* class [FontResourceBase](../fontresourcebase)
* spazio dei nomi [GroupDocs.Editor.HtmlCss.Resources.Fonts](../../groupdocs.editor.htmlcss.resources.fonts)
* assemblea [GroupDocs.Editor](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Editor.dll -->
