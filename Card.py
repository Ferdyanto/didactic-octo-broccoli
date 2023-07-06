import random

SUIT_TUPLE = ('Spades', 'Hearts', 'Clubs', 'Diamonds')
RANK_TUPLE = ('Ace', '2', '3', '4', '5', '6', '7', '8', '9',
'10', 'Jack', 'Queen', 'King')
NCARDS = 8

def getCard(deckListIn):
  thisCard = deckListIn.pop()
  return thisCard
  
def shuffle(deckListIn):
  deckListOut = deckListIn.copy()
  random.shuffle(deckListOut)
  return deckListOut
  
print('Welcome to Higher or Lower.\nYou have to choose whether the next card to be shown will be higher or lower than the current card.\nGetting it right adds 20 points; get it wrong and you lose 15 points.\nYou have 50 points to start.\n')

startingDeckList = []
for suit in SUIT_TUPLE:
  for thisValue, rank in enumerate(RANK_TUPLE):
    cardDict = {'rank':rank, 'suit':suit,
'value':thisValue +1}
    startingDeckList.append(cardDict)
score = 50

while True:
  gameDeckList = shuffle(startingDeckList)
  currentCardDict = getCard(gameDeckList)
  currentCardRank = currentCardDict['rank']
  currentCardSuit = currentCardDict['suit']
  currentCardValue = currentCardDict['value']
  
  print('Starting card is', currentCardRank,'of', currentCardSuit)
  for cardnum in range(NCARDS):
    answer = input('higher or lower?(h/l)\n').casefold()
  
    nextCardDict = getCard(gameDeckList)
    nextCardRank = nextCardDict['rank']
    nextCardSuit = nextCardDict['suit']
    nextCardValue = nextCardDict['value']
    print('\nNext card is', nextCardRank,'of', nextCardSuit)
  
    if answer == 'h':
      if nextCardValue > currentCardValue:
        print('Correct')
        score += 20
      else:
        print('Wrong')
        score -= 15
    elif answer == 'l':
      if nextCardValue < currentCardValue:
        print('Correct')
        score += 20
      else:
        print('Wrong')
        score -=15
  print('Your score is:',score)
  currentCardRank = nextCardRank
  currentCardSuit = nextCardSuit
  
  goAgain = input('Play again?(ENTER/q)\n')
  if goAgain == 'q':
    break
    print('Thanks for playing')