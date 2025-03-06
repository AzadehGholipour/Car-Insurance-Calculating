# Car Insurance Premium Calculator

- [Introduction](#introduction)
- [Distinctiveness and Complexity](#distinctiveness-and-complexity)
- [How To Run](#how-to-run)
- [User Guide](#user-guide)
- [Models](#models)
- [Pages](#pages)
- [Javascript](#javascript)
- [Django](#Django)
- [Future Improvements](#future-improvements)
- [Additional Points](#additional-points)

-----------------------------------------------------------------------------
## Introduction

The **Car Insurance Premium Calculator** is a web application designed to simplify the process of estimating car insurance premiums. By leveraging Python and Django for the backend and JavaScript for client-side interactions, the application provides a user-friendly interface for customers and insurers alike.

This tool uses a customizable algorithm to calculate premiums based on factors like the car value, optional coverages, and no-claim discounts. Users can apply for insurance by submitting a form, while administrators can manage these submissions.

Built with a responsive design, the application ensures compatibility across devices, from desktops to mobile screens.
Please visit my YouTube video at: https://youtu.be/e-gK__bHjIs

-----------------------------------------------------------------------------
## Distinctiveness and Complexity

This project satisfies the distinctiveness and complexity criteria for the following reasons:

   - The application incorporates three interrelated Django models: `User`, `Car`, and `Insurance`, which efficiently manage insurance-related data. The `Car` and `User` models contain essential fields necessary for insurance contracts, while the `Insurance` model has foreign key relationships with `Car` and `User`, along with additional fields for defining insurance conditions.
   - The `Post` model is designed for insurers to publish useful information and important announcements in a dynamic, animated environment. These posts are displayed on the main page (index), sorted in descending order by upload date (newest first).
   - The application features an algorithm that calculates insurance premiums based on multiple user-provided variables. By clicking on "Click `here` to calculate your car insurance", the user is redirected to a form page containing various input fields. The `Cost of Car` is the primary factor in premium calculation. Additionally, users can select a `No-Claims Discount` from a dropdown menu and choose `optional coverage` by toggling yes/no checkboxes.
   - after all, The premium calculation is performed by JavaScript `function calculatePremium` in the `index.js` file. The ratios of the cost and optional coverages are defined as constants. Also, the percentages of discount are calculated based on `No-Claims Discount`.
   - Now, if the customer wants to contract the insurance, they should fill the necessary information about their car and themselves. Frontend interactivity with JavaScript, including real-time form updates (e.g., updating dropdowns based on selections) is designed to make the process user-friendly and simple. 

-----------------------------------------------------------------------------
## How To Run

Follow these steps to set up and run the Car Insurance Premium Calculator on your local machine:

- Navigate to the project directory, click "Open in Integrated Terminal"
- Install project dependencies by running pip install -r requirements.txt
- Run python manage.py makemigrations
- Run python manage.py migrate
- Run python manage.py createsuperuser, and register an administrative
- Run local server, in the terminal enter: "python manage.py runserver"
- Now, you can open the premium calculator in browser by inserting the path: http://127.0.0.1:8000/ in the search bar.

-----------------------------------------------------------------------------
## User Guide

### For Users
- Register or log in to calculate insurance premiums and submit application forms.
- Fill in required fields (e.g., car cost, optional coverages, no-claim discount) to receive an estimated premium.
- Fill the information form and submit to apply the insurance contract.

### For Administrators
- Log in to the admin panel at http://127.0.0.1:8000/admin.
- Access and manage user data, car information, posts and insurance applications stored in the database.

-----------------------------------------------------------------------------
## Models

The application utilizes four primary Django models:

| Model     | Description                                                                   | Fields                                                                               |
|-----------|-------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|
|`User`     | extending `AbstractUser` to include additional fields for user identification | `date_of_birth`, `ID_number`, `driving_licence_number`                               |
|`Car`      | Represents the insured car with details used for insurance contracts.         | `license_plate`, `vin`, `year`, `brand`, `serie`                                     |
|`Insurance`| Links a user with a car to create an insurance policy.                        | `policyholder` (FK to `User`), `insured` (FK to `Car`), `coverage_details`, `premium`|
|`Post`     | Everything the insurer wants to announce or inform the customers about. | `title`, `content`, `image`, `date_of_upload`                               |

These models are designed to handle complex relationships and ensure data integrity across the application.

-----------------------------------------------------------------------------
## Pages

### Index page includes:
- Useful and motivational information about Car Insurance
- Users can register or log in, if already registered
- Provides efficient links to important resources such as insurer/admin contact information and user's profile forms.

### Form page includes:
- Users can estimate their car insurance premium based on specific parameters: cost of the car is required, optional coverages and no-claim discount.

- Click the 'Application Form' button to appear the car information form.

- By the next level, they can fill out and submit the car information form to apply for the insurance contract.

-----------------------------------------------------------------------------
## Javascript

The index.js contains the function of calculating based on risk rates. Other parameters e.g. the cost of car, optional coverages and no-claim discount are get from the calculating form. eventually, it updates the premium textbox by result.
Also the function to design the information form. the form appears by clicking the button "Applicattion Form".
The other function in index.js is for operation of some objects in the application form. it updates the car serie dropdown after changing the car name dropdown by user.

-----------------------------------------------------------------------------
## Django

all the django functions are combined in the views.py file. At first, register, login and logout functions. Next, the functions for rendering data to load the pages and getting data from pages to save in database, db.sqlite3 file. There are some tools and libraries from django which are used in functions. so, you should install django by installing requirements.txt file before running the application.

-----------------------------------------------------------------------------
## Future Improvements

-  There are so many features could be added to the **Car Insurance Premium Calculator**, e.g. payment section or damage declaration form.
-  The application can be extended for other types of insurance.
-  It should allow administrators to create and manage posts or announcements displayed in different and more interesting formats.
-  The customer should upload files, e.g. the documents of car or driving license.
  
-----------------------------------------------------------------------------
## Additional Points

The algorithm takes into account multiple variables to ensure accurate and tailored premium estimations. The parameters and insurance rates used in this application, are based on practices in my country.

For designing the pages, CSS and bootstrap are used in some features, written in styles.css.