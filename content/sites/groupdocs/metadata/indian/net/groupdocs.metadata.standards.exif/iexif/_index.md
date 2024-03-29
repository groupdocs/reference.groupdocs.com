---
title: IExif
second_title: .NET API संदर्भ के लिए GroupDocs.Metadata
description: EXIF मेटडेट के सथ कम करने के उद्देश्य से बेस ऑपरेशंस क परभषत करत है
type: docs
weight: 2800
url: /hi/net/groupdocs.metadata.standards.exif/iexif/
---
## IExif interface

EXIF मेटाडेटा के साथ काम करने के उद्देश्य से बेस ऑपरेशंस को परिभाषित करता है।

```csharp
public interface IExif
```

## गुण

| नाम | विवरण |
| --- | --- |
| [ExifPackage](../../groupdocs.metadata.standards.exif/iexif/exifpackage) { get; set; } | फ़ाइल से जुड़े EXIF मेटाडेटा पैकेज को प्राप्त या सेट करता है। |

### टिप्पणियों

**और अधिक जानें**

* [EXIF मेटाडेटा के साथ काम करना](https://docs.groupdocs.com/display/metadatanet/Working+with+EXIF+metadata)

### उदाहरण

यह कोड नमूना प्रदर्शित करता है कि बुनियादी EXIF मेटाडेटा गुणों को कैसे निकाला जाए।

```csharp
using (Metadata metadata = new Metadata(Constants.TiffWithExif))
{
    IExif root = metadata.GetRootPackage() as IExif;
    if (root != null && root.ExifPackage != null)
    {
        Console.WriteLine(root.ExifPackage.Artist);
        Console.WriteLine(root.ExifPackage.Copyright);
        Console.WriteLine(root.ExifPackage.ImageDescription);
        Console.WriteLine(root.ExifPackage.Make);
        Console.WriteLine(root.ExifPackage.Model);
        Console.WriteLine(root.ExifPackage.Software);
        Console.WriteLine(root.ExifPackage.ImageWidth);
        Console.WriteLine(root.ExifPackage.ImageLength);

        // ...

        Console.WriteLine(root.ExifPackage.ExifIfdPackage.BodySerialNumber);
        Console.WriteLine(root.ExifPackage.ExifIfdPackage.CameraOwnerName);
        Console.WriteLine(root.ExifPackage.ExifIfdPackage.UserComment);

        // ...

        Console.WriteLine(root.ExifPackage.GpsPackage.Altitude);
        Console.WriteLine(root.ExifPackage.GpsPackage.LatitudeRef);
        Console.WriteLine(root.ExifPackage.GpsPackage.LongitudeRef);

        // ...
    }
}
```

### यह सभी देखें

* नाम स्थान [GroupDocs.Metadata.Standards.Exif](../../groupdocs.metadata.standards.exif)
* सभा [GroupDocs.Metadata](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Metadata.dll -->
