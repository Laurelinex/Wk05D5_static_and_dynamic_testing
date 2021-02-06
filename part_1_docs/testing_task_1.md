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

# The issue is that the code is not checking that the value is equal to 1, it should be '==' for comparaison and not '='.
# else needs a colon.
  def check_for_ace(self, card):
    if card.value = 1:
      return True
    else
      return False
   
# 'def' is mispelled and so the method is not being declared. 
# There should be a comma between parameters.
# card should be card1
  dif highest_card(self, card1 card2):
  if card1.value > card2.value:
    return card
  else:
    return card2
  
# Total should be a variable assigned with a value, e.g. 'total = 0'
# The return statement indentation is incorrect and should have the prefix 'f' and total be within {} brackets.
def cards_total(self, cards):
  total
  for card in cards:
    total += card.value
    return "You have a total of" + total
  
```
