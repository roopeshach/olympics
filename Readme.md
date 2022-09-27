# Beijing Olympics

## Install Python for App Setup

After Python Installation is complete, you can clone the application by 

```
git clone https://github.com/roopeshach/olympics.git
cd olympics

```

## Create Virtual Environment

```
python3 -m venv .env
```

## Activate Virtual Environment

```
source .env/bin/activate #in linux
.env\Scripts\activate #in windows
```


## Install Python Packages

```
pip install -r requirements.txt

```

## Run the Application

```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

And you can access the application at http://127.0.0.1:8000/. 
For admin access, you can create a superuser by 

```
python manage.py createsuperuser
```

And navigate to admin page at http://127.0.0.1:8000/admin

Fill the data in the appication and you can see the results in the admin page.




