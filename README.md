# PassTheBooking

## An property management app for dealing with the workload involving various bookings, clients and properties.

# Design
This project was built in Django and Python. Django has several useful generic features and standards which I took advantage of.
I opted for a simple design with a home page and three pages for each model.

Index: Displays all database entries for that model, with a links to individual pages for all the information on each entry.

Info page: Displays information for that specific entry, with an option to edit.

Edit: Contains a form to edit the entry. I used Django's generic Form function to generate forms for each model for this page.
The home page simply provides links to each models index page, which are displayed on every page through the use of a base.html which all other templates extend. There's also a distinct url for displaying properties associated with a particular client.

I used Django's inbuilt fixtures feature to generate data for testing and using the app, and Bootstrap 3 for basic styling.
I tried to keep the views as straightforward as possible, with minimal logic, simply passing data to the necessary templates.  
Separation of concerns was central: although there is little data currently on each page, all the parts are clear and separate which would make it ideal to build upon.

Testing, I used Django's default test library, there are unit tests for models, templates and views though no comprehensive feature and user tests. In future I would use perhaps Selenium to simulate a browser and run through the user experience on the app.

Data, I used Django's fixtures function which was simple and worked well for my purposes although it can be problematic when scaling up.

# Built With
- Python
- Django
- Bootstrap 3

# Requirements
Models:
- Client – holding information about the client’s personal details.
- Property – holding information about property details, e.g. address, number of bedrooms, etc. A property must be connected to a client, and a client may have many properties.
- Booking – holding information about the reservation, e.g. date of check-in, check-out, guest information, etc. A booking must be connected to a property, and a property may have many bookings.
- User - Django default

Interface:
- Homepage with access to other indexes
- Individual URLs for each object e.g. clients/4/
- Edit pages for each object e.g. clients/4/edit/
- Basic Bootstrap front-end

Data:
- A method to generate test/dummy Data
- A database such as PostgreSQL or SQLite

# Instructions
