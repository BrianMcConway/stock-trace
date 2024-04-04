# Stock Trace

View the app here: [Stock Trace](https://stock-trace-8ceccf662779.herokuapp.com/)\
View Google Sheets here: [Google Sheets](https://docs.google.com/spreadsheets/d/1qIUw4Cs-FAEzoi18zY4VcJ_trZYqNWqI5AYZb930VtA/edit?usp=sharing)

<img src="readme-docs/stock-trace-logo.png" alt="Image of Stock Trace logo as seen on application." width="70%" height="auto">

## Intro

- The purpose of this project is to create a fully functional back-end site that responds to users' interactions. In this case I have created a Command Line Interface (CLI) called 'Stock Trace', using Python. This application is designed for a method of adding, removing and monitoring stock levels, specifically food items/ingredients in this case. This application is designed more for large industrial type kitchens such as in a hospital, or a factory canteen. The reason for this is that in these environments, there is a better idea of the amount of food required so items can be signed out on the previous evening according to the menu for the next day.

- Current stock levels of food items from can be viewed in real time.
- New stock can be added to the relevant section when a delivery arrives. Unused items can also be added back to the inventory lists and is safe to do so.

- The stock levels can also be monitored by persons outside of the physical kitchen, such as the kitchen manager and accounts.

## User Stories

- As a user, I would like to be able to check my current stock levels.
- As a user, I would like to be able to add to my stock levels when deliveries arrive.
- As a user, I would like to be able to remove items from the available stock when required.
- As a user, I would like to see these changes to stock levels reflected in the related Google Sheets.
- As a user, I would like to be able to easily navigate the menus, and be notified if I have made incorrect choices.

## Features

### Menu Options 
  
**Main Menu**\
The Main Menu consists of three options:
1. The user can proceed to the Current Stock Menu by inputting 1 & Enter.
2. The user can proceed to the Input New Items Menu by inputting 2 & Enter.
3. The user can proceed to the Use Stock Menu by inputting 3 & Enter.

<img src="readme-docs/main-menu.png" alt="Image of 'How to Play' button" width="80%" height="auto">
    
<br>  

**Current Stock Menu**
The Current Stock Menu Consists of six options:
1. The user can proceed to view the Meat & Fish stock list by inputting 1 & Enter.
2. The user can proceed to view the Fruit& Veg stock list by inputting 2 & Enter.
3. The user can proceed to view the Dry Goods stock list by inputting 3 & Enter.
4. The user can proceed to view the Chilled Goods list by inputting 4 & Enter.
5. The user can proceed to view the Frozen Items by inputting 5 & Enter.
6. The user can return to the Main Menu by inputting 6 & Enter.


<img src="readme-docs/current-stock-main.png" alt="Image of Current Stock Menu." width="80%" height="auto">
    
<br>

**Current Stock List screens**

The Current Stock lists show the user the name, weight/volume, and current amount of each item held in stock as per Google Sheets.

- Meat & Fish list. Pressing Enter returns to the Current Stock menu.

<img src="readme-docs/meat-fish-list.png" alt="Image of 'Audio muted' button" width="80%" height="auto">

<br>

- Fruit & Veg list. Pressing Enter returns to the Current Stock menu.

<img src="readme-docs/fruit-veg-list.png" alt="Image of 'Audio muted' button" width="80%" height="auto">

<br>

- Dry Goods list. Pressing Enter returns to the Current Stock menu.

<img src="readme-docs/dry-goods-list.png" alt="Image of 'Audio muted' button" width="80%" height="auto">

<br>

- Chilled Goods list. Pressing Enter returns to the Current Stock menu.

<img src="readme-docs/chilled-goods-list.png" alt="Image of 'Audio muted' button" width="80%" height="auto">

<br>

- Chilled Goods list. Pressing Enter returns to the Current Stock menu.

<img src="readme-docs/frozen-items-list.png" alt="Image of 'Audio muted' button" width="80%" height="auto">

<br>

**Input New Items**

- The Input New Items menu displays the same five list options, and a sixth option to return to the previous menu. A menu choice is made by entering the relevant number selection and pressing Enter.

<img src="readme-docs/input-new-items.png" alt="image of turns counter" width="80%" height="auto">

<br>

- Input New Items screen. User is prompted input name of an existing stock item from the category they have currently selected, then press Enter to confirm. After that the user is prompted to enter the amount they wish to add, then press Enter to confirm. If the inputs are successful, the user will be give a confirmation message indicating what was added, how much was added, and the new stock level.

<img src="readme-docs/input-new-items-input-confirm.png" alt="image of turns counter" width="80%" height="auto">

<br>

**Use Stock Items**

- The Use Stock Items menu displays the same six options, five categories and a sixth option to return to the previous menu. The user should input the relevant number and press Enter to confirm.

<img src="readme-docs/use-stock-items-menu.png" alt="image of end of game message" width="80%" height="auto">

<br>

- Use Stock Items screen. User is prompted input name of an existing stock item from the category they have currently selected, then press Enter to confirm. After that the user is prompted to enter the amount they wish to use, then press Enter to confirm. If the inputs are successful, the user will be give a confirmation message indicating what was checked out, how much was checked out, and the new stock level.

<img src="readme-docs/use-stock-items-input-confirm.png" alt="image of end of game message" width="80%" height="auto">

<br>

**Google Sheets**

- The data used in the lists is stored in Google Sheets. The data updates when the user either adds or removes stock from the list. In this case the units of weight/volume remain the same. This is relevant to the real world example of a purchase order being in place with the supplier to provide the same unit of stock each time an order is made.

<img src="readme-docs/sheets-shot-1.png" alt="image of end of game message" width="80%" height="auto">

<br>

- The data categories relevant to the menu categories displayed in the app are shown here separated into real-world sections. The sections are divided this way as to be more intuitive to the user to find the required menu option. 

<img src="readme-docs/sheets-shot-2.png" alt="image of end of game message" width="80%" height="auto">

<br>

## Future Features

The possible future features with this application are:
- Connecting this app to a well presented front-end display with drop-down menus and/or predictive text for item entry to speed up the entry process and reduce the possible amount of errors in entering stock item names. This app would be accessed though a designated tablet device which would make it portable.
- A user login for each person authorized to use the app. Also, an administrator account.
- Logging of ingoing/outgoing stock which contains dates, times, and person involved.
- Recording food wastage at the end of day.
- Recording of cooking times, food temperature, and fridge temperatures. This feature will reduce the amount of paper used, and comply with HACCP kitchen safety regulations. 
- The administrator can add/remove items from the list according to menu changes and availability, also change the weight/volume of a unit of the item. This is currently only possible by editing directly through Google Sheets.
- An alert message can be displayed when items go below a set amount to prompt the user to place a new order.

## Flowchart

- The flowchart shows the logic I followed in the creation of this application.

   <img src="readme-docs/flow-chart-pp3.png" alt="Flowchart showing the logic of app navigation." width="90%" height="auto">

## Technology Used

### Language Used

- Python was the language I used to write my code for this project.
- All other language was provided by the Code Institute in the template provided for this project.

### Programs, Libraries & Frameworks Used

- Google Sheets was used for the storage of data used in this application.
- VS Code Desktop was used to write the code.
- Gitpod was used for 
- Lucidchart was used to create the flowchart provided.
- Figma was used to design the wireframe for the project.
- Github was used to store the project code after being pushed.

## Testing

- I validated my code using the Code Institute Python Linter. The final testing shows a result of no errors or warnings. 
- I have not included any other validations because all other code was provided as a template by the Code Institute. 

<img src="readme-docs/ci-python-linter.png" alt="Code Institute Python Linter pass with zero warnings or errors." width="100%" height="auto">

<br>

## Manual Testing

### Test Cases: 

- When a user makes an invalid input in the main menu, they are notified with an error message. They are then prompted to re-enter a selection within the parameters shown. As seen below, the error message is shown because of a string being entered instead of the required numerical input. 

<img src="readme-docs/test-cases-pic-1.png" alt="Performance score image desktop." width="80%" height="auto">

<br>

- When a user makes an invalid input in the current stock menu, they are notified with an error message. They are then prompted to re-enter a selection within the parameters shown. As seen below, the error message is shown because of a out of range number being input. This number is also a negative, which is not accepted.

<img src="readme-docs/test-cases-pic-2.png" alt="Performance score image mobile." width="80%" height="auto">

<br>

- When a user makes an invalid input in the input new items menu, they are notified with an error message. They are then prompted to re-enter a selection within the parameters shown. As seen below, the error message is shown because of an out of range number being input. 

<img src="readme-docs/test-cases-pic-3.png" alt="Performance score image mobile." width="80%" height="auto">

<br>

- When a user makes an invalid input in the input new items menu, they are notified with an error message. They are then prompted to re-enter a selection within the parameters shown. As seen below, the error message is shown because of a negative value being input.

<img src="readme-docs/test-cases-pic-4.png" alt="Performance score image mobile." width="80%" height="auto">

<br>

- When a user makes an invalid input in the input new items menu, they are notified with an error message. They are then prompted to re-enter a selection within the parameters shown. As seen below, the error message is shown because of a valid stock item being input to the wrong Google Sheets category list. 

<img src="readme-docs/test-cases-pic-5.png" alt="Performance score image mobile." width="80%" height="auto">

<br>

- When a user makes an invalid input in the use stock items menu, they are notified with an error message. They are then prompted to re-enter a selection within the parameters shown. As seen below, the error message is shown because of an attempt to check out more stock than is available at that time. 

<img src="readme-docs/test-cases-pic-6.png" alt="Performance score image mobile." width="80%" height="auto">

<br>

- When a user makes an invalid input in the use stock items menu, they are notified with an error message. They are then prompted to re-enter a selection within the parameters shown. As seen below, the error message is shown because of a string being entered instead of a numerical input. 

<img src="readme-docs/test-cases-pic-7.png" alt="Performance score image mobile." width="80%" height="auto">

<br>

- All of these test cases have been tested on all menus and item name/amount inputs across the app without encountering any issues. 

### Known Bugs

- I noticed that some of the current stock lists appeared to be not clearing when I deployed the project with Heroku. I altering my code several times without success. After contacting Tutor Support, I was informed that the lists that were appearing to not be cleared were longer than the live console window, and only the visible data was being cleared. The issue lies with the CI template that was used for this project. For the purposes of this project, I have shortened my current stock lists to all fit inside the console window.
- To the best of my knowledge, there are no more bugs in my deployed application.

## Setup & Deployment

### Setup

- To begin this project I created a new GitHub repository using the Code Institute's Python Essentials template. This was done by using the 'use this template' option, and then 'create new repository'. 
- I named the repository stock-trace, and copied the url to Gitpod to confirm the workspace creation.
- Using Gitpod, I open my workspace in VS Code desktop version and begin my project.

### Google Sheets

- Using my personal Google account, I set up a spreadsheet called stock-trace via the Google Cloud Platform and created five worksheets corresponding to my five categories mentioned above in my menu options.
- To access the data for the purpose of my project I used an Application Programming Interface (API) called Google Drive. 
- I then set up a Service Account and created a private credentials key in the form of a JSON file which was downloaded onto my computer. 

### Credentials 

- The JSON credentials file is then added to the opened VS Code workspace by dragging and dropping into the file section at the left side of the workspace. I renamed the file creds.json and added it to the .gitignore list for safety. This will ensure that none of the info is sent to GitHub when commits are made. 
- The client email address is then copied from the creds.json file and pasted into the share section of the Google Sheets section at the top right of the screen. This allows the project to access and edit the data contained in the spreadsheet.

### External Python Libraries

- In order to use the Google Sheets API, google-auth and gspread are required. These are imported by entering 'pip3 install gspread google-auth' into the console,
 then entering 'import gspread' & 'from google.oauth2.service_account import Credentials' into line 1 & 2 of the codespace.
 - I then copied in the relevant SCOPE provided as part of the Love Sandwiches walkthrough for the Identity and Access Management configuration.
 - I also imported Operating Systems API (os) for my clear screen functions, and Patterns for my welcome screen graphics. This is stored in the patterns.py folder. 

 ### Deployment
 - Before deployment it is important to create a list of requirements to populate the requirements.txt file. this is done by 'inputting Pip3 freeze > requirements.txt' and Heroku will install the requirements into the application before the code is run. Remember to commit this change.
 - Using Heroku to deploy this project as a mock terminal, I used the Create New App option, gave it the name of stock-trace and selected Europe as my region, then select Create App.
 - In the settings section, add the creds.json file to the config vars by naming it CREDS and copying the contents of the creds.json file into the value field. 
 - Add Python buildpack, then save changes.
 -Add node.js buildpack, then save changes. It is important to add the buildpacks in this order.
 - In the Deploy section, select GitHub and confirm. Add repository name and select 'Search', then 'Connect' when the repository is found.
 - In this case I used the manual deployment option called 'Deploy Branch'. I deployed my project in the earlier stages of development to see how it responded in relation to how my code responded in the workspace console.
 - When the build log has completed and the app has successfully deployed, there is a message to show that this is the case and a button to click to view the live app.

## Credits

**During this project I took inspiration from:**
- Love Sandwiches Walkthrough Project.
- [Bakestock Project by Amy Richardson](https://github.com/amylour/BakeStock?tab=readme-ov-file#creation--deployment)
- [NetworkChuck Python Course](https://www.youtube.com/watch?v=mRMmlo_Uqcs)

I also used perplexity & ChatGpt which referenced: 
- [python.org](https://docs.python.org/3/) 
- [Stack Overflow](https://stackoverflow.com/questions/tagged/python)
- [Real Python](https://realpython.com/)

## Acknowledgements

I would like to thank the following people: 
- Friends, family and colleagues, for testing my project at every stage, and also for their feedback.
- My Mentor Rohit for his guidance, constructive feedback, and direction.
- Support from The Code Institute tutors along the way.
