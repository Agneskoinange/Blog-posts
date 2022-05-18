### Blog Spar
# By Agnes Koinange
# Description
 This is a personal blogging website where one can create and share their opinions and other users can read and comment on them. Additionally, one ca add a feature that displays random quotes to inspire your users. 

It Uses an api endpoint to help display the random quotes.

# Live Link
https://blogspar.herokuapp.com/

# User Stories

* A user, would view the blog posts on the site
* A user, would comment on blog posts
* A user, would view the most recent posts
* A user, would  an email alert when a new post is made by joining a subscription.
* A user, would  see random quotes on the site
* A writer, would  sign in to the blog.
* A writer, would create a blog from the application.
* A writer, would delete comments that they find insulting or degrading.
* A writer, ould update or delete blogs they have created.

# Development Installation

To get the code..

* Cloning the repository:
https://github.com/Agneskoinange/Blog-posts.git
* Move to the folder and install requirements
* cd Blog-posts
* pip install -r requirements.txt
* Exporting Configurations
* export SQLALCHEMY_DATABASE_URI=postgresql+psycopg2://{User Name}:{password}@localhost/{database name}
* Running the application
* python manage.py server
* Testing the application
* python manage.py test
* Open the application on your browser 127.0.0.1:5000.

# Technology used
* Python3
* Flask
* Heroku
* Github

# Support and contact details
If you have any questions, concerns or comments regarding this project, please contact me through koinangeagnes@gmail.com

# License

MIT License

Copyright (c) 2022 Agnes Koinange

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.