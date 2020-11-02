STRAIGHT_FLUSH = 8000000                                      
QUAD           = 7000000                                              
BOAT           = 6000000       
FLUSH          = 5000000          
STRAIGHT       = 4000000        
SET            = 3000000       
TWO_PAIR       = 2000000  
ONE_PAIR       = 1000000

def hand_strength(c):
    if len(c) != 7: raise Exception("Incorrect Number of Cards")
    # elif isFlush(c) and isStraight(c): return valueStraightFlush(c)
    # elif isQuads(c): return valueFourOfAKind(c)
    # elif isBoat(c): return valueFullHouse(c)
    # elif isFlush(c):  return valueFlush(c)
    # elif isStraight(c): return valueStraight(c)
    # elif isSet(c): return valueSet(c)
    # elif is2Pair(c): return valueTwoPair(c)
    elif isPair(c): return valueOnePair(c)
    else: return valueHighCard(c)

def sortByRank(c):
    return sorted(c, key=lambda x: x.Rank(), reverse=True)

############################# High Card Function ###############################

def valueHighCard(c):
    best = sorted(c, key=lambda x: x.Rank(), reverse=True)
    val = best[0].Rank() + 14* best[1].Rank() + 14*14* best[2].Rank() + 14*14*14* best[3].Rank() + 14*14*14*14* best[4].Rank()
    return val, best
    
############################# One Pair Functions ###############################

def valueOnePair(c):
    best = bestPairHand(c)
    val = 14*14*14*best[0].Rank() + 14*14*best[2].Rank() + 14*best[3].Rank() + best[4].Rank()
    
    return ONE_PAIR + val, best
    
def bestPairHand(c):
    best_five = list()
    c = sortByRank(c)
    for i in range(6):
        if c[i].Rank() == c[i + 1].Rank():
            final.append(c[i], c[i + 1])
            c = list(filter(lambda a: a.Rank() != c[i].Rank, c))
            final.append(c[0], c[1], c[2])
            return best_five
    raise "Not a pair"
    
def isPair(h):
    for i in range(6):
        if h[i].Rank() == h[i + 1].Rank(): return True
    return False

############################# Two Pair Functions ###############################
def valueTwoPair(h):
    best = twoPairBestHand(c)
    val = 14*14*h[2].Rank() + 14*h[0].Rank() + h[4].Rank()
    return TWO_PAIR + val, best

def best2PHand(c): return

def is2Pair(c): return

################################ Set Functions #################################

def isSet(c): return
def bestSetHand(c): return
def valueSet(c): 
    c = sortByRank(c)
    return SET + h[2].Rank()

############################# Straight Functions ###############################
def isStraight(c): return
def bestStraightHand(c): return
def valueStraight(c):
    return STRAIGHT + valueHighCard(c); 
    
############################### Flush Functions ################################
def isFlush(c): return true
def bestFlushHand(c): return
def valueFlush(c): 
    return FLUSH + valueHighCard(c)
############################### 4ofaK Functions ################################

def isQuads(c): 
    sortByRank(h)
    return
def bestQuadsHand(c): return
def valueFourOfAKind(c):
    c = sortByRank(c)
    return FOUR_OF_A_KIND + c[2].Rank()
############################# Full House Functions #############################

def isBoat(c):return 
def bestBoatHand(c):return 

def valueFullHouse(c):
    c = sortByRank(c)
    return FULL_HOUSE + h[2].Rank()





    