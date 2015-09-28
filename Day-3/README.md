##Simulating the "Monty Hall" Scenario

The Monty Hall scenario is this:

> Monty offers you 3 doors and you pick one (randomly).

> Behind one door is a new car.  Behind the other two doors are goats.

> Monty then opens one of the doors you didn't choose, revealing a goat.  He asks you if you want to
> keep your initial selection ("STAY"), or change to the other door ("SWITCH").

> (Note:  Monty never opens a door that has a car behind it.  He always opens a door with a goat.)

In terms of your chances to win a car, do you think it's better to STAY, SWITCH, or it doesn't matter?

Most people think it doesn't matter - that your chances of winning are the same either way.

Let's test it.  

Write a Python program to:

- Simulate the Monty Hall scenario
    - the code should randomly choose:
        - which door has the car
        - which door the player chooses
        - which door Monty opens (keeping to the rule that monty never
         opens your door, and never opens a door with  the car behind it)
        - whether to STAY or SWITCH
- Run the scenario many times and keep track of the results
- Print a summary of the results at the end.

Your output should look something like this:

    You played the game 10 times.
    Of those, you STAYed   5 times. Won 3, and lost 2 or 60.00% winning
    Of those, you SWITCHed 5 times. Won 2, and lost 3 or 40.00% winning

To help debug your code, you might want to have it print out what it's
doing, so you know it's working correctly.  Then your output might look like this:

    You picked Door #2.  Monty opens door #3 to reveal a goat.  You STAY with door #2  Car is behind door #1  You LOSE.
    You picked Door #1.  Monty opens door #3 to reveal a goat.  You STAY with door #1  Car is behind door #2  You LOSE.
    You picked Door #1.  Monty opens door #3 to reveal a goat.  You SWITCH to door #2  Car is behind door #1  You LOSE.
    You picked Door #1.  Monty opens door #3 to reveal a goat.  You STAY with door #1  Car is behind door #1  You WIN.
    You picked Door #1.  Monty opens door #3 to reveal a goat.  You STAY with door #1  Car is behind door #1  You WIN.
    You picked Door #3.  Monty opens door #2 to reveal a goat.  You STAY with door #3  Car is behind door #3  You WIN.
    You picked Door #1.  Monty opens door #3 to reveal a goat.  You SWITCH to door #2  Car is behind door #2  You WIN.
    You picked Door #1.  Monty opens door #2 to reveal a goat.  You SWITCH to door #3  Car is behind door #3  You WIN.
    You picked Door #2.  Monty opens door #1 to reveal a goat.  You STAY with door #2  Car is behind door #3  You LOSE.
    You picked Door #2.  Monty opens door #3 to reveal a goat.  You SWITCH to door #1  Car is behind door #1  You WIN.
    ... and so on, 100 times...
    
    You played the game 100 times.
    Of those, you STAYed   44 times. Won [some number], and lost [some number] or [some %] winning
    Of those, you SWITCHed 56 times. Won [some number], and lost [some number] or [some %] winning