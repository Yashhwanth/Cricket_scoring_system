# Cricket Scoring System
## Overview  
  This **Cricket Scoring System** is a console-based application designed to accurately score cricket matches in real-time. It follows the official rules of cricket and simulates all match scenarios such as batting, bowling, wickets, extras, partnerships, and overs. The system is built in Python and aims to provide accurate real-time score updates, making it suitable for use in live cricket matches.
## Features
1.  **Real-Time Scoring**: Keep track of each ball's runs, wickets, and extras (wides, no-balls, byes, leg byes).  
2.	**Batsman and Bowler Statistics**: Automatically updates individual and team stats after each ball.  
3.	**Partnership Tracking**: Records partnerships between batsmen.  
4.	**Wicket Handling**: Identifies which batsman got out (striker or non-striker) and accurately reflects the dismissal in the scorecard.  
5.	**Extras Handling**: Includes scenarios like wides, no-balls, byes, and leg-byes according to official cricket rules.  
6.	**Maiden Over Detection**: Checks if the bowler bowled a maiden over.  
7.	**Undo Feature**: Allows you to revert to the previous ball in case of incorrect inputs.  
8.	**Multiple Innings**: Supports scoring for both innings of the match.  
9.	**Non-playing Members**: Stores data for players who did not bat or bowl in the match but are part of the team.  
## Requirements
1.	Python 3.x  
2.	Basic understanding of cricket rules  
## How to Run  
1.  **Clone the repository**:  
`git clone https://github.com/Yashhwanth/MyCric.git`  
`cd MyCric`  
2.  **Ensure you have Python 3 installed. You can check by running:**  
`python --version`   
3.  **Run the main Python file:**  
`python main.py`  
4. **Follow the prompts on the console to input match details, ball-by-ball updates, and track the game.**  
## Usage
1.	**Start the Match**: Enter team names, number of overs, and choose the batting side.  
2.	**Input Ball Data**: After every ball, enter the runs, type of ball (normal, wide, no-ball, etc.), and update whether a wicket has fallen.  
3.	**Track Partnerships**: The system automatically tracks partnerships and updates the score accordingly.  
4.	**Handle Wickets**: When a batsman gets out, the system updates the score and prompts for the next batsman.  
5.	**End Innings**: At the end of an innings, set the target for the other team and repeat the process for the second team.  
6.	**Undo Function**: If an error occurs, the last ball's data can be undone and corrected.  
## Future Development
This system is currently in a console-based phase. Future developments include:  
1.	**Website and App Development**: Build a web and mobile app version for better user experience and more robust features.  
2.	**Database Integration**: Store match data in a database for long-term tracking and statistics generation.  
3.	**UI/UX Enhancements**: Provide a graphical user interface for more intuitive inputs and display of real-time match statistics.  
4.	**Team and Player Management**: Include functionality to manage teams and players over multiple matches or tournaments.  
## Contributing
We welcome contributions to enhance the system's functionality! To contribute:  
1.	Fork the repository.  
2.	Create a new feature branch. 
3.	Make your changes and test them.  
4.	Submit a pull request, and describe the changes you’ve made.  

