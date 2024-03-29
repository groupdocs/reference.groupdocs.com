---
title: MpegAudioPackage
second_title: .NET API संदर्भ के लिए GroupDocs.Metadata
description: एमपईज ऑडय मेटडेट पैकेज प्रप्त करत है
type: docs
weight: 50
url: /hi/net/groupdocs.metadata.formats.audio/mp3rootpackage/mpegaudiopackage/
---
## MP3RootPackage.MpegAudioPackage property

एमपीईजी ऑडियो मेटाडेटा पैकेज प्राप्त करता है।

```csharp
public MpegAudioPackage MpegAudioPackage { get; }
```

### संपत्ति मूल्य

एमपीईजी ऑडियो मेटाडाटा पैकेज.

### उदाहरण

यह उदाहरण दर्शाता है कि एमपी3 फ़ाइल से एमपीईजी ऑडियो मेटाडेटा कैसे पढ़ा जाए।

```csharp
using (Metadata metadata = new Metadata(Constants.MP3WithID3V2))
{
    var root = metadata.GetRootPackage<MP3RootPackage>();

    Console.WriteLine(root.MpegAudioPackage.Bitrate);
    Console.WriteLine(root.MpegAudioPackage.ChannelMode);
    Console.WriteLine(root.MpegAudioPackage.Emphasis);
    Console.WriteLine(root.MpegAudioPackage.Frequency);
    Console.WriteLine(root.MpegAudioPackage.HeaderPosition);
    Console.WriteLine(root.MpegAudioPackage.Layer);

    // ...
}
```

### यह सभी देखें

* class [MpegAudioPackage](../../../groupdocs.metadata.formats.mpeg/mpegaudiopackage)
* class [MP3RootPackage](../../mp3rootpackage)
* नाम स्थान [GroupDocs.Metadata.Formats.Audio](../../mp3rootpackage)
* सभा [GroupDocs.Metadata](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Metadata.dll -->
