# Techdegree Project 1

First Python tech degree project

Project one we were required to create a very simple number guessing game with the following user stories:
1. Display an intro/welcome message to the player.
2. Store a random number as the answer/solution.
3. Continuously prompt the player for a guess.
4. Once the guess is correct, stop looping, inform the user they "Got it" and show how many attempts it took them to get the correct number.
5. Let the player know the game is ending, or something that indicates the game is over

I was taught to use Trello cards and unload sprint tickets, every time I completed a user story onto the "Done" pile but due to the simplicity of the task at hand I chose not to.

I started by downloading the starter code and coded in a simple "Hello World!" to check if the code is working in the terminal.

### Challenges
- I created a function called **question()** which I though I will invoke every time a user got a wrong guess but because I was using a while true loop it did not work and was superfluous. I had to use the re assignment of guess variable at the beginning of the loop
- It was challenging to code the error handler using while loop, try except block and setting boolean to False

### Wins
- I created a variable named guess_tally which allowed me to keep track of all guesses
- I managed to use += shorthand to update the guess value
- In order to test the code quickly I printed the solution at the beginning of each run, making the development much easier

### Future
- If I was to attempt this 2 hour challenge again I would create a way for the user to play more than one game, this way I could print the high score of all games played
