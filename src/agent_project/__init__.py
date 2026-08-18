import os

from dotenv import load_dotenv

ROOTPATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
env_path = os.path.join(ROOTPATH, '.env')

#获取env中的参数
load_dotenv(env_path)

model_name = os.getenv('ModelName')
model_url = os.getenv('ModelURL')
model_api_key = os.getenv('ModelAPIKey')

google_api_url = os.getenv('GoogleApiURL')
google_api_key = os.getenv('GoogleApiKey')


def main() -> None:
    print("agent-project")








