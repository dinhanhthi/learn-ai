# What is SQLite?

*Learn about the SQLite database engine and how to install it on your computer.*

In this article we will be exploring the extremely prevalent database engine called [SQLite](https://www.sqlite.org/index.html). We will describe what it does, its main uses, and then explain how to set it up and use it on your own computer.

## Overview

- [Home page](https://www.sqlite.org/index.html) ([download](https://www.sqlite.org/download.html) `sqlite-tools-win-...`)
- SQLite is a database engine
- **Advantage**
  - In SQLite, a database is stored in a single file
  - Copy database = copy file
  - access and manipulate a database without involving a server application
  - used worldwide for testing, development
- **Drawback**:
  - poor choice when many different users are updating the table at the same time
  - require some more work to ensure the security of private data
  - SQLite does not offer the same exact functionality as many other database systems
  - SQLite does not validate data types
  - SQLite will not reject values of the wrong type

## How to?

- Setting up SQLite locally: [Windows](https://youtu.be/dcfh5iQ_-3s), [Mac](https://youtu.be/4MJSZi4qvIE)
- Need to add to `path` (on Windows, press `Start` and search `variable...` and then add to `Environment Variables`)
- On Windows: after adding to `path`, run `sqlite3`.
  - exit: `Ctrl` + `C`
- On Linux: `sudo apt-get install sqlite3`
  - `sqlite3 newdb.sqlite` to run
  - exit: `.exit` and then press `Enter`
- 

