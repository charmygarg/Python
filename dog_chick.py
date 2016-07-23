def _sample_fun_puzzle_ (heads,legs):
    dogs=(legs-heads*2)/2
    if dogs<0 or dogs%1:
        return None
    dogs=int(dogs)
    chickens=heads-dogs
    if chickens< 0:
        return None
    return [chickens,dogs]