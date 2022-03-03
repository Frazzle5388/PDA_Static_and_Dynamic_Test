### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:


  def check_for_ace(self, card):
    # if card.value = 1: - missing an '='
      return True
    #else - missing ':'
      return False
   

  #dif highest_card(self, card1 card2): - dif should be def and would stop tests from running and mising a 'comma' after card1
  if card1.value > card2.value:
    #return card - should say card1
  else:
    return card2
  


# def cards_total(self, cards): needs to be indented
  #total - should say total = 0
  for card in cards:
    total += card.value
    return "You have a total of" + total
  
```
