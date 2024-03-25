# DecentralizedAI Developer Guide

Welcome to the DecentralizedAI developer guide! This guide will walk you through the process of developing and deploying your own decentralized AI system using the DecentralizedAI framework.

# Prerequisites

Before you begin, make sure you have the following tools and libraries installed:

- Node.js version 14 or later
- NPM version 6 or later
- Web5.js SDK version 1.0.0 or later

# Getting Started

To get started, create a new directory for your project and navigate to it in your terminal. Then, run the following command to initialize a new DecentralizedAI project:

`npx create-decentralizedai-app my-app`

Replace my-app with the name of your project. This will create a new directory with the following structure:

`my-app/
  node_modules/
  public/
    index.html
  src/
    index.js
  package.json`

  Next, navigate to the src directory and open the index.js file. This is where you will write the code for your decentralized AI system.

# Writing Your Code

To interact with the Decentralized Web Node (DWN) and perform CRUD operations on your data, you can use the web5.dwn.records API provided by the Web5.js SDK. Here are some examples of how to use this API:

# Create (write) records

To create a new record, use the web5.dwn.records.create method. This method takes an object with the following properties:

- data: The data to be written to the record.
- message (optional): An object describing the message.

Here is an example of how to create a new record:

`const { record } = await web5.dwn.records.create({
  data: "I'm writing a new record!",
  message: {
    dataFormat: 'text/plain',
  },
});`

`console.log('writeResult', record);`

# Read records

To read the data from a record, use the data property of the record object. This property contains a function that returns the data in the format specified in the message object.

Here is an example of how to read the data from a record:

`const readResult = await record.data.text();
console.log('readResult', readResult)`

# Update (edit) records

To update the data in a record, use the update method of the record object. This method takes an object with the following properties:

data: The new data to be written to the record.
Here is an example of how to update a record:

`const updateResult = await record.update({data: "I updated the record!"});
console.log('updateResult', updateResult)`

# Delete records

To delete a record, use the delete method of the record object. This method does not return a value.

Here is an example of how to delete a record:

`const deleteResult = await record.delete();
console.log('deleteResult', deleteResult)`

# Running Your Code
To run your code, use the web5.start method. This method takes an object with the following properties:

loglevel (optional): The log level for the Decentralized Web Node.
Here is an example of how to start the Decentralized Web Node:

`await web5.start({loglevel: 'debug'});`

This will start the Decentralized Web Node and begin listening for incoming connections.
