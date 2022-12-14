---
title: ForeignKeyConstraint
second_title: GroupDocs.Assembly for Java API Reference
description: Represents an action restriction enforced on a set of columns in a primary key/foreign key relationship when a value or row is either deleted or updated.
type: docs
weight: 29
url: /java/com.groupdocs.assembly.system.data/foreignkeyconstraint/
---
**Inheritance:**
java.lang.Object, [com.groupdocs.assembly.system.data.Constraint](../../com.groupdocs.assembly.system.data/constraint)
```
public class ForeignKeyConstraint extends Constraint
```

Represents an action restriction enforced on a set of columns in a primary key/foreign key relationship when a value or row is either deleted or updated.
## Constructors

| Constructor | Description |
| --- | --- |
| [ForeignKeyConstraint(String constraintName, DataColumn[] parentColumns, DataColumn[] childColumns)](#ForeignKeyConstraint-java.lang.String-com.groupdocs.assembly.system.data.DataColumn---com.groupdocs.assembly.system.data.DataColumn---) | Initializes a new instance of the [ForeignKeyConstraint](../../com.groupdocs.assembly.system.data/foreignkeyconstraint) class with the specified name, and arrays of parent and child [DataColumn](../../com.groupdocs.assembly.system.data/datacolumn) objects. |
| [ForeignKeyConstraint(DataColumn parentColumn, DataColumn childColumn)](#ForeignKeyConstraint-com.groupdocs.assembly.system.data.DataColumn-com.groupdocs.assembly.system.data.DataColumn-) | Initializes a new instance of the [ForeignKeyConstraint](../../com.groupdocs.assembly.system.data/foreignkeyconstraint) class with the specified parent and child [DataColumn](../../com.groupdocs.assembly.system.data/datacolumn) objects. |
| [ForeignKeyConstraint(String constraintName, DataColumn parentColumn, DataColumn childColumn)](#ForeignKeyConstraint-java.lang.String-com.groupdocs.assembly.system.data.DataColumn-com.groupdocs.assembly.system.data.DataColumn-) | Initializes a new instance of the [ForeignKeyConstraint](../../com.groupdocs.assembly.system.data/foreignkeyconstraint) class with the specified name, parent and child [DataColumn](../../com.groupdocs.assembly.system.data/datacolumn) objects. |
## Methods

| Method | Description |
| --- | --- |
| [getDeleteRule()](#getDeleteRule--) | Gets the action that occurs across this constraint when a row is deleted. |
| [getUpdateRule()](#getUpdateRule--) | Gets the action that occurs across this constraint on when a row is updated. |
| [hashCode()](#hashCode--) |  |
| [equals(Object key)](#equals-java.lang.Object-) | Gets a value indicating whether the current [ForeignKeyConstraint](../../com.groupdocs.assembly.system.data/foreignkeyconstraint) is identical to the specified object. |
| [getColumns()](#getColumns--) | Gets the child columns of this constraint. |
| [getRelatedColumns()](#getRelatedColumns--) | The parent columns of this constraint. |
| [getTable()](#getTable--) | Gets the child table of this constraint. |
| [getRelatedTable()](#getRelatedTable--) | Gets the parent table of this constraint. |
### ForeignKeyConstraint(String constraintName, DataColumn[] parentColumns, DataColumn[] childColumns) {#ForeignKeyConstraint-java.lang.String-com.groupdocs.assembly.system.data.DataColumn---com.groupdocs.assembly.system.data.DataColumn---}
```
public ForeignKeyConstraint(String constraintName, DataColumn[] parentColumns, DataColumn[] childColumns)
```


Initializes a new instance of the [ForeignKeyConstraint](../../com.groupdocs.assembly.system.data/foreignkeyconstraint) class with the specified name, and arrays of parent and child [DataColumn](../../com.groupdocs.assembly.system.data/datacolumn) objects.

**Parameters:**
| Parameter | Type | Description |
| --- | --- | --- |
| constraintName | java.lang.String | The name of the [ForeignKeyConstraint](../../com.groupdocs.assembly.system.data/foreignkeyconstraint). If null or empty string, a default name will be given when added to the constraints collection. |
| parentColumns | [DataColumn\[\]](../../com.groupdocs.assembly.system.data/datacolumn) | An array of parent [DataColumn](../../com.groupdocs.assembly.system.data/datacolumn) in the constraint. |
| childColumns | [DataColumn\[\]](../../com.groupdocs.assembly.system.data/datacolumn) | An array of child [DataColumn](../../com.groupdocs.assembly.system.data/datacolumn) in the constraint. |

### ForeignKeyConstraint(DataColumn parentColumn, DataColumn childColumn) {#ForeignKeyConstraint-com.groupdocs.assembly.system.data.DataColumn-com.groupdocs.assembly.system.data.DataColumn-}
```
public ForeignKeyConstraint(DataColumn parentColumn, DataColumn childColumn)
```


Initializes a new instance of the [ForeignKeyConstraint](../../com.groupdocs.assembly.system.data/foreignkeyconstraint) class with the specified parent and child [DataColumn](../../com.groupdocs.assembly.system.data/datacolumn) objects.

**Parameters:**
| Parameter | Type | Description |
| --- | --- | --- |
| parentColumn | [DataColumn](../../com.groupdocs.assembly.system.data/datacolumn) | The parent [DataColumn](../../com.groupdocs.assembly.system.data/datacolumn) in the constraint. |
| childColumn | [DataColumn](../../com.groupdocs.assembly.system.data/datacolumn) | The child [DataColumn](../../com.groupdocs.assembly.system.data/datacolumn) in the constraint. |

### ForeignKeyConstraint(String constraintName, DataColumn parentColumn, DataColumn childColumn) {#ForeignKeyConstraint-java.lang.String-com.groupdocs.assembly.system.data.DataColumn-com.groupdocs.assembly.system.data.DataColumn-}
```
public ForeignKeyConstraint(String constraintName, DataColumn parentColumn, DataColumn childColumn)
```


Initializes a new instance of the [ForeignKeyConstraint](../../com.groupdocs.assembly.system.data/foreignkeyconstraint) class with the specified name, parent and child [DataColumn](../../com.groupdocs.assembly.system.data/datacolumn) objects.

**Parameters:**
| Parameter | Type | Description |
| --- | --- | --- |
| constraintName | java.lang.String | The name of the constraint. |
| parentColumn | [DataColumn](../../com.groupdocs.assembly.system.data/datacolumn) | The parent [DataColumn](../../com.groupdocs.assembly.system.data/datacolumn) in the constraint. |
| childColumn | [DataColumn](../../com.groupdocs.assembly.system.data/datacolumn) | The child [DataColumn](../../com.groupdocs.assembly.system.data/datacolumn) in the constraint. |

### getDeleteRule() {#getDeleteRule--}
```
public Rule getDeleteRule()
```


Gets the action that occurs across this constraint when a row is deleted.

**Returns:**
[Rule](../../com.groupdocs.assembly.system.data/rule) - One of the [Rule](../../com.groupdocs.assembly.system.data/rule) values. The default is Cascade. The returned value is one of [Rule](../../com.groupdocs.assembly.system.data/rule) constants.
### getUpdateRule() {#getUpdateRule--}
```
public Rule getUpdateRule()
```


Gets the action that occurs across this constraint on when a row is updated.

**Returns:**
[Rule](../../com.groupdocs.assembly.system.data/rule) - One of the [Rule](../../com.groupdocs.assembly.system.data/rule) values. The default is Cascade. The returned value is one of [Rule](../../com.groupdocs.assembly.system.data/rule) constants.
### hashCode() {#hashCode--}
```
public int hashCode()
```




**Returns:**
int
### equals(Object key) {#equals-java.lang.Object-}
```
public boolean equals(Object key)
```


Gets a value indicating whether the current [ForeignKeyConstraint](../../com.groupdocs.assembly.system.data/foreignkeyconstraint) is identical to the specified object.

**Parameters:**
| Parameter | Type | Description |
| --- | --- | --- |
| key | java.lang.Object | The object to which this [ForeignKeyConstraint](../../com.groupdocs.assembly.system.data/foreignkeyconstraint) is compared. Two [ForeignKeyConstraint](../../com.groupdocs.assembly.system.data/foreignkeyconstraint) are equal if they constrain the same columns. |

**Returns:**
boolean - true, if the objects are identical; otherwise, false.
### getColumns() {#getColumns--}
```
public DataColumn[] getColumns()
```


Gets the child columns of this constraint.

**Returns:**
com.groupdocs.assembly.system.data.DataColumn[] - An array of [DataColumn](../../com.groupdocs.assembly.system.data/datacolumn) objects that are the child columns of the constraint.
### getRelatedColumns() {#getRelatedColumns--}
```
public DataColumn[] getRelatedColumns()
```


The parent columns of this constraint.

**Returns:**
com.groupdocs.assembly.system.data.DataColumn[] - An array of [DataColumn](../../com.groupdocs.assembly.system.data/datacolumn) objects that are the parent columns of the constraint.
### getTable() {#getTable--}
```
public DataTable getTable()
```


Gets the child table of this constraint.

**Returns:**
[DataTable](../../com.groupdocs.assembly.system.data/datatable) - A [DataTable](../../com.groupdocs.assembly.system.data/datatable) that is the child table in the constraint.
### getRelatedTable() {#getRelatedTable--}
```
public DataTable getRelatedTable()
```


Gets the parent table of this constraint.

**Returns:**
[DataTable](../../com.groupdocs.assembly.system.data/datatable) - The parent [DataTable](../../com.groupdocs.assembly.system.data/datatable) of this constraint.
