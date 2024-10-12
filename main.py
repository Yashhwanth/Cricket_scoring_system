overs = int(input("no of overs to be played"))
balls=overs*6
tballs=balls
over_count=0
total=0
wickets=0
extras=0
batsmans={}
#batsmanMap={"0":0,"1":0,"2":0,"3":0,"4":0,"5":0,"6":0}
bastman_reset={"score":0,"balls":0,"0":0,"1":0,"2":0,"3":0,"4":0,"5":0,"6":0}
s=input("striker")
ns=input("non-striker")
batsmans[s]=bastman_reset
batsmans[ns]=bastman_reset
playing_batsman={s:{"score":0,"balls":0,"0":0,"1":0,"2":0,"3":0,"4":0,"5":0,"6":0},ns:{"score":0,"balls":0,"0":0,"1":0,"2":0,"3":0,"4":0,"5":0,"6":0}}

bowlers={}
bowler_name = None
bowler_input_done = False
bowlsmap={"0":0,"1":0,"2":0,"3":0,"4":0,"5":0,"6":0,"wb":0,"nb":1,"db":0,"wk":0,"by":0,"lb":0}

score={"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"wb":1,"nb":1,"db":0,"wk":0,"by":0,"lb":0,"stm":0}
scoreMap={"0":0,"1":0,"2":0,"3":0,"4":0,"5":0,"6":0,"wk":0,"wb":0,"nb":0,"by":0,"lb":0,"rtd":0,"db":0}
scoreFreq={"0":0,"1":0,"2":0,"3":0,"4":0,"5":0,"6":0,"wb":0,"nb":0,"db":0,"wk":0,"by":0,"lb":0,"rtd":0}

wicketsMap={"b":"bowled","c":"caught","lbw":"lbw","c&b":"caught&bowled","ro":"runout","stm":"stumped","hw":"hitwicket","hb":"handled the ball","obs":"obstructing the feild","to":"timedout","rtdo":"retired out"}
wicketFreq={"b":0,"c":0,"lbw":0,"c&b":0,"ro":0,"stm":0,"hw":0,"hb":0,"obs":0,"to":0,"rtdo":0}


def striker_resetting(out_batsman,out_end):
    global s,ns,curr_playing_batsman
    del curr_playing_batsman[out_batsman]
    new_batsman_name = input("Enter the new batsman's name: ")
    batsmans[new_batsman_name]=bastman_reset
    curr_playing_batsman[new_batsman_name] = {"score":0,"balls": 0, "0": 0, "1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0}
    if out_end=="s":
        #del curr_playing_batsman[s]
        #curr_playing_batsman[new_batsman_name] = {"balls":0,"0": 0, "1": 0, "2": 0, "3": 0, "4": 0, "5": 0,"6": 0}  # Reset stats
        ns=s
        s = new_batsman_name
    elif out_end=="ns":
        #del curr_playing_batsman[s]
        #curr_playing_batsman[new_batsman_name] = {"balls": 0, "0": 0, "1": 0, "2": 0, "3": 0, "4": 0, "5": 0,"6": 0}  # Reset stats
        s=ns
        ns = new_batsman_name
    return s,ns
def teams_stats_while_wicket(x,extra_runs,type_of_ball):
    global total,scoreFreq,scoreMap
    total += score[x] + score[extra_runs] + score[type_of_ball]
    scoreFreq[x] += 1
    scoreFreq[extra_runs] += 1
    scoreFreq[type_of_ball] += 1
    scoreMap[extra_runs] += score[extra_runs]
    scoreMap[type_of_ball] += score[type_of_ball]

def strikeRotate(s,ns,runs):
    if int(runs)%2!=0:
        return ns,s
    return s,ns

def inputScenario(a): # function to get the scenario present in corr. maps
    while a not in score:
        a = input("re enter")
    return a

while balls: #if there is a ball it has too be bowled
    if (tballs - balls) % 6 == 0 and not bowler_input_done: # Ask for new bowler at the start of each over
        bowler_name = input("Enter bowler's name:")
        if bowler_name not in bowlers:
            bowlers[bowler_name] = {"balls": 0, "runs": 0, "0": 0, "1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0,"wk": 0, "by": 0, "lb": 0, "wb": 0, "nb": 0, "db": 0}
            bowler_input_done = True
    curr_playing_batsman=playing_batsman
    c=(tballs-balls)%6+1 # just to ask input score for each ball
    inputscene=input("enter score of {} ball".format(c)) #scenaio when ball is bowled
    x=inputScenario(inputscene) # to get correct scenario
    if x=="wb":
        extra_in_wide = input("enter extra scenario")
        extra_runs = inputScenario(extra_in_wide) # extra runs in wide ball
        s,ns=strikeRotate(s,ns,extra_runs)
        bowlers[bowler_name][x] += 1
        bowlers[bowler_name][extra_runs] += 1
        bowlers[bowler_name]["runs"] += score[x] + score[extra_runs]
        scoreFreq[x] += 1  # update score freq
        scoreFreq[extra_runs] += 1  # update score freq
        scoreMap[x] += score[x] + score[extra_runs]  # update score map
        total += score[extra_runs] + score[x]  # update total
        extras+=score[x]+score[extra_runs]
    elif x=="nb":
        extra_in_wide = input("enter extra scenario")
        extra_runs = inputScenario(extra_in_wide) # extra runs in wide ball
        #curr_playing_batsman[s]["balls"] += 1
        curr_playing_batsman[s]["score"] += score[extra_runs]
        curr_playing_batsman[s][extra_runs] += 1
        s, ns = strikeRotate(s, ns, extra_runs)
        bowlers[bowler_name][x] += 1
        bowlers[bowler_name][extra_runs] += 1
        bowlers[bowler_name]["runs"] += score[x] + score[extra_runs]
        scoreFreq[x] += 1  # update score freq
        scoreFreq[extra_runs] += 1  # update score freq
        scoreMap[x] += score[x] + score[extra_runs]  # update score map
        total += score[extra_runs] + score[x]  # update total
        extras+=score[x]+score[extra_runs]
        print(curr_playing_batsman)
    elif x=="db":
        bowlers[bowler_name][x]+=1
        scoreFreq[x]+=1
    elif x=="by" or x=="lb":
        extra_runs=input("enter runs in by or legbyes")
        s, ns = strikeRotate(s, ns, extra_runs)
        bowlers[bowler_name][x] += 1
        bowlers[bowler_name][extra_runs] += 1
        bowlers[bowler_name]["runs"] += score[x] + score[extra_runs]
        scoreFreq[x] += 1  # update score freq
        scoreFreq[extra_runs] += 1  # update score freq
        scoreMap[x] += score[x] + score[extra_runs]  # update score map
        total += score[extra_runs] + score[x]  # update total
        extras+=score[x]+score[extra_runs]
        balls-=1
    elif x=="wk":
        wickets+=1
        extra_runs=input("runs in wicket ball")
        type_of_ball=input("enter type of ball-n/nb/wb/lb/b")
        out_batsman=input("mention out bs name")
        out_end=input("enter s/ns")
        type_of_w = input("type of dis")
        if type_of_ball=="nb":
            #curr_playing_batsman[s]["balls"] += 1
            curr_playing_batsman[s][extra_runs] += 1
            curr_playing_batsman[s]["score"] += score[x]+score[extra_runs]

            batsmans[out_batsman] = curr_playing_batsman[out_batsman]
            striker_resetting(out_batsman, out_end)

            #bowlers[bowler_name][x] += 1
            #bowlers[bowler_name]["balls"] += 1
            bowlers[bowler_name][extra_runs] += 1
            bowlers[bowler_name][type_of_ball] += 1
            bowlers[bowler_name]["runs"] += score[x] + score[extra_runs]+score[type_of_ball]
            #teams
            teams_stats_while_wicket(x, extra_runs, type_of_ball)
            extras += score[type_of_ball]

            wicketFreq[type_of_w]+=1

        elif type_of_ball=="wb":
            #curr_playing_batsman[s]["balls"] += 1
            # curr_playing_batsman[s][extra_runs] += 1
            #curr_playing_batsman[s]["score"] += score[x]

            batsmans[out_batsman] = curr_playing_batsman[out_batsman]
            striker_resetting(out_batsman, out_end)

            #bowlers[bowler_name][x] += 1
            #bowlers[bowler_name]["balls"] += 1
            bowlers[bowler_name][extra_runs] += 1
            bowlers[bowler_name][type_of_ball] += 1
            bowlers[bowler_name]["runs"] += score[x] + score[extra_runs] + score[type_of_ball]
            # teams
            teams_stats_while_wicket(x, extra_runs, type_of_ball)
            extras += score[type_of_ball]

            wicketFreq[type_of_w] += 1

        elif type_of_ball=="lb" or type_of_ball=="b":
            curr_playing_batsman[s]["balls"] += 1
            # curr_playing_batsman[s][extra_runs] += 1
            # curr_playing_batsman[s]["score"] += score[x]

            batsmans[out_batsman] = curr_playing_batsman[out_batsman]
            striker_resetting(out_batsman, out_end)

            #bowlers[bowler_name][x] += 1
            bowlers[bowler_name]["balls"] += 1
            bowlers[bowler_name][extra_runs] += 1
            bowlers[bowler_name][type_of_ball] += 1
            bowlers[bowler_name]["runs"] += score[x] + score[extra_runs] + score[type_of_ball]
            # teams
            teams_stats_while_wicket(x, extra_runs, type_of_ball)
            extras += score[type_of_ball]
            balls -= 1

            wicketFreq[type_of_w] += 1

        else:
            type_of_ball = '0'
            curr_playing_batsman[s]["balls"] += 1
            curr_playing_batsman[s][extra_runs] += 1
            curr_playing_batsman[s]["score"] += score[x] + score[extra_runs]

            batsmans[out_batsman] = curr_playing_batsman[out_batsman]
            striker_resetting(out_batsman, out_end)

            bowlers[bowler_name][x] += 1
            bowlers[bowler_name]["balls"] += 1
            bowlers[bowler_name][extra_runs] += 1
            bowlers[bowler_name][type_of_ball] += 1
            bowlers[bowler_name]["runs"] += score[x] + score[extra_runs] + score[type_of_ball]
            # teams
            teams_stats_while_wicket(x, extra_runs, type_of_ball)
            balls -= 1

            wicketFreq[type_of_w] += 1
    else :
        curr_playing_batsman[s]["balls"]+=1
        curr_playing_batsman[s]["score"]+=score[x]
        curr_playing_batsman[s][x] += 1
        s,ns=strikeRotate(s,ns,x)
        #updatin bowler's
        bowlers[bowler_name][x]+=1
        bowlers[bowler_name]["balls"]+=1
        bowlers[bowler_name]["runs"]+=score[x]
        #updatin total team's
        total+=score[x]
        scoreFreq[x] += 1
        scoreMap[x]+=score[x]
        balls -= 1
    batsmans[s]=curr_playing_batsman[s]
    if (tballs - balls) % 6 == 6:  # if c is 6, it means the over is complete
        s,ns=strikeRotate(s,ns,x)
        bowler_input_done = False
        over_count += 1  # increment the over count
    print(batsmans)
    print(curr_playing_batsman)
    print(total)
    print(scoreMap)
    print(scoreFreq)


'''print(total)
        print(scoreMap)
        print(scoreFreq)
        print(wicketFreq)
        print("balls",balls)'''

