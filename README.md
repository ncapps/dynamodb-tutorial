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