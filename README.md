# ApnaHealthCare

ApnaHealthCare is your go-to app for managing and sharing healthcare services. Get started by registering with your username, email ID, and password. Once registered, log in securely to access your personalized dashboard.

As a registered user, you can effortlessly add your healthcare services by providing essential details like name, description, price, contact number, and email. You have complete control over your entries, with the ability to edit or delete your data anytime.

---

## How to Run the ApnaHealthCare App

### 1. Clone the Repository

Open your terminal and run the following commands to clone the repository:

```bash
git clone https://github.com/yourusername/apnahealthcare.git
cd apnahealthcare
django-admin startproject chailheadq
cd chailheadq
python manage.py startapp tweet
INSTALLED_APPS = [
    ...
    'tweet',
    ...
]
mkdir static
mkdir templates
import os

# Directory for static files
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

# Directory for templates
TEMPLATES = [
    {
        ...
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        ...
    },
]
python manage.py migrate
python manage.py runserver
Open your web browser and navigate to the following URLs:

Home: http://127.0.0.1:8000/tweet/
Admin: http://127.0.0.1:8000/admin
Contact: http://127.0.0.1:8000/contact
