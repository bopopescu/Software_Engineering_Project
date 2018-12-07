Run integration tests by making sure you have node installed on computer "install node on mac"

The integration test is written by combining unit tests from five components which is create account, login, feed, event and messaging. The map page test code is not working because of restriction from Google Map API

To run integration test, simply cd to 1_code/Proximity-Angular folder on terminal and type "ng e2e", and the program will automatically run integration test and give you back the result of which test failed and which is pass in the console.

*****Since Demo 1, we had added two more tests for the new pages that we created (event, messaging). As of right now, the integration tests still is not be able to run probably and it may or may not print anything to the console. We will take this as a feedback for improving future works.


This is what we expect to happen if the integration test run probably:

**Step 1: Test the account creation page by going through unit tests for that page. In the end, expect to successfully create a new account with the username equal "test" and password equals "pass"

**Step 2: Test the login page by going through unit tests for that page. In the end, expect login successfully by using the username and password that create in step 1

**Step 3: Test the feed page by going through unit tests for that page. In the end, expect the feed page to successfully loaded feed data from the database

**Step 4: Test the event page by going through unit tests for that page. In the end, expect the event page to successfully loaded event data from the database

**Step 5: Test the messaging page by going through unit tests for that page. In the end, expect the messaging page to successfully loaded messages data from the database