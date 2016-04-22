from mapstory.settings import *
import json

ENABLE_SOCIAL_LOGIN = True
USE_AWS_S3= False
MAPSTORY_APPS = (

 'mapstory.apps.boxes',
 'provider',
 'provider.oauth2',
 'mapstory.apps.flag', # - temporarily using this instead of the flag app for django because they need to use AUTH_USER_MODEL

)

INSTALLED_APPS += MAPSTORY_APPS