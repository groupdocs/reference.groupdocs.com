---
title: JpegImage
second_title: GroupDocs.Editor για Αναφορά API .NET
description: Αντιπροσωπεύει μία εικόνα σε μορφή JPEG Joint Photographic Experts Group με τα μεταδεδομένα και τις πρόσθετες μεθόδους
type: docs
weight: 530
url: /el/net/groupdocs.editor.htmlcss.resources.images.raster/jpegimage/
---
## JpegImage class

Αντιπροσωπεύει μία εικόνα σε μορφή JPEG (Joint Photographic Experts Group) με τα μεταδεδομένα και τις πρόσθετες μεθόδους

```csharp
public sealed class JpegImage : RasterImageResourceBase
```

## Κατασκευαστές

| Ονομα | Περιγραφή |
| --- | --- |
| [JpegImage](jpegimage#constructor)(string, Stream) | Δημιουργεί νέα παρουσία JpegImage από περιεχόμενο, που αναπαρίσταται ως ροή byte και με καθορισμένο όνομα |
| [JpegImage](jpegimage#constructor_1)(string, string) | Δημιουργεί νέα παρουσία JpegImage από περιεχόμενο, που αναπαρίσταται ως συμβολοσειρά με κωδικοποίηση base64 και με καθορισμένο όνομα |

## Ιδιότητες

| Ονομα | Περιγραφή |
| --- | --- |
| [AspectRatio](../../groupdocs.editor.htmlcss.resources.images.raster/rasterimageresourcebase/aspectratio) { get; } | Επιστρέφει έναν λόγο διαστάσεων αυτής της εικόνας ως σχέση πλάτους προς ύψος |
| [ByteContent](../../groupdocs.editor.htmlcss.resources.images.raster/rasterimageresourcebase/bytecontent) { get; } | Επιστρέφει περιεχόμενο αυτής της εικόνας ράστερ ως byte stream |
| [FilenameWithExtension](../../groupdocs.editor.htmlcss.resources.images.raster/rasterimageresourcebase/filenamewithextension) { get; } | Επιστρέφει το σωστό όνομα αρχείου αυτής της εικόνας ράστερ, το οποίο αποτελείται από όνομα και επέκταση. Θεωρητικά μπορεί να διαφέρει από το όνομα. |
| [IsDisposed](../../groupdocs.editor.htmlcss.resources.images.raster/rasterimageresourcebase/isdisposed) { get; } | Καθορίζει εάν αυτή η εικόνα ράστερ είναι τοποθετημένη ή όχι |
| [Length](../../groupdocs.editor.htmlcss.resources.images.raster/rasterimageresourcebase/length) { get; } | Επιστρέφει το μήκος αυτού του αρχείου εικόνας ράστερ σε bytes |
| [LinearDimensions](../../groupdocs.editor.htmlcss.resources.images.raster/rasterimageresourcebase/lineardimensions) { get; } | Επιστρέφει γραμμικές διαστάσεις αυτής της εικόνας ράστερ (πλάτος και ύψος) |
| [Name](../../groupdocs.editor.htmlcss.resources.images.raster/rasterimageresourcebase/name) { get; } | Επιστρέφει το όνομα αυτής της εικόνας ράστερ. Συνήθως δεν περιέχει επέκταση ονόματος αρχείου και θεωρητικά μπορεί να διαφέρει από το όνομα αρχείου. |
| [TextContent](../../groupdocs.editor.htmlcss.resources.images.raster/rasterimageresourcebase/textcontent) { get; } | Επιστρέφει περιεχόμενο αυτής της εικόνας ράστερ ως string με κωδικοποίηση base64 |
| override [Type](../../groupdocs.editor.htmlcss.resources.images.raster/jpegimage/type) { get; } | Επιστρέφει ImageType.Jpeg |

## Μέθοδοι

| Ονομα | Περιγραφή |
| --- | --- |
| [Dispose](../../groupdocs.editor.htmlcss.resources.images.raster/rasterimageresourcebase/dispose)() | Απορρίπτει αυτήν την εικόνα ράστερ, απορρίπτει το περιεχόμενό της και καθιστά τις περισσότερες μεθόδους και ιδιότητες μη λειτουργικές |
| [Equals](../../groupdocs.editor.htmlcss.resources.images.raster/rasterimageresourcebase/equals)(IHtmlResource) | Ελέγχει αυτό το στιγμιότυπο με καθορισμένο στην ισότητα αναφοράς. |
| [GenerateBitmap](../../groupdocs.editor.htmlcss.resources.images.raster/rasterimageresourcebase/generatebitmap)() | Δημιουργεί και επιστρέφει μια νέα παρουσία του 'System.Drawing.Bitmap' από αυτήν την εικόνα ράστερ. |
| [ReduceToNewHeight](../../groupdocs.editor.htmlcss.resources.images.raster/jpegimage/reducetonewheight#reducetonewheight)(ushort) | Δημιουργεί και επιστρέφει μια νέα μειωμένη εικόνα JPEG, αλλά με καθορισμένο νέο μειωμένο ύψος και αναλογικά μειωμένο πλάτος. (2 methods) |
| [Save](../../groupdocs.editor.htmlcss.resources.images.raster/rasterimageresourcebase/save)(string) | Αποθηκεύει αυτήν την εικόνα ράστερ στο καθορισμένο αρχείο |
| static [IsValid](../../groupdocs.editor.htmlcss.resources.images.raster/jpegimage/isvalid#isvalid)(Stream) | Ελέγχει εάν η καθορισμένη ροή είναι έγκυρη εικόνα JPEG |
| static [IsValid](../../groupdocs.editor.htmlcss.resources.images.raster/jpegimage/isvalid#isvalid_1)(string) | Ελέγχει εάν η καθορισμένη συμβολοσειρά με κωδικοποίηση base64 είναι έγκυρη εικόνα JPEG |

## Εκδηλώσεις

| Ονομα | Περιγραφή |
| --- | --- |
| event [Disposed](../../groupdocs.editor.htmlcss.resources.images.raster/rasterimageresourcebase/disposed) | Συμβάν, το οποίο συμβαίνει όταν αυτή η εικόνα ράστερ είναι disposed |

### Δείτε επίσης

* class [RasterImageResourceBase](../rasterimageresourcebase)
* χώρος ονομάτων [GroupDocs.Editor.HtmlCss.Resources.Images.Raster](../../groupdocs.editor.htmlcss.resources.images.raster)
* συνέλευση [GroupDocs.Editor](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Editor.dll -->
