# Project Proposal
## Title
MAYA - Cumulative Chess Player Insights
## Summary
Through this project, we aim to create a platform where a chess 
player is able to analyse a given opponent/opponents' moves given 
the state of the game in a specific subset of their games. These games 
will be extracted through lichess.com, one of the most common chess websites. 
The subset of game can be queried based on game type, time of day,
opposing player rating, period of time, etc. Through the generated analysis, 
the user will be able to timestep through the opponent's most common moves 
and opposing moves. Based on the state of the timestep, a user will 
be able to see the opponent's moves in the past in response to that state,
 how often each move is played in response, and how many games have they won, lost or drawn (winrate due to the move). 
 Multiple users may be inputted to analyse more generic gameplay. 
  Other statistics such as opening names will be queried and displayed.

## Description
Our project will create a website that will allow chess players to view the stats of the their opponents so they can can make decisions on how to best play against them.
There are current chess analysis websites, but those will only give a user general analysis data, and will recommend, in general, the next best move to make in a certain game state. However, what is good to do in general will not always work against an experienced chess player. To help chess players be more competitive, our website would be able to give our users data on speciafic opponents so they can can see which moves will probably work against them. The problem that this solves is players who are just starting to get competitive would now be able to compete against much more experienced players despite not having the level of experience that they command.

## Usefulness
This analyis is motivated by lichess.com not making opponent user insights public. 
This way we can generate the non-public insights in a user friendly way that can be used 
to stategize against a specific player, teams of players, before a competition or for personal improvement.
When playing chess against specific opponents, some openings or sequences of moves that opponents have made in the past
 have led to most of those games being lost despite the game appearing to be equal. We would like to take advantage of this 
 by spotting our own weaknesses and opponents weaknesses. We achieve this by analysing all games of a specific opponent
 or subset of opponents. As competitive chess players tend to play over a 1000 games online a year, 
 such analysis would be lucerative to direct your strategy towards certain players. 

## Realness
Our data will originate from lichess.com through publicly available API's or moves from all games played by the 
inputted user(s). The data we would require to achieve such analysis are all games played by the inputted users, 
all moves for that game encoded in some format for each player, time the game was played, player 1 rating, player 2 rating 
game type (blitz, rapid etc.), a seperate dataset with opening moves and their respective names. 

Average chess games end in 30-40 moves for a competitive player and such a game can be encoded in less than 
150 bytes. Players who play blitz games competitively tend to play at least a couple thousand games per year online. 
Players who play rapid games tend to at least play a thousand games a year online. Therefore analysing all of a players games 
in the history of their lifetime would only total to at max a couple hundred megabytes which is a feasible amount of data 
to be extracted and queried. As a user timesteps through the data, they will see all the moves played by the opponent, 
in response and then they will select the next step they would like to play based on the grouping of past games with the exact sequence until that point. 
Thus the dataset will be queried to be smaller as we go which is feasible. 

## Functionality
The main functionality for this website would be to display a chess player's opponent's data so they can understand their oppenent's playstyle.
In terms of create, delete, update, and search, our users will be able to create and display a table with different data sets based off their opponet's previous games.
To streamline and make our website as fast and efficient as possible, before making a second search, our users will have to delete their first query before making a second one.
This is so our users don't overload on data and they only analyze the last selected player/group of players' games/moves at a time. As far as update is concerned, say that a user first creates a query that only shows 
10 games worth of data. If they want to instead look at 20 games worth of data, they can update their query to show 20 games instead of 10. 
The base of the website is the user's ability to search for a set of game data on their opponents. The type of data stored in the data base will be
the users game data such as games won, date/time played, the type of game (i.e. classic, blitz, etc.) A seperate table would store individual moves for each game that a player has played.
The data we will be using will be from an api called lichess. Our data would be stored on a GCP platform that we create. The creative/fun component will be 
a users ability to take a certain game and recreate a certain gamestate from that game on lichess. 

The entities of the data will be LoginUser, ChessAccount, Leaderboard, Player, Game where each of the following attributes will have attributes. 

Attributes of the following entities: <br/>
  LoginUser - Email, AccountUsername (key), Password, DateCreated <br/>
  ChessAccount - AccountUsername, ChessUsername, WinRate, ProfileID (key) <br/>
  Leaderboard - Country, Chess_Username, Rank (key) <br/>
  Player - PlayerID (key), WinRate, Country, ChessUsername, Title <br/>
  Game - GameId (key), Time, Status, Opening_Strategy, OpponentID, OpponentRating, PlayerRating, GameType, Moves, Time, States <br/>
  
More information can be found in the Entity Relationship Model. <br/>

## Mockup
![image](https://media.github-dev.cs.illinois.edu/user/10801/files/10a11ebf-c3b9-49d5-aeff-cdaf9f24d47d)



## Project work distribution
Frontend - Armaan, Abbas  
Backend - Mukhil, Yuhao  
SQL Schema - Armaan, Yuhao, Mukhil  
Fethching data - Armaan, Mukhil  
Basic SQL queries - Everyone individually as there are many  
Advanced SQL queries - Everyone in pairs of two  
GCP setup and hosting - Yuhao, Abbas  

