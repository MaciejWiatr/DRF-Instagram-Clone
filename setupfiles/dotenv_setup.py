from django.core.management.utils import get_random_secret_key
import os
dir_path = os.path.dirname(os.path.realpath(__file__))
parent_path = os.path.join(dir_path, os.pardir)

with open(os.path.join(parent_path, ".env"), "w") as f:
    f.write("SECRET_KEY="+get_random_secret_key())
    print("Successfully created dotenv file")
