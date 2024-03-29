---
title: SpreadsheetFormat
second_title: Riferimento API GroupDocs.Metadata per .NET
description: Definisce vari sottoformati del foglio di calcolo.
type: docs
weight: 1180
url: /it/net/groupdocs.metadata.formats.document/spreadsheetformat/
---
## SpreadsheetFormat enumeration

Definisce vari sottoformati del foglio di calcolo.

```csharp
public enum SpreadsheetFormat
```

### I valori

| Nome | Valore | Descrizione |
| --- | --- | --- |
| Unknown | `0` | Il formato non è riconosciuto. |
| Xls | `1` | Rappresenta il formato Excel .XLS. I file con estensione XLS rappresentano il formato file binario di Excel. Tali file possono essere creati da Microsoft Excel e da altri programmi di fogli di calcolo simili come OpenOffice Calc o Apple Numbers. Il file salvato da Excel è noto come Cartella di lavoro in cui ogni cartella di lavoro può avere uno o più fogli di lavoro. Ulteriori informazioni su questo formato di file[Qui](https://wiki.fileformat.com/spreadsheet/xls/) . |
| Xlsb | `2` | Rappresenta il formato Excel .XLSB. Il formato file XLSB specifica il formato file binario Excel, ovvero una raccolta di record e strutture che specificano il contenuto della cartella di lavoro di Excel. Il contenuto può includere tabelle non strutturate o semi-strutturate di numeri, testo o sia numeri che testo, formule, connessioni dati esterne, grafici e immagini. Ulteriori informazioni su questo formato di file[Qui](https://wiki.fileformat.com/spreadsheet/xlsb/) . |
| Xlsx | `3` | Rappresenta il formato Excel .XLSX. XLSX è un formato ben noto per i documenti Microsoft Excel introdotto da Microsoft con il rilascio di Microsoft Office 2007. Basato su una struttura organizzata secondo le Convenzioni Open Packaging come delineato nella Parte 2 del OOXML standard ECMA-376, il nuovo formato è un pacchetto zip che contiene una serie di file XML. Ulteriori informazioni su questo formato di file[Qui](https://wiki.fileformat.com/spreadsheet/xlsx/) . |
| Xlsm | `4` | Rappresenta il formato Excel .XLSM. I file con estensione XLSM sono un tipo di file Spreasheet che supportano le macro. Dal punto di vista dell'applicazione, una macro è un insieme di istruzioni utilizzate per automatizzare i processi. Una macro viene utilizzata per registrare i passaggi che vengono eseguiti ripetutamente e facilita l'esecuzione delle azioni eseguendo nuovamente la macro. Ulteriori informazioni su questo formato di file[Qui](https://wiki.fileformat.com/spreadsheet/xlsm/) . |
| Xltx | `5` | Rappresenta il formato Excel .XLTX. I file con estensione XLTX rappresentano i file modello Microsoft Excel basati sulle specifiche del formato file Office OpenXML. Viene utilizzato per creare un file modello standard che può essere utilizzato per generare file XLSX che presentano il stesse impostazioni specificate nel file XLTX. Ulteriori informazioni su questo formato di file[Qui](https://wiki.fileformat.com/spreadsheet/xltx/) . |
| Xltm | `6` | Rappresenta il formato .XLTM Excel. L'estensione del file XLTM rappresenta i file generati da Microsoft Excel come file modello con attivazione macro. I file XLTM sono simili a XLTX nella struttura, a parte il fatto che il successivo non supporta la creazione di file modello con macros. Tali file modello vengono utilizzati per generare e impostare il layout, la formattazione e altre impostazioni insieme alle macro per facilitare la creazione di file XLSX simili. Ulteriori informazioni su questo formato di file[Qui](https://wiki.fileformat.com/spreadsheet/xltm/) . |
| Ods | `7` | Rappresenta il formato Opendocument Spreadsheet. I file con estensione ODS rappresentano il formato OpenDocument Spreadsheet Document modificabile dall'utente. I dati vengono memorizzati all'interno del file ODF in righe e colonne. È un formato basato su XML ed è uno dei numerosi sottotipi nella famiglia Open Document Formats (ODF). Ulteriori informazioni su questo formato di file[Qui](https://wiki.fileformat.com/spreadsheet/ods/) . |
| Xlt | `8` | Rappresenta il formato .XLT Excel. I file con estensione .XLT sono file modello creati con Microsoft Excel, un'applicazione per fogli di calcolo inclusa nella suite Microsoft Office. Microsoft Office 97-2003 supportava la creazione di nuovi file XLT e l'apertura these. L'ultima versione di Excel è ancora in grado di aprire i file modello di questo vecchio formato. Ulteriori informazioni su questo formato di file[Qui](https://wiki.fileformat.com/spreadsheet/xlt/) . |

### Guarda anche

* spazio dei nomi [GroupDocs.Metadata.Formats.Document](../../groupdocs.metadata.formats.document)
* assemblea [GroupDocs.Metadata](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Metadata.dll -->
