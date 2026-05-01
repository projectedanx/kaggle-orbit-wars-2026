> Source: https://www.kaggle.com/code/aminmahmoudalifayed/orbital-strategist-the-revolutionary-orbit-wars

Orbital Strategist — The Revolutionary Orbit Wars
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
Dr/ameen Fayed
· 12h ago
· 625 views
more_vert
Orbital Strategist — The Revolutionary Orbit Wars
Copy & Edit
6
file_download Download
arrow_drop_up 20 
Orbital Strategist — The Revolutionary Orbit Wars
Notebook Input Output Logs Comments (0)
menu_open 
Competition Notebook
Orbit Wars
Public Score
496.8
Best Score
496.8 V10
Runtime
play_arrow
8m 27s · GPU P100
history Version 10 of 10
Input
COMPETITIONS 
Orbit Wars
Language
Python
expand_more View Metadata
link code
🤖 KRONOS RL — Deep Reinforcement Learning ## Orbit Wars · $50,000 Prize · Deadline June 16, 2026
Architecture ¶
Reward Shaping: ¶
link code
⚙ Cell 1 — Install ¶
In [1]:
link code
link code
📦 Cell 2 — Imports ¶
In [2]:
link code
link code
⚙ Cell 3 — Physics Core ¶
In [3]:
link code
link code
🔬 Cell 4 — KRONOS Heuristic (Opponent + Rollout) ¶
In [4]:
link code
link code
🌍 Cell 5 — OrbitWarsEnv (Complete Gymnasium Environment) ¶
Observation: 60-dim flat vector (20 planets × 3 features)
Action: MultiDiscrete([20, 20, 10])
src_idx : which of our planets to send from
tgt_idx : which enemy/neutral planet to attack
fraction : 10%–100% of ships to send
Reward: shaped per-tick + terminal
In [5]:
link code
link code
🧪 Cell 6 — Environment Sanity Test ¶
In [6]:
link code
link code
🚀 Cell 7 — PPO Training ¶
⏰ 100k steps ≈ 30 min on CPU, 10 min on GPU ⏰ 500k steps ≈ 2-3 hours (recommended) ⏰ 2M steps ≈ overnight (best results)
In [7]:
link code
link code
🤖 Cell 8 — Load PPO Agent & Test ¶
In [8]:
link code
link code
📊 Cell 9 — Tournament 20 Games ¶
In [9]:
link code
link code
💾 Cell 10 — Write Submission ¶
Before training: submits KRONOS heuristic After training: switch orbital_strategist = ppo_agent
In [10]:
link code
link code
✅ Cell 11 — Verify Submission ¶
In [11]:
link code
License
This Notebook has been released under the Apache 2.0 open source license.
Continue exploring
Input 1 file arrow_right_alt
Output 2 files arrow_right_alt
Logs 506.7 second run - successful arrow_right_alt
Comments 0 comments arrow_right_alt