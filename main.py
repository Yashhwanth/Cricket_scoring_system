import copy
overs = int(input("no of overs to be played"))
balls=overs*6
tballs=balls
over_count=0
total=0
wickets=0
extras=0
overs_runs=0
curr_runs=0

batsmans={}
#batsmanMap={"0":0,"1":0,"2":0,"3":0,"4":0,"5":0,"6":0}
bastman_reset={"score":0,"balls":0,"diss":"","0":0,"1":0,"2":0,"3":0,"4":0,"5":0,"6":0}
s=input("striker")
ns=input("non-striker")
batsmans[s]=bastman_reset
batsmans[ns]=bastman_reset
playing_batsman={s:{"score":0,"balls":0,"0":0,"1":0,"2":0,"3":0,"4":0,"5":0,"6":0},ns:{"score":0,"balls":0,"0":0,"1":0,"2":0,"3":0,"4":0,"5":0,"6":0}}

partnerships={}

bowlers={}
bowler_name = None
bowler_input_done = False
bowlsmap={"0":0,"1":0,"2":0,"3":0,"4":0,"5":0,"6":0,"wb":0,"nb":1,"db":0,"wk":0,"by":0,"lb":0}

score={"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"wb":1,"nb":1,"db":0,"wk":0,"by":0,"lb":0,"stm":0}
scoreMap={"0":0,"1":0,"2":0,"3":0,"4":0,"5":0,"6":0,"wk":0,"wb":0,"nb":0,"by":0,"lb":0,"rtd":0,"db":0}
scoreFreq={"0":0,"1":0,"2":0,"3":0,"4":0,"5":0,"6":0,"wb":0,"nb":0,"db":0,"wk":0,"by":0,"lb":0,"rtd":0}

wicketsMap={"b":"bowled","c":"caught","lbw":"lbw","c&b":"caught&bowled","ro":"runout","stm":"stumped","hw":"hitwicket","hb":"handled the ball","obs":"obstructing the feild","to":"timedout","rtdo":"retired out"}
wicketFreq={"b":0,"c":0,"lbw":0,"c&b":0,"ro":0,"stm":0,"hw":0,"hb":0,"obs":0,"to":0,"rtdo":0}

# Stack to store the state after each ball
state_stack = []

# Function to capture the current state
def save_state():
    state = {
        "balls": balls,
        "tballs": tballs,
        "over_count": over_count,
        "total": total,
        "wickets": wickets,
        "extras": extras,
        "overs_runs": overs_runs,
        "curr_runs": curr_runs,
        "batsmans": copy.deepcopy(batsmans),
        "playing_batsman": copy.deepcopy(playing_batsman),
        "partnerships": copy.deepcopy(partnerships),
        "bowlers": copy.deepcopy(bowlers),
        "bowler_name": bowler_name,
        "bowler_input_done": bowler_input_done,
        "bowlsmap": copy.deepcopy(bowlsmap),
        "score": copy.deepcopy(score),
        "scoreMap": copy.deepcopy(scoreMap),
        "scoreFreq": copy.deepcopy(scoreFreq),
        "wicketsMap": copy.deepcopy(wicketsMap),
        "wicketFreq": copy.deepcopy(wicketFreq)
    }
    state_stack.append(state)

# Function to undo the last ball
def undo_last_ball():
    if state_stack:
        last_state = state_stack.pop()
        # Restore the state
        global balls, tballs, over_count, total, wickets, extras, overs_runs, curr_runs
        global batsmans, playing_batsman, partnerships, bowlers, bowler_name, bowler_input_done
        global bowlsmap, score, scoreMap, scoreFreq, wicketsMap, wicketFreq

        balls = last_state["balls"]
        tballs = last_state["tballs"]
        over_count = last_state["over_count"]
        total = last_state["total"]
        wickets = last_state["wickets"]
        extras = last_state["extras"]
        overs_runs = last_state["overs_runs"]
        curr_runs = last_state["curr_runs"]
        batsmans = last_state["batsmans"]
        playing_batsman = last_state["playing_batsman"]
        partnerships = last_state["partnerships"]
        bowlers = last_state["bowlers"]
        bowler_name = last_state["bowler_name"]
        bowler_input_done = last_state["bowler_input_done"]
        bowlsmap = last_state["bowlsmap"]
        score = last_state["score"]
        scoreMap = last_state["scoreMap"]
        scoreFreq = last_state["scoreFreq"]
        wicketsMap = last_state["wicketsMap"]
        wicketFreq = last_state["wicketFreq"]

        print("Last ball undone successfully!")
    else:
        print("No more actions to undo!")

def update_partnership(striker, non_striker, runs, score, partnerships,type_of_ball="0"):
    key = tuple(sorted((striker, non_striker)))
    # Initialize the partnership if it doesn't exist
    if key not in partnerships:
        partnerships[key] = 0
    # Update the partnership score
    partnerships[key] += score[runs]+score[type_of_ball]
    return partnerships
def striker_resetting(out_batsman,out_end,s,ns,curr_playing_batsman,partnerships,batsmans,bastman_reset):
    #global s,ns,curr_playing_batsman,partnerships
    del curr_playing_batsman[out_batsman]
    new_batsman_name = input("Enter the new batsman's name: ")
    batsmans[new_batsman_name]=bastman_reset
    curr_playing_batsman[new_batsman_name] = {"score":0,"balls": 0, "0": 0, "1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0}
    if out_batsman==s:
        if out_end=="s":
            ns=ns
            s = new_batsman_name
        elif out_end=="ns":
            s=ns
            ns = new_batsman_name
    if out_batsman==ns:
        if out_end=="s":
            ns=s
            s = new_batsman_name
        elif out_end=="ns":
            s=s
            ns = new_batsman_name
    return s,ns,curr_playing_batsman,batsmans
def teams_stats_while_wicket(total,scoreFreq,scoreMap,x,extra_runs,type_of_ball):
    #global total,scoreFreq,scoreMap
    total += score[x] + score[extra_runs] + score[type_of_ball]
    scoreFreq[x] += 1
    scoreFreq[extra_runs] += 1
    scoreFreq[type_of_ball] += 1
    scoreMap[extra_runs] += score[extra_runs]
    scoreMap[type_of_ball] += score[type_of_ball]
    return total,scoreFreq,scoreMap
def strikeRotate(s,ns,runs="1"):
    if int(runs)%2!=0:
        return ns,s
    return s,ns
def inputScenario(a): # function to get the scenario present in corr. maps
    while a not in score:
        a = input("re enter")
    return a
def over_ending(tballs,balls,s,ns,bowler_input_done,over_count,bowlers,bowler_name,total,curr_runs):
    if (tballs - balls)%6==5:
        s, ns = strikeRotate(s, ns)
        bowler_input_done = False
        over_count += 1
        bowlers, bowler_name, total, curr_runs=maiden_or_not(bowlers,bowler_name,total,curr_runs)
    return s,ns,bowler_input_done,over_count,bowlers,bowler_name,total,curr_runs
def maiden_or_not(bowlers,bowler_name,total,curr_runs):
    if curr_runs==0:
        bowlers[bowler_name]["maidens"]+=1
    return bowlers,bowler_name,total,curr_runs
while balls: #if there is a ball it has too be bowled
    save_state()
    #print((tballs - balls) % 6)
    if (tballs - balls) % 6 == 0 and not bowler_input_done: # Ask for new bowler at the start of each over
        curr_runs=0
        bowler_name = input("Enter bowler's name:")
        if bowler_name not in bowlers:
            bowlers[bowler_name] = {"maidens":0, "balls": 0, "runs": 0,"economy":0, "0": 0, "1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0,"wk": 0, "by": 0, "lb": 0, "wb": 0, "nb": 0, "db": 0}
            bowler_input_done = True
    curr_playing_batsman=playing_batsman
    c=(tballs-balls)%6+1 # just to ask input score for each ball
    inputscene=input("enter score of {} ball".format((tballs-balls)%6+1)) #scenaio when ball is bowled
    x=inputScenario(inputscene) # to get correct scenario
    if x=="wb":
        extra_in_wide = input("enter extra scenario")
        extra_runs = inputScenario(extra_in_wide) # extra runs in wide ball
        batsmans[s] = curr_playing_batsman[s]
        s,ns=strikeRotate(s,ns,extra_runs)
        bowlers[bowler_name][x] += 1
        bowlers[bowler_name][extra_runs] += 1
        bowlers[bowler_name]["runs"] += score[x] + score[extra_runs]
        total += score[extra_runs] + score[x]  # update total
        curr_runs+=score[extra_runs] + score[x]
        scoreFreq[x] += 1  # update score freq
        scoreFreq[extra_runs] += 1  # update score freq
        scoreMap[x] += score[x] + score[extra_runs]  # update score map
        extras+=score[x]+score[extra_runs]
        partnerships=update_partnership(s,ns,extra_runs,score,partnerships,x)
        save_state()
    elif x=="nb":
        extra_in_wide = input("enter extra scenario")
        extra_runs = inputScenario(extra_in_wide) # extra runs in wide ball
        curr_playing_batsman[s]["score"] += score[extra_runs]
        curr_playing_batsman[s][extra_runs] += 1
        batsmans[s] = curr_playing_batsman[s]
        s, ns = strikeRotate(s, ns, extra_runs)
        bowlers[bowler_name][x] += 1
        bowlers[bowler_name][extra_runs] += 1
        bowlers[bowler_name]["runs"] += score[x] + score[extra_runs]
        total += score[extra_runs] + score[x]  # update total
        curr_runs += score[extra_runs] + score[x]
        scoreFreq[x] += 1  # update score freq
        scoreFreq[extra_runs] += 1  # update score freq
        scoreMap[x] += score[x] + score[extra_runs]  # update score map
        extras+=score[x]+score[extra_runs]
        partnerships=update_partnership(s,ns,extra_runs,score,partnerships,x)
    elif x=="db":
        bowlers[bowler_name][x]+=1
        scoreFreq[x]+=1
    elif x=="by" or x=="lb":
        extra_runs=input("enter runs in by or legbyes")
        curr_playing_batsman[s]["balls"] += 1
        batsmans[s] = curr_playing_batsman[s]
        s, ns = strikeRotate(s, ns, extra_runs)
        bowlers[bowler_name][x] += 1
        #bowlers[bowler_name][extra_runs] += 1
        bowlers[bowler_name]["balls"]+=1
        bowlers[bowler_name]["runs"] += score[x] + score[extra_runs]
        total += score[extra_runs] + score[x]  # update total
        curr_runs += score[extra_runs] + score[x]
        scoreFreq[x] += 1  # update score freq
        scoreFreq[extra_runs] += 1  # update score freq
        scoreMap[x] += score[x] + score[extra_runs]  # update score map
        extras+=score[x]+score[extra_runs]
        s,ns,bowler_input_done,over_count,bowlers,bowler_name,total,curr_runs=over_ending(tballs, balls,s,ns, bowler_input_done, over_count,bowlers,bowler_name,total,curr_runs)
        balls-=1
        partnerships=update_partnership(s,ns,extra_runs,score,partnerships,x)
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
            batsmans[s] = curr_playing_batsman[s]
            partnerships = update_partnership(s, ns, extra_runs, score, partnerships, type_of_ball)
            s,ns,curr_playing_batsman,batsmans=striker_resetting(out_batsman, out_end,s,ns,curr_playing_batsman,partnerships,batsmans,bastman_reset)
            #partnerships=update_partnership(s,ns,extra_runs,score,partnerships,type_of_ball)


            #bowlers[bowler_name][x] += 1
            #bowlers[bowler_name]["balls"] += 1
            bowlers[bowler_name][extra_runs] += 1
            bowlers[bowler_name][type_of_ball] += 1
            bowlers[bowler_name]["runs"] += score[x] + score[extra_runs]+score[type_of_ball]
            #teams
            total,scoreFreq,scoreMap=teams_stats_while_wicket(total,scoreFreq,scoreMap,x, extra_runs, type_of_ball)
            curr_runs += score[extra_runs] + score[x]
            extras += score[type_of_ball]

            wicketFreq[type_of_w]+=1
        elif type_of_ball=="wb":
            #curr_playing_batsman[s]["balls"] += 1
            # curr_playing_batsman[s][extra_runs] += 1
            #curr_playing_batsman[s]["score"] += score[x]
            batsmans[s] = curr_playing_batsman[s]
            batsmans[out_batsman] = curr_playing_batsman[out_batsman]
            partnerships = update_partnership(s, ns, extra_runs, score, partnerships, type_of_ball)
            s,ns,curr_playing_batsman,batsmans=striker_resetting(out_batsman, out_end,s,ns,curr_playing_batsman,partnerships,batsmans,bastman_reset)
            #partnerships=update_partnership(s,ns,extra_runs,score,partnerships,type_of_ball)
            #bowlers[bowler_name][x] += 1
            #bowlers[bowler_name]["balls"] += 1
            bowlers[bowler_name][extra_runs] += 1
            bowlers[bowler_name][type_of_ball] += 1
            bowlers[bowler_name]["runs"] += score[x] + score[extra_runs] + score[type_of_ball]
            # teams
            total,scoreFreq,scoreMap=teams_stats_while_wicket(total,scoreFreq,scoreMap,x, extra_runs, type_of_ball)
            curr_runs += score[extra_runs] + score[x]
            extras += score[type_of_ball]

            wicketFreq[type_of_w] += 1
        elif type_of_ball=="lb" or type_of_ball=="by":
            curr_playing_batsman[s]["balls"] += 1
            # curr_playing_batsman[s][extra_runs] += 1
            # curr_playing_batsman[s]["score"] += score[x]
            batsmans[s] = curr_playing_batsman[s]
            batsmans[out_batsman] = curr_playing_batsman[out_batsman]
            partnerships = update_partnership(s, ns, extra_runs, score, partnerships, type_of_ball)
            s,ns,curr_playing_batsman,batsmans=striker_resetting(out_batsman, out_end,s,ns,curr_playing_batsman,partnerships,batsmans,bastman_reset)
            #partnerships=update_partnership(s,ns,extra_runs,score,partnerships,type_of_ball)
            #bowlers[bowler_name][x] += 1
            bowlers[bowler_name]["balls"] += 1
            #bowlers[bowler_name][extra_runs] += 1
            bowlers[bowler_name][type_of_ball] += 1
            bowlers[bowler_name]["runs"] += score[x] + score[extra_runs] + score[type_of_ball]
            # teams
            total,scoreFreq,scoreMap=teams_stats_while_wicket(total,scoreFreq,scoreMap,x, extra_runs, type_of_ball)
            curr_runs += score[extra_runs] + score[x]
            extras += score[type_of_ball]
            s,ns,bowler_input_done,over_count,bowlers,bowler_name,total,curr_runs=over_ending(tballs, balls,s,ns, bowler_input_done, over_count,bowlers,bowler_name,total,curr_runs)
            balls -= 1
            wicketFreq[type_of_w] += 1
        else:
            type_of_ball = '0'
            curr_playing_batsman[s]["balls"] += 1
            curr_playing_batsman[s][extra_runs] += 1
            curr_playing_batsman[s]["score"] += score[x] + score[extra_runs]
            batsmans[s] = curr_playing_batsman[s]
            batsmans[out_batsman] = curr_playing_batsman[out_batsman]
            #update_partnership(s, ns, x, extra_runs)
            partnerships = update_partnership(s, ns, extra_runs, score, partnerships, type_of_ball)
            s,ns,curr_playing_batsman,batsmans=striker_resetting(out_batsman, out_end,s,ns,curr_playing_batsman,partnerships,batsmans,bastman_reset)
            #partnerships=update_partnership(s,ns,extra_runs,score,partnerships,type_of_ball)
            bowlers[bowler_name][x] += 1
            bowlers[bowler_name]["balls"] += 1
            bowlers[bowler_name][extra_runs] += 1
            bowlers[bowler_name][type_of_ball] += 1
            bowlers[bowler_name]["runs"] += score[x] + score[extra_runs] + score[type_of_ball]
            # teams
            total,scoreFreq,scoreMap=teams_stats_while_wicket(total,scoreFreq,scoreMap,x, extra_runs, type_of_ball)
            curr_runs += score[extra_runs] + score[x]
            s,ns,bowler_input_done,over_count,bowlers,bowler_name,total,curr_runs=over_ending(tballs, balls,s,ns, bowler_input_done, over_count,bowlers,bowler_name,total,curr_runs)
            balls -= 1
            wicketFreq[type_of_w] += 1
        batsmans[out_batsman]["diss"]=type_of_w
    else :
        curr_playing_batsman[s]["balls"]+=1
        curr_playing_batsman[s]["score"]+=score[x]
        curr_playing_batsman[s][x] += 1
        batsmans[s] = curr_playing_batsman[s]
        partnerships=update_partnership(s,ns,x,score,partnerships)
        s,ns=strikeRotate(s,ns,x)
        #updatin bowler's
        bowlers[bowler_name][x]+=1
        bowlers[bowler_name]["balls"]+=1
        bowlers[bowler_name]["runs"]+=score[x]
        #updatin total team's
        total+=score[x]
        curr_runs += score[x]
        scoreFreq[x] += 1
        scoreMap[x]+=score[x]
        s,ns,bowler_input_done,over_count,bowlers,bowler_name,total,curr_runs=over_ending(tballs, balls,s,ns, bowler_input_done, over_count,bowlers,bowler_name,total,curr_runs)

        balls -= 1
    #print(state_stack)
    print(batsmans)
    #print("score:",total,"/",wickets)
    while True:  # Inner loop for undo functionality
        undo_choice = input("Do you want to undo the last ball? (y/n): ")
        if undo_choice.lower() == 'y':
            undo_last_ball()  # Undo the last ball's stats
            #print("score:", total, "/", wickets)
            print(batsmans)
        else:
            break  # Exit the undo loop if the user doesn't want to undo
    #print("score:", total, "/", wickets)
    print(batsmans)


