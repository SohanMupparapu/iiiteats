Name of our APP: "IIITEATS!"
Some running instructions: 
=> Firstly, our web-app will run through the terminal following  the command 'python3 app.py'.
=> It will redirect the user to a local host on clicking the IP address generated on the terminal.
FEATURES:
=>The website will redirect the user to the home page consisting of links to the several webpages such as about us, the home page itself,etc. 
=>Following the navigation bar, there comes the display of the menu items of various categories of food of various canteen spreaded over our iiit campus, such as  BBC,VC,JC,DAVID along with their multi-dimensional cuisines!
=> Each  of the food items consist of an increment/decrement option which allows the user to select as many items they wanna order. There is check-box option too which allows user to select the item to be ordered(it's just static and for display purpose)
=> Following this, the inline js-script will automatically calculate the final price to be paid by the user and writes the data(in "read-only" mode ) to the given field of bill at the bottom of the page.The prices data are stored in the respective script files.
=>The user also need to enter his/her name,email-id,delivery-address and the canteen from which the food needs to be ordered.
=> The data is then (through the flask server) is being sent to the database and a new webpage showing current orders list is being displayed where the user can see the table of the current orders being placed at the canteens.

Team Members and their respective Contributions:
1.Tanishq  Agarwal:- Whole Frontend of Home page and some Backend work of it.Also added counter increment decrement javascript effects to it.
2.Sohan Mupaparapu:-Created and handled Database management system and also added some javascript features of order's page
3.Deekshitha Yattapu:-Did About Us page