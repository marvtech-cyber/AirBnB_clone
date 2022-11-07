# HBNB - The Console
This resparatory contains the inital stage of AirBnB web application clone project. This implement the back end interface, or counsoul, actively modifing the database or file storage data so that we can see effective changes on website. Console commands allow the user to create, update, and distory objects, as well as manage file storage. 
## Reparatory Contents
| Tasks | Files | Description |
| ---- | ---- | ----- |
| 0. AUTHORS/README | [ AUTHORS ](models/AUTHORS) | Project Authors |
| 1. Unit Testing | [/tests](models/engine/__init__.py) | All class defining modules are unit tested |
| 3. Make BaseModel | [/models/base_model.py](models/base_model.py) | Defines parent classes to be inherited by all model classes |
| 4. Create FileStorage class | [/models/engine/file_storage.py](https://github.com/Abelmafi/AirBnB_clone/blob/dev/models/engine/file_storage.py) [/models/__init__.py](https://github.com/Abelmafi/AirBnB_clone/blob/dev/models/init.py) [/models/base_model.py](https://github.com/Abelmafi/AirBnB_clone/blob/dev/models/base_model.py) | Defines a class to manage persistent file storage system|
| 5. Console 0.0.1 | [console.py](https://github.com/Abelmafi/AirBnB_clone/blob/dev/console.py) | Add basic functionality to console program, allowing it to quit, handle empty lines and ^D |
| 6. Console 0.1 | [console.py](https://github.com/Abelmafi/AirBnB_clone/blob/dev/console.py) | Update the console with methods allowing the user to create, destroy, show, and update stored data |
| 8. Create User class | [console.py](https://github.com/Abelmafi/AirBnB_clone/blob/dev/console.py) [/models/engine/file_storage.py](https://github.com/Abelmafi/AirBnB_clone/blob/dev/models/engine/file_storage.py) [/models/user.py](https://github.com/Abelmafi/AirBnB_clone/blob/dev/models/user.py) | Dynamically implements a user class |
| 9. More Classes | [/models/user.py](https://github.com/Abelmafi/AirBnB_clone/blob/dev/models/user.py) [/models/place.py](https://github.com/Abelmafi/AirBnB_clone/blob/dev/models/place.py) [/models/city.py](https://github.com/Abelmafi/AirBnB_clone/blob/dev/models/city.py) [/models/amenity.py](https://github.com/Abelmafi/AirBnB_clone/blob/dev/models/amenity.py) [/models/state.py](https://github.com/Abelmafi/AirBnB_clone/blob/dev/models/state.py) [/models/review.py](https://github.com/Abelmafi/AirBnB_clone/blob/dev/models/review.py) | Dynamically implements more classes |
| 10. Console 1.0 | [console.py](https://github.com/Abelmafi/AirBnB_clone/blob/dev/console.py) [/models/engine/file_storage.py](https://github.com/Abelmafi/AirBnB_clone/blob/dev/models/engine/file_storage.py) | Update the console and file storage system to work dynamically with all  classes update file storage |
## General Use
1. Clone this resparatory
2. Open Resparatory folder and run * counsole.py * as follows:
```shell
/AirBnB_clone$ ./console.py
```
3. After step two the following prompt should apper:
```
(hbnb)
```
4. from varity of available commands insert your commans according to the following syntax:
#### Commands
```
- create - Creats an instance based on given class
- destroy - Destroys an object based on giden class and UUID
- show - Shows an onject based on given class and UUID
- destroy - Destroys an object based on class and UUID
- update - Updates existing attributes an object based on class name and UUID
```
#### Syntax
#### Example 0: Create an object
Usage: create <class_name>
```
(hbnb) create BaseModel
```
```
(hbnb) create BaseModel
3aa5babc-efb6-4041-bfe9-3cc9727588f8
(hbnb)                   
```
#### Example 1: Show an object
Usage: show <class_name> <_id>
```
(hbnb) show BaseModel 3aa5babc-efb6-4041-bfe9-3cc9727588f8
[BaseModel] (3aa5babc-efb6-4041-bfe9-3cc9727588f8) {'id': '3aa5babc-efb6-4041-bfe9-3cc9727588f8', 'created_at': datetime.datetime(2020, 2, 18, 14, 21, 12, 96959), 
'updated_at': datetime.datetime(2020, 2, 18, 14, 21, 12, 96971)}
(hbnb)  
```
#### Example 2: Destroy an object
Usage: destroy <class_name> <_id>
```
(hbnb) destroy BaseModel 3aa5babc-efb6-4041-bfe9-3cc9727588f8
(hbnb) show BaseModel 3aa5babc-efb6-4041-bfe9-3cc9727588f8
 no instance found 
(hbnb)   
```
#### Example 3: Update an object
Usage: update <class_name> <_id>
```
(hb
nb) update BaseModel b405fc64-9724-498f-b405-e4071c3d857f first_name "person"
(hbnb) show BaseModel b405fc64-9724-498f-b405-e4071c3d857f
[BaseModel] (b405fc64-9724-498f-b405-e4071c3d857f) {'id': 'b405fc64-9724-498f-b405-e4071c3d857f', 'created_at': datetime.datetime(2020, 2, 18, 14, 33, 45, 729889), 
'updated_at': datetime.datetime(2020, 2, 18, 14, 33, 45, 729907), 'first_name': 'person'}
(hbnb)
```
### Alternative Syntax

#### Example 0: Show all User objects
Usage: <class_name>.all()
```
(hb
nb) User.all()
["[User] (99f45908-1d17-46d1-9dd2-b7571128115b) {'updated_at': datetime.datetime(2020, 2, 19, 21, 47, 34, 92071), 'id': '99f45908-1d17-46d1-9dd2-b7571128115b', 'created_at': datetime.datetime(2020, 2, 19, 21, 47, 34, 92056)}", "[User] (98bea5de-9cb0-4d78-8a9d-c4de03521c30) {'updated_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134362), 'id': '98bea5de-9cb0-4d78-8a9d-c4de03521c30', 'created_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134343)}"]
```
#### Example 1: Destroy a User
Usage: <class_name>.destroy(<_id>)
```
(hb
nb) User.destroy("99f45908-1d17-46d1-9dd2-b7571128115b")
(hbnb)
(hbnb) User.all()
(hbnb) ["[User] (98bea5de-9cb0-4d78-8a9d-c4de03521c30) {'updated_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134362), 'id': '98bea5de-9cb0-4d78-8a9d-c4de03521c30', 'created_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134343)}"]
```
#### Example 2: Update User (by attribute)
Usage: <class_name>.update(<_id>, <attribute_name>, <attribute_value>)
```
(hb
nb) User.update("98bea5de-9cb0-4d78-8a9d-c4de03521c30", name "Todd the Toad")
(hbnb)
(hbnb) User.all()
(hbnb) ["[User] (98bea5de-9cb0-4d78-8a9d-c4de03521c30) {'updated_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134362), 'id': '98bea5de-9cb0-4d78-8a9d-c4de03521c30', 'name': 'Todd the Toad', 'created_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134343)}"]
```
#### Example 3: Update User (by dictionary)
Usage: <class_name>.update(<_id>, <dictionary>)
```
(hb
nb) User.update("98bea5de-9cb0-4d78-8a9d-c4de03521c30", {'name': 'Fred the Frog', 'age': 9})
(hbnb)
(hbnb) User.all()
(hbnb) ["[User] (98bea5de-9cb0-4d78-8a9d-c4de03521c30) {'updated_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134362), 'name': 'Fred the Frog', 'age': 9, 'id': '98bea5de-9cb0-4d78-8a9d-c4de03521c30', 'created_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134343)}"]
```
