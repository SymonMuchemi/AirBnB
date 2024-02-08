# AirBnB_clone

## Introduction

This is project incoporates a console application for manipulating data without visual interface.

## The console

The first piece is to manipulate a powerful storage system. This storage engine will give us an abstraction between “My object” and “How they are stored and persisted”. This means: from the console code (the command interpreter itself) and from the front-end and RestAPI to be built later, it won’t pay attention (take care) of how objects are stored.

This abstraction will also allow you to change the type of storage easily without updating all of your codebase.

The console will be a tool to validate this storage engine

![Project structure](/the-console.png)

## Storage


This project focuses on the importance of persistency in web applications, where data from previous executions should be retained. Two types of storage, file and database, are addressed, with the initial focus on file storage. The project advocates for separating "storage management" from "model" to ensure modular and independent models. This approach allows for easy replacement of the storage system without extensive recoding. Class attributes are preferred over instance attributes for clarity, default value provision, and future-proofing for potential transition between file and database storage.

## Data Diagram

![Data diagram](/AirBNB-project%20data%20diagram.jpg)
