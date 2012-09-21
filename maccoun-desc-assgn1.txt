README

Steven MacCoun
NLP CSCI 5832 Fall 2012

HW 1


Part 3 ->

For part 3 I first removed all one and two letter words that were not in a list of most frequent one/two letter words.

For the maxMatch algorithm, I used a search ahead in the algorithm. Once a match for a word is found, the algorithm first searches ahead and each time it finds a match, it records it as a possible match. It selects the longest possible word in its search ahead that it can find, adds that maxMatch list, and then increments the pointer to that point in the word.

I ran this algorithm both forwards and backwards. After getting both results, I compared the lists by looking at which had the longest first and last words (I did this by summing the lenght of the first and last words for each result). The intuition behind this was that long words tend to be correct more often, and maxMatch tends to really screw up once it starts missing after its initial hits. Thus, if it had a long first word and last word, it was more likely that those words were correct, and so were the words in between. If the words had the same length first and last words, then maxMatch compared which had more long words (where I defined long as >= 4) since, again, I assumed that long words were more likely to be correct and if a long word was matched it was more likely the other words would be correct.