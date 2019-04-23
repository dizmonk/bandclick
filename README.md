# bandclick_project
newest version

how to get your system set up to run the project:

1.) make sure you have python 3.7 installed AND when you install it, check the box to add it to "environment variables"
then check from command line...cmd -> "python --version" should tell you python 3.7.3 or something like that, if it is older, uninstall it and 3.7 should show up

2.) if you get that 'python' is not recognized as an internal or external command when trying to run it, you need to add python to your path, here is a link that will show you a video on how to do that...(its for python27 so make sure you use 37 instead)

https://www.youtube.com/watch?v=UTUlp6L2zkw

3.) inside pycharm: make sure your interpreter is set to the correct one for 3.7  (ctrl-alt-s for settings, check interpreter)

4.) Run these separately in the pycharm terminal: pip install django, pip install django-crispy-forms, pip install Pillow, python manage.py makemigrations, python manage.py migrate, python manage.py runserver

5.) Hopefully it worked!!  :P

