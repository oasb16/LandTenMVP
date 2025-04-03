from flask import Flask, request, redirect, url_for, session
from authlib.integrations.flask_client import OAuth
import os
import json
from datetime import datetime
import boto3
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
app.secret_key = os.urandom(24)

oauth = OAuth(app)

oauth.register(
  name='cognito',
  authority='https://cognito-idp.us-east-1.amazonaws.com/us-east-1_lIYcxnaDT',
  client_id='6kqji9guk9qaekonm115ek2k58',
  client_secret=os.getenv("COGNITO_CLIENT_SECRET"),
  server_metadata_url='https://cognito-idp.us-east-1.amazonaws.com/us-east-1_lIYcxnaDT/.well-known/openid-configuration',
  client_kwargs={"scope": "phone openid email"},
)

def save_user_to_dynamodb(email, persona):
    dynamo = boto3.resource('dynamodb', region_name='us-east-1')
    table = dynamo.Table('LandTena')
    table.put_item(
        Item={
            "email": email,
            "persona": persona,
            "created_at": datetime.utcnow().isoformat()
        }
    )

@app.route('/signin')
def signin():
    session['flow'] = 'signin'
    return oauth.cognito.authorize_redirect("https://landten-1c3e689566b5.herokuapp.com/authorize")

@app.route('/signup')
def signup():
    persona = request.args.get('persona', 'tenant')
    session['flow'] = 'signup'
    session['persona'] = persona
    return oauth.cognito.authorize_redirect("https://landten-1c3e689566b5.herokuapp.com/authorize")

@app.route('/authorize')
def authorize():
    token = oauth.cognito.authorize_access_token()
    user = token.get('userinfo')
    session['user'] = user
    flow = session.get('flow', 'signin')
    persona = session.get('persona', 'auto')

    # Save to DynamoDB only during sign-up
    if flow == 'signup':
        save_user_to_dynamodb(user["email"], persona)

    # Write session state to shared file
    state = {
        "email": user['email'],
        "persona": persona,
        "logged_in": True
    }
    with open("shared/user_state.json", "w") as f:
        json.dump(state, f)

    return redirect(url_for('login_complete'))

@app.route('/login_complete')
def login_complete():
    return "Login complete. You can return to the Streamlit app."

if __name__ == '__main__':
    app.run(port=5000, debug=True)
