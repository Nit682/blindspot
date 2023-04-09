#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  9 

@author: parshgoel
"""



from twilio.rest import Client
from twilio.jwt.access_token import AccessToken
from twilio.jwt.access_token.grants import VideoGrant

# Twilio account SID, API key, and API secret
import os

# Retrieve values from environment variables
account_sid = os.environ.get('ACCOUNT_SID')
api_key = os.environ.get('API_KEY')
api_secret = os.environ.get('API_SECRET')



# Participant identities
participant1_identity = 'user1'  
participant2_identity = 'user2' 

# Create Twilio client for Voice API
voice_client = Client(account_sid, api_key, api_secret)

# Make a voice call
call = voice_client.calls.create(
    url='http://demo.twilio.com/docs/voice.xml', 
    to=to_number,
    from_=from_number,
)

# Generate access token for participant 1
participant1_token = AccessToken(account_sid, api_key, api_secret, identity=participant1_identity)
participant1_token.add_grant(VideoGrant(room='my-room'))  # Replace 'my-room' with desired room name

# Generate access token for participant 2
participant2_token = AccessToken(account_sid, api_key, api_secret, identity=participant2_identity)
participant2_token.add_grant(VideoGrant(room='my-room'))  # Replace 'my-room' with desired room name

# Create Twilio Video room
video_client = Client(api_key, api_secret, account_sid)
room = video_client.video.rooms.create(unique_name='my-room')  # Replace 'my-room' with desired room name

# Create video call links for each participant
participant1_call_link = f'https://video.twilio.com/v1/Rooms/{room.sid}/Participants/{participant1_token.identity}'
participant2_call_link = f'https://video.twilio.com/v1/Rooms/{room.sid}/Participants/{participant2_token.identity}'

# Use the call links to initiate video call for each participant
print(f'Participant 1: {participant1_call_link}')
print(f'Participant 2: {participant2_call_link}')