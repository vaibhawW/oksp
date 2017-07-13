[![Code Health](https://landscape.io/github/stabiitb/oksp/master/landscape.svg?style=flat-square)](https://landscape.io/github/stabiitb/oksp/master) [![Build Status](https://img.shields.io/travis/stabiitb/oksp.svg?style=flat-square)](https://travis-ci.org/stabiitb/oksp) [![Requirements Status](https://img.shields.io/requires/github/stabiitb/oksp.svg?style=flat-square)](https://requires.io/github/stabiitb/oksp/requirements/?branch=master) [![Coverage Status](https://img.shields.io/coveralls/stabiitb/oksp.svg?style=flat-square)](https://coveralls.io/github/stabiitb/oksp?branch=master)

# Online Knowledge Sharing Platform

Online Knowledge Sharing Platform, aka **OKSP** 

Using OKSP
----------------
We will soon be deploying our website. But till then, you may run it on localserver.

Installation on local machine
-----------------
We have tried to simplify the process as much as possible. However, if you find trouble installing or working on this project, feel free to contact us on gitter or our mails, as given below. We have used postgresSQL for database in this project. Also we assume you have create/delete access to database in DB. If you don't, contact your administrator. If you are the administrator, check out the [Additional Helps](#additionalHelps)
<ul style="padding-left:50px;list-style-type:disc">
  <li><a href="#quickSetup">Quick Setup]</a></li>
  <li><a href="#requiredSoftwares">Required Softwares]</a></li>
  <li><a href="#requiredPythonPackages">Required Python Packages]</a></li>
  <li><a href="#settingUpLocalserver">Seting up localserver]</a></li>
  <li><a href="#additionalHelps">Additional Helps]</a></li>
</ul>

 + ### Quick Setup  <a name="quickSetup"></a>
	

 + ### Required Softwares   <a name="requiredSoftwares"></a>
 	+	python3-pip 
 	+	python3.5-dev 
 	+	libpq-dev 
 	+	postgresql 
 	+	postgresql-contrib 
 	+	memcached 
 	+	libjpeg8 
 	+	libjpeg62-dev 
 	+	libfreetype6 
 	+	libfreetype6-dev 
 	+	libxml2-dev 
 	+	libxslt1-dev 
 	+	libffi-dev 
 	+	nodejs 
 	+	nodejs-legacy 
 	+	npm
 	+	pandoc
	
 	**These softwares MAYBE required, I was not able to check which of these were required for current build and which were not. Also some of these have become outdated and/or unsupported. However,  having these softwares will not be harmfull.**
 	
    >dont forget to add python, pip, node etc. to your environent variables 
    
 	<a name="ubuntuInstructions"></a>*For ubuntu Users*
 	You can use following terminal commands for installing above softwares
 	```lang=bash	
 	sudo apt-get update
	sudo apt-get install python3-pip python3.5-dev libpq-dev postgresql postgresql-contrib memcached \
	libjpeg8 libjpeg62-dev libfreetype6 libfreetype6-dev libxml2-dev libxslt1-dev libffi-dev nodejs \
	nodejs-legacy npm pandoc
	```
 + ### Required Python Packages  <a name="requiredPythonPackages"></a>
 	Since we have mentioned pip already in previously, we will directly be writing the code to install the packages. Also, we recommend using virtual environment and wrapper for your safety as the packages may conflict with some other project's packages.
    
    > **(optional)** Chekout [virtualenv](https://pypi.python.org/pypi/virtualenv) and [virtualenvwrapper](http://virtualenvwrapper.readthedocs.io/en/latest/) at their official links. **We highly recommend using these**

	Use the following commands in terminal for installing the required packages. <br>
    Run this from the same directory as manage.py
    
    **Procuction**
    ```lang=bash
    pip install -r requirements/production.txt
    ```
    **Local**
    ```lang=bash
    pip install -r requirements/local.txt
    ```
    
 + ### Setting up localserver  <a name="settingUpLocalserver"></a>

	We will be using django, so you will have to pretty much do the usual configurations required for it. Go to *\<home>/oksp/settings/* and copy *config.sample.py* to *config.py* in the same directory. Now edit this file to setup database settings. [Check this out](#PostgresSQL)
    
 + ### Additional Helps <a name="additionalHelps"></a>
    
    __Creating a PostgreSQL database with required permissions.__ You should have postgreSQL installed and administrator rights. [Check this](#requiredSoftwares) 
    
    ```lang=bash
    sudo su - postgres
    psql # Now you must be in postgresql command line mode

    CREATE DATABASE oksp;
    CREATE USER oksp WITH PASSWORD 'oksp';
    GRANT ALL PRIVILEGES ON DATABASE oksp TO oksp;
    \q
    exit
    ```
    
    __Installing virtualEnv and virtualEnvWrapper__
    
    I recommend you to see the official documentations at[virtualenv](https://pypi.python.org/pypi/virtualenv) and [virtualenvwrapper](http://virtualenvwrapper.readthedocs.io/en/latest/) for installing them. If you are using ubuntu, you could also install and configure them as follows
    ```lang=bash
    pip install virtualenv virtualenvwrapper
    export WORKON_HOME=~/Envs
    mkdir -p $WORKON_HOME
    source /usr/local/bin/virtualenvwrapper.sh
    source /usr/local/bin/virtualenvwrapper.sh
    ```
    
   Creating a new virtualEnvWrapper
   ```lang=bash
   mkvirtualenv oksp
   workon oksp
   ```
   
   Working on virtualEnvWrappers
   ```lang=bash
   workon oksp
   ```

Hacking OKSP
-----------------
This project is entirely open source, and licensed under the **MIT License**. Contributions welcome!<br>
	

Some notes on working on the code:
+ Obviously, since we are working on Django, we will follow the [Coding Style](https://docs.djangoproject.com/en/dev/internals/contributing/writing-code/coding-style/) as specified by official django documentation.

+	Nomenclature
	+ Variables names should start in lowercase [a-z].<br>
	+ **Letter-case separated words** to be followed.<br>
	+ 4 space indentation.
	+ namespacing is must.
+	Commenting
	+ All files, functions, classes should be commented properly.
+	Tests
	+ Tests are must. Test everything. 
	+ Previous tests should pass.
+	Other Specifications
	+ If you are working on local development server, and have used some additional python packages, add them to _\<home>/requirements/common.txt_ with the version of package.
	+ If you want to add some additional packages to production server, add them to _\<home>/requirements/prodution.txt_ with the version of the package

Before submitting a Pull Request, please check that all test are passing. Also mention clearly what you have added/improved/corrected in the project.

Fork this to begin contributing.

Final Notes
----------------------
We will soon be hosting this on our STAB website. Cheers :)
