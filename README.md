Check Your Privilege!
====
This is a Service that allows you to check your privilege once a day.

# Installation
1. Pull this repo in some director (I recommend `/var/www/checkyourprivilege`).
2. Execute `pip install -r requirements.txt`
3. Apply migrations `python manage.py migrate` (maybe you need to do more IDK)
3. Create a superuser `python manage.py createsuperuser` (you don't need to, but maybe you should...)
3. Copy `checkyourprivilege.service` into your systemd directory.
4. Enable it with `systemctl enable checkyourprivilege.service` (ensure the proper directories and user permissions!)
5. Check your Privilege! (once a day)

