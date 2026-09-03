"""
3 2 6
browns martellus tyrod tom john teddy danny
rams danny tyrod martellus john teddy tom
giants teddy danny tyrod john tom martellus
teddy giants browns rams
danny giants browns rams
tyrod giants rams browns
john giants rams browns
tom browns giants rams
martellus giants browns rams

"""
def stable_matching(teams: dict, players: dict, matchings: dict, tot_matchings: int, m): 
    curr_match: int = 0 
    while curr_match < tot_matchings: 
        for team, list_of_players in matchings.items():
            if len(list_of_players) >= int(m): 
                continue 
            else: 
                items = teams[team]
                first_item = items[0]
                if not any(first_item in players for players in matchings.values()):
                    # matchings[team] = first_item
                    matchings[team].append(first_item)
                    
                    curr_match += 1
                else: 
                    # What team is the player engaged to? 
                    team_of_engagement = ""
                    for t, p in matchings.items(): 
                        if first_item in p: 
                            team_of_engagement = t
                            break 
                    
                    #Now, we got the team. Check if THIS team is less preferred than the current team.
                    best_team = ""
                    for pref in players[first_item]: 
                        if pref == team_of_engagement or pref == team: 
                            best_team = pref
                            break
                    
                    if best_team == team: 
                        matchings[team_of_engagement].remove(first_item)
                        matchings[team].append(first_item)

                #Remove the engaged person from preference list of given team
                entry = teams[team]
                del entry[0] 

    return matchings      
                
    
        
   
                

                
                

    

def printdict(mydict):
    for k, v in mydict.items():
        print(k, " ".join(v))
    
def main():
    n, m, k = input().split(" ")
    teams_ = {} 
    players_ = {}

    ctr = 1
    for i in range(int(n) + int(k)):
        if ctr <= int(n):
            line = input()
            lst = line.split(" ")
            teams_[lst[0]] = lst[1:]
            
        else:
            line = input()
            lst = line.split(" ")
            players_[lst[0]] = lst[1:]
        ctr += 1

    matchings: dict = {}
    for k in teams_.keys():
        matchings[k] = []

    no_matchings = int(n)*int(m)


    
    result = stable_matching(teams_, players_, matchings, no_matchings, m)    
    printdict(result)
if __name__=="__main__":
    main()