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

<img src="readme-docs/main-menu.png" alt="Image of 'How to Play' button" width="90%" height="auto">
    
    

**Current Stock Menu**\
The Current Stock Menu Consists of six options:
1. The user can proceed to view the Meat & Fish stock list by inputting 1 & Enter.
2. The user can proceed to view the Fruit& Veg stock list by inputting 2 & Enter.
3. The user can proceed to view the Dry Goods stock list by inputting 3 & Enter.
4. The user can proceed to view the Chilled Goods list by inputting 4 & Enter.
5. The user can proceed to view the Frozen Items by inputting 5 & Enter.
6. The user can return to the Main Menu by inputting 6 & Enter.


<img src="readme-docs/current-stock-main.png" alt="Image of Current Stock Menu." width="90%" height="auto">  
    

**Current Stock List screens**


<img src="readme-docs/audio-off.png" alt="Image of 'Audio muted' button" width="10%" height="auto">
<img src="readme-docs/audio-on.png" alt="Image of 'Audio unmuted' button" width="9.8%" height="auto">

**Turns Counter**

- The Turns counter will increase by one every time a move is made in the puzzle. This will be displayed in the pop-up window when the puzzle is solved.

<img src="readme-docs\turns-counter.png" alt="image of turns counter" width="30%" height="auto">

**End of Game Message**

- When the puzzle is solved, a pop-up message will congratulate you for solving the puzzle and let you know how many moves you made.

<img src="readme-docs/win-screen.png" alt="image of end of game message" width="20%" height="auto">

### The Footer

- The footer section includes links to the relevant social media sites for the puzzle. The links will open to a new tab to allow easy navigation for the user.
- The footer is valuable to the user as it encourages them to keep connected via social media.

    <img src="readme-docs/footer.png" alt="image of website footer" width="65%" height="auto">

## Future Features

- Future features will include recording of high scores, an audio alert when you complete the game (if audio is enabled), 

## Typography and Color Scheme

- The Honk font from Google Fonts will be used for this project Heading.
- A custom color palette from Adobe Color will be used for this project. This color pallet consists of #3498E9 for the background, #E7EB09 for the yellow which transitions to red #DA3A8A in the heading and footer

    
    <img src="readme-docs/adobe-project-palette.png" alt="Adobe color pallet image." width="50%" height="auto">

## Flowchart

   <img src="readme-docs/flow-chart-pp3.png" alt="Flowchart showing the logic of app navigation." width="90%" height="auto">

## Technology Used

### Language Used

- HTML5 & JavaScript were provided as part of the Code Institute template for this project.
- Python was the language I used to write my code for this project.

### Programs, Libraries & Frameworks Used

- Google Sheets was used for the storage of data used in this application.
- VS Code Desktop was used to write the code.
- Gitpod was used for 
- Lucidchart was used to create the flowchart provided.
- 
- Figma was used to design the wireframe for the project.
- Github was used to store the project code after being pushed.

## Testing

- W3C Markup Validator, W3C CSS Validator & JS Hint were used to validate all code contained in the project. The final tests were completed without errors. 
- Lighthouse developer tool was also used to gauge the performance of the project on desktop and mobile views. The desktop scored a 99, and the mobile test scored 72 for performance.

    <img src="readme-docs/performance-desktop.png" alt="Performance score image desktop." width="27%" height="auto">
    <img src="readme-docs/performance-mobile.png" alt="Performance score image mobile." width="25%" height="auto">

- All buttons and external links were tested manually to ensure there were no connection errors. The modals all open and close as expected, and external links open in a new page in the browser. 
- The project was also tested with Google's dev tools to show responsiveness on different screen sizes, and also on different browsers.
- Testing was done on several desktop and laptop computers, various mobile devices like the iPhone, Nokia, Samsung and Huawei to make sure that the navigation and external links were functioning correctly.
- Family members, friends and colleagues also kindly tested the functionality and user experience at several stages of the projects development.

### Known Bugs

- When refreshing the page, the win-modal appears for a fraction of a second on the reload. 
- On mobile view, the picture tiles were flasing when selected to move. I removed this by add -webkit-tap-highlight-color: transparent; to the body CSS. This has removed the flashing but shows up as a warning on the validator. 

## Deployment

- The code was written on VS Code desktop version, commits were commented and pushed to the relevant Github repository.
- The site was deployed to GitHub pages. The steps to deploy are as follows:
- In the GitHub repository, navigate to the Settings tab
- From the source section drop-down menu, select the Master Branch
- Once the master branch has been selected, the page will be automatically refreshed with a detailed ribbon display to indicate the successful deployment.

The live link can be followed here - <https://brianmcconway.github.io/puppy-puzzle-game/>

## Credits

**During this project I used:**
- https://rocoderes.com/slide-puzzle-game-in-html-css-and-javascript/  for puzzle-board sertup and movement of puzzle pieces.
- https://codeguppy.com/code.html?t=sliding_puzzle
 to help with the JavaScript for the movement of the puzzle pieces.
- https://www.youtube.com/watch?v=o5ffh3KUaTM to help with the creation of modals.
-  I also used Perplexity & ChatGPT which referenced MDN Web Docs including: Event Handling, Dom Manipulation, Arrays & Functions in JavaScript, 
- This Readme file template, for the suggested layout.

## Acknowledgements

- Friends, family and colleagues, for testing my project at every stage, and also for their feedback.
- My Mentor for constructive feedback and direction.
- Support from The Code Institute.
