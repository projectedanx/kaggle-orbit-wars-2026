> Source: https://www.themoonlight.io/en/review/sea-ts-self-evolving-agent-for-autonomous-code-generation-of-time-series-forecasting-algorithms

[Literature Review] SEA-TS: Self-Evolving Agent for Autonomous Code Generation of Time Series Forecasting Algorithms
open navigation menu
Features
Pricing
FAQ
Blog
open navigation menu
Features
Pricing
FAQ
Blog
EN
Upload Paper
Get Started Free
Sign in
This page provides the most accurate and concise summary worldwide for the paper titled SEA-TS: Self-Evolving Agent for Autonomous Code Generation of Time Series Forecasting Algorithms. With Moonlight, your AI research colleague, you can effortlessly and quickly grasp all the papers you read. Install the Chrome extension from https://www.themoonlight.io/ or directly upload files on the web. Moonlight offers features tailored to your needs: - Text Explanation: AI simplifies complex concepts and paragraphs. - Image Explanation: One-click explanations of images, tables, and formulas. - AI Chat: Engage with AI to dive deeper into paper discussions. - Smart Citations: Instantly view information (title, author, summary) of cited papers without scrolling to the References. - Translation: Quickly translate unfamiliar words, sentences, or the entire page. - Auto Highlight: AI highlights key points automatically, helping you identify originality, methods, and results swiftly. - External Link Explanation: AI analyzes external sources and explains their relevance to your document. - Markup: Highlight important sentences and annotate to create personalized research notes. - Save and Share: Store documents in your library and easily share them. - Scholar Deep Search: Receive recommendations of relevant papers based on your stored documents.
[Literature Review] SEA-TS: Self-Evolving Agent for Autonomous Code Generation of Time Series Forecasting Algorithms
Open original PDF
Original Paper Blog Post
[
[Literature Review] SEA-TS: Self-Evolving Agent for Autonomous Code Generation of Time Series Forecasting Algorithms
](https://www.themoonlight.io/file?url=https%3A%2F%2Farxiv.org%2Fpdf%2F2603.04873)
AI Unlock SOTA time series forecasting: Discover the first agent to autonomously evolve novel, high-performance forecasting algorithms and surpass manual engineering.
Open with AI Viewer
Translation, summaries, and formula explanations - all in one AI paper viewer
The Self-Evolving Agent for Time Series Algorithms (SEA-TS) framework addresses the challenges in developing high-performance machine learning models for time series forecasting, which include data scarcity, poor adaptability to distribution shifts, and diminishing returns from manual iteration. Conventional LLM-based ML engineering agents suffer from reward hacking, simplistic reward mechanisms, limited reasoning context, and static prompts. SEA-TS mitigates these issues through an iterative self-evolution loop that autonomously generates, validates, and optimizes forecasting algorithm code.
The core methodology of SEA-TS is built upon three synergistic innovations:
Metric-Advantage Monte Carlo Tree Search (MA-MCTS): This innovation replaces conventional fixed rewards with a statistically normalized advantage score to provide discriminative search guidance. The search problem is formalized over the space of ML programs , aiming to find , where is a task-dependent evaluation metric. The search is modeled as a sequential decision process over a tree , where each node represents a complete solution state, containing its code , plan , metric , visit count , cumulative value , and a buggy flag .
Node Selection: A leaf node is selected for expansion using the Upper Confidence Bound for Trees (UCT): where is the exploration constant.
Metric Advantage Reward (M–A–R–Q Chain):
Metric ( ): The raw evaluation metric obtained by executing code : .
Advantage ( ): A standardized z-score computed from the historical metric distribution : This provides discriminative, adaptive, and metric-agnostic reward signals.
Reward ( ): The final reward incorporates the code review outcome:
Cumulative Value ( ): When node is created, its reward is backpropagated to all ancestors: , .
Code Review with Running Prompt Refinement: Every successfully executed solution undergoes automated logical review by an LLM reviewer. This review checks for common time series forecasting flaws like data leakage (e.g., using future information in rolling statistics), incorrect inverse normalization, train-test contamination, and other logical errors. If a logical flaw is detected, the buggy flag is set to true , leading to a penalty in the reward . Crucially, the running prompt Prun —a continuously evolving knowledge base—is updated after every code review and global node comparison. Both positive design patterns and corrective safeguards (e.g., specific instructions to prevent data leakage like "Apply .shift(1) before any rolling window computation") are distilled into Prun , ensuring that subsequent code generations learn from past successes and failures.
Global Steerable Reasoning: Unlike agents limited to local context, SEA-TS compares each newly evaluated non-buggy node against the global best ( ) and global worst ( ) solutions identified across the entire search history. An auxiliary LLM generates a structured comparison summary, identifying successful strategies to emulate and failure patterns to avoid. This Pglobal information is appended to the node's analysis and fed into the running prompt refinement, enabling cross-trajectory knowledge transfer and allowing "jumps" across the tree rather than purely incremental improvements.
Additionally, SEA-TS integrates a MAP-Elites quality-diversity archive to maintain architectural diversity. Solutions are indexed along three phenotypic dimensions relevant to time series forecasting: architecture type (e.g., tree-based to hybrid), feature engineering sophistication, and training sophistication. This archive preserves diverse high-performing solutions, preventing premature convergence.
The framework operates within a closed-loop self-evolution system, iterating through node selection, prompt assembly & code generation, sandbox execution & evaluation, code review & prompt update, and tree update. The prompt for code generation Pfull combines a base task description P0 , the accumulated running prompt Prun , parent/sibling context Context(Nparent) , global best/worst comparisons Pglobal , and samples from the MAP-Elites archive Parchive(A) .
In terms of computational complexity, the system makes at most four LLM calls per iteration (code generation, code review, global reasoning, prompt refinement). The wall-clock time is primarily dominated by the sandbox execution (training and evaluating generated ML models), which can range from minutes to hours per iteration, depending on model complexity and dataset size.
Empirical evaluation on the public Solar-Energy benchmark showed SEA-TS achieving a 40% MAE reduction relative to TimeMixer, surpassing state-of-the-art methods. On industry proprietary datasets, SEA-TS reduced WAPE by 8.6% on solar PV forecasting and 7.7% on residential load forecasting compared to human-engineered baselines, and achieved 26.17% MAPE on load forecasting versus 29.34% by TimeMixer.
Notably, the autonomously evolved models discovered novel architectural patterns, demonstrating the potential of autonomous ML engineering to generate genuinely new algorithmic ideas:
Physics-informed Monotonic Decay Head: For solar PV forecasting, a learnable head was discovered to explicitly encode the physical law of solar irradiance decline after solar noon, complete with regularization for physical monotonicity.
Per-station Learned Diurnal Cycle Profiles: Rather than a global pattern, the agent evolved per-station daily cycle profiles with fractional hour interpolation.
Learnable Hourly Bias Correction: For residential load forecasting, a novel magnitude-proportional bias correction ( out + bias[h] * |out| * 0.1 ) was discovered, with learnable hourly bias initialized with domain-informed priors.
Robust Preprocessing: The agent consistently favored MAD-based normalization for outlier robustness across tasks.
Limitations include the bounding of generated code quality by the LLM's capabilities and the high API costs due to frequent LLM calls. Future work will explore multi-objective optimization, context pruning, automated dimension discovery for MAP-Elites, advanced search algorithms, systematic domain knowledge injection, and combining coding and deep research agents within the framework.
Related Papers Go to library
Diffusion-TS: Interpretable Diffusion for General Time Series Generation
"Revolutionize time series generation: Diffusion-TS delivers SOTA realism and interpretability by uniquely decomposing temporal data."
Highlighted by 61 researchers!
View Review Read Paper
TS-LIF: A Temporal Segment Spiking Neuron Network for Time Series Forecasting
"Master multi-frequency time series forecasting with a novel dual-compartment spiking neuron capturing complex temporal dynamics."
View Review Read Paper
PAX-TS: Model-agnostic multi-granular explanations for time series forecasting via localized perturbations
"Unlock the first model-agnostic, multi-granular explanations for time series forecasting with PAX-TS's novel perturbation method."
View Review Read Paper
TS-Inverse: A Gradient Inversion Attack Tailored for Federated Time Series Forecasting Models
"Uncover privacy leaks in TSF: TS-Inverse is the first attack to effectively reconstruct federated time series data. Understand the threat."
View Review Read Paper
TS-Agent: A Time Series Reasoning Agent with Iterative Statistical Insight Gathering
"Solve LLM time series analysis pitfalls: TS-Agent combines LLMs with tools for verifiable, hallucination-free insights."
View Review Read Paper
AI One-Click Summary Real-time Translation AI Q&A
With Free AI PDF Viewer Revolutionize Your Paper Reading
Open This Paper in AI Viewer Now 
Terms of Use Privacy Policy Medium GitHub LinkedIn Email
Corca, Inc. / CEO Younghyun Chung / Business Registration Number 271-86-02206
6F, 11-8 Teheran-ro 77-gil, Gangnam-gu, Seoul, Republic of Korea, 06159
Contact 02-6925-6978 E-mail: moonlight@corca.ai
© 2026 Corca, Inc. All rights reserved.