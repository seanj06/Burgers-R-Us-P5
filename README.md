# **Burgers R-Us**

## **Overview**

Burgers R-Us is a local takeaway e-commerce site that specialises in Burgers and Fries. Users are able to add Products to the cart and checkout securely
via stripe whether they are signed in or not. If users sign up for an account they unlock more features such as saving  default delivery info, being able
to contact the site with any issues or queries and writing and liking reviews.

Other features of the site include users being able to searh for products via a search bar, a product filter search by category, sub category and being 
able to sort products by a wide range of different filters.

Developed by Sean Johnston for code institute Project Portfolio project 5.

Link to the live site : [Burgers R-Us](https://burgers-r-us1.herokuapp.com/)

## **Project Goals**

As my fifth project for the [Code Institute](https://codeinstitute.net/) 5P course, the goal of the project is to demonstrate all of the skills I have learned in the course so far including languages such as HTML, CSS, Javascript and Python. Frameworks such as Django and Bootstrap and version control technologies such as Git and Github.

## **UX**

## **The Strategy Plane**

Burgers R-Us is an e-commerce site for a local takeaway which is designed to be easy for users to find products, add them into their cart, securely checkout
and enter their delivery details.

Registered users will be able to contact the site owners about any enquiries or issues, save default delivery info and write and like reviews.
Users with Staff status will be able to add, edit or delete products from the site aswell as the admin area.

The design of the overall site is aimed to be eye catching for the users and easy on the eye with a darker theme rather than light.

### **Target Users**

- A user looking to order a takeaway online
- A user who likes to read/add reviews about food
- A user who likes the convenience of being able to save default delivery info to their profile
- A user who likes using a recognisable secure checkout method(stripe)

### **Site Goals**

- To provide users with the ability to order food for delivery online
- To provide users with the ability to make an account to save their details
- To provide users with the ability to write/like reviews
- To provide users with the ability to contact the site owners about any issues or queries
- To provide users with the ability to search fro different products in a wide variety of different ways.

## **The Scope Plane**

- CRUD Ability for authenticated users on Reviews and profile info
- CRUD Ability for both authenticated and non authenticated users on cart
- Restricted site features for authenticated and non-authenticated users such as adding and liking reviews, saving profile info and contact section.
- Restricted site features for staff such as adding, editing and deleting products.
- Full responsiveness for all screen sizes down to 320px including different navbar layout for medium to small screens.

## **Agile Planning**

This project was built using the Agile method throughout by creating EPIC Milestones which were broken down into smaller user stories with labels "must-have", "should-have", "could-have", and wont have. 

Epics milestones were given Acceptance criteria and the must haves were completed first to complete the milestone. Any user stories that were not completed were moved back into the project backlog.

The Kanban board was created using Github projects and can be located [here]()  and can be viewed to see the completed and backlogged user stories.

![Kanban Board]()

### **Epics**

Epics were broken down into 13 EPIC Milestones(including backlog)
which includes 56 user stories in total. Each Milestone was closed when all the criteria had been met / all user stories were completed.
User stories were given tasks, and when each task and the given user stories were completed a comment was left with the commit number underneath the user story. When all tasks were complete the user story was closed.
All user stories attached to the milestones will be tested in the testing user stories section of testing.md

#### **EPIC: Django Installation and app setup [Milestone #1](https://github.com/seanj06/Burgers-R-Us-P5/milestone/1)**

This Epic had 3 user stories attached and was the first to be completed 
due to it being needed for the project work to start

1. **[USER STORY: Create Django Project And App #3](https://github.com/seanj06/Burgers-R-Us-P5/issues/3)**

2. **[USER STORY: Install Django and relevant libraries #2](https://github.com/seanj06/Burgers-R-Us-P5/issues/2)**

3. **[USER STORY: Create Superuser #1](https://github.com/seanj06/Burgers-R-Us-P5/issues/1)**

#### **EPIC: First Heroku Deployment [Milestone #2](https://github.com/seanj06/Burgers-R-Us-P5/milestone/2)**

This Epic had 2 user stories attached and involved setting up heroku and aws bucket for deployment

1. **[USER STORY: Static File Hosting #8](https://github.com/seanj06/Burgers-R-Us-P5/issues/8)**

2. **[USER STORY: Create new Heroku app #7](https://github.com/seanj06/Burgers-R-Us-P5/issues/7)**

#### **EPIC: Allauth Installation And Setup [Milestone #3](https://github.com/seanj06/Burgers-R-Us-P5/milestone/9)**

This Epic had 4 user stories attached and involved setting up allauth, customising allauth templates and setting up emails.

1. **[USER STORY: Install Allauth #4](https://github.com/seanj06/Burgers-R-Us-P5/issues/4)**

2. **[USER STORY: Customise Allauth templates #10](https://github.com/seanj06/Burgers-R-Us-P5/issues/10)**

3. **[USER STORY: Sign Up/Sign In/ Sign out #5](https://github.com/seanj06/Burgers-R-Us-P5/issues/5)**

4. **[USER STORY: Email Verification #6](https://github.com/seanj06/Burgers-R-Us-P5/issues/6)**

#### **EPIC: User Checkout [Milestone #4](https://github.com/seanj06/Burgers-R-Us-P5/milestone/12?closed=1)**

This Epic had 3 user stories attached and involved setting up the checkout models, templates and forms.

1. **[USER STORY: Checkout Models #26](https://github.com/seanj06/Burgers-R-Us-P5/issues/26)**

2. **[USER STORY: Checkout Form #28](https://github.com/seanj06/Burgers-R-Us-P5/issues/28)**

3. **[USER STORY: Checkout Template #27](https://github.com/seanj06/Burgers-R-Us-P5/issues/27)**

#### **EPIC: User profile [Milestone #5](https://github.com/seanj06/Burgers-R-Us-P5/milestone/5?closed=1)**

This Epic had 5 user stories attached and involved setting up the profile models, view app and order history

1. **[USER STORY: Profile app #32](https://github.com/seanj06/Burgers-R-Us-P5/issues/32)**

2. **[USER STORY: Profile Model #33](https://github.com/seanj06/Burgers-R-Us-P5/issues/33)**

3. **[USER STORY: Profile View #34](https://github.com/seanj06/Burgers-R-Us-P5/issues/34)**

4. **[USER STORY: Default form info #36](https://github.com/seanj06/Burgers-R-Us-P5/issues/36)**

5. **[USER STORY: Order History #35](https://github.com/seanj06/Burgers-R-Us-P5/issues/35)**

#### **EPIC: Home page creation [Milestone #6](https://github.com/seanj06/Burgers-R-Us-P5/milestone/4)**

This Epic had 5 user stories attached and involved setting up the navbar, search functionality and styling for the home page

1. **[USER STORY: Navbar creation #11](https://github.com/seanj06/Burgers-R-Us-P5/issues/11)**

2. **[USER STORY: Search functionality #17](https://github.com/seanj06/Burgers-R-Us-P5/issues/17)**

3. **[USER STORY: Hero Image #12](https://github.com/seanj06/Burgers-R-Us-P5/issues/12)**

4. **[USER STORY: Home page styling #18](https://github.com/seanj06/Burgers-R-Us-P5/issues/18)**

5. **[USER STORY: Contact Form #37](https://github.com/seanj06/Burgers-R-Us-P5/issues/37)**













