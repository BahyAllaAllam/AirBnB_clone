# AirBnB Clone

The AirBnB clone project starts now until the end of the first year. The goal of the project is to deploy on your server a simple copy of the AirBnB website.

You won’t implement all the features, only some of them to cover all fundamental concepts of the higher level programming track.

After 4 months, you will have a complete web application composed by:

- A command interpreter to manipulate data without a visual interface, like in a Shell (perfect for development and debugging)
- A website (the front-end) that shows the final product to everybody: static and dynamic
- A database or files that store data (data = objects)
- An API that provides a communication interface between the front-end and your data (retrieve, create, delete, update them)

## Concepts to Learn

- Unittest - and please work all together on tests cases
- Python packages concept page
- Serialization/Deserialization
- *args, **kwargs
- datetime

## Steps

You won’t build this application all at once, but step by step.

Each step will link to a concept:

### The Console

- Create your data model
- Manage (create, update, destroy, etc.) objects via a console / command interpreter
- Store and persist objects to a file (JSON file)

### Web Static

- Learn HTML/CSS
- Create the HTML of your application
- Create templates for each object

### MySQL Storage

- Replace the file storage by a Database storage
- Map your models to a table in the database by using an O.R.M.

### Web Framework - Templating

- Create your first web server in Python
- Make your static HTML file dynamic by using objects stored in a file or database

### RESTful API

- Expose all your objects stored via a JSON web interface
- Manipulate your objects via a RESTful API

### Web Dynamic

- Learn JQuery
- Load objects from the client-side by using your own RESTful API

### Files and Directories

- `models` directory will contain all classes used for the entire project. A class, called “model” in an OOP project, is the representation of an object/instance.
- `tests` directory will contain all unit tests.
- `console.py` file is the entry point of our command interpreter.
- `models/base_model.py` file is the base class of all our models. It contains common elements:
  - Attributes: id, created_at, and updated_at
  - Methods: save() and to_json()
- `models/engine` directory will contain all storage classes (using the same prototype). For the moment, you will have only one: `file_storage.py`.

## Storage

Persistency is essential for a web application. It means every time your program is executed, it starts with all objects previously created from another execution. Without persistency, all the work done in a previous execution won’t be saved and will be gone.

In this project, you will manipulate two types of storage: file and database. For the moment, you will focus on file.

## File Storage == JSON Serialization

For this first step, you have to write in a file all your objects/instances created/updated in your command interpreter and restore them when you start it. You can’t store and restore a Python instance of a class as “Bytes”; the only way is to convert it to a serializable data structure:

1. Convert an instance to a Python built-in serializable data structure (list, dict, number, and string) - for us, it will be the method my_instance.to_json() to retrieve a dictionary.
2. Convert this data structure to a string (JSON format, but it can be YAML, XML, CSV…) - for us, it will be my_string = JSON.dumps(my_dict).
3. Write this string to a file on disk.

And the process of deserialization?

The same but in the other way:

1. Read a string from a file on disk.
2. Convert this string to a data structure. This string is a JSON representation, so it’s easy to convert - for us, it will be my_dict = JSON.loads(my_string).
3. Convert this data structure to an instance - for us, it will be my_instance = MyObject(my_dict).

## *args, **kwargs

### How To Use Them

How do you pass arguments to a function?

```python
def my_fct(param_1, param_2):
    ...

my_fct("Best", "School")
# AirBnB Clone

The AirBnB clone project starts now until the end of the first year. The goal of the project is to deploy on your server a simple copy of the AirBnB website.

You won’t implement all the features, only some of them to cover all fundamental concepts of the higher level programming track.

After 4 months, you will have a complete web application composed by:

- A command interpreter to manipulate data without a visual interface, like in a Shell (perfect for development and debugging)
- A website (the front-end) that shows the final product to everybody: static and dynamic
- A database or files that store data (data = objects)
- An API that provides a communication interface between the front-end and your data (retrieve, create, delete, update them)

## Concepts to Learn

- Unittest - and please work all together on tests cases
- Python packages concept page
- Serialization/Deserialization
- *args, **kwargs
- datetime

## Steps

You won’t build this application all at once, but step by step.

Each step will link to a concept:

### The Console

- Create your data model
- Manage (create, update, destroy, etc.) objects via a console / command interpreter
- Store and persist objects to a file (JSON file)

### Web Static

- Learn HTML/CSS
- Create the HTML of your application
- Create templates for each object

### MySQL Storage

- Replace the file storage by a Database storage
- Map your models to a table in the database by using an O.R.M.

### Web Framework - Templating

- Create your first web server in Python
- Make your static HTML file dynamic by using objects stored in a file or database

### RESTful API

- Expose all your objects stored via a JSON web interface
- Manipulate your objects via a RESTful API

### Web Dynamic

- Learn JQuery
- Load objects from the client-side by using your own RESTful API

### Files and Directories

- `models` directory will contain all classes used for the entire project. A class, called “model” in an OOP project, is the representation of an object/instance.
- `tests` directory will contain all unit tests.
- `console.py` file is the entry point of our command interpreter.
- `models/base_model.py` file is the base class of all our models. It contains common elements:
  - Attributes: id, created_at, and updated_at
  - Methods: save() and to_json()
- `models/engine` directory will contain all storage classes (using the same prototype). For the moment, you will have only one: `file_storage.py`.

## Storage

Persistency is essential for a web application. It means every time your program is executed, it starts with all objects previously created from another execution. Without persistency, all the work done in a previous execution won’t be saved and will be gone.

In this project, you will manipulate two types of storage: file and database. For the moment, you will focus on file.

## File Storage == JSON Serialization

For this first step, you have to write in a file all your objects/instances created/updated in your command interpreter and restore them when you start it. You can’t store and restore a Python instance of a class as “Bytes”; the only way is to convert it to a serializable data structure:

1. Convert an instance to a Python built-in serializable data structure (list, dict, number, and string) - for us, it will be the method my_instance.to_json() to retrieve a dictionary.
2. Convert this data structure to a string (JSON format, but it can be YAML, XML, CSV…) - for us, it will be my_string = JSON.dumps(my_dict).
3. Write this string to a file on disk.

And the process of deserialization?

The same but in the other way:

1. Read a string from a file on disk.
2. Convert this string to a data structure. This string is a JSON representation, so it’s easy to convert - for us, it will be my_dict = JSON.loads(my_string).
3. Convert this data structure to an instance - for us, it will be my_instance = MyObject(my_dict).

## *args, **kwargs

### How To Use Them

How do you pass arguments to a function?

```python
def my_fct(param_1, param_2):
    ...

my_fct("Best", "School")
# AirBnB Clone

The AirBnB clone project starts now until the end of the first year. The goal of the project is to deploy on your server a simple copy of the AirBnB website.

You won’t implement all the features, only some of them to cover all fundamental concepts of the higher level programming track.

After 4 months, you will have a complete web application composed by:

- A command interpreter to manipulate data without a visual interface, like in a Shell (perfect for development and debugging)
- A website (the front-end) that shows the final product to everybody: static and dynamic
- A database or files that store data (data = objects)
- An API that provides a communication interface between the front-end and your data (retrieve, create, delete, update them)

## Concepts to Learn

- Unittest - and please work all together on tests cases
- Python packages concept page
- Serialization/Deserialization
- *args, **kwargs
- datetime

## Steps

You won’t build this application all at once, but step by step.

Each step will link to a concept:

### The Console

- Create your data model
- Manage (create, update, destroy, etc.) objects via a console / command interpreter
- Store and persist objects to a file (JSON file)

### Web Static

- Learn HTML/CSS
- Create the HTML of your application
- Create templates for each object

### MySQL Storage

- Replace the file storage by a Database storage
- Map your models to a table in the database by using an O.R.M.

### Web Framework - Templating

- Create your first web server in Python
- Make your static HTML file dynamic by using objects stored in a file or database

### RESTful API

- Expose all your objects stored via a JSON web interface
- Manipulate your objects via a RESTful API

### Web Dynamic

- Learn JQuery
- Load objects from the client-side by using your own RESTful API

### Files and Directories

- `models` directory will contain all classes used for the entire project. A class, called “model” in an OOP project, is the representation of an object/instance.
- `tests` directory will contain all unit tests.
- `console.py` file is the entry point of our command interpreter.
- `models/base_model.py` file is the base class of all our models. It contains common elements:
  - Attributes: id, created_at, and updated_at
  - Methods: save() and to_json()
- `models/engine` directory will contain all storage classes (using the same prototype). For the moment, you will have only one: `file_storage.py`.

## Storage

Persistency is essential for a web application. It means every time your program is executed, it starts with all objects previously created from another execution. Without persistency, all the work done in a previous execution won’t be saved and will be gone.

In this project, you will manipulate two types of storage: file and database. For the moment, you will focus on file.

## File Storage == JSON Serialization

For this first step, you have to write in a file all your objects/instances created/updated in your command interpreter and restore them when you start it. You can’t store and restore a Python instance of a class as “Bytes”; the only way is to convert it to a serializable data structure:

1. Convert an instance to a Python built-in serializable data structure (list, dict, number, and string) - for us, it will be the method my_instance.to_json() to retrieve a dictionary.
2. Convert this data structure to a string (JSON format, but it can be YAML, XML, CSV…) - for us, it will be my_string = JSON.dumps(my_dict).
3. Write this string to a file on disk.

And the process of deserialization?

The same but in the other way:

1. Read a string from a file on disk.
2. Convert this string to a data structure. This string is a JSON representation, so it’s easy to convert - for us, it will be my_dict = JSON.loads(my_string).
3. Convert this data structure to an instance - for us, it will be my_instance = MyObject(my_dict).

## *args, **kwargs

### How To Use Them

How do you pass arguments to a function?

```python
def my_fct(param_1, param_2):
    ...

my_fct("Best", "School")
# AirBnB Clone

The AirBnB clone project starts now until the end of the first year. The goal of the project is to deploy on your server a simple copy of the AirBnB website.

You won’t implement all the features, only some of them to cover all fundamental concepts of the higher level programming track.

After 4 months, you will have a complete web application composed by:

- A command interpreter to manipulate data without a visual interface, like in a Shell (perfect for development and debugging)
- A website (the front-end) that shows the final product to everybody: static and dynamic
- A database or files that store data (data = objects)
- An API that provides a communication interface between the front-end and your data (retrieve, create, delete, update them)

## Concepts to Learn

- Unittest - and please work all together on tests cases
- Python packages concept page
- Serialization/Deserialization
- *args, **kwargs
- datetime

## Steps

You won’t build this application all at once, but step by step.

Each step will link to a concept:

### The Console

- Create your data model
- Manage (create, update, destroy, etc.) objects via a console / command interpreter
- Store and persist objects to a file (JSON file)

### Web Static

- Learn HTML/CSS
- Create the HTML of your application
- Create templates for each object

### MySQL Storage

- Replace the file storage by a Database storage
- Map your models to a table in the database by using an O.R.M.

### Web Framework - Templating

- Create your first web server in Python
- Make your static HTML file dynamic by using objects stored in a file or database

### RESTful API

- Expose all your objects stored via a JSON web interface
- Manipulate your objects via a RESTful API

### Web Dynamic

- Learn JQuery
- Load objects from the client-side by using your own RESTful API

### Files and Directories

- `models` directory will contain all classes used for the entire project. A class, called “model” in an OOP project, is the representation of an object/instance.
- `tests` directory will contain all unit tests.
- `console.py` file is the entry point of our command interpreter.
- `models/base_model.py` file is the base class of all our models. It contains common elements:
  - Attributes: id, created_at, and updated_at
  - Methods: save() and to_json()
- `models/engine` directory will contain all storage classes (using the same prototype). For the moment, you will have only one: `file_storage.py`.

## Storage

Persistency is essential for a web application. It means every time your program is executed, it starts with all objects previously created from another execution. Without persistency, all the work done in a previous execution won’t be saved and will be gone.

In this project, you will manipulate two types of storage: file and database. For the moment, you will focus on file.

## File Storage == JSON Serialization

For this first step, you have to write in a file all your objects/instances created/updated in your command interpreter and restore them when you start it. You can’t store and restore a Python instance of a class as “Bytes”; the only way is to convert it to a serializable data structure:

1. Convert an instance to a Python built-in serializable data structure (list, dict, number, and string) - for us, it will be the method my_instance.to_json() to retrieve a dictionary.
2. Convert this data structure to a string (JSON format, but it can be YAML, XML, CSV…) - for us, it will be my_string = JSON.dumps(my_dict).
3. Write this string to a file on disk.

And the process of deserialization?

The same but in the other way:

1. Read a string from a file on disk.
2. Convert this string to a data structure. This string is a JSON representation, so it’s easy to convert - for us, it will be my_dict = JSON.loads(my_string).
3. Convert this data structure to an instance - for us, it will be my_instance = MyObject(my_dict).

## *args, **kwargs

### How To Use Them

How do you pass arguments to a function?

```python
def my_fct(param_1, param_2):
    ...

my_fct("Best", "School")
# AirBnB Clone

The AirBnB clone project starts now until the end of the first year. The goal of the project is to deploy on your server a simple copy of the AirBnB website.

You won’t implement all the features, only some of them to cover all fundamental concepts of the higher level programming track.

After 4 months, you will have a complete web application composed by:

- A command interpreter to manipulate data without a visual interface, like in a Shell (perfect for development and debugging)
- A website (the front-end) that shows the final product to everybody: static and dynamic
- A database or files that store data (data = objects)
- An API that provides a communication interface between the front-end and your data (retrieve, create, delete, update them)

## Concepts to Learn

- Unittest - and please work all together on tests cases
- Python packages concept page
- Serialization/Deserialization
- *args, **kwargs
- datetime

## Steps

You won’t build this application all at once, but step by step.

Each step will link to a concept:

### The Console

- Create your data model
- Manage (create, update, destroy, etc.) objects via a console / command interpreter
- Store and persist objects to a file (JSON file)

### Web Static

- Learn HTML/CSS
- Create the HTML of your application
- Create templates for each object

### MySQL Storage

- Replace the file storage by a Database storage
- Map your models to a table in the database by using an O.R.M.

### Web Framework - Templating

- Create your first web server in Python
- Make your static HTML file dynamic by using objects stored in a file or database

### RESTful API

- Expose all your objects stored via a JSON web interface
- Manipulate your objects via a RESTful API

### Web Dynamic

- Learn JQuery
- Load objects from the client-side by using your own RESTful API

### Files and Directories

- `models` directory will contain all classes used for the entire project. A class, called “model” in an OOP project, is the representation of an object/instance.
- `tests` directory will contain all unit tests.
- `console.py` file is the entry point of our command interpreter.
- `models/base_model.py` file is the base class of all our models. It contains common elements:
  - Attributes: id, created_at, and updated_at
  - Methods: save() and to_json()
- `models/engine` directory will contain all storage classes (using the same prototype). For the moment, you will have only one: `file_storage.py`.

## Storage

Persistency is essential for a web application. It means every time your program is executed, it starts with all objects previously created from another execution. Without persistency, all the work done in a previous execution won’t be saved and will be gone.

In this project, you will manipulate two types of storage: file and database. For the moment, you will focus on file.

## File Storage == JSON Serialization

For this first step, you have to write in a file all your objects/instances created/updated in your command interpreter and restore them when you start it. You can’t store and restore a Python instance of a class as “Bytes”; the only way is to convert it to a serializable data structure:

1. Convert an instance to a Python built-in serializable data structure (list, dict, number, and string) - for us, it will be the method my_instance.to_json() to retrieve a dictionary.
2. Convert this data structure to a string (JSON format, but it can be YAML, XML, CSV…) - for us, it will be my_string = JSON.dumps(my_dict).
3. Write this string to a file on disk.

And the process of deserialization?

The same but in the other way:

1. Read a string from a file on disk.
2. Convert this string to a data structure. This string is a JSON representation, so it’s easy to convert - for us, it will be my_dict = JSON.loads(my_string).
3. Convert this data structure to an instance - for us, it will be my_instance = MyObject(my_dict).

## *args, **kwargs

### How To Use Them

How do you pass arguments to a function?

```python
def my_fct(param_1, param_2):
    ...

my_fct("Best", "School")
# AirBnB Clone

The AirBnB clone project starts now until the end of the first year. The goal of the project is to deploy on your server a simple copy of the AirBnB website.

You won’t implement all the features, only some of them to cover all fundamental concepts of the higher level programming track.

After 4 months, you will have a complete web application composed by:

- A command interpreter to manipulate data without a visual interface, like in a Shell (perfect for development and debugging)
- A website (the front-end) that shows the final product to everybody: static and dynamic
- A database or files that store data (data = objects)
- An API that provides a communication interface between the front-end and your data (retrieve, create, delete, update them)

## Concepts to Learn

- Unittest - and please work all together on tests cases
- Python packages concept page
- Serialization/Deserialization
- *args, **kwargs
- datetime

## Steps

You won’t build this application all at once, but step by step.

Each step will link to a concept:

### The Console

- Create your data model
- Manage (create, update, destroy, etc.) objects via a console / command interpreter
- Store and persist objects to a file (JSON file)

### Web Static

- Learn HTML/CSS
- Create the HTML of your application
- Create templates for each object

### MySQL Storage

- Replace the file storage by a Database storage
- Map your models to a table in the database by using an O.R.M.

### Web Framework - Templating

- Create your first web server in Python
- Make your static HTML file dynamic by using objects stored in a file or database

### RESTful API

- Expose all your objects stored via a JSON web interface
- Manipulate your objects via a RESTful API

### Web Dynamic

- Learn JQuery
- Load objects from the client-side by using your own RESTful API

### Files and Directories

- `models` directory will contain all classes used for the entire project. A class, called “model” in an OOP project, is the representation of an object/instance.
- `tests` directory will contain all unit tests.
- `console.py` file is the entry point of our command interpreter.
- `models/base_model.py` file is the base class of all our models. It contains common elements:
  - Attributes: id, created_at, and updated_at
  - Methods: save() and to_json()
- `models/engine` directory will contain all storage classes (using the same prototype). For the moment, you will have only one: `file_storage.py`.

## Storage

Persistency is essential for a web application. It means every time your program is executed, it starts with all objects previously created from another execution. Without persistency, all the work done in a previous execution won’t be saved and will be gone.

In this project, you will manipulate two types of storage: file and database. For the moment, you will focus on file.

## File Storage == JSON Serialization

For this first step, you have to write in a file all your objects/instances created/updated in your command interpreter and restore them when you start it. You can’t store and restore a Python instance of a class as “Bytes”; the only way is to convert it to a serializable data structure:

1. Convert an instance to a Python built-in serializable data structure (list, dict, number, and string) - for us, it will be the method my_instance.to_json() to retrieve a dictionary.
2. Convert this data structure to a string (JSON format, but it can be YAML, XML, CSV…) - for us, it will be my_string = JSON.dumps(my_dict).
3. Write this string to a file on disk.

And the process of deserialization?

The same but in the other way:

1. Read a string from a file on disk.
2. Convert this string to a data structure. This string is a JSON representation, so it’s easy to convert - for us, it will be my_dict = JSON.loads(my_string).
3. Convert this data structure to an instance - for us, it will be my_instance = MyObject(my_dict).

## *args, **kwargs

### How To Use Them

How do you pass arguments to a function?

```python
def my_fct(param_1, param_2):
    ...

my_fct("Best", "School")

