### Credits
The idea for this project is loosely based on software testing card games introduced by  Rapid Software Testing authors James Bach<sup>[1]</sup> and James Bolton<sup>[2]</sup>.
This project would be much harder to achieve without deckofcardsapi.com and Python.     

### The game
The version of the game I was playing with my team and on the testing conferences, has the following simple rules:

The  master (one who deals ATM) deals 5 cards for everybody to see and says whether the hand on the table is true or false. The game master continues to draw 5 cards and states with every hand if it is true or false. That statement is based on some sort of rule that is known only to the game master. Eg: true is if the sum of all the numbered cards is more than 14, or if there are at least 3 red cards in the hand, or if there are at least two hearts. 

Basicaly, there are _dimensions_ that should be representable in a number - eg: sum of numbered cards, number of face cards, number of cards with female characters, number of cards where a character holds a sword etc, and _rules_ which is result of some mathematical operation within dimension in the current hand. For example, a rule can be that 2 kings are true (=), or at least 3 face cards are true (=>), the sum of cards wiht numnbers is less than 20 (<) etc. 

A player who guesses the rule (think of it as the unknown unknown of the cynefin framework<sup>[3]</sup>) is a winner and contender for the next game master in the game.

### Project goals

This project has two goals - one is to generate lists with hands of actual playing cards (represented with their simbols, eg 3D is three of diamnond and KH is King of hearths). Second is to use machine learning to "guess" the rule. 
The question is would that be possible without revealing the dimension. 


[1]: http://blog.markpearl.co.za/assets/documents/exploratory-testing-with-playing-cards.pdf
[2]: http://www.bettertesting.co.uk/content/?p=438 
[3]: https://en.wikipedia.org/wiki/Cynefin_framework
 

