> Source: https://www.kaggle.com/code/pilkwang/score-1-000-orbit-wars-structured-baseline/log?scriptVersionId=312720116

🛰 Orbit Wars: Structured Baseline
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
Pilkwang Kim
· 2d ago
· 1,824 views
more_vert
🛰 Orbit Wars: Structured Baseline
Copy & Edit
114
file_download Download
arrow_drop_up 97 
🛰 Orbit Wars: Structured Baseline
Notebook Input Output Logs Comments (1)
menu_open 
Competition Notebook
Orbit Wars
Public Score
875.4
Best Score
911.1 V40
Runtime
play_arrow
41s
history Version 42 of 45
Input
COMPETITIONS 
Orbit Wars
Language
Python
expand_more View Metadata
link code
🛰 Orbit Wars: Structured Baseline ¶
v11: Arrival-Time Ownership, Reinforce-To-Hold, Rescue And Recapture, Swarm Pressure, And Crash Exploits ¶
This notebook follows one decision flow: find a legal direct shot, forecast the target at that arrival time, and spend ships only on missions that still make sense after earlier launches are committed.
That produces a layered agent:
shared setup defines the mission vocabulary, horizons, and scoring knobs,
physics answers whether one direct launch is legal for a realistic fleet size,
world model replays arrivals, production, and same-turn combat to predict ownership,
strategy allocates ships across reinforce, rescue, recapture, capture, snipe, swarm, crash exploit, salvage, and rear funneling.
Sun-crossing lines are rejected outright, moving targets are revisited only through later legal direct intercepts, and every accepted launch updates the future state before the next mission is judged. A full strategy reference appears in the final section of the notebook.
unfold_more Show hidden code
In [1]:
link code
🛰 Structured System Map
v11 combines arrival-time ownership forecasting, reinforce-to-hold defense, rescue-versus-recapture timing, multi-source swarm pressure, and crash-window opportunism inside one structured baseline.
Ships are spent only after three things agree: one direct shot is legal, the target still looks good at the true arrival turn, and the mission remains valid after earlier launches are written into the future.
1
🧱 Legal Shot
Probe several realistic fleet sizes, reject sun-crossing segments, and keep only one direct launch that the rules can actually execute.
2
🛡 Future State
Replay arrivals, production, and same-turn combat at that ETA so ownership, garrison, and exact need are forecasted instead of guessed.
3
🧯 Hold Logic
Split owned-planet decisions into reinforce-to-hold, rescue, and recapture so defense respects fall timing instead of collapsing into one shortcut.
4
🚀 Mission Layer
Spend ships on the best forecasted conversion: single capture, snipe, compact swarm, hostile swarm, post-crash exploit, or one more clean follow-up.
5
🔁 Commit Loop
Re-aim final sends, append ETA-aware commitments, refresh live doomed checks, and use leftover ships for salvage or rear-to-front staging.
☀ Direct Means Direct
Sun-crossing lines are discarded. No waypoint route is invented beyond what the game allows.
⚔ Ownership At ETA
Same-turn arrivals cancel by owner before the garrison fight, so need and hold logic are always arrival-time questions.
🤝 Partial Sources Matter
Small contributors stay alive long enough to assemble two-source and three-source swarms at one synchronized arrival window.
🧭 Refresh The Future
Every accepted launch rewrites the future. Later missions, salvage, and rear staging all read that updated commitment-aware state.
link code
🧭 Big Picture ¶
Read the notebook in that same order: route feasibility first, arrival-time state second, defense semantics third, pressure missions fourth, and commitment-aware cleanup last.
unfold_more Show hidden code
In [2]:
link code
link code
🧰 Shared Setup ¶
This section defines the common language used by every later layer.
The goal of this setup layer is consistency: every later decision should speak the same vocabulary for timing, ownership, send sizing, and mission type.
unfold_more Show hidden code
In [3]:
link code
link code
🧱 Physics ¶
This layer narrows the board to legal direct actions.
Physics does not decide whether a launch is valuable. It only answers whether one direct launch can exist, what angle it needs, and when it arrives. If a line crosses the sun, the route is rejected or revisited only through a later legal direct window on a moving target; no waypoint route is invented.
unfold_more Show hidden code
In [4]:
link code
link code
🛡 World Model ¶
This layer turns visible motion into forecastable ownership.
The world model does not rank missions. It supplies forecasts and ownership facts so strategy can compare options without slipping back into current-state heuristics.
unfold_more Show hidden code
In [5]:
link code
link code
🤝 Strategy ¶
This layer turns forecasted facts into ship allocation.
The key execution detail is settle_plan : it starts from a tested legal seed, moves toward the desired send, and still keeps a known legal fallback if one intermediate fleet size becomes unreachable. Split launches also stay split, because fleet size changes speed, ETA, and tactical meaning.
unfold_more Show hidden code
In [6]:
link code
link code
🛰 Agent Entry Point ¶
The final wrapper is intentionally thin.
It only reads the observation, builds the world snapshot, asks the strategy layer for launches, and returns those actions in the environment format. All of the real reasoning stays in the three layers above: legal route search, arrival-time forecasting, and commitment-aware mission selection.
Keeping this wrapper small makes the notebook easier to audit, because the path from geometry to world state to policy stays explicit instead of disappearing inside one monolithic agent() block.
unfold_more Show hidden code
In [7]:
link code
link code
✅ Verification ¶
The closing checks exercise the same contracts used by the code.
They confirm that:
direct launches still respect sun safety and moving-target prediction,
arrival-time state queries match same-turn combat rules,
reinforce-to-hold, rescue, and recapture remain distinct hold semantics,
swarm and crash-window helpers are judged at true arrival times,
live doomed salvage reacts to updated commitments rather than stale labels.
These checks matter because the notebook depends on one joined design: legal routing, forecasted ownership, hold-aware defense, coordinated pressure, and commitment-aware cleanup all have to agree with one another.
unfold_more Show hidden code
In [8]:
link code
link code
The section below mirrors STRATEGY.md so readers can inspect the full policy without leaving the notebook.
Orbit Wars Strategy ¶
This document describes the structured baseline implemented by orbit-war-submit-v11.ipynb and submission.py .
The identity of v11 is:
arrival-time ownership instead of snapshot-only targeting
reinforce-to-hold defense instead of one generic defensive rule
rescue and recapture as separate mission families
multi-probe direct reachability for moving targets
multi-source swarm pressure from partial source options
crash-window exploitation in multi-player fights
One principle drives the whole policy:
a launch is worth ships only if it is legal, arrives on a useful turn, and still creates ownership after same-turn combat and already-planned commitments are taken into account
1. Decision Flow ¶
The decision flow always runs in that order. It starts with route legality, then checks arrival-time state, then chooses whether ships should preserve, expand, pressure, or clean up.
2. Strategic Contracts ¶
These contracts are shared across capture, rescue, reinforce-to-hold, recapture, snipe, swarm, crash exploit, and salvage logic.
3. World Facts The Strategy Reads ¶
Strategy does not recompute geometry by itself. It asks the world model for facts.
Important queries include:
plan_shot(src_id, target_id, ships)
returns a legal direct angle and ETA for one fleet size
best_probe_aim(src_id, target_id, source_cap, ...)
searches several realistic fleet sizes and keeps the best legal probe
projected_state(target_id, turn, ...)
returns forecasted owner and garrison at a chosen turn
projected_timeline(target_id, horizon, ...)
returns the full future ownership timeline under visible arrivals and planned commitments
hold_status(target_id, ...)
returns whether a friendly planet holds, how many ships it must keep, and when it falls
min_ships_to_own_at(target_id, arrival_turn, attacker_owner, ...)
returns the exact ships needed to own a target on that arrival turn
min_ships_to_own_by(target_id, eval_turn, attacker_owner, arrival_turn, ...)
checks ownership by a later evaluation turn
reinforcement_needed_to_hold_until(target_id, arrival_turn, hold_until, ...)
returns the reinforcement needed to keep a friendly planet ours through a hold horizon
Those queries let the policy ask concrete questions:
if reinforcement lands before the fall turn, do we still hold?
if rescue is too late, how many ships are needed to reclaim the planet soon after?
if two or three sources arrive together, do we still own the target after same-turn combat?
if enemy fleets collide first, is there a cheap post-crash window right after the fight?
4. Policy State ¶
Before building missions, the policy converts world facts into local signals.
Indirect Wealth ¶
Each target gets a local value signal from nearby production:
nearby friendly production adds stability value
nearby neutral production adds expansion value
nearby enemy production adds pressure value
This helps separate empty travel distance from genuinely important map space.
Reserve And Attack Budget ¶
Each owned planet keeps the larger of:
exact keep needed against forecast inbound pressure
proactive keep against nearby enemy launch threats
stacked proactive keep when several enemy launch timings cluster in a short window
Normal offensive use follows:
attack budget = current ships - reserve
This keeps expansion and hostile pressure from consuming ships that the hold forecast still needs.
Shot-Based Reaction Map ¶
Neutral safety is tagged from legal shot probes rather than rough center-to-center distance.
For each target, legal shots are probed from nearby friendly and enemy sources, and the minimum legal ETA on each side is recorded. That reaction map is then used for:
safe neutral detection
contested neutral detection
opening filters
value adjustments
Macro Modes ¶
The policy derives a compact set of mode flags from total ships and production:
is_behind
is_ahead
is_dominating
is_finishing
attack_margin_mult
These modes tilt appetite and margin sizing, but they never replace arrival-time reasoning.
5. Mission Families ¶
Reinforce-To-Hold ¶
Reinforce-to-hold is the longest-horizon defensive mission.
It is valid only when:
the target is already ours
the planet is forecast to fall without help
reinforcement arrives by the required window
the added ships keep ownership through a hold horizon, not just one instant
This is different from a generic attack. Reinforcement is preserving a productive asset and its local position, so it uses its own capped source inventory and hold-oriented value model.
Rescue ¶
Rescue handles the clean hold-before-fall case.
A rescue mission is valid only when:
the target is ours
the fleet arrives on or before fall_turn
the planet is still ours at fall_turn after adding that reinforcement
Rescue is the fast defensive answer when the planet can still be saved in time.
Recapture ¶
Recapture handles the recover-after-fall case.
A recapture mission is valid only when:
rescue is too late
the fleet arrives after fall_turn
the delay remains inside the recapture window
This keeps the semantics sharp:
rescue means hold before the loss
recapture means take it back soon after the loss
Single-Source Capture ¶
This is the default expansion and attack mission.
For each owned source and non-owned target, the policy:
searches for a legal route with multi-probe reachability
rejects invalid late or low-life comet cases
computes exact arrival-time need
applies opening and reaction-gap filters
sizes the launch with margin
re-aims with the final send
scores the mission
This is the main path from forecast to action.
Snipe ¶
Snipe missions target neutrals that enemies are already cracking.
The idea is:
let an enemy help open the neutral
arrive on the same turn or inside a tight timing window
own the target after exact same-turn combat resolution
Several enemy inbound ETAs are evaluated, and the best feasible snipe is kept instead of stopping at the first legal one.
Swarm ¶
Swarm missions are coordinated direct attacks assembled from partial source options.
Important properties:
a source can contribute even when it cannot finish the target alone
swarm candidates are built only from legal direct shots
committed sends are re-aimed before acceptance
final synchronized ownership is checked again at the true joint arrival turn
There are two swarm forms:
two-source swarm
three-source hostile swarm
Three-source swarm is used only when:
the target is hostile
the target is large enough to justify the extra coordination
three sources can arrive inside a tight ETA tolerance
no two-source subset is already sufficient
Crash Exploit ¶
Crash exploit is the four-player opportunistic attack.
The world model scans the visible arrival ledger for cases where two enemy owners are about to collide on the same target. Strategy then looks for a legal direct shot that lands at or shortly after that crash window, never before it.
This turns multi-owner combat into a capture opportunity rather than treating every pressured planet as uniformly dangerous.
Follow-Up Capture ¶
After the first commitment wave, one more pass is made with leftover attack budget. This pass looks only for one more clean conversion and evaluates it against updated future commitments rather than the original snapshot.
Live Doomed Salvage ¶
A doomed label is not trusted if it was computed too early.
Before salvage, doomed status is recomputed from current planned commitments. If a planet still looks doomed:
it first checks whether the remaining stack can make one last useful capture
otherwise it retreats the stack to a safer allied planet
This avoids evacuating planets that were already stabilized by earlier rescue or reinforcement missions.
Rear Funneling ¶
Rear planets should not behave like isolated long-range attackers once a real frontier exists.
Outside late game:
a practical front anchor is identified
rear planets meaningfully behind that front are found
part of their attack budget is sent to a staging ally closer to action
This converts rear production into faster pressure instead of slow solo expeditions.
6. Candidate Generation And Commitment ¶
Candidate generation and commitment are intentionally separate.
Candidate Generation ¶
Mission families are generated roughly in this order:
reinforce-to-hold
rescue
recapture
single-source captures
snipes
two-source and three-source swarms
crash exploits
That order shapes the search space, but it is not the final execution order.
Global Commit Order ¶
After generation:
all mission candidates are scored
all missions are sorted globally by score
missions are then re-solved and committed one by one
That means a high-value snipe or swarm can still beat a weaker single capture even if it was generated later.
7. Settlement Logic ¶
settle_plan() is the main execution guardrail.
Its job is to keep send sizing, reachability, ETA, and ownership need aligned.
It works like this:
start from a legal seed found through probe search
evaluate exact ownership need at the resulting arrival turn
move toward the desired send
if one intermediate ship count is unreachable, fall back to an already tested legal send instead of failing immediately
This keeps moving-target execution stable even when route feasibility changes with fleet size. settle_reinforce_plan() applies the same idea to hold-defense missions, except the objective is to remain ours through a hold horizon rather than to capture at one instant.
All missions are committed one by one in score order. After every accepted launch:
source inventory is reduced
the move is appended
planned_commitments is updated with ETA and ship count
Later missions therefore reason against the updated future, not against a stale pre-commit snapshot.
8. Valuation And Send Sizing ¶
Target Value ¶
Base value begins with profitable production horizon and is then corrected by:
indirect local wealth
static versus rotating target type
neutral versus hostile ownership
safe versus contested neutral status
comet timing
mission type such as snipe, swarm, reinforce, or crash exploit
late-game immediate ship swing
finishing and behind modes
Reinforcement uses a more hold-oriented value formula than generic capture. It values saved production, saved ships, and frontier stability rather than treating a friendly planet like just another capture target.
Send Philosophy ¶
The policy usually sends more than the exact minimum.
Margins grow with factors such as:
hostile ownership
higher production
contested timing
four-player pressure
longer travel time
Margins are relaxed in cases like comets where overcommitting is more expensive, and rescue and reinforce use their own hold-focused sizing logic.
9. Phase Behavior ¶
Opening ¶
The opening favors:
safe neutrals
favorable legal reaction gaps
disciplined reserve
caution on rotating four-player races
Midgame ¶
The midgame emphasizes:
reinforce and rescue before greed
fast recapture when rescue is too late
timing-based snipes
compact swarms
hostile pressure that still preserves defensive reserves
Late Game ¶
Late play shifts weight toward:
immediate ship swing
hostile pressure
elimination value
avoiding launches that arrive too late to matter
10. Deliberate Boundaries ¶
The current strategy intentionally does not do the following:
fake sun-dodging detours
launch merging
broad combinatorial fleet assignment
current-state-only targeting
blind all-in opening races
treating late recapture as if it were true rescue
These omissions are deliberate. The design goal is consistent sun safety, arrival-time ownership, hold-defense semantics, and commitment timing before adding broader tactical complexity.
License
This Notebook has been released under the Apache 2.0 open source license.
Continue exploring
Input 1 file arrow_right_alt
Output 2 files arrow_right_alt
Logs 40.9 second run - successful arrow_right_alt
Comments 1 comment arrow_right_alt