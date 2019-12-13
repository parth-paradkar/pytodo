# pytodo
[![Gitter](https://badges.gitter.im/pytodo/community.svg)](https://gitter.im/pytodo/community?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge)

A minimal command line todo list built with Python and MongoDB

![Mongo + Python](/img/mongo_python_love.png)

Living in the command line is blissful. Keeping your things together sometimes isn't. Track your tasks and deadlines with this command line app built with Python and MongoDB

## Installation

### Installing Python libraries
This project uses pipenv to manage dependencies, so make sure you have pipenv installed.
```
pip install pipenv
```
This project requires pymongo as well
```
sudo pip install pymongo
```
Clone this repository
```
git clone https://github.com/thescriptninja/pytodo.git
```
Use pipenv to install the dependencies
```
pipenv install
```
Create an executable file from the ```script.py``` file

```
cd pytodo/pytodo
cp script.py script
sudo chmod +x script
```
We are going to create an alias to your path so that instead of changing your directory everytime you want to use the todo functions , you can just use the command pytodo

From your home directory , open the .bashrc file in terminal using
```
nano .bashrc
```
add the following command at# pytodo
[![Gitter](https://badges.gitter.im/pytodo/community.svg)](https://gitter.im/pytodo/community?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge)

A minimal command line todo list built with Python and MongoDB

![Mongo + Python](/img/mongo_python_love.png)

Living in the command line is blissful. Keeping your things together sometimes isn't. Track your tasks and deadlines with this command line app built with Python and MongoDB

## Installation

### Installing Python libraries
This project uses pipenv to manage dependencies, so make sure you have pipenv installed.
```
pip install pipenv
```
This project requires pymongo as well
```
sudo pip install pymongo
```
Clone this repository
```
git clone https://github.com/thescriptninja/pytodo.git
```
Use pipenv to install the dependencies
```
pipenv install
```
Create an executable file from the ```script.py``` file

```
cd pytodo/pytodo
cp script.py script
sudo chmod +x script
```
We are going to create an alias to your path so that instead of changing your directory everytime you want to use the todo functions , you can just use the command pytodo

From your home directory , open the .bashrc file in terminal using
'''
nano .bashrc
'''
add the following command in the end of your bash file
```
alias pytodo='python3 <CLONED_REPO_PATH>/pytodo/script
```

### Installing MongoDB
Download the required MongoDB package the package repository.
#### For Ubuntu, run the following commands
```
sudo apt update
sudo apt install -y mongodb
```

#### For Fedora users, run the following commands
*Configure the dnf repository*
```
sudo vi /etc/yum.repos.d/mongodb.repo
```
*Install Mongodb*
```
sudo dnf update
sudo dnf install mongodb-org 
```
*Start the Mongodb service*
```
sudo systemctl enable mongod.service
sudo systemctl start mongod.service
```

#### For Arch users, run the following commands
Aur package at [mongodb 4.2.1-1](https://aur.archlinux.org/packages/mongodb/)

### Creating a local database
Start the mongo shell and create a new database with a collection to store the todos
```
mongo
use todo-app
db.createCollection('todos')
```

##Using the TODO application
To view the list of commands to use the todo application type
```
pytodo -h
```

There you will find different commands to use the application

screenshots:
![image](https://user-images.githubusercontent.com/56514792/70776840-405e8600-1da4-11ea-897d-499a4d0c1c70.png)

## Community Channel
Join the converstaion on [Gitter](https://gitter.im/pytodo/community?utm_source=share-link&utm_medium=link&utm_campaign=share-link)# pytodo
[![Gitter](https://badges.gitter.im/pytodo/community.svg)](https://gitter.im/pytodo/community?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge)

A minimal command line todo list built with Python and MongoDB

![Mongo + Python](/img/mongo_python_love.png)

Living in the command line is blissful. Keeping your things together sometimes isn't. Track your tasks and deadlines with this command line app built with Python and MongoDB

## Installation

### Installing Python libraries
This project uses pipenv to manage dependencies, so make sure you have pipenv installed.
```
pip install pipenv
```
This project requires pymongo as well
```
sudo pip install pymongo
```
Clone this repository
```
git clone https://github.com/thescriptninja/pytodo.git
```
Use pipenv to install the dependencies
```
pipenv install
```
Create an executable file from the ```script.py``` file

```
cd pytodo/pytodo
cp script.py script
sudo chmod +x script
```
We are going to create an alias to your path so that instead of changing your directory everytime you want to use the todo functions , you can just use the command pytodo

From your home directory , open the .bashrc file in terminal using
'''
nano .bashrc
'''
add the following command in the end of your bash file
```
alias pytodo='python3 <CLONED_REPO_PATH>/pytodo/script
```

### Installing MongoDB
Download the required MongoDB package the package repository.
#### For Ubuntu, run the following commands
```
sudo apt update
sudo apt install -y mongodb
```

#### For Fedora users, run the following commands
*Configure the dnf repository*
```
sudo vi /etc/yum.repos.d/mongodb.repo
```
*Install Mongodb*
```
sudo dnf update
sudo dnf install mongodb-org 
```
*Start the Mongodb service*
```
sudo systemctl enable mongod.service
sudo systemctl start mongod.service
```

#### For Arch users, run the following commands
Aur package at [mongodb 4.2.1-1](https://aur.archlinux.org/packages/mongodb/)

### Creating a local database
Start the mongo shell and create a new database with a collection to store the todos
```
mongo
use todo-app
db.createCollection('todos')
```

##Using the TODO application
To view the list of commands to use the todo application type
```
pytodo -h
```

There you will find different commands to use the application

screenshots:
![image](https://user-images.githubusercontent.com/56514792/70776840-405e8600-1da4-11ea-897d-499a4d0c1c70.png)

## Community Channel
Join the converstaion on [Gitter](https://gitter.im/pytodo/community?utm_source=share-link&utm_medium=link&utm_campaign=share-link) the end of your bash file
```
alias pytodo='python3 <CLONED_REPO_PATH>/pytodo/script
```

### Installing MongoDB
Download the required MongoDB package the package repository.
#### For Ubuntu, run the following commands
```
sudo apt update
sudo apt install -y mongodb
```

#### For Fedora users, run the following commands
*Configure the dnf repository*
```
sudo vi /etc/yum.repos.d/mongodb.repo
```
*Install Mongodb*
```
sudo dnf update
sudo dnf install mongodb-org 
```
*Start the Mongodb service*
```
sudo systemctl enable mongod.service
sudo systemctl start mongod.service
```

#### For Arch users, run the following commands
Aur package at [mongodb 4.2.1-1](https://aur.archlinux.org/packages/mongodb/)

### Creating a local database
Start the mongo shell and create a new database with a collection to store the todos
```
mongo
use todo-app
db.createCollection('todos')
```

## Using the TODO application
To view the list of commands to use the todo application type
```
pytodo -h
```

There you will find different commands to use the application

screenshots:
![image](https://user-images.githubusercontent.com/56514792/70776840-405e8600-1da4-11ea-897d-499a4d0c1c70.png)

## Community Channel
Join the converstaion on [Gitter](https://gitter.im/pytodo/community?utm_source=share-link&utm_medium=link&utm_campaign=share-link)
