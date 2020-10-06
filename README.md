# Amazon DynamoDB Tutorials
Create and manage a Nonrelational Database with Amazon DynamoDB

## DynamoDB concepts
- Table: A collection of DynamoDB data records.
- Item: A single data record in a DynamoDB table. It is comparable to a row in a relational database.
- Attribute: A single data element on an item. It is comparable to a column in a relational database. However, unlike columns in a relational database, attributes do not need to be specified at table creation, other than the primary key discussed later in this module. Attributes can be simple types such as strings, integers, or Boolean, or they can be complex types such as lists or maps.
- Primary key: A primary key is a unique identifier for a single item in a DynamoDB table. The primary key name and type must be specified on table creation, and a primary key of the specified type must be included with each item written to a table. A simple primary key consists of a single attribute, and a composite primary key consists of two attributes: a partition key and a sort key. For example, you can create a simple primary key using “UserID” as an identifier, or create a composite primary key by combining “UserID” and “Creation_Date” as an item identifier.

## Prerequisite
Configure AWS CLI
``` bash
$ aws configure
AWS Access Key ID [None]: AWS_ACCESS_KEY_ID
AWS Secret Access Key [None]: AWS_SECRET_ACCESS_KEY
Default region name [None]: us-west-2
Default output format [None]: json
```

## 1. [Query and manage DynamoDB tables using Python](https://aws.amazon.com/getting-started/hands-on/create-manage-nonrelational-database-dynamodb/)
Learn how to insert data, run queries, create indexes, and update items by using the Python SDK.

Download support code
```
curl -sL https://s3.amazonaws.com/ddb-deep-dive/dynamodb.tar | tar -xv
```

## 2. [Model a DynamoDB database for gaming applications](https://aws.amazon.com/getting-started/projects/data-modeling-gaming-app-with-dynamodb/)
Learn how to design a data model for access patterns used in gaming apps using DynamoDB.

Download support code
```
curl -sL https://s3.amazonaws.com/ddb-labs/battle-royale.tar | tar -xv
```

Achieving best results with a NoSQL database such as DynamoDB requires a shift in thinking from the typical relational database. Use the following best practices when modeling data with DynamoDB.

1. Focus on access patterns
    - In DynamoDB, you think about access patterns before modeling your table. NoSQL databases are focused on speed, not flexibility. You first ask how you will access your data, and then model your data in the shape it will be accessed.
    - Before designing your DynamoDB table, document every need you have for reading and writing data in your application. Be thorough and think about all the flows in your application because you are going to optimize your table for your access patterns.

2. Optimize for the number of requests to DynamoDB
    - After you have documented your application’s access pattern needs, you are ready to design your table. You should design your table to minimize the number of requests to DynamoDB for each access pattern. 
    - Ideally, each access pattern should require only a single request to DynamoDB because network requests are slow, and this limits the number of network requests you will make in your application.

3. Don’t fake a relational model
    - People new to DynamoDB often try to implement a relational model on top of nonrelational DynamoDB. If you try to do this, you will lose most of the benefits of DynamoDB.


### DynamoDB Antipatterns
- **Normalization:**  In a relational database, you normalize your data to reduce data redundancy and storage space, and then use joins to combine multiple different tables. However, joins at scale are slow and expensive. DynamoDB does not allow for joins because they slow down as your table grows.

- **One data type per table:** Your DynamoDB table will often include different types of data in a single table. In our example, we have User, Game, and UserGameMapping entities in a single table. In a relational database, this would be modeled as three different tables.

- **Too many secondary indexes:** People often try to create a secondary index for each additional access pattern they need. DynamoDB is schemaless, and this applies to your indexes, too. Use the flexibility in your attributes to reuse a single secondary index across multiple data types in your table. This is called index overloading.

### Primary Key Best Practices
- Start with the different entities in your table. If you are storing multiple different types of data in a single table—such as employees, departments, customers, and orders—be sure your primary key has a way to distinctly identify each entity and enable core actions on individual items.
- Use prefixes to distinguish between entity types. Using prefixes to distinguish between entity types can prevent collisions and assist in querying. For example, if you have both customers and employees in the same table, the primary key for a customer could be CUSTOMER#<CUSTOMERID>, and the primary key for an employee could be EMPLOYEE#<EMPLOYEEID>.
- Focus on single-item actions first, and then add multiple-item actions if possible. For a primary key, it’s important that you can satisfy the read and write options on a single item by using the single-item APIs: GetItem, PutItem, UpdateItem, and DeleteItem. You may also be able to satisfy your multiple-item read patterns with the primary key by using Query. If not, you can add a secondary index to handle the Query use cases.

- If your data model has multiple entities with relationships among them, you generally use a composite primary key with both HASH and RANGE values. 
- The composite primary key gives us the Query ability on the HASH key to satisfy one of the query patterns we need. In the DynamoDB documentation, the partition key is called HASH and the sort key is called RANGE,

- Because we’re storing different entities in a single table, we can’t use primary key attribute names such as UserId. The attribute means something different based on the type of entity being stored. For example, the primary key for a user might be its USERNAME, and the primary key for a game might be its GAMEID. Accordingly, we use generic names for the attributes, such as PK (for partition key) and SK (for sort key).

- You should optimize DynamoDB tables for the number of requests it receives. We also mentioned that DynamoDB does not have joins that a relational database has. Instead, you design your table to allow for join-like behavior in your requests.

 - In a relational database, you use joins to retrieve multiple entity types from different tables in a single request. With DynamoDB, you specifically model your data, so that entities you should access together are located next to each other in a single table. This approach replaces the need for joins in a typical relational database and keeps your application high-performing as you scale up.

 ### Query the sparse secondary index
 To use a secondary index, you have two API calls available: Query and Scan. With Query, you must specify the HASH key, and it returns a targeted result. With Scan, you don’t specify a HASH key, and the operation runs across your entire table. Scans are discouraged in DynamoDB except in specific circumstances because they access every item in your database. If you have a significant amount of data in your table, scanning can take a very long time

 ### DynamoDB transactions
 DynamoDB transactions make it easier to build applications that alter multiple items as part of a single operation. With transactions, you can operate on up to 10 items as part of a single transaction request.

 ### Inverted index pattern
 In DynamoDB, an inverted index is a secondary index that is the inverse of your primary key. The RANGE key becomes your HASH key and vice versa. This pattern flips your table and allows you to query on the other side of your many-to-many relationships.

## 3. Recipes Practice
- In our application, we have the following entities:
    1. Ingredient
    2. Base spirit
    3. Mix method
    4. Glassware
    5. Recipe
    6. RecipeIngredientMapping
    7. User

An ingredient can be in multiple recipes. A recipe contains multiple ingredients. There is a many-to-many relationship between Ingredients and Recipes. We represent this relationship with the RecipeIngredientMapping.

### Ingredient access patterns
- Create an ingredient
- Update an ingredient
- Get an ingredient

### Recipe access patterns
- Create a recipe
- Add ingredient to recipe
- Update ingredient in recipe
- Remove ingredient from recipe
- Find recipes by base spirit
- Find recipes by mix method
- Find recipes by glassware
- Get recipe
- Get ingredients in recipe
- Find recipes by ingredient
- React to a recipe
- View recipe and reactions


## User access patterns
- Create user profile
- Update user profile
- Get user profile
- Get user's favorite recipes

### Design the primary key
Entity Hash | HASH | RANGE
--- | --- | ---
Ingredient | INGREDIENT#<INGREDIENT_ID> | #METADATA#<INGREDIENT_ID>
Recipe | RECIPE#<RECIPE_ID> | #METADATA#<RECIPE_ID>
RecipeIngredientMapping | RECIPE#<RECIPE_ID> | INGREDIENT#<INGREDIENT_ID>
User | USER#<USERNAME> | #METADATA#<USERNAME>
Reaction | REACTION#<USERNAME>#<TYPE> | RECIPE#<RECIPE_ID>

Ensure that all your data was loaded into the table by running a Scan operation and getting the count.
```
aws dynamodb scan \
 --table-name <TABLE_NAME> \
 --select COUNT
```

### Retrieve multiple entity types in a single request
You should optimize DynamoDB tables for the number of requests it receives. We also mentioned that DynamoDB does not have joins that a relational database has. Instead, you design your table to allow for join-like behavior in your requests.

Sort keys of the string type are sorted by ASCII character codes. The dollar sign ($) comes directly after the pound sign (#) in ASCII, so this ensures that we will get all mappings in the RecipeIngredientMapping entity.

In a relational database, you use joins to retrieve multiple entity types from different tables in a single request. With DynamoDB, you specifically model your data, so that entities you should access together are located next to each other in a single table. This approach replaces the need for joins in a typical relational database and keeps your application high-performing as you scale up.

### Model a sparse secondary index
- The primary key for a global secondary index does not have to be unique for each item. DynamoDB then copies items into the index based on the attributes specified, and you can query it just like you do the table.
-  With secondary indexes, DynamoDB copies items from the original table only if they have the elements of the primary key in the secondary index. 
- Items that don’t have the primary key elements are not copied, which is why these secondary indexes are called “sparse.”

### Inverted index pattern
In DynamoDB, an inverted index is a secondary index that is the inverse of your primary key. The RANGE key becomes your HASH key and vice versa. This pattern flips your table and allows you to query on the other side of your many-to-many relationships.

## 4. [Design a database for a mobile app with Amazon DynamoDB](https://aws.amazon.com/getting-started/hands-on/design-a-database-for-a-mobile-app-with-dynamodb/2/)

### Designing the primary key
You want a RANGE value with different values across different User entities to enable even partitioning if you use this column as a HASH key for an index. For that reason, you append the username to the RANGE key.

Whenever you need something ordered by a particular property, you will need to include that property in your RANGE key to allow for sorting.

### Bulk-load data into the table
Resource objects provide an easier interface for using the AWS APIs. The Resource object is useful in this situation because it batches our requests

### Retrieve multiple entity types in a single request
First make a Query request to DynamoDB. The Query specifies a HASH key of USER#<Username> to isolate the returned items to a particular user.

Then, the Query specifies a RANGE key condition expression that is between #METADATA#<Username> and PHOTO$. This Query will return a User entity, as its sort key is #METADATA#<Username>, as well as all of the Photo entities for this user, whose sort keys start with PHOTO#.

Sort keys of the String type are sorted by ASCII character codes.

With DynamoDB, you specifically model your data, so that entities you should access together are located next to each other in a single table. This approach replaces the need for joins in a typical relational database and keeps your application high-performing as you scale up.

### Inverted indexes
Secondary indexes are crucial data modeling tools in DynamoDB. They allow you to reshape your data to allow for alternate query patterns.

An inverted index is a common secondary index design pattern with DynamoDB. With an inverted index, you create a secondary index that is the inverse of the primary key for your table. The HASH key for your table becomes the RANGE key in your index, and the RANGE key for your table becomes the primary key for your index.

An inverted index is helpful in two scenarios.
    - First, an inverted index is useful to query the “other” side of a many-to-many relationship
    - An inverted index is also useful to query a one-to-many relationship for an entity that is itself the subject of a one-to-many relationship

### Creating a secondary index
To create a secondary index, you specify the primary key of the index, just like when you were creating a table. Note that the primary key for a global secondary index does not have to be unique. DynamoDB then copies your items into the index based on the attributes specified, and you can query it just like your table.

An inverted index is a common pattern in DynamoDB where you create a secondary index that is the inverse of your table’s primary key. The HASH key for your table is specified as the RANGE key in your secondary index, and the RANGE key for your table is specified as the HASH key in your secondary index.

Note that an inverted index is a name of a design pattern rather than an official property in DynamoDB. Creating an inverted index is just like creating any other secondary index.

### Query the inverted index
To use a secondary index, you only have two API calls available -- Query and Scan.

With Query, you must specify the HASH key, and it returns a targeted result. 

With Scan, you don’t specify a HASH key, and the operation runs across your entire table. Scans are discouraged in DynamoDB except in specific circumstances because they access every item in your database. If you have a significant amount of data in your table, scanning can take a very long time

### Partrial normalization
Partial normalization and the BatchGetItem API call can be helpful to maintain data integrity across objects while still keeping query requests low.

With DynamoDB, you often want to denormalize your data. Denormalization helps to avoid joins and improve query performance. To do this, you may copy attributes from one item into another item that refers to it in order to avoid fetching both items during a query.

Rather than storing the full information about each user in the Friendship entity, you can use the BatchGetItem API to retrieve information about a user in a Friendship entity.

The function first makes a Query request using the inverted index to find all of the users that the given username is following. It then assembles a BatchGetItem to fetch the full User entity for each of the followed users and returns those entities.

This results in two requests to DynamoDB, rather than the ideal of one. However, it’s satisfying a fairly complex access pattern, and it avoids the need to constantly update Friendship entities every time a user profile is updated. This partial normalization can be a great tool for your modeling needs.

### DynamoDB Transactions
Transactions are popular in relational systems for operations that affect multiple data elements at once

The addition of transactions to DynamoDB makes it easier to build applications where you need to alter multiple items as part of a single operation. With DynamoDB transactions, you can operate on up to 10 items as part of a transaction request.

We’re using the transact_write_items() method to perform a write transaction. Our transaction has two operations.

First, we’re doing a Put operation to insert a new Reaction entity. As part of that operation, we’re specifying a condition that the SK attribute should not exist for this item. This is a way to ensure that an item with this PK and SK doesn’t already exist. If it did, that would mean the user has already added this reaction to this photo.

The second operation is an Update operation on the User entity to increment the reaction type in the reactions attribute map.

 DynamoDB’s powerful update expressions allow you to perform atomic increments without needing to first retrieve the item and then update it.

The addition of DynamoDB transactions greatly simplifies the workflow around complex operations like these. Previously, this would have required multiple API calls with complex conditions and manual rollbacks in the event of conflicts. Now it can be implemented with less than 50 lines of code.

### DynamoDB Strategies Summary
The strategies we used to satisfy these patterns included:

1. A single-table design that combined multiple entity types in one table.
2. A composite primary key that allow for many-to-many relationships.
3. An inverted index to allow reverse lookups on our many-to-many entity.
4. Partial normalization to keep our data fresh while remaining performant.
5. DynamoDB transactions to handle complex write patterns across multiple items.

## 5. [Best Practices for Designing and Architecting with DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/best-practices.html)
### Two Key Concepts for NoSQL Design
1. You shouldn't start designing your schema for DynamoDB until you know the questions it will need to answer. Understanding the business problems and the application use cases up front is essential.

2. You should maintain as few tables as possible in a DynamoDB application.

### Secondary indexes
Keep the number of indexes to a minimum. Don't create secondary indexes on attributes that you don't query often. Indexes that are seldom used contribute to increased storage and I/O costs without improving application performance.