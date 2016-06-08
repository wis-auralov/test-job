#Web interface for company customers database

One of the test tasks. 

* Implemented the upload of customer cards into the Excel. The file is generated in a separate celery thread.
* Implemented the voting page.
* The vote will be blocked if the vote count will be more than 10. The counter increasing can happen at the same time in a multi processes without the race conditions.  

## Run project
You need make two commands for the project run: 

* python manage.py runserver  # developer server
* python manage.py celeryd    # celery server