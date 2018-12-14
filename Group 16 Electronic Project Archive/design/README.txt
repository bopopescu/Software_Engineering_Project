Here is the directory tree shows where in our source code folder matches with the UML diagram

-
|
+-----> code                                               //source code
      |
      +----->Proximity-Angular                            //contain source code for the front-end of the webApp
            |
            +-----> src
                  |
                  +------>app
                         |
                         +------>create-account           //contain source code for AccountModule (account_create())
                         |
                         +------>create-post-dialog       //contain source code for FeedModule (create_post())
                         |
                         +------>feed-page                //contain source code for FeedModule (get_post()) 
                         |
                         +------>login-page               //contain source code for AccountModule (account_login())
                         |
                         +------>map-page                 //contain source code for MapModule (get_events())
                         |
                         +------>messaging-page           //contain source code for MessagingModule (get_messages())
                         |
                         +------>reset-password           //contain source code for AccountModule (password_reset())
                         |
                         +------>services
                                |
                                +------->data.service.ts  //contain source code for ServiceWorker




****Note: Since we used Angular for our webApp, there aren't any classes or method names so our source code doesn't always match our UML diagram 100%                                                                                                            