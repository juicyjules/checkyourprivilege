Check Your Privilege!
====
This is a Service that allows you to check your privilege once a day.

# Installation
1. Pull this repo in some director (I recommend `/var/www/checkyourprivilege`).
2. Execute `pip install -r requirements.txt`
3. Copy `checkyourprivilege.service` into your systemd directory.
4. Enable it with `systemctl enable checkyourprivilege.service` (ensure the proper directories and user permissions!)
5. Check your Privilege! (once a day)

