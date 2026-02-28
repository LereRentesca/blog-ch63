# Mini Challenge 1 - About Page

Create a new view called about. That view should display to the user the following:
- A title that says About me
- A subtitle with your name
- A paragraph with a brief introudction of yourselves

STR:
1. Create a new class called AboutPageView inside of pages/views.py
2. Create a new html file inside of pages folder called about.html
3. Create a url to link the AboutPageView
4. Test it! Run the server and modify the address bar to localhost:8000/about/

# Mini Challenge 2 - Home Page

Customize the home page applying the following:

1. At least 1 way to implement css (external or internal)
2. At least 1 way to implement js (internal or external)
3. At least 1 image loaded from the static
4. On the css implement at least 2 classes with any rules.
5. On the js implement only a message printed on the console.

# Mini Challenge 1 (FSDI 113) - Post application
STR:
1.  Create a new app called 'posts'

    1. Add the new app to the INSTALLED_APPS list inside of settings.py

2. Create a 'urls.py' file inside of posts and add the includes to the 'urls.py' in config folder (Remember to add a new name for the new endpoints inside of config.urls e.g. "posts/")
3. Create a new folder called posts inside of templates.

    1. Create a new file for list.html
    2. Create a new file for detail.html
    3. Create a new file for new.html
    4. Create a new file for delete.html
    5. Create a new file for edit.html


# Mini Challenge 2 (FSDI 113) - Post model
Create a Post model with the following attributes:
- title is a charfield attribute with a maximum length of 128 characters
- subtitle is a charfield attribute with a maximum length of 256 characters
- body is textfield attribute
- created_on is a datetimefield attribute that is added automatically
- author is foreignkey attribute that is linked to the user model and when deleted it should delete all of the posts related to the author

- Add the to string method and display "title by author"

Once the model is created, make sure to create the migration file and then display the model in the admin site

Required imports:
from django.contrib.auth import get_user_model

# Mini Challenge 3 (FSDI 113) - PostListView
Create a new view insisde of the Posts application that renders all elements in list.html from the post table

Add the option to the navbar to see all posts 

# Mini Challenge 4 (FSDI 113) - Update functionalities
Update the following views:

1. PostListView: Add a html tag to display the status
2. PostDetailView: Add a html tag to display the status
3. PostCreateView: Add the input to select status
4. PostUpdateView: Add the input to select status 