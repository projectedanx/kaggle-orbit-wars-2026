> Source: https://www.kaggle.com/code/pawanmali/10-agents-walked-into-orbit-wars

10 Agents Walked Into Orbit Wars
menu
Skip to content
Create
search
explore Home
emoji_events Competitions
table_chart Datasets
tenancy Models
leaderboard Benchmarks
smart_toy Game Arena
code Code
comment Discussions
school Learn
expand_more More
menu
Skip to content
search
Sign In
Register
Kaggle uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic.
Learn more
OK, Got it. 
Pawan Rama Mali
· 1d ago
· 139 views
more_vert
10 Agents Walked Into Orbit Wars
Copy & Edit
4
file_download Download
arrow_drop_up 7 
10 Agents Walked Into Orbit Wars
Notebook Input Output Logs Comments (0)
menu_open 
Competition Notebook
Orbit Wars
Runtime
play_arrow
18s
history Version 1 of 1
Input
COMPETITIONS 
Orbit Wars
Language
Python
expand_more View Metadata
link code
10 Agents Walked Into Orbit Wars (Devlog) ¶
Three days, ten versions, one embarrassing learning curve. This is what each version got right, what each one broke, and the numbers behind both.
I started at 643 (lead-intercept sniper, vanilla ROI). Peaked at 787 with v11. Bounced around 600 since then. Along the way I watched a pile of public winning games from higher-rated agents and played my own versions against each other a lot. Four of the "this should obviously work" ideas turned out to make things worse.
If you're stuck somewhere between 600 and 900 and you're not sure why, this is the notebook I wish I'd had on day one.
link code
The scoreboard ¶
Scores drift as the pool evolves. My 787 peak at v11 was against an earlier pool; today v11 re-scores around 605 against the same arena that scores v14 at 600. So the absolute numbers matter less than the deltas.
The pattern I notice, looking back: every gain came from either reading the env source or adopting a pattern I saw working near the top of the leaderboard. Every regression came from believing a clever idea of my own.
link code
v1 - Lead-Intercept Sniper (643) ¶
First working version. Predict where orbital planets will be when a fleet arrives (you have to lead them like a moving target, otherwise most shots miss). Reject any ray that crosses the sun. Pick one best ROI target per source per turn. Keep some ships home if enemy fleets are incoming.
Lead-intercept alone kept me above most starter kernels that just aim at the target's current position and miss rotating inner planets. But capping at one launch per source per turn meant a lot of cheap neutrals sat there untaken while my planets hoarded ships for "the best shot."
link code
v2 - Forecast + Real Combat Sim (720, +77) ¶
v1 was approximating combat with heuristic costs. v2 replaced that with the actual rules the engine uses: top attacker fights second, ties annihilate both, third-and-lower attackers just vanish. Binary-search the minimum ships I need to add for my fleet to end up owning the planet.
Then forecast every planet 60 turns forward - production tick, then any arrivals, resolve combat, repeat - so I know which of my planets are in trouble and what enemy garrisons will look like when my own fleets arrive.
Also went from "best launch per source" to a global candidate list sorted by value / (cost * distance_penalty) . Each turn I could now take the top-N captures, not just one per source.
The 77-point jump was entirely about not approximating something I could model exactly.
link code
v3 - I finally read the source (721, early peak) ¶
I spent an afternoon reading kaggle_environments/envs/orbit_wars/orbit_wars.py end to end. It's not long, and almost every page changed something in my agent that I'd been getting subtly wrong.
Eight things I fixed, in no particular order:
Orbital planets use initial_angle + angular_velocity * step - absolute, not accumulated from last frame. Once I tracked step directly, predictions got much more stable.
Bigger fleets move faster (speed curve is log-scaled), so travel time depends on ship count, which depends on enemy production during travel, which depends on travel time. I wrote a fixed-point loop over (cost, turns) that iterates until it converges.
The engine breaks out of the planet-collision loop on the first planet along your ray, not the closest. If there's another planet sitting between you and your target, your fleet hits that instead. Started rejecting those shots.
Comets have pre-materialized paths. Instead of lead-intercepting based on angular velocity I just read the future position out of comets.paths[i][path_index + turns] .
New comets spawn at (-99, -99) for exactly one turn before their first path step. Targeting them in that window sends your fleet off the board.
Sun padding - I'd been using 0.75 to be safe. The engine uses SUN_RADIUS flat with no pad of its own, so 0.3 is plenty and clears more legitimate shots.
In the last ~30 turns I skip attacks that won't land before episode end.
Third-attacker avoidance: if the arrivals already have a stronger top-2 than I can beat, my ships vanish - better to just not launch.
Took me from 720 to 721. Not a big jump but it killed a whole class of silent misses I'd been making.
link code
v4 - The Retention Model That Cost Me 88 Points ¶
I noticed my agent kept undershooting enemy captures. My cost estimation assumed enemies would keep every ship they produced during my travel time. They obviously don't - they launch some of those ships too. So I added a retention factor: enemies keep 40% of produced ships, spend 60%.
Self-play against v3: won 58% of games. I was excited.
Kaggle: 721 -> 633. The biggest single regression of the run.
What happened is pretty obvious in retrospect. v4 was good at predicting v3's behaviour because I designed the retention factor by watching v3 play. The Kaggle pool isn't just v3 - it's hundreds of opponents with very different patterns. My model was over-fit to one of them and mispredicted everybody else.
This is the lesson I'd tattoo on my forearm if I could: self-play is not a leaderboard predictor. It's easy to forget because the numbers feel so concrete.
link code
v5 - Bigger Beachheads (682) ¶
Different angle on the same problem. Instead of estimating enemy production better, just send more ships so captured planets can survive the inevitable counter-punch.
Partial recovery - 682, up from 633 but still short of v3's 721. Bigger fleets move slower (the speed curve flattens above ~1000 ships), so over-sending wastes ship-turns that could've opened a second front. Turns out "just send more" has its own ceiling.
link code
v6 - FLEET_CAP from Public Replays (639, another -82) ¶
Started watching public replays of higher-scoring agents. First thing that jumped out: the vast majority of their launches are under 100 ships. Median around 18. Nobody was sending 500-ship fleets. So I capped mine.
Self-play: mixed results, beats some of my versions, loses to others. Kaggle: 682 -> 639. Another regression.
What I missed: the replays I was averaging over included both 2-player and 4-player matches. In 4-player matches, small fleets make sense (each player has fewer planets and contested fronts). In 2-player matches - which the arena runs more often - winners sometimes send a huge fleet at a single key capture. A blanket cap breaks those captures.
Aggregate stats hide their sampling. Check the distribution, not the mean.
link code
v9 - The Collapse-Point Fix (615) ¶
I was losing games to simple opponents in weird ways, so I dumped the ship count and planet count every 25 turns and just eyeballed the trajectory.
One game stood out: v6 vs v1 on a specific seed. At turn 75 I had 9 planets and was ahead. By turn 125 I had 4. Where did they go?
It was the reserves. v6 kept 1 ship at each planet when launching. The opponent was sending 2-ship probes at what looked like empty planets and flipping them trivially. Classic "you're ahead until you're not."
Proportional reserves - a prod-5 planet keeps 15, a prod-1 keeps 3. Solved the collapse. Didn't solve the underlying score (615, still flat), but it stopped the midgame implosions that were eating into the win rate.
When an agent suddenly flips from winning to losing, the cause is almost always one specific turn. Tracing state over time is how you find it.
link code
v11 - The Measured-Style Rewrite (787, peak) ¶
This is the one that actually worked. I observed some humbling contrasts between my agent's launch patterns and what I was seeing in public replays of higher-scoring agents:
I was launching more than ten times as often as the higher-scoring agents. Spraying tiny fleets while they were sending fewer, larger, more consolidated ones. No wonder I kept getting out-accumulated.
v11 adopted the measured style: hard cap of 2 offensive launches per turn, skip everything below a minimum ROI, run defensive reinforcement before the offensive allocator instead of after.
615 -> 787. Biggest single-version jump of the project.
My intuition going in was "more launches = more pressure = better." That intuition is wrong for this game. The top of the pool rewards patience and consolidation far more than constant skirmishing.
link code
v13 - The Target-Mix Rebalance That Backfired (578) ¶
Once I had the mix tool I looked at where the winning launches went on average. The higher-scoring agents I tracked were splitting roughly 33% at enemy planets, 27% at neutrals, 41% at their own planets (defence + moving ships around). Mine was 57/19/24 - way more aggressive, way less logistics.
So in v13 I removed the enemy-denial bonus, boosted neutral value a bit, and added a rear-to-frontline transfer pass so rearward planets could ship idle garrisons up to the fighting line.
Self-play vs v11: roughly tied, 50/50. Kaggle: 787 -> 578. Another expensive surprise.
My best guess for what went wrong: that 41% self-target figure gets inflated by 4-player games - more fronts, more need to move ships between your own planets. On a 2-player map (which the arena picks more often), direct attacks are higher-ROI than shuffling ships behind your own lines. The average hid a distribution.
Stats don't travel between game modes. Always check what game count the sample is drawn from before porting a behaviour.
link code
v14 - Four Data-Backed Tweaks (600, current) ¶
After v13 blew up I went back to the replays and did a more careful pass. I picked the four patterns with the tightest agreement across the top-4 players and kept the rest out.
Early-game neutral filter: penalize prod-1/2 neutrals in the first 20 turns since winners almost never open on them.
Expansion-pressure check: if I'm behind on planet count at t=50 or production at t=100, bump neutral values by 1.5x.
Fleet size scales with target production - prod-5 neutrals get 1.25x ships, prod-4 get 1.12x.
A value bonus on high-production neutrals so they win close scoring ties.
Best part: this is the first version of mine to beat the simple v1-style accumulator over 50% of the time in self-play (54%, v11 was 46%, v13 was 38%). That's a real crack in the anti-accumulator problem that was eating me alive.
Kaggle score is flat at 600 though. Close to v11's current 605. The direction is right; individual magnitudes still need work.
link code
Five things I'd tell day-one me ¶
Read the env source first. Writing an agent without reading the environment is guessing. orbit_wars.py is short. Everything you need to know about combat ordering, sun collision, comet paths, and orbit math is there.
Self-play is not a leaderboard test. v4 beat v3 58% in self-play and scored 88 points lower. v13 tied v11 in self-play and scored 200 points lower. The reason is obvious but the numbers are seductive: you get a specific high-fidelity measurement against one opponent and it feels more trustworthy than the noisy Kaggle arena. It isn't. Use self-play for sanity checks - does this new version crash, does it beat the starter kernel - not for promotion decisions.
Watch a few games from the top of the leaderboard. Public replays are public. Pull up a handful of winning matches from agents above your current score and a few of their losses too. Count the launches per turn. Check the fleet sizes. Note where the early attacks go. You'll see the patterns faster than you can invent them.
Trace state over time when the agent regresses. Dump (turn, my_planets, my_ships, opp_planets, opp_ships) every 25 steps and squint at the trajectory. Every mid-game collapse I saw traced back to a specific turn where something simple and exploitable was happening (for v6, it was 1-ship reserves). You can't debug what you can't see.
Measure the distribution, not the mean. Aggregate "higher-scoring agents cap at 60 ships" was wrong - the distribution had a long tail of big fleets for key captures. "41% self-target launches" was wrong for 2-player. Any time you pull a single number out of an aggregate, ask what the spread looks like and which samples contributed.
link code
The patterns I kept coming back to ¶
After enough replays I stopped tracking new things and just kept referring back to the same handful of numbers. These are the ones worth the time. By "consistency" I just mean how tightly the higher-scoring agents seemed to agree on a given value - tight agreement felt safer to adopt than one outlier.
High-consistency (the ones I trust most)
Medium-consistency (useful, watch the sample)
Style-dependent (both extremes win)
Two distinct styles both seem to work near the top:
Measured: around 70 launches per game, mid-size fleets, minimal swarming, lots of saving. Volume: around 250 launches per game, tiny fleets, constant pressure.
Both get to 1000+. What doesn't work is sitting between them - spraying small fleets without the coordinated volume to back it up. That's what my v1 through v10 were doing, and it shows in the scores.
link code
Things I couldn't crack ¶
If you've figured any of these out I'd love to hear about it:
Lightweight forward search. Top kernels at 1000+ seem to do some kind of rollout inside the 1s act budget. What's the cheapest depth that actually helps?
Opponent classification. Is the other agent accumulating or racing? A simple classifier on their first 50 turns could switch my strategy mode - hasn't worked cleanly for me.
Multi-source synchronised arrivals that actually hit. I tried tuning fleet sizes so two sources arrive the same turn. Breaks for orbital targets because the intercept point shifts with fleet size. The clean solution is eluding me.
Structural anti-accumulator play. v14 gets to 54% vs a v1-style stockpiler, which feels like a reactive ceiling. Is there a cleaner way than just matching their accumulation rate?
2-player vs 4-player detection. The two configurations reward quite different behaviour and my agent doesn't distinguish. Is it worth the complexity?
link code
Wrap-up ¶
Most of this agent's progress wasn't clever. It was sitting down and actually reading the env source, actually watching winning games, and actually admitting when one of my "improvements" had regressed. Every time I built on data I made progress. Every time I built on intuition I paid for it.
If I had to pick one thing to start with, I'd pull up orbit_wars.py and read it cover to cover before writing a single heuristic.
Thanks for reading. Questions and counter-experiences welcome in the comments.
License
This Notebook has been released under the Apache 2.0 open source license.
Continue exploring
Input 1 file arrow_right_alt
Output 0 files arrow_right_alt
Logs 18.3 second run - successful arrow_right_alt
Comments 0 comments arrow_right_alt