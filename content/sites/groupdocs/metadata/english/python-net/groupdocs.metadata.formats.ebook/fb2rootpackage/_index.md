﻿---
title: Fb2RootPackage class
second_title: GroupDocs.Metadata for Python via .NET API References
description: 
type: docs
url: /python-net/groupdocs.metadata.formats.ebook/fb2rootpackage/
is_root: false
weight: 30
---

## Fb2RootPackage class

Represents the root package allowing working with metadata in an Fb2 e-book.



**Inheritance:** [`Fb2RootPackage`](/metadata/python-net/groupdocs.metadata.formats.ebook/fb2rootpackage) → 
[`RootMetadataPackage`](/metadata/python-net/groupdocs.metadata.common/rootmetadatapackage) → 
[`MetadataPackage`](/metadata/python-net/groupdocs.metadata.common/metadatapackage)



The Fb2RootPackage type exposes the following members:

### Properties
| Property | Description |
| :- | :- |
| [metadata_type](/metadata/python-net/groupdocs.metadata.formats.ebook/fb2rootpackage/metadata_type) | Gets the metadata type. |
| [keys](/metadata/python-net/groupdocs.metadata.formats.ebook/fb2rootpackage/keys) | Gets a collection of the metadata property names. |
| [property_descriptors](/metadata/python-net/groupdocs.metadata.formats.ebook/fb2rootpackage/property_descriptors) | Gets a collection of descriptors that contain information about properties accessible through the GroupDocs.Metadata search engine. |
| [count](/metadata/python-net/groupdocs.metadata.formats.ebook/fb2rootpackage/count) | Gets the number of metadata properties. |
| [file_type](/metadata/python-net/groupdocs.metadata.formats.ebook/fb2rootpackage/file_type) | Gets the file type metadata package. |
| [fb_2_package](/metadata/python-net/groupdocs.metadata.formats.ebook/fb2rootpackage/fb_2_package) | Gets the Fb2 metadata package. |


### Methods
| Method | Description |
| :- | :- |
| [contains](/metadata/python-net/groupdocs.metadata.formats.ebook/fb2rootpackage/contains/#str) | Determines whether the package contains a metadata property with the specified name. |
| [find_properties](/metadata/python-net/groupdocs.metadata.formats.ebook/fb2rootpackage/find_properties/#groupdocs.metadata.search.Specification) | Finds the metadata properties satisfying a specification. <br/>The search is recursive so it affects all nested packages as well. |
| [update_properties](/metadata/python-net/groupdocs.metadata.formats.ebook/fb2rootpackage/update_properties/#groupdocs.metadata.search.Specification-groupdocs.metadata.common.PropertyValue) | Updates known metadata properties satisfying a specification.<br/>The operation is recursive so it affects all nested packages as well. |
| [remove_properties](/metadata/python-net/groupdocs.metadata.formats.ebook/fb2rootpackage/remove_properties/#groupdocs.metadata.search.Specification) | Removes metadata properties satisfying a specification. |
| [add_properties](/metadata/python-net/groupdocs.metadata.formats.ebook/fb2rootpackage/add_properties/#groupdocs.metadata.search.Specification-groupdocs.metadata.common.PropertyValue) | Adds known metadata properties satisfying the specification.<br/>The operation is recursive so it affects all nested packages as well. |
| [set_properties](/metadata/python-net/groupdocs.metadata.formats.ebook/fb2rootpackage/set_properties/#groupdocs.metadata.search.Specification-groupdocs.metadata.common.PropertyValue) | Sets known metadata properties satisfying the specification.<br/>The operation is recursive so it affects all nested packages as well.<br/>This method is a combination of [`MetadataPackage.add_properties`](/metadata/python-net/groupdocs.metadata.common/metadatapackage/add_properties) and [`MetadataPackage.update_properties`](/metadata/python-net/groupdocs.metadata.common/metadatapackage/update_properties). <br/>If an existing property satisfies the specification its value is updated. <br/>If there is a known property missing in the package that satisfies the specification it is added to the package. |
| [sanitize](/metadata/python-net/groupdocs.metadata.formats.ebook/fb2rootpackage/sanitize/#) | Removes writable metadata properties from the package.<br/>The operation is recursive so it affects all nested packages as well. |



### Remarks 


**Learn more** |
|
 |

### See Also
* module [`groupdocs.metadata.formats.ebook`](..)
* class [`Fb2RootPackage`](/metadata/python-net/groupdocs.metadata.formats.ebook/fb2rootpackage)
* class [`MetadataPackage`](/metadata/python-net/groupdocs.metadata.common/metadatapackage)
* class [`RootMetadataPackage`](/metadata/python-net/groupdocs.metadata.common/rootmetadatapackage)
