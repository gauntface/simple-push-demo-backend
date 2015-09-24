#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import urllib
import logging
import datetime
import json
from google.appengine.api import urlfetch
from google.appengine.ext import db

class SendPushHandler(webapp2.RequestHandler):
  def post(self):
    logging.info('SendPushHandler')

    # Enable CORS
    self.response.headers.add_header("Access-Control-Allow-Origin", "*")

    # Enable the endpoint
    endpoint = self.request.get("endpoint")

    headers = {}
    form_data = None
    if endpoint.startswith('https://android.googleapis.com/gcm/send'):
      logging.info('Handling a GCM request')

      subscriptionId = self.request.get("subscriptionId")
      authorization = self.request.get("authorization")
      payload = self.request.get("payload")
      if len(authorization) is 0:
        authorization = 'AIzaSyBBh4ddPa96rQQNxqiq_qQj7sq1JdsNQUQ';
      
      headers = {
        'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
        'Authorization': 'key='+authorization
      }

      if len(subscriptionId) is 0 :
        endpointParts = endpoint.split('/')
        subscriptionId = endpointParts[len(endpointParts) - 1]
       
        endpoint = 'https://android.googleapis.com/gcm/send'

      logging.info('Endpoint: ' + endpoint)
      logging.info('regId: ' + subscriptionId)
      logging.info('authorization: ' + authorization)
      logging.info('payload: ' + payload);

      form_fields = {
        "registration_id": subscriptionId,
        "data": payload
      }
      form_data = urllib.urlencode(form_fields)
    else :
      logging.info('We don\'t currently support any other endpoints')
      self.response.write('{ "success": false }')

    result = urlfetch.fetch(url=endpoint,
                            payload=form_data,
                            method=urlfetch.POST,
                            headers=headers)
    
    if result.status_code == 200 and not result.content.startswith("Error") :
      logging.info('Successful Request')
      self.response.write('{ "success": true }')
    else:
      logging.info('Failed Request')
      logging.info(result.status_code)
      logging.info(result.content)
      self.response.write('{ "success": false }')

app = webapp2.WSGIApplication([
  ('/send_push', SendPushHandler)
], debug=True)