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
    # Enable CORS - Always set in case of preflight check
    self.response.headers.add_header("Access-Control-Allow-Origin", "*")

    # Parse the request content
    requestData = json.loads(self.request.body)

    # Check if we have minimum we know we need for web push
    if not ('endpoint' in requestData) or not ('headers' in requestData):
        self.response.write('{ "error": "Missing required field." }')
        return

    # Get the endpoint, headers and body if it exists
    endpoint = requestData['endpoint']
    headers = requestData['headers']
    body = None
    if 'body' in requestData:
        if endpoint.startswith('https://android.googleapis.com/gcm/send'):
            # body = json.dumps(requestData['body'])
            body = requestData['body']
        else:
            body = requestData['body']

    # Call the api with the appropriate info
    result = urlfetch.fetch(url=endpoint,
                            payload=body,
                            method=urlfetch.POST,
                            headers=headers)

    # Get the body and return as body
    self.response.set_status(result.status_code);
    self.response.write(result.content)

app = webapp2.WSGIApplication([
  ('/api/v2/sendpush', SendPushHandler)
], debug=True)
