﻿---
title: CmsPackage class
second_title: GroupDocs.Metadata for Python via .NET API References
description: 
type: docs
url: /python-net/groupdocs.metadata.standards.pkcs/cmspackage/
is_root: false
weight: 50
---

## CmsPackage class

Represents a CMS digital signature metadata package.



**Inheritance:** [`CmsPackage`](/metadata/python-net/groupdocs.metadata.standards.pkcs/cmspackage) → 
[`CustomPackage`](/metadata/python-net/groupdocs.metadata.common/custompackage) → 
[`MetadataPackage`](/metadata/python-net/groupdocs.metadata.common/metadatapackage)



The CmsPackage type exposes the following members:

### Properties
| Property | Description |
| :- | :- |
| [metadata_type](/metadata/python-net/groupdocs.metadata.standards.pkcs/cmspackage/metadata_type) | Gets the metadata type. |
| [keys](/metadata/python-net/groupdocs.metadata.standards.pkcs/cmspackage/keys) | Gets a collection of the metadata property names. |
| [property_descriptors](/metadata/python-net/groupdocs.metadata.standards.pkcs/cmspackage/property_descriptors) | Gets a collection of descriptors that contain information about properties accessible through the GroupDocs.Metadata search engine. |
| [count](/metadata/python-net/groupdocs.metadata.standards.pkcs/cmspackage/count) | Gets the number of metadata properties. |
| [signatures](/metadata/python-net/groupdocs.metadata.standards.pkcs/cmspackage/signatures) | Gets an array of the signatures extracted from the file. |
| [flags](/metadata/python-net/groupdocs.metadata.standards.pkcs/cmspackage/flags) | Gets the digital signature flags. |


### Methods
| Method | Description |
| :- | :- |
| [contains](/metadata/python-net/groupdocs.metadata.standards.pkcs/cmspackage/contains/#str) | Determines whether the package contains a metadata property with the specified name. |
| [find_properties](/metadata/python-net/groupdocs.metadata.standards.pkcs/cmspackage/find_properties/#groupdocs.metadata.search.Specification) | Finds the metadata properties satisfying a specification. <br/>The search is recursive so it affects all nested packages as well. |
| [update_properties](/metadata/python-net/groupdocs.metadata.standards.pkcs/cmspackage/update_properties/#groupdocs.metadata.search.Specification-groupdocs.metadata.common.PropertyValue) | Updates known metadata properties satisfying a specification.<br/>The operation is recursive so it affects all nested packages as well. |
| [remove_properties](/metadata/python-net/groupdocs.metadata.standards.pkcs/cmspackage/remove_properties/#groupdocs.metadata.search.Specification) | Removes metadata properties satisfying a specification. |
| [add_properties](/metadata/python-net/groupdocs.metadata.standards.pkcs/cmspackage/add_properties/#groupdocs.metadata.search.Specification-groupdocs.metadata.common.PropertyValue) | Adds known metadata properties satisfying the specification.<br/>The operation is recursive so it affects all nested packages as well. |
| [set_properties](/metadata/python-net/groupdocs.metadata.standards.pkcs/cmspackage/set_properties/#groupdocs.metadata.search.Specification-groupdocs.metadata.common.PropertyValue) | Sets known metadata properties satisfying the specification.<br/>The operation is recursive so it affects all nested packages as well.<br/>This method is a combination of [`MetadataPackage.add_properties`](/metadata/python-net/groupdocs.metadata.common/metadatapackage/add_properties) and [`MetadataPackage.update_properties`](/metadata/python-net/groupdocs.metadata.common/metadatapackage/update_properties). <br/>If an existing property satisfies the specification its value is updated. <br/>If there is a known property missing in the package that satisfies the specification it is added to the package. |
| [sanitize](/metadata/python-net/groupdocs.metadata.standards.pkcs/cmspackage/sanitize/#) | Removes writable metadata properties from the package.<br/>The operation is recursive so it affects all nested packages as well. |



### See Also
* module [`groupdocs.metadata.standards.pkcs`](..)
* class [`CmsPackage`](/metadata/python-net/groupdocs.metadata.standards.pkcs/cmspackage)
* class [`CustomPackage`](/metadata/python-net/groupdocs.metadata.common/custompackage)
* class [`MetadataPackage`](/metadata/python-net/groupdocs.metadata.common/metadatapackage)
