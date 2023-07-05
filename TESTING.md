# **Burgers R-Us Testing**

## **Overview**
A wide range of testing was carried out during development including, Automated testing, manual testing, user story testing, code validation and bug testing.

[Back to README](/README.md)

## **User Story Testing**

Overall there were 55 completed user stories and 1 uncompleted user story throughout the projects development. They will all be tested below to ensure criteria has been met for each story. The users stories will be broken down into their respetive milestones to be tested.

### **EPIC: Django Installation and app setup**

#### 1. [**USER STORY: Create Superuser**](https://github.com/seanj06/Burgers-R-Us-P5/issues/1)

As a developer I can create a superuser so that i can manage my application from the admin panel.

This user story had a must-have label.

**Acceptance Criteria**

- 1.Superuser is created from command line with secure password.

  - The superuser was created at the beginning of development from the cli.

- 2.Login to admin panel to check superuser has been created 
    successfully.   
  -  After the superuser was created a check was made from the admin panel that the superuser could successfully login.

#### 2. [USER STORY: Install Django and relevant libraries](https://github.com/seanj06/Burgers-R-Us-P5/issues/2)   

As a developer I can install Django and all other relevant libraries so that development on my app can start.

This user story had a must-have label.

**Acceptance Criteria**

- 1.Django installed correctly from command line

  - Django was installed from cli at start of development

- 2.All other packages installed from command line

  - All other django related projects were also installed.

- 3.All packages freezed into requirements.txt file   

  -  All django related packages were pip freezed to requirements.txt file.

#### 3. [USER STORY: Create Django Project And App](https://github.com/seanj06/Burgers-R-Us-P5/issues/3)

As a developer I can create a new django project and app so that I can start development on my project

This user story had a must have label.

**Acceptance Criteria**

- 1.New django project created with appropriate name

  - New django project was created and named from the cli

- 2.New django app created with appropriate name

  - The home app was the first app created within the project.

- 3.New app added to installed apps in settings.py

  - After creation the home app was added to installed apps in settings.py.

[Top of page &uarr;](#contents)

### **EPIC: First Heroku Deployment** 

#### 4. [USER STORY: Create new Heroku app](https://github.com/seanj06/Burgers-R-Us-P5/issues/7)

As a developer I can create a new Heroku app so that my site can be deployed correctly.

This user story had a must have label.

**Acceptance Criteria**

- 1.New Heroku app created

  - A new app was created on Heroku to link to my project

- 2.Relevant config vars entered for deployment

  - All relevant config vars were added to heroku pre delployment including DATABASE_URL and SECRET_KEY.

- 3.Disable collect static initially set as a config var before was bucket is set up.

  - One the first deployment the disablecollect static config var was added.

- 4.Link github repo to heroku app

  - The projects github repo was linked to the heroku app in the deployment tab.

#### 5. [USER STORY: Static File Hosting](https://github.com/seanj06/Burgers-R-Us-P5/issues/8)

As a developer I can set up an aws bucket and link it to my deployed heroku app so that it serves the static files of my deployed app

This user story had a must-have label

**Acceptance Criteria**

- 1.Set up aws bucket and get secret keys

  - Secret keys were downloaded onto my machine after the aws bucket was setup

- 2.Add aws keys to heroku config vars

  - The aws secret key variables were added to my heroku app after the aws bucket was set up.

- 3.Remove disable collectstatic config vars

  - The disable collect static config var was removed and the site was deployed with aws static file hosting.

[Top of page &uarr;](#contents)

### **EPIC: Allauth Installation And Setup**

#### 6. [USER STORY: Email Verification](https://github.com/seanj06/Burgers-R-Us-P5/issues/6)

As a user I want to receive email verification so that my account is set up correctly

This user story had a should-have label

**Acceptance Criteria**

- 1.Set up backend email settings in settings.py

  - Email settings were set up in settings.py for both development and production.

- 2.Set up heroku config vars for email host and password

  - Heroku config vars were added to link to email backend setup.

#### 7. [USER STORY: Sign Up/Sign In/ Sign out](https://github.com/seanj06/Burgers-R-Us-P5/issues/5)

As a user I want to make an account and be able to sign in and out so that I can access all the features available to registered users

This user story had a must-have label

**Acceptance Criteria**

- 1.Users are able to sign in/out and sign up from the navbar

  - Sign in, sign out and register links are available to the user from the navbar.

- 2.All of the allauth templates match the rest of the site

  - All of the allauth templates have been custom styled to match the rest of the site.

#### 8. [USER STORY: Customise Allauth templates](https://github.com/seanj06/Burgers-R-Us-P5/issues/10)  

As a developer I can customise the alluth templates so that they match the theme of the rest of the site

This user story had a should-have label.

**Acceptance Criteria**

- 1.Allauth templates are imported into correct folder

  - Allauth templates were imported from the cli into the templates folder.

- 2.Templates match the theme of the rest of the site

  - All of the allauth templates have been custom styled to match the rest of the site.

#### 9. [USER STORY: Install Allauth](https://github.com/seanj06/Burgers-R-Us-P5/issues/4)

As a developer I can install allauth so that users can make an account and sign in

**Acceptance Criteria**

- 1.Allauth installed from command line

  - Allauth was installed from the cli at the start of development

- 2.Allauth added to installed apps in settings.py

  - Allauth was added to installed apps in settings.py

- 3.Alluth freeze to requirements.txt  

  - After allauth was installed it was added to the requirements.txt file.

[Top of page &uarr;](#contents)

### **EPIC: User Checkout**

#### 10. [USER STORY: Checkout Template](https://github.com/seanj06/Burgers-R-Us-P5/issues/27)

As a developer I can create a checkout template so that the user has a page to navigate to to checkout securely

This user story had a must-have label

**Acceptance Criteria**

- 1.Checkout page features checkout form which is linked to checkout model

  - Checkout form was added to the checkout page which links to the model.

- 2.User only able to submit form if all fields are valid

  - Form validation was added to form fields and users are shwon an error message if the form is invalid.

- 3.User form and checkout page matches rest of site

  - The checkout page was styled to match the rest of the site.

#### 11. [USER STORY: Checkout Form](https://github.com/seanj06/Burgers-R-Us-P5/issues/28)

As a developer I can create a custom user form so that users can securely checkout

This user story had a should-have label

**Acceptance Criteria**

- 1.Form has correct attributes attached

  - Custom widgets were added to the form in forms.py

- 2.All fields that are required are set to required

  - All required fields were set to required in both the model and forms.py

- 3.Form only valid on correct user input

  - Error handling was added for the form fields.

#### 12. [USER STORY: Checkout Models](https://github.com/seanj06/Burgers-R-Us-P5/issues/26)

As a developer I can create checkout database models so that the correct user information is saved in thee database upon checkout

This user story had a must-have label

**Acceptance Criteria**

- 1.All vital user information is saved in database model

  - All of the users personal and delivery info are included in the model fields.

- 2.Unique order number is included in model

  - A custom order generator was created to add a unique order number for every order.

- 3.Delivery information, and cost is saved in database

  - All user delivery information and delivery cost information are included in the model.

[Top of page &uarr;](#contents)

### **EPIC: User profile**

#### 13. [USER STORY: Order History](https://github.com/seanj06/Burgers-R-Us-P5/issues/35)

As a user I can view my order history from my profile so that I can view all my orders from one place

This user story had a should-have label

**Acceptance Criteria**

- 1.Users can view order history from profile page

  - Code was added to let users view their order history from the profile page

- 2.All order details are shown

  - All order history details are shown to the user including product info and costs.

#### 14. [USER STORY: Default form info](https://github.com/seanj06/Burgers-R-Us-P5/issues/36)


As a user I can have all of my default delivery information saved so that I can easily fill out delivery forms when needed

This user story had a could-have label.

**Acceptance Criteria**

- 1.Users can update their default info from profile page

  - Users are able to enter their default delivery info and save it from the profile page

- 2.Users can choose to save their info when checking out

  - When checking out users can click the save info box to save the delivery info for the next time.

#### 15. [USER STORY: Profile View](https://github.com/seanj06/Burgers-R-Us-P5/issues/34)

As a developer I can set up profile views so that the logic can be handled for the profile app

**Acceptance Criteria**

- 1.Home view is set up to render profile page

  - Profile view was set up to render profile template

- 2.Url is added for profile home view

  - Profile url was added to urls.py file

#### 16. [USER STORY: Profile Model](https://github.com/seanj06/Burgers-R-Us-P5/issues/33)

As a developer I can **create a profile model ** so that users can access their delivery and order information and history

This user story had a must-have label

**Acceptance Criteria**

- 1.Profile model is linked to User model

  - Profile model is linked to User model via a OneToOne field

- 2.Profile model is linked to Order model 

   - The Profile model is linked to the Order model via a ForeignKey

#### 17. [USER STORY: Profile app](https://github.com/seanj06/Burgers-R-Us-P5/issues/32)

As a developer I can create a profile app so that user profiles can be organised into their own models views and urls

This user story had a must-have label

**Acceptance Criteria**

- 1.Profile app created from terminal

  - The profile app was created from the terminal

- 2.Profile app is added to installed apps

  - After creation the profile app was added to installed apps in settings.py

- 3.Profile app added to main URL file

  - The profile app urls was added to the main urls.py file

[Top of page &uarr;](#contents)

### **EPIC: U/X**

#### 18. [USER STORY: Custom Error Pages](https://github.com/seanj06/Burgers-R-Us-P5/issues/49)

As a developer I can add custom error pages so that the error pages users see match the rest of the site

This user story had a must-have label

**Acceptance Criteria**

- 1.All error pages match the theme of the rest of the site

  - All custom error pages have been styled to match the rest of the site

- 2.All error pages show the user a home button to navigate back to the home page

  - All error pages include a home button for the users to return to the homepage.

#### 19. [USER STORY: Finish styling allauth pages](https://github.com/seanj06/Burgers-R-Us-P5/issues/47)

As a developer I can finish styling the allauth pages so that the pages match the theme of the rest of the site

This user story had a should-have label

**Acceptance Criteria**

- 1.All pages match the theme of the rest of the site

  - All allauth pages have been styled to match the rest of the site

- 2.All pages are responsive on all screen sizes and no content is blocked by page header

  - Appropriate padding and classes were added to ensure responsiveness

- 3.All correct user toast messages are shown

  - All pages were tested to ensure users are shown correct toasts.

#### 20. [USER STORY: Finish stying product pages](https://github.com/seanj06/Burgers-R-Us-P5/issues/48)

As a developer I can finish styling the product pages so that the pages match the rest of the site

This user story had a must-have label.

**Acceptance Criteria**

- 1.Product pages match the rest of the site

  - All product pages match the theme of the rest of the site

- 2.Pages are fully responsive on all screen sizes

  - Relevant media queries and bootstrap classed were added to ensure responsiveness.

- 3.Users are shown correct toast messages

  - All product pages were tested to ensure users were shown correct toast messages.

- 4.Only authorized users can access certain features

  - There is login required and user checks to ensure only authorized users can access certain features.




















































