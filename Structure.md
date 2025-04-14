# Finance Tracker Application - Directory Structure

finance_tracker_app/                # Root folder of the project repository
├── finance_tracker/                # Django project configuration folder
│   ├── __init__.py
│   ├── settings.py                 # Main settings/configuration file
│   ├── urls.py                     # URL routes for global application
│   ├── wsgi.py                     # WSGI entry point for deployment
│   └── asgi.py                     # ASGI entry point (optional, for async support)
│
├── tracker_app/                    # Main Django app for tracking finances
│   ├── __init__.py
│   ├── admin.py                    # Django admin configuration for the app
│   ├── apps.py                     # Application configuration
│   ├── models.py                   # Data models (e.g., User transactions, Categories)
│   ├── views.py                    # Views (controller logic)
│   ├── urls.py                     # App-specific URL routes
│   ├── forms.py                    # Django forms for user input (optional)
│   └── migrations/                 # Database migration scripts
│       └── __init__.py
│
├── templates/                      # Global template directory for Django HTML files
│   ├── base.html                   # Base template (common UI elements)
│   └── tracker_app/                # App-specific templates folder
│       ├── index.html              # Homepage or landing page
│       ├── dashboard.html          # Dashboard view displaying data visualization
│       └── login.html              # Login page for user authentication
│
├── static/                         # Static files (CSS, JavaScript, images, etc.)
│   ├── css/
│   │   └── style.css               # Custom styles
│   ├── js/
│   │   └── scripts.js              # Custom JavaScript files
│   └── images/                     # Image files used in the project
│
├── media/                          # Media files (user uploads, if applicable)
│
├── requirements.txt                # Dependency list (Python packages)
├── manage.py                       # Django’s command-line utility
├── README.md                       # Project overview and basic info
└── .gitignore                      # Files and folders for Git to ignore