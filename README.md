Zendesk Challenge
===================

Description
-----------

- The application is a simulation of a search system.
- The application has been implemented in python3.6.
- This application uses a sqlite3 data base to store the data in memory. the system frees the memory when the users close the application.
- The application uses Sqlite3.row like the main structure to iterate through the data.
- The data file (Json_data) contains the json format data for users, 
organizations and tickets. Also, it contains to data files for testing
(test.json and test2_json).


Getting Started
---------------

These instructions will get you a copy of the project up and running on your 
local machine for development and testing purposes.

### Prerequisites

  * Python 3.6 and up
  * Unittest package (Python Supports Natively)
  * sqlite3 (Python Supports Natively)
  * Json (Python Supports Natively)
  * Datetime (Python Supports Natively)

### Installing

  - The application doesn't need to be installed. However, you should have installed
  	Python in your local machine. 

Running the code
----------------
   
  ### Running test file
   	
  * Open a new terminal window
  * Move into the project directory
  ```
  $ cd your/local/folder/Search_Challenge
  ```
  * Run test file 
  ```
  $ python test.py
  ```
  ```
  * The output should be similar to:
  ```
  $ Ran 52 tests in 0.630s
	OK
  ```

  ### Running the application

  * Open a terminal window
  * Move into the project directory
  ```
  $ cd your/local/folder/Search_Challenge
  ```
  * Run Zendesk application
  ```
  $ python zendesk_application.py
  ```
  * Enter your commands
  ```
  $ Welcome to Zendesk Search
    Type "quit" to exit at any time, Press "Enter" to continue
  $
  $ Select search options:
    * Press 1 to search
    * Press 2 to view a list of searchable field
    * Type "quit" to exit
  $ 1
  $ Select table:
    * Select 1 users
    * Select 2 organizations
    * Select 3 tickets
  $ 1
  $ Enter search term
  $ _id
  $ Enter search value
  $ 4
  ```
  * The output should be similar to:
  ```
  $ _id                  4                   
    url                  http://initech.zendesk.com/api/v2/users/4.json
    external_id          37c9aef5-cf01-4b07-af24-c6c49ac1d1c7
    name                 Rose Newton         
    alias                Mr Cardenas         
    created_at           2016-02-09T07:52:10 -11:00
    active               True                
    verified             True                
    shared               True                
    locale               de-CH               
    timezone             Netherlands         
    last_login_at        2012-09-25T01:32:46 -10:00
    email                cardenasnewton@flotonic.com
    phone                8685-482-450        
    signature            Don't Worry Be Happy!
    organization_id      122                 
    tags                 ['Gallina', 'Glenshaw', 'Rowe', 'Babb']
    suspended            True                
    role                 end-user            
    organization_name    Geekfarm            
    ticket_0             A Nuisance in Equatorial Guinea
    ticket_1             A Drama in Uruguay  
    ticket_2             A Nuisance in Virgin Islands (British)
    ticket_3             A Drama in Kazakhstan
  ```
  - Notes:
  	* If you press 'ctrl+d' will create the EOF in the system.
  	
  	* If you type 'quit' any time to exit.
  	
  	* This system has been tested in Mac, Linux, Ubuntu and Centos.
