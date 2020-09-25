# Create and Manage a Nonrelational Database with Amazon DynamoDB
## Overview
This is an [AWS tutorial](https://aws.amazon.com/getting-started/hands-on/create-manage-nonrelational-database-dynamodb/) where you create a DynamoDB table and use the table to store and retrieve data. You use Python and Boto 3 for interacting with DynamoDB APIs.

## Getting started
1. Download support code
```
curl -sL https://s3.amazonaws.com/ddb-deep-dive/dynamodb.tar | tar -xv
```

2. Configure AWS CLI
``` bash
$ aws configure
AWS Access Key ID [None]: AWS_ACCESS_KEY_ID
AWS Secret Access Key [None]: AWS_SECRET_ACCESS_KEY
Default region name [None]: us-west-2
Default output format [None]: json
```

## Inserting and retrieving data
**DynamoDB concepts:**

- Table: A collection of DynamoDB data records.
- Item: A single data record in a DynamoDB table. It is comparable to a row in a relational database.
- Attribute: A single data element on an item. It is comparable to a column in a relational database. However, unlike columns in a relational database, attributes do not need to be specified at table creation, other than the primary key discussed later in this module. Attributes can be simple types such as strings, integers, or Boolean, or they can be complex types such as lists or maps.
- Primary key: A primary key is a unique identifier for a single item in a DynamoDB table. The primary key name and type must be specified on table creation, and a primary key of the specified type must be included with each item written to a table. A simple primary key consists of a single attribute, and a composite primary key consists of two attributes: a partition key and a sort key. For example, you can create a simple primary key using “UserID” as an identifier, or create a composite primary key by combining “UserID” and “Creation_Date” as an item identifier.