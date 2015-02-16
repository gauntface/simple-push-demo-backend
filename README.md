Back End for the Simple Service Worker Push Demo
=======

This repo contains a basic server to take a restful request containing
a subscription ID and a GCM (Google Cloud Messaging) endpoint and make a request to GCM to send a push message.

## Using the Demo

I have only tested this out on my OS X machine, for testing the server out locally I use the [Google App Engine Launcher](https://cloud.google.com/appengine/downloads?csw=1).

I'm afraid I don't know how to use the App Engine server on other platforms but there should be a way to use the project.

The frontend is a [git submodule of this repo](https://github.com/gauntface/simple-push-demo). If all you want is to test out push, follow the instructions on that page. 
