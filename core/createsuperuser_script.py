from django.contrib.auth import get_user_model

User = get_user_model()

username = "Demo_admin_DP"
email = "admin_dp@test.com"
password = "Demo1234!"

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username=username, email=email, password=password)
    print("Superuser créé avec succès !")
else:
    print("Le superuser existe déjà.")
