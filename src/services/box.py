from boxsdk import CCGAuth, Client
from dotenv import load_dotenv
import os

load_dotenv()


def setConnBox():
    auth = CCGAuth(
        client_id=os.environ['BOX_CLIENT_ID'],
        client_secret=os.environ['BOX_CLIENT_SECRET'],
        enterprise_id=os.environ['BOX_ENTERPRISE_ID']
    )
    client = Client(auth)
    return client

