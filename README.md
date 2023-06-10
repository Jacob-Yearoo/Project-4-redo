
# Computer Jargon | Blog Site


Project four

This is a website I made, that will act as a portfolio of my work as the number of projects I work on increase, I'm hoping that it will act as a good reference point for employers to make an accurate estimate of my ability. the website itself is a Blog site focusing on different topics surrounding Technology.

It aims to be a site where people who are invested in computer/technology and more specifically gaming, on the PC platform, can come together to read about topics that interest them and engage with a community by liking posts and leaving comments.

The Value that the site owner will get out of this website are:

- Build the business's brand.
- Have a platform that is fluid and can be updated and added to.
- The inverse is also possible the site admin can also remove posts or comments for various reason if they need to.
- It's a platform that can be used to generate revenue through advertisments.

The Value that visitors will get from this site are:

- A fun site to delve into different topics about a subject that interests them.
- A way to look into other projects or work I have done through links to social accounts
- An opportunity to voice their opinion about a certain topic and discuss with other likeminded individuals.


## Demo

[App page](https://dashboard.heroku.com/apps/project-4-redo)

[Live Demo](https://project-4-redo.herokuapp.com/)

## User Experience

### The Strategy
As the site owner the goal was to create a modern and aesthetically pleasing site, in order to increase site traffic, which could eventually generate income through ad revenue.

### The Scope
The idea was to make each individual blog post pop, so the page had to be minimalist with an emphasis on the blogs themselves to really make them stand out, also added, would be login functionality to try and retain the visitors that find themselves on the page

### The Structure

As above, I wanted the blog posts to pop, the featured images in the front page are very eye catching and desgined to draw people in, the small heading of the page and navbar are desinbged to be as unintrusive as possible to people's experience.  

### The Skeleton

[Main Structure Wireframe](https://i.imgur.com/ftW8kHq.jpg)

[Content Wireframe](https://i.imgur.com/PHeYW2L.jpg)

[User Registration Wireframe](https://i.imgur.com/z6WnwPn.jpg)

### The Surface

the colour scheme, I opted for a dark mode to add to that modernist feeling, the dark background contrasts well with the blog images, and the orange used in the logo stands out because of the background colour. 

## Features

- All pages feature a fixed footer that responds to screen size and allows for easy access to different social links. 
- At the top of the page there is a Nav bar that can be used to access the home page or "sign in"/"sign up" which then changes to "Logout" once you are signed in.
- A fully featured admin panel, which when accessed can be used to give admin privileges to other users, make new posts, delete posts, approve comments, delete comments, delete users.
- a like and comment counter that automatically increases when a post is liked or has received a comment
- the ability to make your own profile which then gives you additional features such as the ability to comment, the information inputted is stored directly into a database
- the ability to report a post (while you're logged in) which an admin can examine.

## Features I'd Like to Implement

- I would like to add a search bar to the site to make it more user-friendly and intuitive to find certain blogs.
- the ability for certain users to make their own posts rather than just through the admin page.
- additional options in the navbar to sort through categories, which each post could be sorted into automatically via tags.

## Tech

**HTML:** Used to input all of the content on index.html and contact.html.

**CSS:** Used to style all of the content.

**Google Fonts:** Supplied the fonts.

**Unsplash:** For the blog images used.

**Font Awesome:** Used for the social media icons in the footer.

**Django:** Supplied the whole framework

**Bootstrap:** was used to style the pages and add responsiveness to different screen sizes.

**Cloudinary:** hosted the images that the site user.

**ElephantSQL:** the DBMS that stores the registration details, etc.


## User Stories

1. As a Site User I can like or unlike posts.

2. As a User I can view a list of posts so I can select one to read through.

3. As a User I can see how many likes and comments are on a certain post.

4. As a User or Admin I can view comments on a post to engage, and also leave comments to get involved.

5. As a User I would like to read the whole post after clicking on the post.

6. As a User i would like to register an account so I can leave comments

7. As an Admin I need to be able to use CRUD on the site

8. As a User I would like to report blogs for various reasons.

## Testing

![Testing](https://i.imgur.com/xhCrLhj.png)

The site was tested on Chrome, Firefox, Edge and Safari to ensure the desired outcome no matter where it is being viewed from, I also adjusted the site to remain readable on different screen sizes (going from my 5120px wide screen, to regular full HD screens, to tablets and finally to phones with the Iphone 5 being the lowest size I made adjustments for)

## Planning

[Agile Planning](https://github.com/users/Jacob-Yearoo/projects/1/views/1)

I used Githubs built-in projects feature to plan beforehand, what user stories I would need to complete in order to build a site/app that would meet the basic needs of a blog.

## Usage

### As A Viewer
1. open the app on Heroku and browse the contents of the page
2. if the user wishes to leave likes and comments then they should register with a Username and Password (Email address is not necessary)

### As An Admin
1. open the app on Heroku
2. at the end of the URL add '/admin'
3. login with the admin credentials provided
4. you will then be able to add posts, delete posts, add/remove user permissions, approve/deny comments, etc.

## Deployment

his site is hosted using Heroku, To set up Heroku you must;


The requirements.txt file in the IDE must be updated to package all dependencies. To do this:

1. Enter the following into the terminal: 'pip3 freeze > requirements.txt'
2. Commit the changes and push to GitHub
3. Next, follow the steps below:
4. Login to Heroku, create an account if necessary
5. Once at your Dashboard, click 'Create New App'
6. Enter a name for your application, this must be unique, and select a region
7. Click 'Create App'
8. At the Application Configuration page, apply the following to the Settings and Deploy sections:
9. add the necessary CONFIG VARS that are relevant to your project
10. Click 'Add'
11. Add another Config Var with the Key of 'PORT' and the Value of '8000'
12. Navigate to the Deploy section, select Github as the deployment method, and connect to GitHub when prompted
13. Use your GitHub repository name created for this project
14. Finally, scroll down to and select to deploy 'Automatically' as this will ensure each time you push code in GitHub, the pages through Heroku are updated
15. Your application can be run from the Application Configuration section, click 'Open App'


## GitPod Commits

The deployed site will update automatically upon new commits to the master branch. In order for the site to deploy correctly on GitHub pages, the landing page must be named index.html.
## Credits

### Media
All Images have come from [Unsplash](https://unsplash.com/)

### Acknowledgements
I would like to credit [RickofManc](https://github.com/RickofManc/vv-pizzas) for his excellent README, I have used his instructions for deployment on Heroku.

This project was heavily inspired by the walkthrough project at Code institute as it aligned with what I wanted my project to be based on.  [this is a link to the source code.](https://github.com/Code-Institute-Solutions/Django3blog/tree/master/01_creating_the_project) the overall layout of my project was inspired by this program.

Special thanks to the Tutors at Code Institute for the support they've given.