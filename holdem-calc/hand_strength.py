def hand_strength(c):
    if len(c) != 7: raise Exception("Incorrect Number of Cards")
    types, ranks, suits = handType(c)
    x = check_SF(suits)
    if(x != False): return x
    elif types["quads"]: return quadsValue(ranks)
    elif types["boat"] : return boatValue(ranks)
    elif types["flush"]: return flushValue(suits)
    elif types["straight"]: return straightValue(ranks)
    elif types["set"]: return setValue(ranks)
    elif types["2pair"]: return twoPairValue(ranks)
    elif types["pair"]: return pairValue(ranks)
    else: return HCvalue(ranks)

def sortByRank(c):
    return sorted(c, key=lambda x: x.Rank(), reverse=True)
    
def handType(c):
    ranks = [[],[],[],[],[],[],[],[],[],[],[],[],[]]
    suits = [[],[],[],[]]
    types = {"flush" : False, "straight" : False, "quads" : False, "boat" : False,
             "set" : False,   "2pair"    : False, "pair"  : False
            }
    return get_best(types, ranks, suits, c)
    
def get_best(types, ranks, suits, c):
    for i in c:
        rank = i.Rank() - 2
        ranks[rank].append(i)
        if len(ranks[rank]) == 4: 
            types["quads"] = True
        elif len(ranks[rank]) == 3:
            if types["2pair"] == True: types["boat"] = True
            else                     : types["set"] =  True
        elif len(ranks[rank]) == 2:
            if types["pair"]  == True: types["2pair"] = True
            else                     : types["pair"] =  True
        
        suits[i.Suit()].append(i)
        if len(suits[i.Suit()]) == 5:
            types["flush"] = True
        
    consecutive = 0
    for i in ranks: 
        if len(i) > 0: consecutive += 1
        else: consecutive = 0
        if consecutive == 5: types["straight"] = True
    return types, ranks, suits

################################# Best Hands ###################################
def check_SF(suits): 
    for i in suits:
        c = []
        if len(i) >= 5: 
            c = i
    if c == []: return False
    for i in reversed([0, len(c) - 5]):
        if (c[i].Rank() == c[i + 1].Rank() - 1 == c[i + 2].Rank() - 2 \
                        == c[i + 3].Rank() - 3 == c[i + 4].Rank() - 4):
            return c[i+4].Rank() + 8000000, c[i:i + 5]
    return False

def quadsValue(ranks):
    quads, hc = list(), list()
    for i in reversed(ranks):
        if len(i) == 4 and len(quads) < 4: quads.extend(i)
        else: hc.extend(i)
    value = 14* quads[0].Rank() + hc[0].Rank() + 7000000
    return value, quads[0:4] + hc[0:1]
    
def boatValue(ranks):
    toak, pair = list(), list()
    for i in reversed(ranks):
        if len(i) == 3 and len(toak) < 3: toak.extend(i)
        if len(i) == 2 and len(pair) < 2: pair.extend(i)
    value = 14 * toak[0].Rank() + pair[0].Rank() + 6000000
    return value, toak[:3] + pair[:2]

def flushValue(suits):
    for i in suits:
        if len(i) == 5:
            sorted_cards = sortByRank(i)
            value = 5000000 + sorted_cards[0].Rank()
            return value, sorted_cards

def straightValue(ranks): 
    straight = list()
    consecutive = 0
    for i in reversed(ranks):
        if len(i) > 0: 
            consecutive += 1
            straight.append(i[0])
            if consecutive == 5: break
        else: 
            consecutive = 0
            straight.clear()
    value = 4000000 + straight[0].Rank()
    return value, straight[:5]

def setValue(ranks):
    toak, hc = list(), list()
    for i in reversed(ranks):
        if len(i) == 3 : toak.extend(i)
        else: hc.extend(i)
    value = toak[0].Rank() + hc[0].Rank() + hc[1].Rank() + 3000000
    return value, toak + hc[:2]
        
def twoPairValue(ranks): 
    pairs, hc = list(), list()
    for i in reversed(ranks):
        if len(i) == 2 and len(pairs) < 4: pairs.extend(i)
        elif len(hc) < 1: hc.extend(i)
    value = 14**2* pairs[0].Rank() +  14 * pairs[2].Rank() + hc[0].Rank() + 2000000
    return value, pairs + hc

def pairValue(ranks): 
    pair, hc = list(), list()
    for i in reversed(ranks):
        if   len(i) == 2 : pair.extend(i)
        hc.extend(i)
    value = 14**3 * pair[0].Rank() +  14**2 * hc[0].Rank() + \
            14 * hc[1].Rank() + hc[2].Rank() + 1000000
    return value, pair + hc[:3]
            
def HCvalue(ranks):
    best = list()
    for i in reversed(ranks): best.extend(i)
    value = 14**4 * best[0].Rank() + 14**3 + best[1].Rank() + \
            14**2 + best[2].Rank() + 14 * best[3].Rank() + best[4].Rank()
    return value, best[:5]
        