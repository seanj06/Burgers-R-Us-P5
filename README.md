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

#### **EPIC: Stripe Setup [Milestone #7](https://github.com/seanj06/Burgers-R-Us-P5/milestone/6?closed=1)**

This Epic had 4 user stories attached and involved setting up stripe on both the code and on Heroku

1. **[USER STORY: Checkout Success #30](https://github.com/seanj06/Burgers-R-Us-P5/issues/30)**

2. **[USER STORY: Render Stripe Field To Template #29](https://github.com/seanj06/Burgers-R-Us-P5/issues/29)**

3. **[USER STORY: Heroku stripe setup #9](https://github.com/seanj06/Burgers-R-Us-P5/issues/9)**

4. **[USER STORY: Webhooks #31](https://github.com/seanj06/Burgers-R-Us-P5/issues/31)**

#### **EPIC: Crud Functionality [Milestone #8](https://github.com/seanj06/Burgers-R-Us-P5/milestone/8)**

This Epic had 11 user stories attached and involved all crud functionality across the site for both staff and users.

1. **[USER STORY: Add Product To Cart #13](https://github.com/seanj06/Burgers-R-Us-P5/issues/13)**

2. **[USER STORY: Edit quantity in cart #15](https://github.com/seanj06/Burgers-R-Us-P5/issues/15)**

3. **[USER STORY: Remove item from cart #14](https://github.com/seanj06/Burgers-R-Us-P5/issues/14)**

4. **[USER STORY: Create a review #38](https://github.com/seanj06/Burgers-R-Us-P5/issues/38)**

5. **[USER STORY: Read A Review #39](https://github.com/seanj06/Burgers-R-Us-P5/issues/39)**

6. **[USER STORY: Update Review #40](https://github.com/seanj06/Burgers-R-Us-P5/issues/40)**

7. **[USER STORY: Delete Review #41](https://github.com/seanj06/Burgers-R-Us-P5/issues/41)**

8. **[USER STORY: Add Products to site #42](https://github.com/seanj06/Burgers-R-Us-P5/issues/42)**

9. **[USER STORY: Edit Product #43](https://github.com/seanj06/Burgers-R-Us-P5/issues/43)**

10. **[USER STORY: Delete Products #44](https://github.com/seanj06/Burgers-R-Us-P5/issues/44)**

11. **[USER STORY: View Items in cart #16](https://github.com/seanj06/Burgers-R-Us-P5/issues/16)**

#### **EPIC: U/X [Milestone #9](https://github.com/seanj06/Burgers-R-Us-P5/milestone/14)**

This Epic had 6 user stories attached and involved finishing off the styling of pages for u/x

1. **[USER STORY: User Notifications #25](https://github.com/seanj06/Burgers-R-Us-P5/issues/25)**

2. **[USER STORY: Finish styling cart page #46](https://github.com/seanj06/Burgers-R-Us-P5/issues/46)**

3. **[USER STORY: Finish styling home page #45](https://github.com/seanj06/Burgers-R-Us-P5/issues/45)**

4. **[USER STORY: Finish stying product pages #48](https://github.com/seanj06/Burgers-R-Us-P5/issues/48)**

5. **[USER STORY: Finish styling allauth pages #47](https://github.com/seanj06/Burgers-R-Us-P5/issues/47)**

6. **[USER STORY: Custom Error Pages #49](https://github.com/seanj06/Burgers-R-Us-P5/issues/49)**

#### **EPIC: SEO [Milestone #10](https://github.com/seanj06/Burgers-R-Us-P5/milestone/10?closed=1)**

This Epic had 3 user stories attached and involved SEO optimization

1. **[USER STORY: Seo implementation #50](https://github.com/seanj06/Burgers-R-Us-P5/issues/50)**

2. **[USER STORY: XML sitemap #51](https://github.com/seanj06/Burgers-R-Us-P5/issues/51)**

3. **[USER STORY: Robots.txt file #52](https://github.com/seanj06/Burgers-R-Us-P5/issues/52)**

#### **EPIC: Product Page [Milestone #11](https://github.com/seanj06/Burgers-R-Us-P5/milestone/13?closed=1)**

This Epic had 5 user stories attached and invloved the creation of the product page and search and filter functionality.

1. **[USER STORY: View Products #20](https://github.com/seanj06/Burgers-R-Us-P5/issues/20)**

2. **[USER STORY: Individual Product Details #21](https://github.com/seanj06/Burgers-R-Us-P5/issues/21)**

3. **[USER STORY: Filter Product By Category #23](https://github.com/seanj06/Burgers-R-Us-P5/issues/23)**

4. **[USER STORY: Sort Food Products #24](https://github.com/seanj06/Burgers-R-Us-P5/issues/24)**

5. **[USER STORY: Product page creation #19](https://github.com/seanj06/Burgers-R-Us-P5/issues/19)**

#### **EPIC: Testing [Milestone #12](https://github.com/seanj06/Burgers-R-Us-P5/milestone/16)**

This Epic had 4 user stories and involved all testing including automated testing, manual testing, code validation and lighthouse testing

1. **[USER STORY: Python Automated testing #53](https://github.com/seanj06/Burgers-R-Us-P5/issues/53)**

2. **[USER STORY: Lighthouse testing #56](https://github.com/seanj06/Burgers-R-Us-P5/issues/56)**

3. **[USER STORY: Code validation #55](https://github.com/seanj06/Burgers-R-Us-P5/issues/55)**

4. **[USER STORY: Python manual testing #54](https://github.com/seanj06/Burgers-R-Us-P5/issues/54)**

#### **[Backlog](Backlog)**

The backlog currently has 1 unfinished user story in it. Products special offer page which was not completed due to time constraints. This will be discussed further in the testing user stories section

1.**[USER STORY: Product Special Offers page #22](https://github.com/seanj06/Burgers-R-Us-P5/issues/22)**













