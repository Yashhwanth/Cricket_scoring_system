overs=int(input("no of overs to be played"))
balls=overs*6
over_count=0
tballs=balls
batsmans={}
bowlers={}

bowlsmap={"0":0,"1":0,"2":0,"3":0,"4":0,"5":0,"6":0,"wb":0,"nb":1,"db":0,"wk":0,"by":0,"lb":0}
score={"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"wb":1,"nb":1,"db":0,"wk":0,"by":0,"lb":0,"stm":0}
scoreFreq={"0":0,"1":0,"2":0,"3":0,"4":0,"5":0,"6":0,"wb":0,"nb":0,"db":0,"wk":0,"by":0,"lb":0,"rtd":0}
wicketsMap={"b":"bowled","c":"caught","lbw":"lbw","c&b":"caught&bowled","ro":"runout","stm":"stumped","hw":"hitwicket","hb":"handled the ball","obs":"obstructing the feild","to":"timedout","rtdo":"retired out"}
wicketFreq={"b":0,"c":0,"lbw":0,"c&b":0,"ro":0,"stm":0,"hw":0,"hb":0,"obs":0,"to":0,"rtdo":0}
scoreMap={"0":0,"1":0,"2":0,"3":0,"4":0,"5":0,"6":0,"wk":0,"wb":0,"nb":0,"by":0,"lb":0,"rtd":0,"db":0}
#batsmanMap={"0":0,"1":0,"2":0,"3":0,"4":0,"5":0,"6":0}
total=0
wickets=0
extras=0
s=input("striker")
ns=input("non-striker")
playing_batsman={s:{"score":0,"balls":0,"0":0,"1":0,"2":0,"3":0,"4":0,"5":0,"6":0},ns:{"score":0,"balls":0,"0":0,"1":0,"2":0,"3":0,"4":0,"5":0,"6":0}}
bastman_reset={"balls":0,"0":0,"1":0,"2":0,"3":0,"4":0,"5":0,"6":0}
bowler_name = None
bowler_input_done = False
def handle_run_out():
    pass
def normal_dismissal(a):
    pass
def strikeRotate(s,ns,runs):
    if int(runs)%2!=0:
        return ns,s
    return s,ns
def inputScenario(a): # function to get the scenario present in corr. maps
    while a not in score:
        a = input("re enter")
    return a
def wicketornot(x,b):
    if (x=="wb") and (b=="stm" or b=="ro" or b=="obs" or b=="hw"): #in wide, these 4 cases are only out
        return True
    if (x=="nb") and (b=="ro" or b=="obs" or b=="hw"): # in nb these 3 cases are out
        return True
    if x=="fh" and (b=="ro" or b=="obs" or b=="hw"): # in fh these 3cases are out
        return True
    return False
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
    if x=="wb" or x=="nb":
        extra_in_wide = input("enter extra scenario")
        extra_runs = inputScenario(extra_in_wide) # extra runs in wide ball
        s,ns=strikeRotate(s,ns,extra_runs)
        scoreFreq[x] += 1  # update score freq
        scoreFreq[extra_runs] += 1  # update score freq
        total += score[extra_runs] + score[x]  # update total
        scoreMap[x] += score[x] + score[extra_runs]  # update score map
        bowlers[bowler_name][x] += 1
        bowlers[bowler_name][extra_runs]+=1
        bowlers[bowler_name]["runs"] += score[x]+score[extra_runs]
        extras+=score[x]+score[extra_runs]
        print(total)
        print(scoreMap)
        print(scoreFreq)
        print(wicketFreq)
        print("balls", balls)
        print(curr_playing_batsman)
        print(bowler_name,":",bowlers[bowler_name])
        print(extras)
    elif x=="by" or x=="lb":
        extra_runs=input("enter runs in by or legbyes")
        scoreFreq[x] += 1  # update score freq
        scoreFreq[extra_runs] += 1  # update score freq
        total += score[extra_runs] + score[x]  # update total
        scoreMap[x] += score[x] + score[extra_runs]  # update score map
        extras+=score[x]+score[extra_runs]
        balls-=1
        s,ns=strikeRotate(s,ns,extra_runs)
    elif x=="db":
        bowlers[bowler_name][x]+=1
        scoreFreq[x]+=1
    elif x=="wk":
        typeofw=input("type of dis")
        scenario_while_wicket=input("enter runs while wicket")
        total += score[x]+score[scenario_while_wicket]
        scoreFreq[x] += 1
        scoreMap[x]+=score[x]
        wicketFreq[typeofw] += 1
        balls-=1
    else: # from 1-6
        #updatin batsman's
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
    if (tballs - balls) % 6 == 0:  # if c is 6, it means the over is complete
        s,ns=strikeRotate(s,ns,x)
        bowler_input_done = False
        #print(s,ns)
        #print(curr_playing_batsman)
        over_count += 1  # increment the over count


'''print(total)
        print(scoreMap)
        print(scoreFreq)
        print(wicketFreq)
        print("balls",balls)'''

