"""
WSGI config for maineblanc_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'maineblanc_project.settings')

application = get_wsgi_application()

try:
    from django.contrib.auth import get_user_model
    User = get_user_model()

    username = "Demo_admin_DP"
    email = "admin_dp@test.com"
    password = "Demo1234!"

    if not User.objects.filter(username=username).exists():
        User.objects.create_superuser(username=username, email=email, password=password)
        print("Superuser Demo_admin_DP créé avec succès !")
    else:
        print("Superuser Demo_admin_DP déjà existant.")
except Exception as e:
    print(f"Erreur lors de la création du superuser : {e}")