[program:car]
directory = {{ app_path }}
user = {{ app_user }}
command = {{ virt_env_path }}/bin/python manage.py runserver 0.0.0.0:4242
stdout_logfile = /var/log/car.log
stderr_logfile = /var/log/car.error

[program:car_command_monitor]
directory = {{ app_path }}
user = root
command = {{ virt_env_path }}/bin/python manage.py command_monitor
stdout_logfile = /var/log/car.log
stderr_logfile = /var/log/car.error