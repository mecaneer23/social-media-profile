from os import environ

# import requests
from linkedin_api import Linkedin
from dotenv import load_dotenv

load_dotenv()


def get_info():
    # url = "https://api.linkedin.com/v2/me?projection=(id,firstName,lastName,profilePicture(displayImage~:playableStreams))"
    # res = requests.get(
    #     url, headers={"Authorization": f"Bearer #{{{environ.get('SECRET')}}}"}
    # )
    # print(res)
    api = Linkedin(environ.get("EMAIL"), environ.get("PASSWORD"))
    profile = api.get_profile(input("LinkedIn user: "))
    print(profile)


get_info()
