> Source: https://www.kaggle.com/competitions/orbit-wars/discussion/692695

Orbit Wars | Kaggle
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
Kaggle
· Featured Simulation Competition · 2 months to go
Orbit Wars
Conquer planets rotating around a sun in continuous 2D space. A real-time strategy game for 2 or 4 players. 
Join Competition
more_horiz
Orbit Wars
Overview Data Code Models Discussion Leaderboard Rules 
c-number
· 4 days ago
more_vert
Possible orbit_wars observation inconsistency: initial_planets differs by player after comet updates
arrow_drop_up 16
While validating a local simulator against the official orbit_wars environment, I noticed what looks like an observation inconsistency around comet spawn / expiry.
This does not seem to affect the main game transition itself. The issue appears to be only in the observation surface.
What I observed
After comet-related updates, these fields appear to stay synchronized across players:
planets
comets
comet_planet_ids
However, initial_planets can differ between player 0 and the other players.
In particular, player 0 can observe the comet-created planets reflected in initial_planets , while player 1+ can keep an older version of that field.
So at the same timestep, different players can receive different initial_planets , even though the rest of the comet-related observation is already aligned.
Minimal reproduction
I can reproduce this with a short noop run to the first comet spawn.
On my side this produces:
So both players see the same live planets and the same comet_planet_ids , but only player 0 sees the comet-created planets reflected in initial_planets .
I also see the same pattern in 4p : player 0 gets the updated initial_planets , while players 1 , 2 , and 3 keep the shorter pre-update version.
Why this seems suspicious
From reading the public implementation, obs0.initial_planets is updated during comet lifecycle handling:
comet spawn appends new comet planets to obs0.initial_planets
comet expiry removes expired comet planets from obs0.initial_planets
But the end-of-turn synchronization block for i > 0 originally copied:
planets
fleets
next_fleet_id
comets
comet_planet_ids
and did not refresh initial_planets .
So the behavior looks like:
player 0 gets the updated obs0.initial_planets
player 1+ keep an older initial_planets
observation parity breaks for that field only
Proposed fix
I opened a minimal PR here:
https://github.com/Kaggle/kaggle-environments/pull/980
The proposed change is just to sync initial_planets in the same per-player block that already syncs the other shared observation fields, plus a regression test. 
3
Please sign in to reply to this topic.
4 Comments
1 appreciations false
Hotness Hotness 
[
Bovard Doerschuk-Tiberi
](https://www.kaggle.com/bovard)
Kaggle Staff
4 days ago
arrow_drop_up 2
more_vert
This has been merged and should be rolling out in the next couple of hours. Thank you! 
[
Ryuhki Kimura
](https://www.kaggle.com/kimura0415)
3 days ago
arrow_drop_up 0
more_vert
152nd in this Competition
エチレンさんエグすぎる。。。これが世界１位。。。 
[
c-number
](https://www.kaggle.com/cnumber)
Topic Author
2 days ago
arrow_drop_up 0
more_vert
I found this when using codex to make a faster environment for RL 
Appreciation (1)
[
Bovard Doerschuk-Tiberi
](https://www.kaggle.com/bovard)
Kaggle Staff
4 days ago
arrow_drop_up 1
more_vert
Thank you! I'll take a look