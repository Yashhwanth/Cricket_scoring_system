import copy
match_stack = []
def stats_comaprison(match_stack):
    first_innings=match_stack[0]
    second_innings=match_stack[1]
    f_score=first_innings["total"]
    s_score=second_innings["total"]
    if f_score>s_score:
        print("team a")
    else:
        print("team b")

def innings(is_innings_done=False,target=float('inf'),target_balls=None):
    #is_innings_done=False
    overs = int(input("no of overs to be played"))
    balls = overs * 6
    if is_innings_done==False:
        target_balls = balls
    else:
        target_balls = target_balls
    print(is_innings_done,target,target_balls)
    is_innings_done=False
    tballs = balls
    played_balls=0
    over_count = 0
    total = 0
    wickets = 0
    extras = 0
    overs_runs = 0
    curr_runs = 0
    batsmans = {}
    # batsmanMap={"0":0,"1":0,"2":0,"3":0,"4":0,"5":0,"6":0}
    bastman_reset = {"score": 0, "balls": 0, "diss": "", "0": 0, "1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0}
    s = input("striker")
    ns = input("non-striker")
    batsmans[s] = bastman_reset
    batsmans[ns] = bastman_reset
    playing_batsman = {s: {"score": 0, "balls": 0, "0": 0, "1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0},
                       ns: {"score": 0, "balls": 0, "0": 0, "1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0}}

    partnerships = {}

    bowlers = {}
    bowler_name = None
    bowler_input_done = False

    bowlsmap = {"0": 0, "1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "wb": 0, "nb": 1, "db": 0, "wk": 0, "by": 0,
                "lb": 0}

    score = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "wb": 1, "nb": 1, "db": 0, "wk": 0, "by": 0,
             "lb": 0, "stm": 0, "declare": 0, "undo": 0}
    scoreMap = {"0": 0, "1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "wk": 0, "wb": 0, "nb": 0, "by": 0, "lb": 0,
                "rtd": 0, "db": 0}
    scoreFreq = {"0": 0, "1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "wb": 0, "nb": 0, "db": 0, "wk": 0, "by": 0,
                 "lb": 0, "rtd": 0}

    wicketsMap = {"b": "bowled", "c": "caught", "lbw": "lbw", "c&b": "caught&bowled", "ro": "runout", "stm": "stumped",
                  "hw": "hitwicket", "hb": "handled the ball", "obs": "obstructing the feild", "to": "timedout",
                  "rtdo": "retired out"}
    wicketFreq = {"b": 0, "c": 0, "lbw": 0, "c&b": 0, "ro": 0, "stm": 0, "hw": 0, "hb": 0, "obs": 0, "to": 0, "rtdo": 0}

    # Stack to store the state after each ball
    state_stack = []
    def other_players():
        while True:
            add=input("still add")
            if add=="y":
                player=input("enter player's name")
                batsmans[player] = bastman_reset
            else:
                break
    def save_state():
        #state_stack
        state = {
            "played_balls":played_balls,
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

    def undo_last_ball():
        print("hhii")
        if state_stack:
            last_state = state_stack.pop()
            # Restore the state
            nonlocal balls, tballs, over_count, total, wickets, extras, overs_runs, curr_runs
            nonlocal batsmans, playing_batsman, partnerships, bowlers, bowler_name, bowler_input_done
            nonlocal bowlsmap, score, scoreMap, scoreFreq, wicketsMap, wicketFreq

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

    def update_partnership(striker, non_striker, runs, score, partnerships, type_of_ball="0"):
        key = tuple(sorted((striker, non_striker)))
        # Initialize the partnership if it doesn't exist
        if key not in partnerships:
            partnerships[key] = 0
        # Update the partnership score
        partnerships[key] += score[runs] + score[type_of_ball]
        return partnerships

    def striker_resetting(out_batsman, out_end, s, ns, curr_playing_batsman, partnerships, batsmans, bastman_reset):
        # global s,ns,curr_playing_batsman,partnerships
        del curr_playing_batsman[out_batsman]
        new_batsman_name = input("Enter the new batsman's name: ")
        if new_batsman_name=="nomore":
            nonlocal is_innings_done
            is_innings_done = True
            nonlocal target_balls
            target_balls=overs*6
            save_state()
            innings_end()
        else:
            batsmans[new_batsman_name] = bastman_reset
            curr_playing_batsman[new_batsman_name] = {"score": 0, "balls": 0, "0": 0, "1": 0, "2": 0, "3": 0, "4": 0,
                                                  "5": 0, "6": 0}
        if out_batsman == s:
            if out_end == "s":
                ns = ns
                s = new_batsman_name
            elif out_end == "ns":
                s = ns
                ns = new_batsman_name
        if out_batsman == ns:
            if out_end == "s":
                ns = s
                s = new_batsman_name
            elif out_end == "ns":
                s = s
                ns = new_batsman_name
        return s, ns, curr_playing_batsman, batsmans

    def teams_stats_while_wicket(total, scoreFreq, scoreMap, x, extra_runs, type_of_ball):
        # global total,scoreFreq,scoreMap
        total += score[x] + score[extra_runs] + score[type_of_ball]
        scoreFreq[x] += 1
        scoreFreq[extra_runs] += 1
        scoreFreq[type_of_ball] += 1
        scoreMap[extra_runs] += score[extra_runs]
        scoreMap[type_of_ball] += score[type_of_ball]
        return total, scoreFreq, scoreMap

    def strikeRotate(s, ns, runs="1"):
        if int(runs) % 2 != 0:
            return ns, s
        return s, ns

    def inputScenario(a):  # function to get the scenario present in corr. maps
        while a not in score:
            a = input("re enter")
        return a

    def innings_end():
        nonlocal target
        nonlocal is_innings_done
        is_innings_done = True
        target = total + 1
        match_stack.append(state_stack.pop())

    def over_ending(tballs, balls, s, ns, bowler_input_done, over_count, bowlers, bowler_name, total, curr_runs):
        if (tballs - balls) % 6 == 5:
            s, ns = strikeRotate(s, ns)
            bowler_input_done = False
            over_count += 1
            bowlers, bowler_name, total, curr_runs = maiden_or_not(bowlers, bowler_name, total, curr_runs)
        return s, ns, bowler_input_done, over_count, bowlers, bowler_name, total, curr_runs

    def maiden_or_not(bowlers, bowler_name, total, curr_runs):
        if curr_runs == 0:
            bowlers[bowler_name]["maidens"] += 1
        return bowlers, bowler_name, total, curr_runs
    print(target_balls)
    while target_balls and not is_innings_done and total<target: #if there is a ball it has too be bowled
        if (tballs - balls) % 6 == 0 and not bowler_input_done: # Ask for new bowler at the start of each over
            curr_runs=0
            bowler_name = input("Enter bowler's name:")
            if bowler_name not in bowlers:
                bowlers[bowler_name] = {"maidens":0, "balls": 0, "runs": 0,"economy":0, "0": 0, "1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0,"wk": 0, "by": 0, "lb": 0, "wb": 0, "nb": 0, "db": 0}
                bowler_input_done = True
        curr_playing_batsman=playing_batsman
        c=(tballs-balls)%6+1 # just to ask input score for each ball
        save_state()
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
            #bowlers[bowler_name]["runs"] += score[x] + score[extra_runs]
            total += score[extra_runs] + score[x]  # update total
            curr_runs += score[extra_runs] + score[x]
            scoreFreq[x] += 1  # update score freq
            scoreFreq[extra_runs] += 1  # update score freq
            scoreMap[x] += score[x] + score[extra_runs]  # update score map
            extras+=score[x]+score[extra_runs]
            s,ns,bowler_input_done,over_count,bowlers,bowler_name,total,curr_runs=over_ending(tballs, balls,s,ns, bowler_input_done, over_count,bowlers,bowler_name,total,curr_runs)
            balls-=1
            target_balls-=1
            played_balls+=1
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
                s, ns, curr_playing_batsman, batsmans = striker_resetting(out_batsman, out_end, s, ns,
                                                                          curr_playing_batsman, partnerships, batsmans,
                                                                          bastman_reset)
                wicketFreq[type_of_w]+=1
            elif type_of_ball=="wb":
                #curr_playing_batsman[s]["balls"] += 1
                # curr_playing_batsman[s][extra_runs] += 1
                #curr_playing_batsman[s]["score"] += score[x]
                batsmans[s] = curr_playing_batsman[s]
                batsmans[out_batsman] = curr_playing_batsman[out_batsman]
                partnerships = update_partnership(s, ns, extra_runs, score, partnerships, type_of_ball)

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
                s, ns, curr_playing_batsman, batsmans = striker_resetting(out_batsman, out_end, s, ns,
                                                                          curr_playing_batsman, partnerships, batsmans,
                                                                          bastman_reset)
                wicketFreq[type_of_w] += 1
            elif type_of_ball=="lb" or type_of_ball=="by":
                curr_playing_batsman[s]["balls"] += 1
                # curr_playing_batsman[s][extra_runs] += 1
                # curr_playing_batsman[s]["score"] += score[x]
                batsmans[s] = curr_playing_batsman[s]
                batsmans[out_batsman] = curr_playing_batsman[out_batsman]
                partnerships = update_partnership(s, ns, extra_runs, score, partnerships, type_of_ball)

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
                played_balls+=1
                s, ns, curr_playing_batsman, batsmans = striker_resetting(out_batsman, out_end, s, ns,
                                                                          curr_playing_batsman, partnerships, batsmans,
                                                                          bastman_reset)
                s,ns,bowler_input_done,over_count,bowlers,bowler_name,total,curr_runs=over_ending(tballs, balls,s,ns, bowler_input_done, over_count,bowlers,bowler_name,total,curr_runs)
                balls -= 1
                target_balls -= 1
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
                #s,ns,curr_playing_batsman,batsmans=striker_resetting(out_batsman, out_end,s,ns,curr_playing_batsman,partnerships,batsmans,bastman_reset)
                #partnerships=update_partnership(s,ns,extra_runs,score,partnerships,type_of_ball)
                if type_of_w!="ro":
                    bowlers[bowler_name][x] += 1
                bowlers[bowler_name]["balls"] += 1
                bowlers[bowler_name][extra_runs] += 1
                bowlers[bowler_name][type_of_ball] += 1
                bowlers[bowler_name]["runs"] += score[x] + score[extra_runs] + score[type_of_ball]
                # teams
                total,scoreFreq,scoreMap=teams_stats_while_wicket(total,scoreFreq,scoreMap,x, extra_runs, type_of_ball)
                curr_runs += score[extra_runs] + score[x]
                s, ns, curr_playing_batsman, batsmans = striker_resetting(out_batsman, out_end, s, ns,curr_playing_batsman, partnerships, batsmans,bastman_reset)
                s,ns,bowler_input_done,over_count,bowlers,bowler_name,total,curr_runs=over_ending(tballs, balls,s,ns, bowler_input_done, over_count,bowlers,bowler_name,total,curr_runs)
                played_balls+=1
                balls -= 1
                target_balls -= 1
                wicketFreq[type_of_w] += 1
            batsmans[out_batsman]["diss"]=type_of_w
        elif x == "declare":
            target_balls=played_balls
            innings_end()
            pass
        else:
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
            played_balls+=1
            balls -= 1
            target_balls -= 1
        while True:
            undo=input("undo??")
            if undo=="y":
                undo_last_ball()
            else:
                break
        if balls==0:
            target_balls=overs*6
            other_players()
            save_state()
            innings_end()
        if total>=target or target_balls==0:
            other_players()
            save_state()
            match_stack.append(state_stack.pop())
    return is_innings_done,target,target_balls
is_innings_done,target,target_balls=innings()
print(innings(is_innings_done,target,target_balls))
stats_comaprison(match_stack)
print(match_stack)
