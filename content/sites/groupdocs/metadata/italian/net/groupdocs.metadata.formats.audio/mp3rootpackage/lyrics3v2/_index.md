---
title: Lyrics3V2
second_title: Riferimento API GroupDocs.Metadata per .NET
description: Ottiene o imposta il tag dei metadati di Lyrics3v2.
type: docs
weight: 40
url: /it/net/groupdocs.metadata.formats.audio/mp3rootpackage/lyrics3v2/
---
## MP3RootPackage.Lyrics3V2 property

Ottiene o imposta il tag dei metadati di Lyrics3v2.

```csharp
public LyricsTag Lyrics3V2 { get; set; }
```

### Valore della proprietà

Il tag dei metadati di Lyrics3v2.

### Esempi

Questo esempio mostra come aggiornare il tag Lyrics in un file MP3

```csharp
using (Metadata metadata = new Metadata(Constants.MP3WithLyrics))
{
    var root = metadata.GetRootPackage<MP3RootPackage>();

    if (root.Lyrics3V2 == null)
    {
        root.Lyrics3V2 = new LyricsTag();
    }

    root.Lyrics3V2.Lyrics = "[00:01]Test lyrics";
    root.Lyrics3V2.Artist = "test artist";
    root.Lyrics3V2.Album = "test album";
    root.Lyrics3V2.Track = "test track";

    // Puoi aggiungere un campo completamente personalizzato al tag
    root.Lyrics3V2.Set(new LyricsField("ABC", "custom value"));

    //...

    metadata.Save(Constants.OutputMp3);
}
```

### Guarda anche

* class [LyricsTag](../../lyricstag)
* class [MP3RootPackage](../../mp3rootpackage)
* spazio dei nomi [GroupDocs.Metadata.Formats.Audio](../../mp3rootpackage)
* assemblea [GroupDocs.Metadata](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Metadata.dll -->
