## daraz sacrapr

This project aims to scrape data from  daraz Nepal, and save the scraped data into a database and show scraped data in simple Django web app.

#### Requirements
To run this project, you need to have the following software installed:

1. Python 3.x
2. Django
3. Scrapy 
4. Database management system (e.g.SQLite)

#### Setup
1. Clone the repository or download the source code.
```
git clone git@github.com:Pradip-p/daraz-py-scraper.git
```
2. Install the required dependencies.
```
pip install -r crawler/requirements.txt
```
#### Usage
1. Run the daraz_com.py script to scrape data from daraz and save it to the database.
```
python crawler/darazy_com.py
```

2. After running scripts, the scraped data will be stored in the SQLite database.

4. Run the Django project.
```
python manage.py makemigrations
```
```
python manage.py migrate
```
```
python manage.py createsuperuser
```
```
python manage.py runserver
```
5. Access the web app by visiting http://localhost:8000/ in your web browser.

#### Contributing
Contributions are welcome! If you encounter any issues or have suggestions for improvements, please submit a pull request.

#### License
This project is licensed under the MIT License.

