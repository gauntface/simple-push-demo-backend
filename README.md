Back End for the Simple Service Worker Push Demo
=======

This repo contains a basic server to take a restful request containing
a subscription ID and a GCM (Google Cloud Messaging) endpoint and make a request to GCM to send a push message.

## Using the Demo

I have only tested this out on my OS X machine, for testing the server out locally I use the [Google App Engine Launcher](https://cloud.google.com/appengine/downloads?csw=1).

I'm afraid I don't know how to use the App Engine server on other platforms but there should be a way to use the project.

The frontend is a [git submodule of this repo](https://github.com/gauntface/simple-push-demo). If all you want is to test out push, follow the instructions on that page.

## Send a Push to GCM

If you just want to use the server to send a push message through GCM, 
then you need to send a **POST** request with the **subscriptionId** 
and **endpoint** pieces of info as form data.

Below is a simple example making a fetch:

    var formData = new FormData();
    formData.append('subscriptionId', subscriptionId);
    formData.append('endpoint', pushEndPoint);

    fetch(PUSH_SERVER_URL + '/send_push', {
        method: 'post',
        body: formData
      }).then(function(response) {
        // NOOP
      }).catch(function(err) {
        console.log('Fetch Error :-S', err);
      });

