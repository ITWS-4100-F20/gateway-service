import os

CLIENT_ID = "05d3667c-b1d5-4b17-861e-f589b8c0e468" # Application (client) ID of app registration

CLIENT_SECRET = "c9irO-2Sph39YyHB~-jZ.-4FrB2V9zzB3G" # Placeholder - for use ONLY during testing.
# In a production app, we recommend you use a more secure method of storing your secret,
# like Azure Key Vault. Or, use an environment variable as described in Flask's documentation:
# https://flask.palletsprojects.com/en/1.1.x/config/#configuring-from-environment-variables
# CLIENT_SECRET = os.getenv("CLIENT_SECRET")
# if not CLIENT_SECRET:
#     raise ValueError("Need to define CLIENT_SECRET environment variable")

AUTHORITY = ""  # For multi-tenant app
# AUTHORITY = "https://login.microsoftonline.com/Enter_the_Tenant_Name_Here"

# You can find the proper permission names from this document
# https://docs.microsoft.com/en-us/graph/permissions-reference
SCOPE = ["User.ReadBasic.All"]

SESSION_TYPE = "filesystem"  # Specifies the token cache should be stored in server-side session

JWK_URI = ""

MONGO_CONNECTION_STRING=""

ANALYTICS_ENGINE_ENDPOINT="http://localhost:3031"