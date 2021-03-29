# How to set up this project

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
```console
> python manage.py import_csv_to_db
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