# ix-lisbon-project-week-1
I first made a dictionary with the cards 2-ACE assigning values to them of 2-14. After this I made a deck by using the class Cards and making the cards multiply by 4 (for the four suits in a deck of cards).  Then I made a new class called Players and had it initiatize itself with the input "What is your name?" and this would be asked the amount of times that the player indicates at the start of the game when prompted "How many players are playing."  Each player is immediately assigned a hand based on a shuffled deck of cards.  I was unable to compare these cards because I could not retrieve numerical values for them as they were part of the class Cards.  This is as far as I have been able to come, after consulting with Manuel and Genc for a while.

Blog: zlg8dt.github.io

------------------------------------------------------------------------------------------------
# Feedback: 
------------------------------------------------------------------------------------------------

| Section | Mark | 
|---|---| 
| Blog | 90% | 
| Poker Game | 75% |
||| 
| Total/100% | 83% | 

Blog is live and has a decent explanation of the poker_game.py inner workings.

Poker game doesn't execute fully:

```
$ python poker_game.py
How many players are you? 3
What is your name? Bru
[Q, K, 4, J, J]
What is your name? Bob
[Q, 5, 4, Q, 2]
What is your name? Brad
[10, 8, A, 3, 9]
Traceback (most recent call last):
  File "poker_game.py", line 78, in <module>
    game.compare()
  File "poker_game.py", line 60, in compare
    if card > high_card:
TypeError: '>' not supported between instances of 'Cards' and 'int'
```

but it is evident that a decent amount of work has gone into it.
