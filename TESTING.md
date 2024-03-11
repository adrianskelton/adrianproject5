Go back to [README.md](/README.md)

# Testing

- [Code Validation](#code-validation)
  - [CSS](#css)
  - [JavaScript](#JavaScript)
  - [Python](#python)
- [Responsiveness](#Responsiveness)
- [Browser Compatibility](#browser-compatibility)
- [Lighthouse](#Lighthouse)
- [CRUD](#crud)
- [Manual Testing](#manual-testing)
- [Automated Testing](#automated-testing)
- [User Story Testing](#user-story-testing)
- [Stripe](#stripe)
- [Bugs](#bugs)

## Code Validation

### CSS

| File     | Validator                                                       | Result           |
| -------- | --------------------------------------------------------------- | ---------------- |
| Base     | ![base](static/media/readme/testing/testing-css-pass.webp)         | <mark>PASS<mark> |
| Home  | ![program](static/media/readme/testing/testing-css-home.png)  | <mark>PASS<mark> |
| Profile  | ![profile](static/media/readme/testing/testing-css-profiles.png)  | <mark>PASS<mark> |
| Checkout | ![checkout](static/media/readme/testing/testing-css-checkout.png) | <mark>PASS<mark> |


## JavaScript

| File               | Validator                                                                   | Result           | Comment                          |
| ------------------ | --------------------------------------------------------------------------- | ---------------- | -------------------------------- |
| stripe_elements.js | ![stripe elements](static/media/readme/testing/testing-jshint-stripe.png) | <mark>PASS<mark> | Global variables and es6 enabled |
| countryfield.js           | ![country](static/media/readme/testing/testing-jshint-country.png)                    | <mark>PASS<mark> | 'let' is available in ES6 (use 'esversion: 6') or Mozilla JS extensions (use moz). |

## Python

| File     | App      | Image                                                                     | Result           | Comment                                                             |
| -------- | -------- | ------------------------------------------------------------------------- | ---------------- | ------------------------------------------------------------------- |
| views    | home     | ![views](static/media/readme/testing/testing-pyhome-views.png)           | <mark>PASS<mark> |                                                                     |
| urls     | home     | ![urls](static/media/readme/testing/testing-pyhome-urls.png)             | <mark>PASS<mark> |                                                                     |<mark>PASS<mark> |                                                                     |
| views    | products | ![views](static/media/readme/testing/testing-pyproducts-views.png)       | <mark>PASS<mark> |                                                                     |
| urls     | products | ![urls](static/media/readme/testing/testing-pyproducts-urls.png)         | <mark>PASS<mark> |                                                                     |
| models   | products | ![models](static/media/readme/testing/testing-pyproducts-models.png)     | <mark>PASS<mark> |                                                                     |
| admin    | products | ![admin](static/media/readme/testing/testing-pyproducts-admin.png)       | <mark>PASS<mark> |                                                                     |
| forms    | products | ![forms](static/media/readme/testing/testing-pyproducts-forms.png)        | <mark>PASS<mark> |                                                                     |                                                                    |
| views    | profiles | ![views](static/media/readme/testing/testing-pyprofile-views.png)       | <mark>PASS<mark> |                                                                     |
| urls     | profiles | ![urls](static/media/readme/testing/testing-pyprofile-urls.png)         | <mark>PASS<mark> |                                                                     |
| models   | profiles | ![models](static/media/readme/testing/testing-pyprofile-models.png)     | <mark>PASS<mark> |                                                                     |
| webhooks | checkout | ![webhooks](static/media/readme/testing/testing-pycheckout-webhooks.png) | <mark>PASS<mark> |  |

## Responsiveness

The responsiveness of the website was thoroughly tested on various devices, including a Huawei matebook 15-inch, and a 24-inch monitor. 

Across all devices, the elements displayed cleanly and were well-organized, ensuring a consistent and user-friendly experience. I also tested it on my google pixel 7a and on google chrome's responsiveness checker with inspector tools.

## Browser Compatibility

| Browser       | Result                                                     | Pass/Fail         |
| ------------- | ---------------------------------------------------------- | ----------------- |
| Google Chrome | All pages, load as expected. All features work as expected | <mark>Pass</mark> |
| Firefox       | All pages, load as expected. All features work as expected | <mark>Pass</mark> |
| Edge          | All pages, load as expected. All features work as expected | <mark>Pass</mark> |
| Safari        | All pages, load as expected. All features work as expected | <mark>Pass</mark> |

## Lighthouse

| Page                   | Validator                                                                                    | Result                 |
| ---------------------- | -------------------------------------------------------------------------------------------- | ---------------------- |
| Home                   | ![home](static/media/readme/testing/testing-lighthouse-home.png)                                  | <mark>Excellent</mark> |
| Home Mobile            | ![home mobile](static/media/readme/testing/testing-lighthouse-home-mobile.png)                     | <mark>Good</mark>      |
| Products               | ![products](static/media/readme/testing/testing-lighthouse-products.png)                          | <mark>Good</mark> |
| Product Mobile         | ![products mobile](static/media/readme/testing/testing-lighthouse-products-mobile.png)             | <mark>Pass</mark>      |
| Product Detail         | ![product detail](static/media/readme/testing/testing-lighthouse-productsdetail.png)               | <mark>Good</mark>      |
| Product Detail Mobile  | ![product detail mobile](static/media/readme/testing/lighthouse-productdetail-mobile.png)  | <mark>Pass</mark>      |
| Artists Mobile    | ![artist mobile](static/media/readme/testing/lighthouse-artists-mobile.png)     | <mark>Pass</mark>      |
| Artists     | ![artist Desktop](static/media/readme/testing/lighthouse-artists-desktop.png)     | <mark>Pass</mark>      |
| Artists Mobile    | ![subscription mobile](static/media/readme/testing/lighthouse-blog-mobile.png)    | <mark>Pass</mark>      |
| Blog            | ![Blog](static/media/readme/testing/lighthouse-blog-desktop.png)                       | <mark>Excellent</mark> |
| Blog Mobile      | ![Blog mobile](static/media/readme/testing/lighthouse-blog-mobile.png)          | <mark>Good</mark> |
| Contact us      | ![Contact ](static/media/readme/testing/lighthouse-contact-desktop.png)          | <mark>Excellent</mark> |
| Contact us Mobile     | ![Contact Mobile ](static/media/readme/testing/lighthouse-contact-mobile.png)          | <mark>Excellent</mark> |

Signficant optimisation practices were used to try and increase the Largest Contentful Paint (LCP)

1. Lazy load of images where possible
2. Defer load non essential JS scripts
3. Use of online image convertor to webp images

I could further reduce the size of images possibly and also minify the scripts but due to time constraints this will need to be done later.

## CRUD

The main custom crud functionality of this website pertains to the comments by the users who are allowed to submit, edit and delete comments. However users can also view products and orders as well as create a user profile for themselves and edit order information such as delivery address.


## Manual Testing

### Site Navigation

| Element                  | Action      | Expected Result                                         | Pass/Fail         |
| ------------------------ | ----------- | ------------------------------------------------------- | ----------------- |
| Logo                     | Click       | Redirect to Home page                                   | <mark>Pass</mark> |
| My Account Button        | Click       | Render a dropdown menu of all account options           | <mark>Pass</mark> |
| Prints Link              | Click       | Dropdown expands showing photography and digital subcategories              | <mark>Pass</mark> |
| Photography Link         | Click       | Redirect to selected photography prints category page   | <mark>Pass</mark> |
| Digital Link             | Click       | Redirect to selected digital prints category page       | <mark>Pass</mark> |
| Artists Link             | Click       | Redirect to selected artists page                       | <mark>Pass</mark> |
| Profile Dropdown         | Click       | Redirect to selected page                               | <mark>Pass</mark> |
| Profile Dropdown Link    | Click       | Redirect to selected page                               | <mark>Pass</mark> |
| Profile Dropdown Auth    | Display     | Render logout, profile, courses, add product links      | <mark>Pass</mark> |
| Profile Dropdown NonAuth | Click       | Render login and register links                         | <mark>Pass</mark> |
| Cart Icon Link           | Click       | Redirect to cart page                                   | <mark>Pass</mark> |
| Hamburger Menu           | Click       | Render a dropdown menu of all links                     | <mark>Pass</mark> |
| Contact Page             | Click       | Redirect to contact page                                | <mark>Pass</mark> |
| Newsletter Input Valid   | Submit      | User notified of success                                | <mark>Pass</mark> |
| Newsletter Input Invalid | Submit      | Error context displayed to UI                           | <mark>Pass</mark> |
| Register Link            | Display     | Render for non authenticated users                      | <mark>Pass</mark> |
| Log in Link              | Display     | Render for non authenticated users                      | <mark>Pass</mark> |
| Log out Link             | Display     | Render only if user is authenticated                    | <mark>Pass</mark> |
| Profile Link             | Display     | Render only if user is authenticated                    | <mark>Pass</mark> |
| Nav Link                 | Hover/Focus | Darken colour of text                                   | <mark>Pass</mark> |
| Footer Socials           | Click       | Opens the related github or facebook page in new tab    | <mark>Pass</mark> |

### Home Page

| Element            | Action | Expected Result                           | Pass/Fail         |
| ------------------ | ------ | ----------------------------------------- | ----------------- |
| Shop Now Button    | Click  | Redirect to selected product page         | <mark>Pass</mark> |


### Product Page

| Element                  | Action      | Expected Result                                                 | Pass/Fail         |
| ------------------------ | ----------- | --------------------------------------------------------------- | ----------------- |
| Category Widgets         | Click       | Redirect to selected product category page                      | <mark>Pass</mark> |
| Filter By..option   | Click       | Filter queried products based on selection                        | <mark>Pass</mark>
| Filter Direction         | Display     | Filter direction displayed via an arrow                         | <mark>Pass</mark> |
| Search Bar               | Search      | Filter products based on query to category, name or description | <mark>Pass</mark> |
| Product Cards            | Display     | All filtered Product Cards Rendered in grid layout              | <mark>Pass</mark> |
| Product View Card Button | Click       | Redirect to product detail page                                 | <mark>Pass</mark> |
| Artist        | Click | See artist page                       | <mark>Pass</mark> |

### Product Detail Page

| Element             | Action      | Expected Result                                                  | Pass/Fail         |
| ------------------- | ----------- | ---------------------------------------------------------------- | ----------------- |
| Quantity Input      | Input       | Updates the total amount of desired product - no negative values | <mark>Pass</mark> |
| Add to Cart Button  | Click       | Total quantity of item added to cart                             | <mark>Pass</mark> |
| Add to Cart Button  | Click       | Notification appears upon outcome of adding to cart              | <mark>Pass</mark> |
| Product Edit Button | Display     | Only moderators and admins can see this button                   | <mark>Pass</mark> |
| Product image hover | Hover       | Shows buy text over image                                    | <mark>Pass</mark> |
| Back Link           | Click       | Redirects back to the products page                              | <mark>Pass</mark> |
| Add to Cart Button  | Hover/Focus | Background darkens, text lightens                                | <mark>Pass</mark> |

### Cart Page

| Element                     | Action      | Expected Result                                                | Pass/Fail         |
| --------------------------- | ----------- | -------------------------------------------------------------- | ----------------- |
| Update Cart Button          | Click       | Updates the quantity of product by desired amount              | <mark>Pass</mark> |
| Remove from Cart Button     | Click       | Removes all quantity of selected item from cart                | <mark>Pass</mark> |
| Add / Remove Cart Button    | Click       | Notification appears upon outcome of adding/removing from cart | <mark>Pass</mark> |
| Checkout Button             | Click       | Redirects to checkout page                                     | <mark>Pass</mark> |
| Continue Shopping Link      | Click       | Redirects to products page                                     | <mark>Pass</mark> |
| Update Cart Button          | Display     | Only available for products                                    | <mark>Pass</mark> |
| Total Cost                  | Display     | Total cost is accurately displayed with breakdown              | <mark>Pass</mark> |
| Update Cart Button          | Hover/Focus | Background darkens, text darkens                               | <mark>Pass</mark> |
| Remove from cart Button     | Hover/Focus | Background darkens, text darkens                               | <mark>Pass</mark> |
| Continue Shopping Link      | Hover/Focus | Text darkens                                                   | <mark>Pass</mark> |

### Checkout Page

| Element                    | Action      | Expected Result                                            | Pass/Fail         |
| -------------------------- | ----------- | ---------------------------------------------------------- | ----------------- |
| Checkout No Items          | Display     | Redirect to cart page with noti                            | <mark>Pass</mark> |
| Checkout Form              | Submit      | Checkout form submit user and delivery data to stripe      | <mark>Pass</mark> |
| Checkout Form              | Submit      | Stripe payment intent, charge and succeeded occurs         | <mark>Pass</mark> |
| Checkout Form              | Submit      | Non valid form returns context of errors                   | <mark>Pass</mark> |
| Checkout Form              | Submit      | Successful order redirects to checkout success page        | <mark>Pass</mark> |
| Checkout Form              | Submit      | Stripe webhooks are logged via stripe listeners            | <mark>Pass</mark> |
| Checkout Form Save Details | Submit      | Authenticated users details are saved if button is checked | <mark>Pass</mark> |
| Stripe Payment Element     | Submit      | Stripe payment element renders error context if not valid  | <mark>Pass</mark> |
| Pay Now Button             | Click       | Submits user/delivery/payment information                  | <mark>Pass</mark> |
| Continue Shopping Link     | Click       | Redirects to products page                                 | <mark>Pass</mark> |
| Remove from Cart Button    | Click       | Removes all quantity of selected item from cart            | <mark>Pass</mark> |
| Loading Spinner            | Display     | A loading spinner is displayed when await payment results  | <mark>Pass</mark> |
| Cart Items                 | Display     | All Cart items are displayed with a price breakdown        | <mark>Pass</mark> |
| Total Cost                 | Display     | The total cost is accounted for for a price breakdown      | <mark>Pass</mark> |


### Checkout Success/ Past Order Page

| Element       | Action  | Expected Result                                                     | Pass/Fail         |
| ------------- | ------- | ------------------------------------------------------------------- | ----------------- |
| Checkout Form | Display | Checkout form rendered all Order information, price, user, delivery | <mark>Pass</mark> |
| Checkout Form | Display | Total cost breakdown is displayed for the user                      | <mark>Pass</mark> |
| Notification  | Display | A Notification appears highlighting the successful order number     | <mark>Pass</mark> |

## User Story Testing
## Manual Testing

I performed manual testing based on my user stories. For it to be deemed successful, it must have satisfied the acceptance criteria. I conducted these tests on Google Chrome, Mozilla Firefox, and Microsoft Edge.

| User story - As a user, I can...                                                                                             | Notes  | 
| ---------------------------------------------------------------------------------------------------------------------------- | ------ |
| **create an account** to **access user only features and have access to shopping**.                                          | Passed ✅ |   
| **log into my account** to **access my personal settings and history, or prefill my details at checkout**.                   | Passed ✅|   
| **log out of my account** to **ensure my account is secure when I am not actively using it**.                                | Passed ✅|  
| **update my account/profile** to **keep my personal information up to date for checking out**.                               | Passed ✅|  
| **access and view my user profile** to **see my personal information, order history, and manage my account settings**.       | Passed ✅|  
| **view a summary of my orders** to **keep track of my purchases** (as a **registered customer**).                            | Passed ✅|  
| **create new products** to **offer more choices to customers** (as a **staff member**).                                      | Passed ✅|  
| **update product details** to **ensure all information about the products is current and accurate** (as a **staff member**). | Passed ✅|  
| **delete products** to **remove items that are no longer available or relevant** (as a **staff member**).                    | Passed ✅|   
| **add products to my cart** to **purchase them** (as a **customer**).                                                        | Passed ✅|   
| **remove products from my cart** to **manage items before finalizing my purchase** (as a **customer**).                      | Passed ✅|   
| **see an order summary in the cart** to **review my order before completing the purchase** (as a **customer**).              | Passed ✅|   
| **complete the checkout process and pay** to **finalise my order** (as a **customer**).                                      | Passed ✅|   
| **create comments for posts** to **share my opinion with others** (as a **registered customer**).                            | Passed ✅|  
| **update my comments** to **modify my feedback if my opinion changes** (as a **registered customer**).                       | Passed ✅|  
| **delete my comments** to **remove my feedback if I no longer wish it to be displayed** (as a **registered customer**).      | Passed ✅|   
| **create blog posts** to **provide valuable content to customers and visitors** (as a **staff member**).                     | Passed ✅|  
| **update blog posts** to **keep the content current and relevant** (as a **staff member**).                                  | Passed ✅|   
| **delete blog posts** to **remove outdated or irrelevant content** (as a **staff member**).                                  | Passed ✅|   
| **create comments on blog posts** to **engage in discussions and share my thoughts** (as a **registered customer**).         | Passed ✅|   
| **update my comments** to **change my input or correct mistakes** (as a **registered customer**).                            | Passed ✅|  
| **delete my comments** to **remove my input if I change my mind (as a registered customer).**                                | Passed ✅|        


## Bugs



### bug non-nullable
While making changes to the models in my post and comment app I kept getting errors. 
You are trying to add a non-nullable field 'image' to post without a default; we can't do that (the database needs something to populate existing rows).
Please select a fix:
 1) Provide a one-off default now (will be set on all existing rows with a null value for this column)
 2) Quit, and let me add a default in models.py
Select an option: 
### Fix: 
The above still did not work so I had to rollback to a previous migration before the errors. I found this information on [Stackoverflow](https://stackoverflow.com/questions/32123477/how-to-revert-the-last-migration)

### bug no white space
I was posting all the blog posts from the admin and for some reason it was stripping the paragraph gaps. Fixed it with whitespace css setting.

[White space article](https://developer.mozilla.org/en-US/docs/Web/CSS/white-space)

***Bug:***
While trying to create custom 404 and 500 pages I kept just getting a simple error "A server error occurred. Please contact the administrator." instead of the custom pages I had made. 

***Fix:*** 
Reading up I saw I could not use extends from tags in custom 404 and 500 pages [Stackoverflow](https://stackoverflow.com/questions/75071972/i-have-problem-with-cutomizing-the-404-page-in-django)

