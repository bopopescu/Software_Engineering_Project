Run integration tests by making sure you have node installed on computer "install node on mac"

The integration test is written by combining unit tests from three components which is create account, login and feed. The map page test code is not working so it will not be part of this demo but will be for the next demo

To run integration test, simply cd to the 1_code/Proximity-Angular folder on terminal and type "ng e2e", and the program will automatically run integration test and give you back the result of which test failed and which is pass in the console.

***As for now, the integration tests is not be able to run probably and will give back all failed results, we will try to fix that in the next demo. 


This is what we expect to happen if the integration test run probably:

**Step 1: Test the account creation page by going through unit tests for that page. In the end, expect to successfully create a new account with the username equal "test" and password equals "pass"

**Step 2: Test the login page by going through unit tests for that page. In the end, expect login successfully by using the username and password that create in step 1

**Step 3: Test the feed page by going through unit tests for that page. In the end, expect the feed page to successfully loaded feed data from the database