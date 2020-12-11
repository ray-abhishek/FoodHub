 #!/bin/sh
 set -e

 ##
 # Run a command to start python runserver
 #
 if [ $1 ];then
     # If we passed a command, run it
     exec "$@"
 else
     # Otherwise start python runserver
     python manage.py runserver 0.0.0.0:8000
 fi
 
