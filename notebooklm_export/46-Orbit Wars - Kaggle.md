> Source: https://www.kaggle.com/competitions/orbit-wars/discussion/692938

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
JM
· 3 days ago
more_vert
'Validation Episode failed' Error on Submit
arrow_drop_up 7
Is there a way we can get some more info from this ? When I submit an agent .zip with a main.py and a checkpoint.pt it does not seem to work. It works if I load it on Kaggle notebook and run it via:
So that passes this:
When you upload a Submission, we first play a Validation Episode where that Submission plays against copies of itself to make sure it works properly.
and I have followed this:
"Your submission should be a python file with the last 'def' accepting an observation and returning an action. You can also upload multiple files in a zip/gz/7z archive with a main.py at the top level."
So not sure what else we need to check before submitting? Seems it can't find the checkpoint.pt once it gets submitted or something else?
The CLI does not match the provided documentation so not sure how else we can get the logs? @bovard
Please sign in to reply to this topic.
8 Comments
Hotness Hotness 
[
Bovard Doerschuk-Tiberi
](https://www.kaggle.com/bovard)
Kaggle Staff
2 days ago
arrow_drop_up 3
more_vert
The abolute path is different on the simulation workers, you code is untarred into /agent/ , for example /agent/main.py . The python is invoked from another directory you you'll need to add a check to see if your .pkl file exists in different locations 
[
Bovard Doerschuk-Tiberi
](https://www.kaggle.com/bovard)
Kaggle Staff
2 days ago
arrow_drop_up 1
more_vert
Also the Validation episodes should have a log file that you can download from the UI? Can you post a picture of what you see when you try to look at the episode replay in the submissions panel? 
[
JM
](https://www.kaggle.com/julianmukaj)
Topic Author
2 days ago
arrow_drop_up 1
more_vert 
There's nothing on the episode column for me, possibly due to the different paths for my .pkl it never loads my agent? Nothing if I try to open the submission up either except the "Validation Episode Failed" error.
If you could update the "Getting Started" notebook with an example for loading a file for the agent would be helpful! I tried /agent/checkpoint.pkl and even os.walk(root) to look for the file but didn't succeed for me. 
[
Dapp
](https://www.kaggle.com/lgloria)
2 days ago
arrow_drop_up 1
more_vert
362nd in this Competition
I'm having the same problem. Where can I find the logs?
3 more replies arrow_drop_down   
emoji_people
[
Tom
](https://www.kaggle.com/tom99763)
7 hours ago
arrow_drop_up 0
more_vert
188th in this Competition
Update: If you are using deep learning module, just change to numpy then it works. 
[
GBoekestijn
](https://www.kaggle.com/gboekestijn)
8 hours ago
arrow_drop_up 0
more_vert
327th in this Competition
I would also greatly appreciate the ability to download logs. I am having trouble getting anything more than the simplest strategies running in the submission, even though I can get them running locally. It is very difficult to debug without any explanation why the validation failed.
emoji_people
[
Tom
](https://www.kaggle.com/tom99763)
10 hours ago
arrow_drop_up 0
more_vert
188th in this Competition
You actually can test whether your approach can pass 4 self-play validation locally using kaggle environment simulation. It'll help you find the bug. I highley recommend using API to submit instead of notebooks, Claude code or Codex can help you doing code review. 
[
Tom
](https://www.kaggle.com/tom99763)
8 hours ago
arrow_drop_up 0
more_vert
188th in this Competition
@bovard I hope there's an explicit logs can check. Although error submission doesn't count submission usage if using kaggle's CLI. But it's hard, experiencing submisison errors again and again without clear instruction makes me really frustrated. 
[
Kurise
](https://www.kaggle.com/kurisew)
20 hours ago
arrow_drop_up 0
more_vert
160th in this Competition
Have you try to set your model path startwith Path( file).parent or '/kaggle_simulations/agent/' ?