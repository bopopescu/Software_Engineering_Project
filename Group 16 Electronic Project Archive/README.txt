Directory Tree and files contents

-
|
+-----> code                                 //source code
      |
      +-----> Proximity-Angular              //contain source code for the front-end of the webApp
      |
      +-----> Proximity-Flask                //contain source code for the back-end of the webApp        
|
+-----> design                               //UML diagram and README.txt explains how it match with our code
|
+-----> doc                                  //contains Report 1-3, demo 1-2 presentation slides 
|
+-----> tests                                //program tests 
      |
      +-----> unit_testing                   //contain code and README.txt explains how to run unit tests
      |
      +-----> integration_testing            //contain README.txt explains how to run integration test




Instruction on how to run our code

Proximity is a web app for finding events and friends in real life. We currently aren’t hosting it on a server so to use it you will have to install angular so you can run it locally. Follow these steps to do this.

Install the latest version of Node.js on your machine.

Open the program “Node.js command prompt”.
Cd into the downloaded folder. Keep cding until you are inside the folder code/Proximity Angular.

Now run the command “npm install -g @angular/cli”. This installs Angular on your machine which is required to run our app locally.

Now run the command “ng serve --open”. The app will now be running at http://localhost:4200/home. You will have to open a browser and type this into a url if it doesn’t open automatically. 





Instruction on how to use our webApp

When you first ran our code and open our website (it hosted on a local server), you will be taken to the home screen. You will notice that without login, you cannot access any of the item when you click on the side navigation bar. To be able to access those items, you first need to create an account by clicking on the create account button. You will be taken to the create account page where you will need enter a username and password as well as other necessary information and click create account. Once done, click the login button on the top navigation and it will take you back to the login page. Enter the username and password you just created to login. When you click login (assuming you enter the correct username and password), you will be taken back to the home page. Now, if you click on the side navigation bar, you should be able to access the content of those pages that you cannot access before. On the Map page, you can view local events that hosted either by the public or your friends. You can use the search bar on top to search for events that hosted by your friend and if you click on the map marker of that event, it will take you to the profile page of the friend that hosted that event. The Feed page displays all the public posts that people made. The Profile page displays all the posts that you made. On the Profile page, you can click create post to create a new post. The post that you made will be display in both your Profile page and Feed page. You will need the refresh the page in order to view the new post. The Event and Messaging page is not complete so it will only displays people events and messages for now.  Once you done explore all the tabs, if you want to logout, you just need to click on the Logout button on the top navigation bar and it will take you back to the login page, where you will need to login again in order to access our webApp.


Important Notes: 
***When you first logged in, you may have to wait a couple of second before it take you back to the home page. If nothing happen, then you need to check your browser and make sure that it allows the website to track location in order for the Google Map API to load. If for some reason you can’t login using the username and password that you created, you can use the admin username: dev and password: pass to login. 
***In order to load the test data that was already on the database, you will need to download and  install a Chrome plugin called Allow-Control-Allow-Origin in order to allow AJAX calls.
***The nature of this application is that data collection and fetching is essentially the only backend unit testing that can occur.
As such, the unit testing script does its own data collection and no other data collection is needed.






        
 