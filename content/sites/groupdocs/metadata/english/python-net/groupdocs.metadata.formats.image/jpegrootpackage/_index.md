﻿---
title: JpegRootPackage class
second_title: GroupDocs.Metadata for Python via .NET API References
description: 
type: docs
url: /python-net/groupdocs.metadata.formats.image/jpegrootpackage/
is_root: false
weight: 160
---

## JpegRootPackage class

Represents the root package allowing working with metadata in a JPEG image.



**Inheritance:** [`JpegRootPackage`](/metadata/python-net/groupdocs.metadata.formats.image/jpegrootpackage) → 
[`ImageRootPackage`](/metadata/python-net/groupdocs.metadata.formats.image/imagerootpackage) → 
[`RootMetadataPackage`](/metadata/python-net/groupdocs.metadata.common/rootmetadatapackage) → 
[`MetadataPackage`](/metadata/python-net/groupdocs.metadata.common/metadatapackage)



The JpegRootPackage type exposes the following members:

### Properties
| Property | Description |
| :- | :- |
| [metadata_type](/metadata/python-net/groupdocs.metadata.formats.image/jpegrootpackage/metadata_type) | Gets the metadata type. |
| [keys](/metadata/python-net/groupdocs.metadata.formats.image/jpegrootpackage/keys) | Gets a collection of the metadata property names. |
| [property_descriptors](/metadata/python-net/groupdocs.metadata.formats.image/jpegrootpackage/property_descriptors) | Gets a collection of descriptors that contain information about properties accessible through the GroupDocs.Metadata search engine. |
| [count](/metadata/python-net/groupdocs.metadata.formats.image/jpegrootpackage/count) | Gets the number of metadata properties. |
| [file_type](/metadata/python-net/groupdocs.metadata.formats.image/jpegrootpackage/file_type) | Gets the file type metadata package. |
| [xmp_package](/metadata/python-net/groupdocs.metadata.formats.image/jpegrootpackage/xmp_package) | Gets or sets the XMP metadata package. |
| [exif_package](/metadata/python-net/groupdocs.metadata.formats.image/jpegrootpackage/exif_package) | Gets or sets the EXIF metadata package. |
| [iptc_package](/metadata/python-net/groupdocs.metadata.formats.image/jpegrootpackage/iptc_package) | Gets or sets the IPTC metadata package. |
| [image_resource_package](/metadata/python-net/groupdocs.metadata.formats.image/jpegrootpackage/image_resource_package) | Gets the Photoshop Image Resource metadata package.<br/>Image resource blocks are the basic building unit of Photoshop native file format. |
| [maker_note_package](/metadata/python-net/groupdocs.metadata.formats.image/jpegrootpackage/maker_note_package) | Gets or sets the MakerNote metadata package. |


### Methods
| Method | Description |
| :- | :- |
| [contains](/metadata/python-net/groupdocs.metadata.formats.image/jpegrootpackage/contains/#str) | Determines whether the package contains a metadata property with the specified name. |
| [find_properties](/metadata/python-net/groupdocs.metadata.formats.image/jpegrootpackage/find_properties/#groupdocs.metadata.search.Specification) | Finds the metadata properties satisfying a specification. <br/>The search is recursive so it affects all nested packages as well. |
| [update_properties](/metadata/python-net/groupdocs.metadata.formats.image/jpegrootpackage/update_properties/#groupdocs.metadata.search.Specification-groupdocs.metadata.common.PropertyValue) | Updates known metadata properties satisfying a specification.<br/>The operation is recursive so it affects all nested packages as well. |
| [remove_properties](/metadata/python-net/groupdocs.metadata.formats.image/jpegrootpackage/remove_properties/#groupdocs.metadata.search.Specification) | Removes metadata properties satisfying a specification. |
| [add_properties](/metadata/python-net/groupdocs.metadata.formats.image/jpegrootpackage/add_properties/#groupdocs.metadata.search.Specification-groupdocs.metadata.common.PropertyValue) | Adds known metadata properties satisfying the specification.<br/>The operation is recursive so it affects all nested packages as well. |
| [set_properties](/metadata/python-net/groupdocs.metadata.formats.image/jpegrootpackage/set_properties/#groupdocs.metadata.search.Specification-groupdocs.metadata.common.PropertyValue) | Sets known metadata properties satisfying the specification.<br/>The operation is recursive so it affects all nested packages as well.<br/>This method is a combination of [`MetadataPackage.add_properties`](/metadata/python-net/groupdocs.metadata.common/metadatapackage/add_properties) and [`MetadataPackage.update_properties`](/metadata/python-net/groupdocs.metadata.common/metadatapackage/update_properties). <br/>If an existing property satisfies the specification its value is updated. <br/>If there is a known property missing in the package that satisfies the specification it is added to the package. |
| [sanitize](/metadata/python-net/groupdocs.metadata.formats.image/jpegrootpackage/sanitize/#) | Removes writable metadata properties from the package.<br/>The operation is recursive so it affects all nested packages as well. |
| [remove_image_resource_package](/metadata/python-net/groupdocs.metadata.formats.image/jpegrootpackage/remove_image_resource_package/#) | Removes Photoshop Image Resource metadata package. |
| [detect_barcode_types](/metadata/python-net/groupdocs.metadata.formats.image/jpegrootpackage/detect_barcode_types/#) | Extracts the types of the barcodes presented in the image. |



### Remarks 


**Learn more** |
|
 |
 |
 |
 |

### See Also
* module [`groupdocs.metadata.formats.image`](..)
* class [`ImageRootPackage`](/metadata/python-net/groupdocs.metadata.formats.image/imagerootpackage)
* class [`JpegRootPackage`](/metadata/python-net/groupdocs.metadata.formats.image/jpegrootpackage)
* class [`MetadataPackage`](/metadata/python-net/groupdocs.metadata.common/metadatapackage)
* class [`RootMetadataPackage`](/metadata/python-net/groupdocs.metadata.common/rootmetadatapackage)
