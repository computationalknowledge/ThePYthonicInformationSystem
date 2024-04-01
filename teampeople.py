put all code into 1 file

**-- Or better way: 
create discrete files for each partition of your application:
PYFlaskMediator.py
Persistence.py   : mediates to sqlite or json pymongo
Controller.py    : run all your controller OBJECTS to implement business rules and algorthms: use the Python Module import system to 
import other files into your Controller.py

