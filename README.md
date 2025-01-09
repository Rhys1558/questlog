# Quest Log Blog
Quest Log Blog is a website that allows video game lovers to create blog posts about their favourite video games. They can let other users know their impressions and opinions of therir favourite video games, what they like and dislike about the games, and give other game recommendations based on their preferred style of game. This website is targeted towards video game lovers of all different types of games, giving them a space to view the opinions of like minded individuals with similiar interests.

## Features

### Navigation Bar

- Logo
    - The logo when clicked allows the user to return to the homepage.
    

- Home
    - This element when clicked brings the user back to the homepage.


#### When Logged In
    
 - 'New Post' allows the user to create a new post that is displayed to the homepage of the wedsite, which other users can view.
 - 
- Log Out
    - This allows user to log out when they are logged in.
    
#### When Logged Out
- Register
    - This allows the user to create a new account and start creating posts about their favourte games for other users to see.

- Log In
    - This allows the user to log in after they have registered an account with the site.
      
## Features To Be Created
- Search bar
    - Adding a Search Bar to the right side of the Navigation Bar would imporove the user experience. This will allow the user to search for relevant blogs using keywords like their favourite video games or authors. The Search Bar tool will use the keyword input by the user to search through titles of blogs, the body of blogs and different user names in order to provide the most relevent posts.

- Bookmark
    - A Bookmark feature will allow the user to save blogs about their favourite games or by a preferred author so they can reference these posts whenever they would like to in the future.

- Share Button
    - This will allow the user to share their favourite blog posts about games they enjoy to people with similiar interests. 
  
## Landing Page Content
 - This landing page has all users blogs to view, this allows anyone to see other user blogs that have been posted.
   
 - The landing page shows the title of the post, a preview of the body, the author of the post and the date it was posted.
   
 - While on the landing page, the user can click the title of a post. This opens the post to show the title of the post, the entire body of the post, the date it was post, the author of the post, along with a 'Back' button and an 'Edit' button if the user is the author of this blog. If the user is not the author of this blog, only the 'Back' button will appear.
   
 - The 'Back' button, when clicked, brings the user back to the homepage of the website.
   
 - The 'Edit' button, when clicked, allows the user to edit or delete the current post.

 ## Footer
 - This has the copyright of the name Quest Log Blog 

 ## Forms
 - Registration Form
    - This form allows the user to register an account.
   
 - Log In Page Form
    - This form allows the user to log in.
   
 - Creat New Blog Form
    - This form allows the user to create a new post.
   
 - Edit Blog Form
    -This form allows the user to edit their post 

## Manual Testing
- logo
   - I manually tested the logo to check and see if it sent me back to the home.
- Home
    - I checked to see if home in the nav bar brough me back to the home page.
- New Post
    - I clicked on the new post button to see if it brough me to the create new post page.
- Log Out
    - I clicked on log out to see if it would sign me out.
- Register
    - I clicked on this to see if it brough me to the register form
## Deployment
I deployed the website by logging into heroku, then in github I made a procfile with web: gunicorn my_project.wsgi inside it.
I then went to setting.py and turned debug to Flase.
I went to allow hosts and put '.herokuapp.com'.
I then commit and pushed the changes to github'
I then went to the deploy tab in heroku and then in the deployment method section I enable GitHub integration by clicking on Connect to GitHub.
I then give heroku my github repo name.
I then clicked deploy branch.

## Credits

https://www.youtube.com/watch?v=B40bteAMM_M&list=PLCC34OHNcOtr025c1kHSPrnP18YPB-NFi
  
