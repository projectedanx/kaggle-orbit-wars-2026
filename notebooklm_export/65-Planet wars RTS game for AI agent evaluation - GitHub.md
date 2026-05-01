> Source: https://github.com/SimonLucas/planet-wars-rts

GitHub - SimonLucas/planet-wars-rts: Planet wars RTS game for AI agent evaluation · GitHub
Skip to content
Navigation Menu
Toggle navigation 
Sign in
Appearance settings
Platform
AI CODE CREATION
GitHub Copilot Write better code with AI
GitHub Spark Build and deploy intelligent apps
GitHub Models Manage and compare prompts
MCP Registry New Integrate external tools
DEVELOPER WORKFLOWS
Actions Automate any workflow
Codespaces Instant dev environments
Issues Plan and track work
Code Review Manage code changes
APPLICATION SECURITY
GitHub Advanced Security Find and fix vulnerabilities
Code security Secure your code as you build
Secret protection Stop leaks before they start
EXPLORE
Why GitHub
Documentation
Blog
Changelog
Marketplace View all features
Solutions
BY COMPANY SIZE
Enterprises
Small and medium teams
Startups
Nonprofits
BY USE CASE
App Modernization
DevSecOps
DevOps
CI/CD
View all use cases
BY INDUSTRY
Healthcare
Financial services
Manufacturing
Government
View all industries View all solutions
Resources
EXPLORE BY TOPIC
AI
Software Development
DevOps
Security
View all topics
EXPLORE BY TYPE
Customer stories
Events & webinars
Ebooks & reports
Business insights
GitHub Skills
SUPPORT & SERVICES
Documentation
Customer support
Community forum
Trust center
Partners View all resources
Open Source
COMMUNITY
GitHub Sponsors Fund open source developers
PROGRAMS
Security Lab
Maintainer Community
Accelerator
GitHub Stars
Archive Program
REPOSITORIES
Topics
Trending
Collections
Enterprise
ENTERPRISE SOLUTIONS
Enterprise platform AI-powered developer platform
AVAILABLE ADD-ONS
GitHub Advanced Security Enterprise-grade security features
Copilot for Business Enterprise-grade AI features
Premium Support Enterprise-grade 24/7 support
Pricing
Search or jump to...
Search code, repositories, users, issues, pull requests...
Search
Clear
Search syntax tips
Provide feedback
We read every piece of feedback, and take your input very seriously. [-]
Include my email address so I can be contacted
Cancel Submit feedback
Saved searches
Use saved searches to filter your results more quickly
Name
Query
To see all available qualifiers, see our documentation.
Cancel Create saved search
Sign in
Sign up
Appearance settings
Resetting focus
You signed in with another tab or window. Reload to refresh your session. You signed out in another tab or window. Reload to refresh your session. You switched accounts on another tab or window. Reload to refresh your session. Dismiss alert
SimonLucas / planet-wars-rts Public
Notifications You must be signed in to change notification settings
Fork 13
Star 24
Code
Issues 2
Pull requests 1
Actions
Projects
Security and quality 0
Insights
Additional navigation options
Code
Issues
Pull requests
Actions
Projects
Security and quality
Insights 
SimonLucas/planet-wars-rts
main
2 Branches 0 Tags  
Go to file
Code
Open more actions menu
Folders and files
Repository files navigation
README
MIT license
Planet Wars RTS
The code is in early access, but the interfaces are intended to be stable both for the fully observable and partially observable versions of the game.
To run headless games use the examples in the games.planetwars.runners package.
To run games with a GUI, use the games.planetwars.view.RunVisualGame class.
The following features are ready for community testing:
containerised version (PodMan or Docker) -- see Submission Instructions - updated with Python instructions.
Introduction
This repo contains the code and instructions for a series of Planet Wars Real-Time Strategy (RTS) games. The challenge for AI agents is to play well across a wide range of different game parameters, and against a wide range of opponent strategies.
For a quick idea of the game, watch some sample AI agents play live.
Upcoming Competitions 2026
We're excited to announce that Planet Wars RTS has been accepted to run at two major conferences in 2026:
IEEE WCCI 2026 (IEEE World Congress on Computational Intelligence)
June 21-26, 2026 in Maastricht, Netherlands
Competition details coming soon
AAMAS 2026 (International Conference on Autonomous Agents and Multiagent Systems)
May 25-29, 2026 in Paphos, Cyprus
Competition details coming soon
Past Competitions
The competition has successfully run at the following conferences:
GECCO 2025 Competition Specifics (Deadline July 9, 2025) -- Results now available
IEEE Conference on Games 2025 -- Specifics: See here Deadline August 27, 2025. -- Results
Figures below show a fully observable and a partially observable game in play.
 
The core idea
Planet Wars is an RTS game where players aim to gain control of planets and destroy enemy units.
We provide a framework for developing and testing AI agents in a fast and flexible way. The challenge is open-ended as the game parameters can be varied to create a range of different game scenarios. Can your bots handle such variation? Even the simpler versions still have the difficulty of dealing with the simultaneous move nature of the game and unpredictable opponent actions.
The software supports a family of games where key details can be varied to affect the difficulty of the game. This includes:
Observability of the game state:
full
partial: full observability of the player's own assets, only ownership of neutral and opponent planets
The number of planets
The battle rules
In-transit collisions
Transit speed
The time allowed per decision
The winning conditions:
the number of planets controlled
the difference in the number of units
whether units in transit count towards the total
The game duration
Agent API
There are two types depending on the observability. For the fully observable version, agents are given a copy of the complete game state at each time step, and follow this interface:
For the partially observable game, agents use this interface:
There are simple helper classes provided to reconstruct a game state from an observation, and an example of using this is given in this agent:
However, part of the skill of an agent is in the assumptions it makes about the hidden information, so we expect high performance agents to improve on the provided reconstruction example.
A GameState object is required for planning algorithms in order to use the forward model provided.
Game Runners
There are two ways to run games: synchronous and asynchronous.
Synchronous
In synchronous mode, the game runner runs in a single thread. At each game tick, it calls the getAction method of each agent, waits for the response, applies the actions of each agent to generate the next state using the forward model, and the repeats until the game is over.
This mode is useful for debugging and testing: it is often faster than asynchronous mode as it avoids any overhead due to coroutines and timeouts (though in theory asynchronous mode could be faster on a multi-core machine as agents could run in their own threads - the actual speed depends on a number of factors).
In asynchronous mode, the game runner runs in multiple threads or coroutines. The key point is that every game tick it sends the current state observation to each agent, and then waits for for a specified number of milliseconds for a response.
If the agent does not respond in time, the game runner assumes a doNothing action, and proceeds to step the game forward.
Hence this mode is truly real-time.
Agent Deployment
For debugging and development run your code locally by extending the examples in the games.planetwars.runners package, if developing in Kotlin, Java or any JVM language.
For competitions, deploy your agent to a Docker / PodMan container, and provide the link via the competition interface. See
Submission Instructions for details, including how to run a Python agent with a trained neural network model.
The codebase and philosophy
The code aims to be well-structured, easy to read and efficient. The agent interface is designed to be the same for all versions of the game, as is the game state representation and game state observations. The key differences between versions of the game are captured in the game parameters, observation details and forward model.
The evaluation
For your own evaluations see the games.planetwars.runners.RoundRobinLeague example. Running this with the sample agents will produce a league table similar to the following one:
For competitions we aim to run sufficient games to arrive at a stable rank order of the agents.
About
Planet wars RTS game for AI agent evaluation
Resources
Readme
License
MIT license
Uh oh!
There was an error while loading. Please reload this page.
Activity
Stars
24 stars
Watchers
4 watching
Forks
13 forks
Report repository
Releases
No releases published
Packages 0
No packages published
Contributors 4
 SimonLucas Simon Lucas
 claude Claude
 Priwinn
 philrod1 Phil
Languages
Python 55.4%
Kotlin 39.2%
HTML 4.0%
Shell 1.1%
Other 0.3%
Footer
© 2026 GitHub, Inc.
Footer navigation
Terms
Privacy
Security
Status
Community
Docs
Contact
Manage cookies
Do not share my personal information
You can't perform that action at this time.