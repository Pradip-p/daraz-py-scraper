## daraz scraper

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
cd crawler/
```
```
pip install .
```
#### Usage

To run project on locally :

1. create a .env file in project directory
set 
```
MYPROJECT_ENV=dev
```

2. Run the daraz_com.py script to scrape data from daraz and save it to the database.
```
python crawler/daraz_com.py
```

3. After running scripts, the scraped data will be stored in the SQLite database.

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

### Future Additional Features

1. **Download Options:** Implement a download button for each crawler run, allowing users to export scraped data in various formats such as JSON, CSV, and Excel. This feature will enhance data accessibility and usability.

2. **Automated Email Delivery:** Integrate an automatic email delivery system that sends scraped data to clients' specified email addresses. This will provide users with a convenient way to receive updates and reports without manual intervention.

3. **Live Logging:** Develop a live log feature that tracks the progress and status of each scraper in real-time. Users will benefit from enhanced transparency and the ability to monitor scraping activities as they happen.

4. **Notification System:** Add a notification system to alert users about the completion of scraping jobs, errors, or other important events. Notifications can be sent via email, Slack, or other preferred communication channels, ensuring users stay informed and can take prompt actions as needed.




#### Contributing
Contributions are welcome! If you encounter any issues or have suggestions for improvements, please submit a pull request.

#### License
This project is licensed under the MIT License.

