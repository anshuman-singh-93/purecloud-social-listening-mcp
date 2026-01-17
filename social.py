import PureCloudPlatformClientV2
import PureCloudPlatformClientV2
import os
from dotenv import load_dotenv
load_dotenv()
client_id = os.environ['GENESYS_CLOUD_CLIENT_ID']
client_secret = os.environ['GENESYS_CLOUD_CLIENT_SECRET']
genesys_environment=os.environ['GENESYS_CLOUD_ENVIRONMENT']

apiclient = PureCloudPlatformClientV2.api_client.ApiClient(genesys_environment).get_client_credentials_token(client_id,client_secret)
social_media_api = PureCloudPlatformClientV2.SocialMediaApi(apiclient)


