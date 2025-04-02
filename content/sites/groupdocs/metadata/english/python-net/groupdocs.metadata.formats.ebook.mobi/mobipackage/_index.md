﻿---
title: MobiPackage class
second_title: GroupDocs.Metadata for Python via .NET API References
description: 
type: docs
url: /python-net/groupdocs.metadata.formats.ebook.mobi/mobipackage/
is_root: false
weight: 20
---

## MobiPackage class

Represents metadata in a Mobi e-book.



**Inheritance:** [`MobiPackage`](/metadata/python-net/groupdocs.metadata.formats.ebook.mobi/mobipackage) → 
[`CustomPackage`](/metadata/python-net/groupdocs.metadata.common/custompackage) → 
[`MetadataPackage`](/metadata/python-net/groupdocs.metadata.common/metadatapackage)



The MobiPackage type exposes the following members:

### Properties
| Property | Description |
| :- | :- |
| [metadata_type](/metadata/python-net/groupdocs.metadata.formats.ebook.mobi/mobipackage/metadata_type) | Gets the metadata type. |
| [keys](/metadata/python-net/groupdocs.metadata.formats.ebook.mobi/mobipackage/keys) | Gets a collection of the metadata property names. |
| [property_descriptors](/metadata/python-net/groupdocs.metadata.formats.ebook.mobi/mobipackage/property_descriptors) | Gets a collection of descriptors that contain information about properties accessible through the GroupDocs.Metadata search engine. |
| [count](/metadata/python-net/groupdocs.metadata.formats.ebook.mobi/mobipackage/count) | Gets the number of metadata properties. |
| [pdb_header](/metadata/python-net/groupdocs.metadata.formats.ebook.mobi/mobipackage/pdb_header) |  |
| [mobi_header](/metadata/python-net/groupdocs.metadata.formats.ebook.mobi/mobipackage/mobi_header) |  |


### Methods
| Method | Description |
| :- | :- |
| [contains](/metadata/python-net/groupdocs.metadata.formats.ebook.mobi/mobipackage/contains/#str) | Determines whether the package contains a metadata property with the specified name. |
| [find_properties](/metadata/python-net/groupdocs.metadata.formats.ebook.mobi/mobipackage/find_properties/#groupdocs.metadata.search.Specification) | Finds the metadata properties satisfying a specification. <br/>The search is recursive so it affects all nested packages as well. |
| [update_properties](/metadata/python-net/groupdocs.metadata.formats.ebook.mobi/mobipackage/update_properties/#groupdocs.metadata.search.Specification-groupdocs.metadata.common.PropertyValue) | Updates known metadata properties satisfying a specification.<br/>The operation is recursive so it affects all nested packages as well. |
| [remove_properties](/metadata/python-net/groupdocs.metadata.formats.ebook.mobi/mobipackage/remove_properties/#groupdocs.metadata.search.Specification) | Removes metadata properties satisfying a specification. |
| [add_properties](/metadata/python-net/groupdocs.metadata.formats.ebook.mobi/mobipackage/add_properties/#groupdocs.metadata.search.Specification-groupdocs.metadata.common.PropertyValue) | Adds known metadata properties satisfying the specification.<br/>The operation is recursive so it affects all nested packages as well. |
| [set_properties](/metadata/python-net/groupdocs.metadata.formats.ebook.mobi/mobipackage/set_properties/#groupdocs.metadata.search.Specification-groupdocs.metadata.common.PropertyValue) | Sets known metadata properties satisfying the specification.<br/>The operation is recursive so it affects all nested packages as well.<br/>This method is a combination of [`MetadataPackage.add_properties`](/metadata/python-net/groupdocs.metadata.common/metadatapackage/add_properties) and [`MetadataPackage.update_properties`](/metadata/python-net/groupdocs.metadata.common/metadatapackage/update_properties). <br/>If an existing property satisfies the specification its value is updated. <br/>If there is a known property missing in the package that satisfies the specification it is added to the package. |
| [sanitize](/metadata/python-net/groupdocs.metadata.formats.ebook.mobi/mobipackage/sanitize/#) | Removes writable metadata properties from the package.<br/>The operation is recursive so it affects all nested packages as well. |



### Remarks 


**Learn more** |
|
 |

### See Also
* module [`groupdocs.metadata.formats.ebook.mobi`](..)
* class [`CustomPackage`](/metadata/python-net/groupdocs.metadata.common/custompackage)
* class [`MetadataPackage`](/metadata/python-net/groupdocs.metadata.common/metadatapackage)
* class [`MobiPackage`](/metadata/python-net/groupdocs.metadata.formats.ebook.mobi/mobipackage)
