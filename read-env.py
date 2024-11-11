# .env in the .gitignore
# PASSWORD="joulu"
# USERNAME="joulupukki"
# PORT=5000
import os
from dotenv import load_dotenv

load_dotenv(override=True) #read .env file
print(os.getenv("PASSWORD"))
print(os.getenv("PORT"))