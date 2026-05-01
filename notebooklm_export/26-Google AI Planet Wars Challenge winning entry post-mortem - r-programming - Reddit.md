> Source: https://www.reddit.com/r/programming/comments/ef40x/google_ai_planet_wars_challenge_winning_entry/

Google AI Planet Wars Challenge winning entry post-mortem : r/programming
Skip to main content Google AI Planet Wars Challenge winning entry post-mortem : r/programming
Open menu
Open navigation 
Go to Reddit Home 
r/programming
TRENDING TODAY
Get App
Get the Reddit app
Log In
Log in to Reddit
Expand user menu
Open settings menu
Skip to Navigation Skip to Right Sidebar
Back
Go to programming
r/programming
•
16y ago
a1k0n
Locked post
Stickied post
Archived post
Language and translations
Report
Google AI Planet Wars Challenge winning entry post-mortem
quotenil.com Open
Upvote 128 Downvote 38 Go to comments Share
Sort by: Best
Open comment sort options
Best
Top
New
Controversial
Old
Q&A
Comments Section
Deimorz
•
16y ago
It's linked in the article, but the second-place competitor wrote a post-mortem as well. It's a little easier to follow, worth reading if you're interested in the topic.
Upvote 15 Downvote Reply Award Share
Report
Language and translations
Award
Share 
jnnnnn
•
16y ago
This was the winner's favourite game.
Upvote 9 Downvote Reply Award Share
Report
Language and translations
Award
Share
Tairnyn
•
16y ago
It's a shame that a heuristic approach proved to be superior to machine learning techniques. Was really expecting a killer genetic algorithm to take the prize. I guess it only goes to reinforce the notion that AI is only as good as the domain understanding of the person(s) writing it.
Upvote 6 Downvote Reply Award Share
Report
Language and translations
Award
Share
mega
•
16y ago
I agree. I would have liked to apply one of my pet algorithms but to my chagrin it became obvious that the way to win was to understand the game really well. The general purpose algorithms, such as genetic algorithms, are almost always safe, but somewhat mediocre choices.
There is no escaping the domain: it's the encoding of the genetic information, it's the random playouts for UCT, it's the evaluation function for my bot.
Upvote 5 Downvote Reply Award Share
Report
Language and translations
Award
Share 
[deleted]
•
16y ago
It's not machine learning, it's genetic programming. He's evolving a program. The program doesn't learn crap, it's just good at what it does.
Upvote 3 Downvote Reply Award Share
Report
Language and translations
Award
Share
Kanin
•
16y ago
Two points: first, participants were allowed to update their bots, meaning it wasn't the only bot "evolving". If he were to evolve it against the final set, it would take less computations (a lot less hehe) to achieve domination. Mind you, real evolution does allow updates across the system.
Second, the branches resulting from evolution were not allowed to populate the system, he had to stick to the "best" result. If allowed, we would find an amazing type breaking amount of useless bots across the ranking, with most being useless at the bottom, but certainly some would have ranked better than what was achieved. You can compensate this with more computations (a lot more hehe).
To conclude, genetic programming is not as good as the domain understanding of the author, it's as good as the amount of computations allowed. But considering the rules and the amount of computations time allowed him, choosing the evolution option was a hopeless move, but an interesting and instructive one.
Upvote 2 Downvote Reply Award Share
Report
Language and translations
Award
Share
3 more replies
linuxlass
•
16y ago
Does anyone happen to know if anyone's written a GUI so a human can play against a bot?
My 13yo son is using his bot for his science fair project and I thought it would be cool if he could make his bot available for anyone who wanted to play against it at the Science Fair.
I was going to hack into the jar files and put together a GUI, but I'm happy to use existing code and save myself some work :)
Upvote 7 Downvote Reply Award Share
Report
Language and translations
Award
Share 
aerique
•
16y ago
• Edited 16y ago
(posting from phone so excuse the lack of links and brevity)
Search the ai-contest.com website for JBotManager.jar or if that doesn't work out for you mail me at aerique@xs4all.nl and I'll mail it to you when I wake up tomorrow morning.
edit: it's here http://www.ai-contest.com/forum/viewtopic.php?f=18&t=751
Upvote 3 Downvote Reply Award Share
Report
Language and translations
Award
Share
More replies
1 more reply 
smallfried
•
16y ago
Okay, that guy went really deep in the analysis of the game. A well deserved win.
Upvote 3 Downvote Reply Award Share
Report
Language and translations
Award
Share 
beeff
•
16y ago
All hail Common Lisp. Risen again from the deeps to bring syntactical insanity to unbelievers.
Upvote 5 Downvote Reply Award Share
Report
Language and translations
Award
Share
pyronautical
•
16y ago
Anyone here enter?
I made a decent bot that finished around 1000 place (Sounds bad, but considering some of the bots on show...). Only had a few days before entries closed so had to rush through a quick few strategies.
Upvote 2 Downvote Reply Award Share
Report
Language and translations
Award
Share
Anonymoose333
•
16y ago
Mine ended up at 158.
Upvote 3 Downvote Reply Award Share
Report
Language and translations
Award
Share 
flat5
•
16y ago
Yeah, I spent a couple long weeks on it before realizing it wasn't the best use of my time. My bot was remarkably similar to bocsimacko's, actually, although his kicked my rear in practice and his bot is why I quit because it looked too difficult to catch it by the deadline. I suspect many of these same ideas (future states, full attack valuation, redistribution, etc.) were reinvented countless times by the top 500 or so bots. My redistribution algorithm was quite weak and I suspect that was my main failing.
Upvote 1 Downvote Reply Award Share
Report
Language and translations
Award
Share
3 more replies
Cobol
•
16y ago
I gotta give props to that magnificent bastard who placed in the top 20 with Haskell. I've always wanted to learn that language.
Upvote 2 Downvote Reply Award Share
Report
Language and translations
Award
Share
wagstaff
•
16y ago
You're too kind.
I doubt that choice of language made a lot of difference for me. I'm a distinctly intermediate Haskeller - actually, getting some practice with Haskell was a large part of my motivation for taking part - and am pretty sure I'd have ended up in much the same place in any reasonable language.
My code - along with that of many others - can be found in this thread.
As for "I've always wanted to learn that language"... what's stopping you? My advice: you should generally do things that you've always wanted to do.
Upvote 6 Downvote Reply Award Share
Report
Language and translations
Award
Share
More replies
G_Morgan
•
16y ago
Haskell isn't particularly inefficient. It is certainly a better fit for this challenge than most languages.
Upvote 3 Downvote Reply Award Share
Report
Language and translations
Award
Share
ryeguy
•
16y ago
Where did that one guy place who made the self-modifying php code? There was an article submitted here a couple weeks or so ago where he was talking about his approach.
Upvote 3 Downvote Reply Award Share
Report
Language and translations
Award
Share
welle
•
16y ago
the genetic bot
the forum thread
Upvote 5 Downvote Reply Award Share
Report
Language and translations
Award
Share
1 more reply
j3camero
•
16y ago
Congrats! Glad you enjoyed the contest!
Will we see you in the next one? Or maybe you want to help us make the next one...? So far all of the past winners have gone on to contribute code the next contest (m2ellis, amstan, a1k0n).
Upvote 3 Downvote Reply Award Share
Report
Language and translations
Award
Share 
flat5
•
16y ago
• Edited 16y ago
Have you considered a stripped down poker-like game for a future contest? Maybe a 20-30 big blind heads-up no-limit hold 'em game. I think you'd get huge interest for something like that. It would very amenable to the kind of machine learning algorithms that people want to apply.
Upvote 2 Downvote Reply Award Share
Report
Language and translations
Award
Share
mega
•
16y ago
Depends on when the next contest is. This one's been a bit too long for an all consuming obsession and I'm behind on almost everything else.
Upvote 1 Downvote Reply Award Share
Report
Language and translations
Award
Share
j0z
•
16y ago
After seeing this, I want to learn lisp. But it looks difficult...
Upvote 1 Downvote Reply Award Share
Report
Language and translations
Award
Share 
beeff
•
16y ago
It doesn't.
http://mitpress.mit.edu/sicp/full-text/book/book.html
Have fun.
Upvote 6 Downvote Reply Award Share
Report
Language and translations
Award
Share
More replies 
aerique
•
16y ago
Looks can be deceiving.
Upvote 3 Downvote Reply Award Share
Report
Language and translations
Award
Share
More replies
5 more replies
[deleted]
•
16y ago
Comment deleted by user
a1k0n
OP
• 16y ago
Yeah, that's why he says "That's enough of tribute, let's steer off the trodden path."
More replies
New to Reddit?
Create your account and connect with a world of communities.
Continue with Email
Continue With Phone Number
By continuing, you agree to our User Agreement and acknowledge that you understand the Privacy Policy.
More posts you may like
what's wrong with google ai r/endlesssky • 6mo ago [
what's wrong with google ai
](https://www.reddit.com/r/endlesssky/comments/1o930zx/whats_wrong_with_google_ai/)  42 upvotes · 23 comments
This brilliantly helpful Google AI summary r/mildlyinfuriating • 9mo ago [
This brilliantly helpful Google AI summary
](https://www.reddit.com/r/mildlyinfuriating/comments/1mhpgju/this_brilliantly_helpful_google_ai_summary/)  1.4K upvotes · 61 comments
Never trust Google AI overview. (Duh) r/BikeMechanics • 7mo ago [
Never trust Google AI overview. (Duh)
](https://www.reddit.com/r/BikeMechanics/comments/1nnt22l/never_trust_google_ai_overview_duh/)  2 122 upvotes · 59 comments
Everyone's pushing AI for dev teams, but something feels off r/AI_Agents • 17d ago [
Everyone's pushing AI for dev teams, but something feels off
](https://www.reddit.com/r/AI_Agents/comments/1sc2zu6/everyones_pushing_ai_for_dev_teams_but_something/) 14 upvotes · 17 comments
IDL how I get an ai response every-time I type something into google r/I_DONT_LIKE • 3mo ago [
IDL how I get an ai response every-time I type something into google
](https://www.reddit.com/r/I_DONT_LIKE/comments/1q600c0/idl_how_i_get_an_ai_response_everytime_i_type/) 44 upvotes · 12 comments
Google's DeepMind Cracks a Century-Old Physics Mystery With AI r/EverythingScience • 5mo ago [
Google's DeepMind Cracks a Century-Old Physics Mystery With AI
](https://www.reddit.com/r/EverythingScience/comments/1owtp5a/googles_deepmind_cracks_a_centuryold_physics/)  businessinsider 801 upvotes · 19 comments
I am disappointed in the AI discourse r/programming • 1y ago [
I am disappointed in the AI discourse
](https://www.reddit.com/r/programming/comments/1kxn91l/i_am_disappointed_in_the_ai_discourse/) 24 comments
Google ai overview is a, a, a, a, a, r/notinteresting • 3mo ago [
Google ai overview is a, a, a, a, a,
](https://www.reddit.com/r/notinteresting/comments/1qp2yux/google_ai_overview_is_a_a_a_a_a/)  74 upvotes · 15 comments
Realizing the difference between "using AI a lot" and being AI-fluent. r/AI_Agents • 11d ago [
Realizing the difference between "using AI a lot" and being AI-fluent.
](https://www.reddit.com/r/AI_Agents/comments/1shdmfw/realizing_the_difference_between_using_ai_a_lot/) 39 upvotes · 22 comments
How to start learning ai agent r/AI_Agents • 3mo ago [
How to start learning ai agent
](https://www.reddit.com/r/AI_Agents/comments/1qtxbkr/how_to_start_learning_ai_agent/) 20 upvotes · 14 comments
Google is adding more links inside AI Answers , Here's what that actually means r/Agent_SEO • 4mo ago [
Google is adding more links inside AI Answers , Here's what that actually means
](https://www.reddit.com/r/Agent_SEO/comments/1pn5b34/google_is_adding_more_links_inside_ai_answers/) 35 upvotes · 13 comments
OpenAI encourages firms to trial four-day weeks in AI era r/bayarea • 14d ago [
OpenAI encourages firms to trial four-day weeks in AI era
](https://www.reddit.com/r/bayarea/comments/1sf0q7e/openai_encourages_firms_to_trial_fourday_weeks_in/) 26 upvotes · 21 comments
The Forced Use of AI is getting out of Hand r/programming • 9mo ago [
The Forced Use of AI is getting out of Hand
](https://www.reddit.com/r/programming/comments/1m5grhc/the_forced_use_of_ai_is_getting_out_of_hand/)  substack 461 upvotes · 199 comments
OpenAI cofounder Andrej Karpathy says it will take a decade before AI agents actually work r/AIAgentsInAction • 4mo ago [
OpenAI cofounder Andrej Karpathy says it will take a decade before AI agents actually work
](https://www.reddit.com/r/AIAgentsInAction/comments/1pomice/openai_cofounder_andrej_karpathy_says_it_will/)  businessinsider 124 upvotes · 6 comments
AI Makes the Easy Part Easier and the Hard Part Harder r/programming • 2mo ago [
AI Makes the Easy Part Easier and the Hard Part Harder
](https://www.reddit.com/r/programming/comments/1qz5g7g/ai_makes_the_easy_part_easier_and_the_hard_part/) 763 upvotes · 133 comments
Need help fixing AI targeting r/FromTheDepths • 4mo ago [
Need help fixing AI targeting
](https://www.reddit.com/r/FromTheDepths/comments/1pvkd4b/need_help_fixing_ai_targeting/)  0:24 108 upvotes · 17 comments
How AI-generated references are polluting scientific papers r/skeptic • 3mo ago [
How AI-generated references are polluting scientific papers
](https://www.reddit.com/r/skeptic/comments/1qmnf7e/how_aigenerated_references_are_polluting/)  earth 97 upvotes · 6 comments
Reverse engineering a $1B Legal AI tool exposed 100k+ confidential files r/programming • 5mo ago [
Reverse engineering a $1B Legal AI tool exposed 100k+ confidential files
](https://www.reddit.com/r/programming/comments/1pddgdw/reverse_engineering_a_1b_legal_ai_tool_exposed/) 593 upvotes · 32 comments
Why Generative AI Coding Tools and Agents Do Not Work For Me r/programming • 10mo ago [
Why Generative AI Coding Tools and Agents Do Not Work For Me
](https://www.reddit.com/r/programming/comments/1ldb16m/why_generative_ai_coding_tools_and_agents_do_not/)  miguelgrinberg 288 upvotes · 269 comments
Be careful with Google's AI overview. r/palmbeach • 5mo ago [
Be careful with Google's AI overview.
](https://www.reddit.com/r/palmbeach/comments/1p8m8g4/be_careful_with_googles_ai_overview/)  56 upvotes · 13 comments
Introduction of our new rule against AI/ChatGPT and our general stance on it - from the Modteam.🛸💫 r/starseeds • 10mo ago [
Introduction of our new rule against AI/ChatGPT and our general stance on it - from the Modteam.🛸💫
](https://www.reddit.com/r/starseeds/comments/1ll9iqz/introduction_of_our_new_rule_against_aichatgpt/) 125 upvotes · 71 comments
Scientists create biological 'artificial intelligence' system r/EverythingScience • 10mo ago [
Scientists create biological 'artificial intelligence' system
](https://www.reddit.com/r/EverythingScience/comments/1lumicf/scientists_create_biological_artificial/)  medicalxpress 396 upvotes · 20 comments
Google literally just made the best way to create AI Agents r/AIAgentsInAction • 5mo ago [
Google literally just made the best way to create AI Agents
](https://www.reddit.com/r/AIAgentsInAction/comments/1p8zy8u/google_literally_just_made_the_best_way_to_create/) 43 upvotes · 13 comments
Google AI Pro Plan r/AntigravityGoogle • 3mo ago [
Google AI Pro Plan
](https://www.reddit.com/r/AntigravityGoogle/comments/1qmf71v/google_ai_pro_plan/)  26 upvotes · 21 comments
Community Info Section
r/programming
Join
programming
Computer Programming
Show more
Public
Anyone can view, post, and comment to this community
Top Posts
Reddit reReddit: Top posts of December 2, 2010
Reddit reReddit: Top posts of December 2010
Reddit reReddit: Top posts of 2010
Reddit Rules Privacy Policy User Agreement Your Privacy Choices Accessibility Reddit, Inc. © 2026. All rights reserved.
Expand Navigation
Expand Navigation
Collapse Navigation
Collapse Navigation 
0cAFcWeA5EXX0yjtM48wk3MzDlxdIYgxe7ijNBGCBMxIBskNMscSdmFrDMYzsv7YHbpTw12W_lw35XInX-xkUrsOa9VRxRqPysqksmGnG6dM6dIZ99uK4H8_Z0p-61owWdmvDA8zb7DMWGjj6IoBx5wh7FBphQkY49QtMmRuR-8puklWkgM_GyZNWcfG69YKZioKZAH_MbAmRU5KsuuyiAT4GORCqfFIFLZs0RePN328TxQ2denKRJlnU_lMJupa6HNJRK80bn7X1-qJLS30UZWDFYct_UiaxaJYhh1Co1bWe_XQ77YejgmUCZhkiicWO3mVnw0yUEqo5JKYJB7b0CcvWO8dZGouPI1rD7cqwGJBiAi33cMjNAtw6dwvd-Cz9yOhV_nGjq7ZDQHlLbKU7AFx6EuRGEG0ue3RmxA60Qj7eWjxFDMS9erfDRK2QTmccUqxmDb2qfsD8cmKpAoQjT5razJA3ejfWqHA48qXu7v4a6NetXiwYoXmFh2i3GNwZkLSwNk8yFfJZBNDyFq-f2kJEyYQ5JHIUJudAEkYSGvP1Dm1U-9ZluizQBrt7IdoNZWEB_7CAJRJjaXfpPM78RDF25VvqTuiwcIxaPC3ysjW2oh0FzV_gDLfGUjlopoIU92EaO5teo4_o7jha9pUcjzvaeR3AsfqKce1nGzUyEpdVG_XWwknTwowxoX0hPQJJ0X9Yrej0ovrVJfh-gWC6IcaFRoH51Jf2Tf1xVu3omsB6x4_eBgXuSVAkxHAS1dhrgcVWvBxm2JJENXifutqflVPleufXTEb68ofgawhNs1HPLWxSOb082hkyDGK_IBqwZ3JtqXm9F70PAJyeRm-AVbGYimE-8ku3P6F7pOReuGE7vr2RP2rEnhSAmYRI9_Ism7o0Dt7AcKM9Yy17TxLC-dE3GdbMSbYDw_1zQstthQ8nRK0zPRO-3eCi8D1Kwfzevac9-xuysxxxsvYCoZA4_SRLF5CE5wubY9qiFjCNx_vzYhubjgfN5e6uvQxXNvq-WUmzgM8gn94cSQsUG4rHsMKbEz4GFChGKZKDgsFCZMluL3FUvVHM86QfKzGmxLrTOB5Q8Nz3KB2QbQ-BxW2WPSnnYJ41w91wwJ0THlHIvNwMhIEqKNQes3_-Fd38xh-cWgGypQF6C_ZeZ9gpZMJ2umO24z-xN8TGoxkd_u4yM_8T7YPBlPnj-arqg30SyrE--0oJS6nartQenwzFl-G6LJPtl0KNOVTA6roF3KZcvxHTtbi9eYSWKlg8als3wlWjUiIoKwP7IJx_vzGTpw_vrDdgNI2FjUejv34rUBnOMPZhG827aRUjimWArPQbM_7ugqLZdbqeBbmKpyAFvgMGE0erejNWdL1wJoYqOKxN3RuxeqSBB4H-lXy84dPKHaocdKqclVE28z_p-Uq693mWEWskpgsK6aRebehTKB1Yd54o262dPCOUyTmB1qxsXXhUpUCZDDROHqZ0rE7GtUNrbxu49jh-ffaT7PzJx08ygkUOmWng3VMYNjRY66Fayiyi-KRcNooY_ERaiTgA3agXE2wug3cSAmx8XV1QXXwr6n9Pw0yyNBE8KaLfFpVQB738B4GgOQeS_6F-0a_ziafZFQV6ZYblIROJ_mhNXludq8dH7Qnyhh-kOHS-MikdbDOlUHYdC4FyulAJqZt0XltfLCDvshYQDMRif4IWUc1loC_eaWXqTDviL6_MVLrF5gBJkGEMqwD5O9_zUBH9XUczNUvMSUfhGt4xH8KkpnDT4zOphjI4o1K3x8Whj8Q-p9qU1IHTuJw8GK6RblmgWmbIJJ-dBXmeMmLgulZv6X85cJ1z0o0NBlTQ1esiXVuK62kYUtt7_r6eSRLMx13YKzS5myBAr3H5HsmCVqZwG_FDbFxe_uuKsKHCyRvlDSF_XHbmAkr_zcg4CMfNJRP_ZH07kyXmKWYAVAtbKaMxuOIctdlpSFxiC4TcM5XKjsQbXxUZb3LbBOd8khYR_zgOppfiZFfXM2dgww2q9p6OGUBuc0Zm-hzwyL5SDHbV-ehaEb3FcXoEo6_AGOXYNJx21KxlJdG6AIFoeW2gc8UaFi6vtsUNbiBTiJinxzmDF8_6S9EpFFCQYLYUZiiYBJn5vip_YphQN_CvY0B3zKuB7_C79PROyurY3UGUAFj7Sbmw6L516mIOJkKJ8H4P0n3H5k_hCfeCcEwF-ugQDATzdx08qbiD15y8ObcRj3i0