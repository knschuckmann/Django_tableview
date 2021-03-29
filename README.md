# How to set up this project

The Goal of this project was the creation of a website that can display a dataset and log all actions to your database.

## Install dependencies

*sometimes pip3 and python3 is required instead of pip and python*

1. Change directory to App (Smart_steel)
2. Install requirements in your environment  

```console
> cd /dir/to/Smart_steel_App
> pip install --user -r requirements.txt
```
## Set up the App
**Python should be installed**

### Fill Database
make sure that your file is called task_data.csv and is located in data folder *data/task\_data.csv*. Your data should have the following headers in given order and written exact as given:

1. id
2. timestamp
3. temperature
4. duration

```console
> python manage.py import_csv_to_db
```
You can change the input by changing the folowing files to your needs 

- **webapp/management/commands/import_csv_to_db.py**
- **webapp/admin.py**
- **webapp/models.py**
- **webapp/templates/webapp.html**


### Migrate Changes
```console
> python manage.py makemigrations
> python manage.py migrate
```

### Start Webserver (localy)
```console
> python manage.py runserver
```
* Go to your browser and insert in address bar

> http://127.0.0.1:8000/

### How to use the App
* On navigation you will find 
	* Display table
	* Admin button for admin area

1. Click on Display table
	* display the database entries
2. Click on Admin
	* 	Get to admin area, where one can CRUD the entries and display the logs
	
	> user: user\_name <br>
	> pw: Smart\_steel1