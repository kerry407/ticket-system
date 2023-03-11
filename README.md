# Event Management and Ticketing Project

This is an Event Management and Ticketing project built using 
Django Rest Framework for the backend and React for the frontend. 
The project allows authenticated users to create events, filter 
events by category and date range, search for events, 
pay for events and get tickets, and create event host profiles.
Authentication and authorization are also implemented to 
ensure that only authorized users can perform certain actions. 
It uses Paystack as for its's Payment Integration.

## Installation
To run this project, you need to have Python 3.8+, Node.js, and PostgreSQL installed on your machine.

* Clone the repository:

```
git clone https://github.com/kerry407/ticket-system.git
```

* Change into the cloned repository:

```
cd ticket-system
```

* Create Virtual Environment:

```
python3 -m venv my_env
```

* Activate the virtual environment:

```
source my_env/bin/activate
```

* Install backend dependencies:

```
pip install -r requirements.txt
```

* Run migrations to create the app's development database:

```
python manage.py migrate --settings=TicketingSystem.settings.dev
```

* Create a superuser for the app:

```
python manage.py createsuperuser --settings=TicketingSystem.settings.dev
```

* Run the development server:

```
python manage.py runserver --settings=TicketingSystem.settings.dev
```

## Usage

1. Register a new user or log in with an existing user account.

2. Create an event host profile by clicking on the "Create Profile" button and filling out the profile details form.

3. Filter events by category and date range using the filters on the events page.

4. Search for events using the search bar on the events page.

5. Purchase a ticket for an event by clicking on the "Buy Ticket" button and following the payment instructions.

6. View and download your purchased tickets on the "My Tickets" page.

7. Create an event by clicking on the "Create Event" button and filling out the event details form.
