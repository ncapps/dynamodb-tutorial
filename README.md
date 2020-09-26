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
    - After you have documented your application’s access pattern needs, you are ready to design your table. You should design your table to minimize the number of requests to DynamoDB for each access pattern. Ideally, each access pattern should require only a single request to DynamoDB because network requests are slow, and this limits the number of network requests you will make in your application.

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
