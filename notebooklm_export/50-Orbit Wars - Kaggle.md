> Source: https://www.kaggle.com/competitions/orbit-wars/discussion/692752

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
Syed Ali Hasnat
· 664th in this Competition · 4 days ago
more_vert
Orbit Wars: Beyond the Basic Sniper - Advanced Strategies for Top Performance
arrow_drop_up 2
Overview The tutorial Nearest Planet Sniper agent is a helpful starting point, but it has critical flaws that prevent it from reaching competitive levels. This post explains the main problems with basic strategies and presents three improved approaches.
The Problem Why Basic Strategies Fail
Issue 1 Travel Time Blindness The flaw is ignoring that the target planet keeps producing ships while your fleet is traveling. By arrival, the enemy is stronger. Fix Calculate travel time and predict the enemy garrison by adding production during travel. Impact Long travel times can add many extra ships, causing failed attacks if not considered.
Issue 2 Sun Destruction Fleets that pass through the sun are destroyed instantly. Fix Check whether the path crosses the sun before sending fleets. Impact Prevents losing ships unnecessarily.
Issue 3 Fleet Duplication Multiple planets may attack the same weak target, wasting ships. Fix Track already assigned targets and send only one fleet per target. Impact Saves resources and avoids overkill.
Issue 4 No Priority System Targets are chosen randomly without considering value. Fix Use return on investment defined as production divided by ships needed. Impact Focuses attacks on valuable planets.
Issue 5 Comets Ignored Temporary planets provide free production but are often ignored. Fix Detect comet planets and prioritize capturing them. Impact Gains extra resources and denies opponents.
Strategy 1 Smart Aggressor Ranks targets by value and attacks efficiently. Advantages Efficient resource use, avoids waste, considers travel and safety. Performance Strong and reliable in most situations.
Strategy 2 Comet Hunter Focuses on capturing temporary planets during their active period. Advantages Gains free production and improves timing skills.
Strategy 3 Adaptive Strategist Switches between attack and defense based on game state. Advantages Flexible, avoids risky moves when losing and expands when winning.
Core Mechanics
Fleet speed increases with fleet size, so larger fleets move faster. Combat resolves by comparing fleet sizes and planet defenses. Sun collision destroys fleets if their path passes too close.
Common Mistakes
Ignoring travel time leads to failed attacks Not checking sun causes fleet loss Attacking same target wastes ships No prioritization reduces efficiency Ignoring comets misses opportunities Overcommitting leaves planets weak
Performance Expectations
Basic strategy performs moderately well Improved strategies significantly increase win rate Advanced optimization is needed for top rankings
Further Optimization Ideas
Predict planet movement Strengthen defense Model enemy behavior Improve endgame strategy Use risk based decisions Control key regions
Conclusion
Success depends on accounting for travel and production, avoiding mistakes, prioritizing targets, adapting strategy, and capturing opportunities like comets. Smart Aggressor is the best starting point, with further improvements adding flexibility and specialization.
Please sign in to reply to this topic.
2 Comments
Hotness Hotness 
[
Syed Ali Hasnat
](https://www.kaggle.com/syedalihasnat)
Topic Author
4 days ago
arrow_drop_up 1
more_vert
664th in this Competition
Basic strategies fail mainly because they ignore dynamic factors like travel time and production. Competitive play requires planning ahead, not just reacting to current conditions. Among the strategies, Smart Aggressor stands out as the most reliable because it balances efficiency and decision making. However, combining it with adaptive behavior and comet prioritization leads to the best overall performance.
This comment has been deleted.