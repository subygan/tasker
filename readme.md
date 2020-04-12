# TASKER

### Setup

`sudo pip install pyenv`

`pyenv install 3.6.9`

`pyenv virtualenv 3.6.9 taskenv`
        
`pyenv activate blogenv`

`pip install -r requirements.txt`

`python manage.py runserver`

### What's working :

* Signup form
* Sign in form
* Profile page (Kinda) (AKA Dashboard)
* Session cookies
* URIs
    * '/'
    * '/signup'
    * '/sign_in'
    * '/profile'

### TO DO :

* Task creation form
    * Task should be associated with the users using the cookies
* Logout
    * Session cookie should be deleted
* Feed page
* redirect to dashboard page, after logged in once

* Beautify the HTML templates (They're pretty barren)

* Pub sub model between users



### To Figure out

* Design ?
    * The whole theme and Color scheme
        * Home design
* Name??
    * It's horrible !!!!!
