> Source: https://arxiv.org/html/2603.04873v1

SEA-TS: Self-Evolving Agent for Autonomous Code Generation of Time Series Forecasting Algorithms
Report GitHub Issue
×
Title:
Content selection saved. Describe the issue below:
Description:
Submit without GitHub Submit in GitHub
 Back to arXiv
Why HTML? Report Issue Back to Abstract Download PDF  
Abstract
1 Introduction
2 Related Work
2.1 Automated Machine Learning
2.2 LLM-Based Machine Learning Engineering Agents
2.3 Quality-Diversity Optimization
2.4 Time Series Forecasting Methods
3 Methodology
3.1 Problem Formulation
3.2 Framework Overview and Self-Evolution Loop
3.3 Metric-Advantage Monte Carlo Tree Search (MA-MCTS)
3.3.1 Search Tree Structure
3.3.2 Node Selection via UCT
3.3.3 Metric Advantage Reward and the M M – A A – R R – Q Q Chain
Step 1: Metric 𝑴 𝒋 \boldsymbol{M_{j}} .
Step 2: Advantage 𝑨 𝒋 \boldsymbol{A_{j}} .
Step 3: Reward 𝑹 𝒋 \boldsymbol{R_{j}} .
Step 4: Cumulative Value 𝑸 𝒋 \boldsymbol{Q_{j}} .
3.4 Code Review with Running Prompt Refinement
3.4.1 Motivation
3.4.2 Automated Code Review
3.4.3 Running Prompt Refinement
3.5 Global Steerable Reasoning
3.5.1 Beyond Local Context
3.5.2 Comparison Prompt Construction
3.5.3 Cross-Trajectory Knowledge Transfer
3.6 MAP-Elites Quality-Diversity Archive
Task-Adaptive Dimension Definitions.
3.7 Computational Complexity Analysis
LLM Call Complexity.
Per-Call Token Estimates.
Wall-Clock Time.
4 Experiments
4.1 Setup
4.1.1 Datasets
Public Dataset.
Proprietary Datasets.
4.1.2 Baselines and Reference Code
4.1.3 Implementation Details
4.2 Results
4.2.1 Public Solar-Energy Benchmark
Evolved Architecture.
4.2.2 Proprietary Solar PV Forecasting
Evolved Architecture.
Monotonic Decay Head.
Daily Cycle Residual Head.
Soft Gating Mechanism.
4.2.3 Residential Load Forecasting
Evolved Architecture.
4.3 Discussion
4.3.1 Autonomously Discovered Patterns
4.3.2 Limitations
5 Conclusion and Future Work
References
A Prompt Templates
A.1 System Prompt (Role Definition)
A.2 Base Prompt (Task Description)
A.3 Code Review Prompt
A.4 Prompt Update Prompt
A.5 Running Prompt (Accumulated Insights)
B Evolved Code Examples
B.1 Solar PV: QuadHeadGatedSolar Model (Excerpt)
B.2 Load Forecasting: Dual-Branch Network (Excerpt)
License: CC BY-NC-ND 4.0
arXiv:2603.04873v1 [cs.AI] 05 Mar 2026
SEA-TS: S elf- E volving A gent for Autonomous Code Generation of T ime S eries Forecasting Algorithms
Longkun Xu luke.xu@ecoflow.com Xiaochun Zhang Qiantu Tuo Rui Li ricky.li@ecoflow.com
Abstract
Accurate time series forecasting underpins decision-making in numerous domains, yet conventional machine learning development paradigms suffer from data scarcity in new deployment scenarios, poor adaptability under distribution shift, and diminishing returns from manual model iteration. We propose Self-Evolving Agent for Time Series Algorithms (SEA-TS), a framework that autonomously generates, validates, and optimizes forecasting algorithm code through an iterative self-evolution loop. Our framework introduces three key innovations: (1) Metric-Advantage Monte Carlo Tree Search (MA-MCTS), which replaces conventional fixed rewards with a statistically normalized advantage score providing reward signals for discriminative search guidance; (2) Code Review with running prompt refinement, where every successfully executed solution undergoes automated logical review followed by running prompt updates that persistently encode corrective patterns, preventing recurrence of similar mistakes in all subsequent iterations; and (3) Global Steerable Reasoning, which compares each evaluated node against global best and worst solutions, enabling cross-trajectory knowledge transfer. We further adopt a MAP-Elites quality-diversity archive to maintain architectural diversity. On the public Solar-Energy benchmark, SEA-TS achieves a 40% MAE reduction relative to TimeMixer, surpassing state-of-the-art methods. On industry proprietary datasets, SEA-TS reduces WAPE by 8.6% on solar PV forecasting and 7.7% on residential load forecasting compared to human-engineered baselines, and achieves 26.17% MAPE on load forecasting versus 29.34% by TimeMixer. Notably, the evolved models autonomously discover novel architectural patterns not previously reported in the time series literature—including physics-informed monotonic decay heads that encode solar irradiance constraints, per-station learned diurnal cycle profiles, and learnable hourly bias correction—demonstrating the potential of autonomous ML engineering to generate genuinely novel algorithmic ideas beyond manual design.
keywords:
Self-evolving agent , Time series forecasting , Autonomous code generation , Monte Carlo tree search , Quality-diversity optimization † †
journal: Energy and AI
\affiliation
[inst1]organization=AI Lab, EcoFlow Inc., city=Shenzhen, country=China
1 Introduction
Developing high-performance machine learning models for time series forecasting remains a labor-intensive process that demands substantial domain expertise and iterative experimentation. Although the task spans numerous application domains—including energy systems [ 8, 23] , financial markets, supply chain logistics, healthcare monitoring, and environmental science—the fundamental challenges are shared across all settings. We identify three pervasive obstacles in the conventional ML development pipeline (data collection → \rightarrow dataset construction → \rightarrow model design → \rightarrow training → \rightarrow deployment):
(i) Data scarcity: Many practical forecasting scenarios lack sufficient historical data. Newly deployed systems, emerging markets, or rare event prediction all face a prolonged cold-start period where training reliable models is infeasible [ 21] . This data scarcity problem is especially severe for tasks requiring seasonal coverage ( e.g., one year of data to capture annual patterns).
(ii) Distribution shift: Real-world time series are inherently non-stationary. Equipment degradation, policy changes, evolving user behaviors, and environmental shifts cause the data distribution to drift continuously. Models trained on historical data degrade under these shifted conditions, necessitating frequent and costly human intervention for retraining and adaptation.
(iii) Diminishing marginal returns: As models approach their performance ceiling, each incremental accuracy improvement requires disproportionately more engineering effort. For instance, once a practitioner improves accuracy from 85% to 90%, further gains yield diminishing returns on investment [ 7] , making manual iteration economically unsustainable.
Recent advances in Large Language Models (LLMs) have opened a new paradigm: using LLMs as machine learning engineers (MLE) that autonomously write, execute, evaluate, and iteratively improve ML code [ 9, 3] . Frameworks such as AIDE [ 27] and ML-Master [ 16] have demonstrated that LLM-based agents, combined with tree search strategies, can generate competitive ML solutions across diverse tasks. However, existing approaches suffer from several limitations:
• Reward hacking and “cheating code”: Agents driven by metric optimization frequently produce code with logical flaws ( e.g., data leakage in time series tasks) that yield artificially inflated scores but fail in deployment. Such flaws do not cause runtime errors, making them difficult to detect without explicit code review [ 1] .
• Simplistic reward mechanisms: Existing approaches typically use binary or fixed rewards ( e.g., + 1 +1 for any improvement [ 16] ), which fail to distinguish marginal gains from significant breakthroughs, leading to inefficient search.
• Limited reasoning context: Most agents reference only local information (parent/sibling nodes) when generating new code, lacking global awareness of best and worst solutions across the entire search history.
• Static prompts: System prompts remain fixed throughout the search, missing opportunities for on-the-fly adaptation based on discovered failure modes or successful patterns.
To address these challenges, we propose the Self-Evolving Agent for Time Series Algorithms (SEA-TS) framework with three synergistic innovations:
Metric-Advantage Monte Carlo Tree Search (MA-MCTS): We replace fixed rewards with a statistically normalized advantage score computed from the full metric distribution, enabling discriminative guidance toward high-potential trajectories.
Code Review with running prompt refinement: Every successfully executed solution undergoes automated logical review. The review findings—together with insights from global node comparisons—are distilled into a continuously evolving running prompt that prevents recurrence of identified issues in all subsequent iterations.
Global Steerable Reasoning: We compare each evaluated node against the global best and worst solutions, enabling cross-trajectory knowledge transfer and avoiding redundant exploration.
Additionally, we integrate a MAP-Elites quality-diversity archive [ 17] to maintain diverse elite solutions across architectural dimensions. We evaluate SEA-TS on energy forecasting as a representative time series domain, demonstrating significant improvements over both human-engineered baselines and published SOTA methods. Notably, the agent autonomously discovers genuinely novel architectural patterns—such as physics-informed monotonic decay heads and per-station learned diurnal profiles—that is novel in the community of time series forecasting.
The main contributions of this paper are:
• A general-purpose self-evolving MLE agent framework unifying metric-advantage tree search, automated code review with running prompt refinement, and global steerable reasoning for autonomous algorithm development.
• The Metric Advantage reward mechanism providing statistically meaningful signals that significantly improve search efficiency.
• Demonstration that autonomously evolved models can discover genuinely novel architectural patterns beyond established techniques, achieving SOTA performance on public benchmarks and substantial improvements on industry datasets.
The source code of SEA-TS will be made available to reviewers during the peer review process and released publicly upon acceptance.
The remainder of this paper is organized as follows. Section 2 reviews related work. Section 3 presents the SEA-TS framework with formal problem formulation and complexity analysis. Section 4 presents experimental setup, results, and discussion. Section 5 concludes with directions for future work.
2 Related Work
2.1 Automated Machine Learning
Traditional AutoML approaches, including neural architecture search (NAS) [ 34, 13] and hyperparameter optimization [ 5] , operate over predefined architectural spaces. While NAS searches over predefined archtecture spaces, LLM-based agents instead generate arbitrary code—including novel feature engineering, custom loss functions, and domain-specific inductive biases—operating at a fundamentally different abstraction level.
2.2 LLM-Based Machine Learning Engineering Agents
The emergence of powerful LLMs has enabled automated ML systems where the LLM acts as a programmer. AIDE [ 27] pioneered this approach using greedy search. ML-Master [ 16] incorporated MCTS and steerable reasoning, achieving SOTA on MLE-Bench among open-source solutions [ 33] . I-MCTS [ 12] introduced hybrid rewarding to balance exploration and exploitation. R&D-Agent [ 30] combined multi-trajectory exploration with a multi-agent framework. However, these systems share common limitations: vulnerability to reward hacking without explicit code review, limited reward granularity, and narrow reasoning context confined to local search neighborhoods. Our work addresses all three simultaneously.
2.3 Quality-Diversity Optimization
MAP-Elites [ 17] and its variants maintain archives of diverse high-performing solutions indexed by behavioral features. AlphaEvolve [ 19] and OpenEvolve [ 20] have applied quality-diversity principles to LLM-based program synthesis. We adapt this paradigm to maintain architectural diversity in generated ML solutions.
2.4 Time Series Forecasting Methods
Time series forecasting has been extensively studied, from statistical models to deep learning. Transformer-based models have shown strong performance on long-horizon tasks [ 32, 29, 18] , though debate on their effectiveness remains [ 31] . TimeMixer [ 24] proposed multi-scale mixing, and iTransformer [ 14] introduced inverted attention. For domain-specific applications, hybrid models combining physical knowledge with data-driven approaches have been widely adopted [ 4, 10, 8, 25] . Despite these advances, adapting such models for specific deployment scenarios remains labor-intensive.
3 Methodology
3.1 Problem Formulation
We formalize autonomous algorithm development as a search problem over the space of programs. Let Π \Pi denote the set of all syntactically valid ML programs that can be generated by an LLM. Given a dataset 𝒟 = ( 𝒟 train , 𝒟 val , 𝒟 test ) \mathcal{D}=(\mathcal{D}{\text{train}},\mathcal{D}{\text{val}},\mathcal{D}_{\text{test}}) and an evaluation metric ℒ : Π × 𝒟 → ℝ \mathcal{L}:\Pi\times\mathcal{D}\to\mathbb{R} , the objective is:
π ∗ = arg  min π ∈ Π  ℒ  ( π  ( 𝒟 train ) , 𝒟 test ) , \pi^{*}=\arg\min_{\pi\in\Pi};\mathcal{L}!\left(\pi(\mathcal{D}{\text{train}}),;\mathcal{D}{\text{test}}\right),
(1)
where π  ( 𝒟 train ) \pi(\mathcal{D}_{\text{train}}) denotes the trained model produced by executing program π \pi on training data, and ℒ \mathcal{L} is task-dependent ( e.g., WAPE, MAPE, or MAE).
Since Π \Pi is combinatorially vast and lacks tractable gradients, we model the search as a sequential decision process over a tree 𝒯 = ( 𝒱 , ℰ ) \mathcal{T}=(\mathcal{V},\mathcal{E}) , where each vertex N j ∈ 𝒱 N_{j}\in\mathcal{V} represents a complete solution state and each edge ( N i , N j ) ∈ ℰ (N_{i},N_{j})\in\mathcal{E} represents a refinement operation. The root N 0 N_{0} contains an initial reference implementation.
3.2 Framework Overview and Self-Evolution Loop
The SEA-TS framework operates as a closed-loop self-evolution system ( Figure 1). At each iteration t ∈ { 1 , … , T } t\in{1,\ldots,T} , the system executes five phases: (1) Node Selection via UCT; (2) Prompt Assembly & Code Generation; (3) Sandbox Execution & Evaluation; (4) Code Review & Prompt Update for every non-buggy node; and (5) Tree Update including reward computation, backpropagation, and archive maintenance.
The prompt for code generation is composed as:
𝒫  ( N parent , 𝒯 ) = 𝒫 0 ⊕ 𝒫 run ⊕ Context  ( N parent ) ⊕ 𝒫 global  ( 𝒯 ) ⊕ 𝒫 archive  ( 𝒜 ) , \mathcal{P}(N_{\text{parent}},\mathcal{T})=\mathcal{P}{0}\oplus\mathcal{P}{\text{run}}\oplus\textsc{Context}(N_{\text{parent}})\oplus\mathcal{P}{\text{global}}(\mathcal{T})\oplus\mathcal{P}{\text{archive}}(\mathcal{A}),
(2)
where 𝒫 0 \mathcal{P}{0} is the base task description (fixed), 𝒫 run \mathcal{P}{\text{run}} is the accumulated running prompt (continuously updated), Context  ( N parent ) \textsc{Context}(N_{\text{parent}}) provides parent and sibling node information, 𝒫 global \mathcal{P}{\text{global}} contains global best/worst comparisons, and 𝒫 archive \mathcal{P}{\text{archive}} samples from the MAP-Elites archive 𝒜 \mathcal{A} . Illustrative prompt templates are provided in Appendix A.
Algorithm 1 formalizes the complete procedure.
Algorithm 1 Self-Evolving Agent for Time Series Algorithms (SEA-TS)
0: Base prompt 𝒫 0 \mathcal{P}_{0} , dataset 𝒟 \mathcal{D} , budget T T , exploration constant C C
1: Initialize tree with root N 0 N_{0} (reference code), 𝒫 run ← ∅ \mathcal{P}_{\text{run}}\leftarrow\emptyset , ℳ ← ∅ \mathcal{M}\leftarrow\emptyset
2: Initialize MAP-Elites archive 𝒜 \mathcal{A} with dimensions ( d 1 , d 2 , d 3 ) (d_{1},d_{2},d_{3})
3: for t = 1 t=1 to T T do
4: Phase 1 – Node Selection:
5: Select leaf N parent N_{\text{parent}} via UCT  ( N j ) = Q j / n j + C  ln  n parent / n j \text{UCT}(N_{j})=Q_{j}/n_{j}+C\sqrt{\ln n_{\text{parent}}/n_{j}}
6: Phase 2 – Prompt Assembly & Code Generation:
7: 𝒫 full ← 𝒫 0 ⊕ 𝒫 run ⊕ Context  ( N parent ) ⊕ 𝒫 global ⊕ 𝒫 archive \mathcal{P}{\text{full}}\leftarrow\mathcal{P}{0}\oplus\mathcal{P}{\text{run}}\oplus\textsc{Context}(N{\text{parent}})\oplus\mathcal{P}{\text{global}}\oplus\mathcal{P}{\text{archive}}
8: c j ← LLM  ( 𝒫 full ) c_{j}\leftarrow\textsc{LLM}(\mathcal{P}_{\text{full}})
9: Phase 3 – Sandbox Execution & Evaluation:
10: Execute c j c_{j} in sandbox; obtain metric M j ← ℒ  ( c j  ( 𝒟 train ) , 𝒟 test ) M_{j}\leftarrow\mathcal{L}(c_{j}(\mathcal{D}{\text{train}}),\mathcal{D}{\text{test}})
11: ℳ ← ℳ ∪ { M j } \mathcal{M}\leftarrow\mathcal{M}\cup{M_{j}}
12: Phase 4 – Code Review & Prompt Update (all non-buggy nodes):
13: if N j N_{j} executed without errors then
14: b j ← CodeReview  ( c j ) b_{j}\leftarrow\textsc{CodeReview}(c_{j}) {Logical review}
15: Compare N j N_{j} with N ∗ N^{*} , N ⊥ N_{\bot} via Global Steerable Reasoning
16: Update 𝒫 run \mathcal{P}_{\text{run}} with review findings and reasoning insights
17: else
18: b j ← true b_{j}\leftarrow\text{true}
19: end if
20: Phase 5 – Tree Update:
21: Compute A j ← ( μ  ( ℳ ) − M j ) / σ  ( ℳ ) A_{j}\leftarrow(\mu(\mathcal{M})-M_{j})/\sigma(\mathcal{M}) {Metric Advantage}
22: R j ← { − 1 if  b j = true A j otherwise R_{j}\leftarrow\begin{cases}-1&\text{if }b_{j}{=}\text{true}\ A_{j}&\text{otherwise}\end{cases}
23: Backpropagate: Q i ← Q i + R j , n i ← n i + 1 Q_{i}\leftarrow Q_{i}+R_{j},;n_{i}\leftarrow n_{i}+1 for all N i ∈ path  ( N j , N 0 ) N_{i}\in\text{path}(N_{j},N_{0})
24: if M j M_{j} is new global best and b j = false b_{j}{=}\text{false} then
25: N ∗ ← N j N^{*}\leftarrow N_{j}
26: end if
27: Update N ⊥ N_{\bot} , MAP-Elites archive 𝒜 \mathcal{A}
28: end for
29: return Best non-buggy solution N ∗ N^{*} 
Figure 1: Overview of the SEA-TS framework. The system iteratively generates, evaluates, and refines ML code through a closed-loop combining MA-MCTS search, code review with running prompt refinement, and global steerable reasoning.
3.3 Metric-Advantage Monte Carlo Tree Search (MA-MCTS)
3.3.1 Search Tree Structure
Each node N j N_{j} in the search tree represents a complete solution state. While the code c j c_{j} is the executable artifact—a self-contained Python program—the node N j N_{j} encapsulates additional metadata:
• Code c j ∈ Σ ∗ c_{j}\in\Sigma^{*} : the full Python ML program (immutable once created)
• Plan p j p_{j} : the design rationale and approach description
• Metric M j ∈ ℝ M_{j}\in\mathbb{R} : the evaluation performance ( e.g., WAPE, MAPE)
• Visit count n j ∈ ℕ n_{j}\in\mathbb{N} and cumulative value Q j ∈ ℝ Q_{j}\in\mathbb{R} , see Figure 1
• Buggy flag b j ∈ { true , false } b_{j}\in{\text{true},\text{false}} : whether code was identified as logically flawed
The search algorithm operates on nodes (selecting, expanding, backpropagating), while the LLM and sandbox operate on code (generating, executing, evaluating). A node's code c j c_{j} is immutable, but its MCTS statistics ( n j n_{j} , Q j Q_{j} ) are continuously updated via backpropagation.
3.3.2 Node Selection via UCT
The agent selects a leaf node for expansion using the standard Upper Confidence Bound for Trees (UCT):
UCT  ( N j ) = Q j n j ⏟ exploitation + C  ln  n parent n j ⏟ exploration , \text{UCT}(N_{j})=\underbrace{\frac{Q_{j}}{n_{j}}}{\text{exploitation}}+\underbrace{C\sqrt{\frac{\ln n{\text{parent}}}{n_{j}}}}_{\text{exploration}},
(3)
where C > 0 C>0 is the exploration constant. The default option in this work is using a fixed constant C C (1.41) while it can be decayed over the budget to shift from exploration to exploitation, supporting linear ( C t = max  ( C 0 − α  t , C min ) C_{t}=\max(C_{0}-\alpha t,C_{\min}) ), exponential ( C t = max  ( C 0  γ t , C min ) C_{t}=\max(C_{0}\gamma^{t},C_{\min}) ), and piecewise schedules.
3.3.3 Metric Advantage Reward and the M M – A A – R R – Q Q Chain
A key innovation is the Metric Advantage Reward, which replaces fixed rewards with a statistically normalized signal. The four key quantities form a causal chain:
M j → standardize A j → review R j → backprop Q j M_{j}\xrightarrow{\text{standardize}}A_{j}\xrightarrow{\text{review}}R_{j}\xrightarrow{\text{backprop}}Q_{j}
(4)
Step 1: Metric 𝑴 𝒋 \boldsymbol{M_{j}} .
The raw evaluation metric obtained by executing code c j c_{j} :
M j = ℒ  ( c j  ( 𝒟 train ) , 𝒟 test ) . M_{j}=\mathcal{L}(c_{j}(\mathcal{D}{\text{train}}),\mathcal{D}{\text{test}}).
(5)
Step 2: Advantage 𝑨 𝒋 \boldsymbol{A_{j}} .
Given historical metrics ℳ = { M 1 , … , M n } \mathcal{M}={M_{1},\ldots,M_{n}} , the advantage is the standardized z-score:
A j = { μ  ( ℳ ) − M j σ  ( ℳ ) if lower is better ( e.g. , WAPE) M j − μ  ( ℳ ) σ  ( ℳ ) if higher is better ( e.g. , accuracy) A_{j}=\begin{cases}\displaystyle\frac{\mu(\mathcal{M})-M_{j}}{\sigma(\mathcal{M})}&\text{if lower is better ({e.g.}, WAPE)}\[8.0pt] \displaystyle\frac{M_{j}-\mu(\mathcal{M})}{\sigma(\mathcal{M})}&\text{if higher is better ({e.g.}, accuracy)}\end{cases}
(6)
where μ  ( ℳ ) \mu(\mathcal{M}) and σ  ( ℳ ) \sigma(\mathcal{M}) are the mean and standard deviation of the historical distribution. By construction, A j A_{j} has zero mean and unit variance over ℳ \mathcal{M} , providing discriminative ( A j ≫ 1 A_{j}\gg 1 for breakthroughs), adaptive (scale adjusts as ℳ \mathcal{M} evolves), and metric-agnostic reward signals.
Step 3: Reward 𝑹 𝒋 \boldsymbol{R_{j}} .
The final reward incorporates the code review outcome:
R j = { − 1 if  b j = true A j otherwise R_{j}=\begin{cases}-1&\text{if }b_{j}=\text{true}\ A_{j}&\text{otherwise}\end{cases}
(7)
where b j b_{j} can be set during execution (runtime errors) or by the code review ( Section 3.4).
Step 4: Cumulative Value 𝑸 𝒋 \boldsymbol{Q_{j}} .
When node N k N_{k} is created as a descendant, its reward R k R_{k} is backpropagated:
Q j ← Q j + R k , n j ← n j + 1 , ∀ N j ∈ path  ( N k , N 0 ) . Q_{j}\leftarrow Q_{j}+R_{k},\quad n_{j}\leftarrow n_{j}+1,\quad\forall,N_{j}\in\text{path}(N_{k},N_{0}).
(8)
Thus Q j = ∑ k ∈ desc  ( j ) R k Q_{j}=\sum_{k\in\text{desc}(j)}R_{k} , and UCT uses Q j / n j Q_{j}/n_{j} as the exploitation term. Breakthrough solutions ( A j ≫ 1 A_{j}\gg 1 ) boost Q j / n j Q_{j}/n_{j} for all ancestors; buggy code ( R j = − 1 R_{j}=-1 ) penalizes the entire ancestor path. As ℳ \mathcal{M} evolves and σ  ( ℳ ) \sigma(\mathcal{M}) shrinks, the same absolute improvement yields larger A j A_{j} , naturally intensifying exploitation as the search matures.
3.4 Code Review with Running Prompt Refinement
3.4.1 Motivation
In time series forecasting, the most insidious form of reward hacking is data leakage—inadvertently using future information in feature construction. Computing rolling statistics without proper temporal shifts allows the model to “see” future values, yielding artificially low error metrics. These issues motivate dedicated review mechanisms.
3.4.2 Automated Code Review
After each candidate solution N j N_{j} is executed without runtime errors, it undergoes automated logical review by an LLM reviewer. Our framework reviews every non-buggy node to prevent flawed solutions from contributing false positive rewards through backpropagation. The reviewer analyzes the code for:
(a) Data leakage in feature engineering (use of future information)
(b) Incorrect inverse normalization in evaluation
(c) Train-test contamination in data splits
(d) Logical errors in model inference code
(e) Checkpoint/parameter mismatches
The reviewer outputs a binary judgment b j ∈ { true , false } b_{j}\in{\text{true},\text{false}} , where b j = true b_{j}=\text{true} indicates a detected logical flaw. This conservative strategy prioritizes reliability—falsely rejecting a valid solution is preferable to allowing a flawed one to corrupt Q j Q_{j} values through backpropagation.
3.4.3 Running Prompt Refinement
Crucially, the running prompt 𝒫 run \mathcal{P}{\text{run}} is updated after every code review and global node comparison—not only when issues are detected. Both the review findings and the Global Steerable Reasoning insights ( Section 3.5) are distilled by an auxiliary LLM into actionable updates integrated into 𝒫 run \mathcal{P}{\text{run}} . For example, if data leakage is detected:
“All features for a given timestamp must be calculated using ONLY information from previous timestamps. Apply .shift(1) before any rolling window computation to prevent data leakage.”
This continuous refinement ensures that the prompt progressively accumulates both corrective safeguards and positive design patterns, creating a self-improving knowledge base for all subsequent code generation.
3.5 Global Steerable Reasoning
3.5.1 Beyond Local Context
Standard MCTS-based MLE agents generate code based only on parent/sibling node information. [ 16] We provide a global view by comparing each newly evaluated non-buggy node against the global best ( N ∗ N^{*} ) and worst ( N ⊥ N_{\bot} ) solutions. The resulting reasoning is appended to the node's analysis, so that when it later serves as a parent, its children inherit the global insights.
3.5.2 Comparison Prompt Construction
At each evaluation step, we construct a structured comparison:
𝒫 global = { ( c ∗ , p ∗ , M ∗ ) , ( c ⊥ , p ⊥ , M ⊥ ) , ( c j , p j , M j ) } , \mathcal{P}{\text{global}}={(c^{},p^{},M^{*}),;(c{\bot},p_{\bot},M_{\bot}),;(c_{j},p_{j},M_{j})},
(9)
where ( c ∗ , p ∗ , M ∗ ) (c^{},p^{},M^{*}) is the global best, ( c ⊥ , p ⊥ , M ⊥ ) (c_{\bot},p_{\bot},M_{\bot}) the global worst, and ( c j , p j , M j ) (c_{j},p_{j},M_{j}) the current node. An auxiliary LLM generates a structured summary identifying successful strategies to emulate, failure patterns to avoid, and specific code-level recommendations.
3.5.3 Cross-Trajectory Knowledge Transfer
Global Steerable Reasoning enables cross-trajectory knowledge transfer: insights from one search branch inform generation in entirely different branches, allowing “jumps” across the tree rather than purely incremental improvements. The comparison summary is also fed into the running prompt refinement, persistently encoding strategies in 𝒫 run \mathcal{P}_{\text{run}} .
3.6 MAP-Elites Quality-Diversity Archive
To prevent convergence to a narrow set of architectures, we integrate a MAP-Elites archive indexing solutions along three phenotypic dimensions:
Architecture type ( d 1 d_{1} ): Tree-based (0.0) → \to decomposition (0.4) → \to attention (0.6) → \to hybrid (1.0).
Feature engineering sophistication ( d 2 d_{2} ): None (0.0) → \to extensive (1.0) including lags, rolling statistics, and Fourier features, etc.
Training sophistication ( d 3 d_{3} ): Basic (0.0) → \to advanced (1.0) including learning rate scheduling, dropout, regularization, and adaptive loss functions, etc.
Each cell maintains only the best solution, creating a curated collection of diverse elites. We further enhance diversity through an Island Model [ 28] with periodic migration.
Task-Adaptive Dimension Definitions.
The dimensions above target time series forecasting. The implementation accepts configurable dimension definitions, but automating dimension selection from task characteristics remains an open challenge addressed in future work.
3.7 Computational Complexity Analysis
LLM Call Complexity.
Each search iteration generates one tree node and invokes the LLM at most four times: (1) code generation, (2) code review, (3) global steerable reasoning, and (4) running prompt refinement. Calls (2)–(4) are triggered only for non-buggy nodes. With a budget of T T iterations, the total number of LLM calls is bounded by 4  T 4T . In our experiments ( T = 500 T{=}500 ), the observed call count is at most 2,000 per experiment.
Per-Call Token Estimates.
Table 1 summarizes the estimated input and output token ranges per call type, measured from our experimental runs. The base prompt 𝒫 0 \mathcal{P}{0} constitutes the largest input component ( ∼ {\sim} 30–50K tokens), while the running prompt 𝒫 run \mathcal{P}{\mathrm{run}} grows gradually across iterations.
Table 1: Estimated input/output token ranges per LLM call type.
Wall-Clock Time.
The wall-clock time is dominated by sandbox execution—actually training and evaluating the generated ML models—rather than by LLM inference. The execution time per iteration varies from minutes (for lightweight models such as gradient-boosted trees) to several hours (for deep neural networks with multi-epoch training), depending on dataset size and the algorithm complexity of the generated code. With parallel sandbox execution ( P P concurrent workers), the total wall-clock time for a full experiment is typically within one week. Algorithmic overhead (UCT selection, backpropagation, archive updates) is negligible in comparison.
4 Experiments
4.1 Setup
4.1.1 Datasets
We evaluate SEA-TS on energy time series forecasting using both public benchmarks and industry proprietary datasets. While the framework is domain-agnostic, energy forecasting provides a practically important evaluation domain with well-established baselines.
Public Dataset.
Solar-Energy [ 11] : Solar power production records from 137 PV plants in Alabama at 10-minute intervals, with standard train/val/test splits.
Proprietary Datasets.
Proprietary PV: Hourly solar generation from multiple distributed PV stations (Oct 2023–Mar 2025; train: Oct 2023–Oct 2024, val: Oct–Dec 2024, test: Dec 2024–Mar 2025). Proprietary Load: Hourly residential electricity consumption (May–Oct 2025) with high inter-user variability.
Note that in the current version of the manuscript, we do not include a public dataset for electricity load. However, TimeMixer also reaches SOTA performance on the ECL (Electricity Consuming Load) dataset [ 24, 32] , demonstrating its strength in both solar energy and load forecasting. We therefore additionally evaluate SEA-TS against TimeMixer on our proprietary load dataset using MAPE as the metric.
4.1.2 Baselines and Reference Code
For each task, SEA-TS starts from a provided baseline reference code (see Table 2). The SOTA performance of TimeMixer [ 24] and Timer [ 15] in solar energy forecasting and load forecasting tasks have been proved in their original paper. The reference code defines the data loading pipeline, evaluation metric computation, and an initial model implementation. The agent iteratively improves upon this starting point through the self-evolution loop.
Table 2: Summary of experimental tasks, baselines, reference code, and evaluation setup.
4.1.3 Implementation Details
SEA-TS uses GPT-5 (high reasoning effort) for code generation and code review, and Qwen3-coder-plus as an alternative model. The MCTS exploration constant is C = 2 C=\sqrt{2} , with budget T = 500 T=500 iterations per task. The MAP-Elites archive uses 7 3 = 343 7^{3}=343 cells. We include the remaining iteration count in the prompt to encourage exploration of underexplored approaches in later stages, following [ 6] . Experiments are conducted on Microsoft Azure cloud infrastructure. The source code of SEA-TS will be made available to reviewers during the peer review process and released publicly upon acceptance.
4.2 Results
4.2.1 Public Solar-Energy Benchmark
On the public Solar-Energy benchmark, the evolved model achieves a 40% reduction in MAE compared to TimeMixer [ 24] . Using the official TimeMixer code with inverse transform, test MAE is 2.929; our generated code achieves 1.757.
Evolved Architecture.
The agent evolved DiurnalMultiScaleGatedLinear, a six-head gated network with multi-scale seasonal-trend decomposition and MLP-Mixer blocks [ 22] . The input 𝐱 ∈ ℝ B × L × N v \mathbf{x}\in\mathbb{R}^{B\times L\times N_{v}} ( L = 96 L{=}96 , N v = 137 N_{v}{=}137 ) is processed at three temporal scales (full, 2 × 2\times downsampled, 4 × 4\times downsampled), each decomposed into trend and seasonal components via moving-average kernels. Three auxiliary heads complement the multi-scale decomposition: a Fixed-Basis Fourier Head (up to 24 harmonics), a Diurnal Bias Head with dual-frequency sinusoidal features and learnable per-station scaling 𝐬 ∈ ℝ N v \mathbf{s}\in\mathbb{R}^{N_{v}} , and a Daily Copy Head capturing diurnal persistence.
The six expert outputs are combined through station-hour gating:
𝐲 ^ t , i = ∑ k = 1 6 w k  ( i , τ t ) ⋅ f k  ( 𝐱 ) t , i , w k = exp  ( g i , k st + g t , k τ ) ∑ k ′ exp  ( g i , k ′ st + g t , k ′ τ ) , \hat{\mathbf{y}}{t,i}=\sum{k=1}^{6}w_{k}(i,\tau_{t})\cdot f_{k}(\mathbf{x}){t,i},\quad w{k}=\frac{\exp(g^{\text{st}}{i,k}+g^{\tau}{t,k})}{\sum_{k^{\prime}}\exp(g^{\text{st}}{i,k^{\prime}}+g^{\tau}{t,k^{\prime}})},
(10)
where g i , k st g^{\text{st}}{i,k} are station-specific gate logits from learnable embeddings and g t , k τ g^{\tau}{t,k} are hour-conditioned logits. The training uses a daylight-weighted Huber loss with predictions clamped to non-negative values and zeroed during nighttime. The agent independently selected MAD scaling over standard normalization for robustness to sensor outliers.
4.2.2 Proprietary Solar PV Forecasting
TimeMixer gives test WAPE of 25.75%; SEA-TS generated code achieves 17.12%, a reduction of 8.6% compared to the human-engineered baseline.
Evolved Architecture.
The agent evolved a seven-head gated MoE architecture (QuadHeadGatedSolar). Table 3 classifies all heads ranked by novelty—from genuinely novel patterns to applications of existing techniques.
Table 3: Expert heads in the evolved QuadHeadGatedSolar model.
The four novel heads ( ⋆ \star ) are the most significant findings:
Monotonic Decay Head.
This head directly encodes the physical law that solar irradiance declines monotonically after solar noon. It uses learnable amplitude, decay rate, and pivot hour parameters with a sigmoid gating function. A regularization term penalizes positive slopes during hours 15–18. This physics-informed design was not present in any reference code or prompted instruction; the agent discovered it autonomously.
Daily Cycle Residual Head.
Rather than learning a single global diurnal pattern, this head maintains per-station profiles with fractional hour interpolation, enabling adaptation to station-specific shading, panel orientation, and local microclimate effects.
Soft Gating Mechanism.
All seven heads are combined through soft gating conditioned on station identity, hour-of-day, and horizon position:
y ^ = ∑ h = 1 7 w h  ( 𝐬 , τ , 𝐩 ) ⋅ f h  ( 𝐱 ) , \hat{y}=\sum_{h=1}^{7}w_{h}(\mathbf{s},\tau,\mathbf{p})\cdot f_{h}(\mathbf{x}),
(11)
where w h w_{h} are softmax-normalized gate weights with learnable hour-based prior biases. The gating temperature is annealed from 1.0 to 0.7 during training. MAD scaling handles sensor noise outliers.
4.2.3 Residential Load Forecasting
We evaluate load forecasting against two SOTA baselines. Using Timer [ 15] , test WAPE is 47.47%; SEA-TS reduces WAPE by 7.7% to 39.74%. Using TimeMixer [ 24] , which is also SOTA on load forecasting benchmarks, test MAPE is 29.34%; SEA-TS achieves 26.17%, a reduction of 3.17%.
Evolved Architecture.
The evolved Dual-Branch Network (ImprovedDualBranchNet) comprises an MLP feature encoder for temporal features, a user embedding branch learning per-household representations, and a learnable 24-hour bias vector initialized with domain-informed priors (upward for nighttime, downward for daytime). The learnable hourly bias is a novel pattern: rather than using fixed time-of-day features, the agent discovered that a proportional bias correction ( out + bias  [ h ] ⋅ | out | ⋅ 0.1 \text{out}+\text{bias}[h]\cdot|\text{out}|\cdot 0.1 ) conditioned on the prediction magnitude itself yields better calibration. The user embedding branch for consumption patterns were also autonomously discovered.
4.3 Discussion
4.3.1 Autonomously Discovered Patterns
The most compelling finding is that SEA-TS discovers novel and robust architectural patterns:
• Physics-informed constraints: The Monotonic Decay Head encodes solar irradiance physics as a learnable architectural component with explicit regularization—a design pattern autonomously discovered without any physics-related prompting.
• Robust preprocessing: The agent consistently selected MAD-based normalization over standard scaling across multiple tasks, demonstrating emergent preference for outlier-robust methods.
• Learnable hourly bias: The magnitude-proportional bias correction in load forecasting represents a novel calibration technique.
• User segmentation: The agent independently discovered that filtering anomalous users improves aggregate prediction quality.
4.3.2 Limitations
• Generated code quality is generally bounded by the LLM's coding capabilities. Although in base prompt we use deep research agent (such as SciMaster [ 2] ) to inject domain knowledge from papers and codebases, we notice GPT-5 (with high reasoning effort) generates more sophisticated algorithm code compared with Qwen3-coder-plus. Besides, how to combine coding agent and deep research agent in one framework to generate expert-level algorithms deserves further study.
• Frequent LLM calls incur high API costs. Future work will investigate context pruning [ 26] to reduce token consumption.
5 Conclusion and Future Work
We presented SEA-TS, a self-evolving MLE agent framework for autonomous time series forecasting algorithm development. By integrating Metric-Advantage MCTS, code review with running prompt refinement, global steerable reasoning, and quality-diversity optimization, SEA-TS autonomously generates high-quality forecasting solutions that surpass both human-engineered and SOTA baselines. The framework discovers novel and robust architectural patterns—including physics-informed monotonic decay heads, per-station diurnal profiles, and learnable hourly bias correction—demonstrating that autonomous ML engineering can generate algorithmic innovations beyond manual design.
Future work will focus on:
• Multi-objective optimization: Jointly optimizing accuracy, inference latency, and model size for deployment-aware generation.
• Context pruning: Reducing prompt length and API costs via techniques such as SWE-Pruner [ 26] .
• Automated dimension discovery: Automatically defining MAP-Elites archive dimensions from task characteristics.
• Advanced search algorithms: Investigating PUCT, Thompson sampling, and adaptive branching strategies.
• Domain knowledge injection: Systematically injecting domain-specific knowledge ( e.g., physical laws, seasonal priors, operational constraints) into the search process through specialized prompt templates or constrained code generation, enabling the agent to start from a stronger knowledge foundation.
• Coding & research agent: Combining both coding agent and deep research agent in one framework, which enables coding agent to reflect needed knowledge on the fly and automatically leverage deep research agent to get related reference papers and code.
Acknowledgments
References
[1] C. B. Browne, E. Powley, D. Whitehouse, S. M. Lucas, P. I. Cowling, P. Rohlfshagen, S. Tavener, D. Perez, S. Samothrakis, and S. Colton (2012) A survey of monte carlo tree search methods. IEEE Transactions on Computational Intelligence and AI in Games 4 ( 1), pp. 1–43. Cited by: 1st item.
[2] J. Chai, S. Tang, R. Ye, Y. Du, X. Zhu, M. Zhou, Y. Wang, Y. Zhang, L. Zhang, S. Chen, et al. (2025) SciMaster: towards general-purpose scientific ai agents, part i. x-master as foundation: can we lead on humanity's last exam?. arXiv preprint arXiv:2507.05241. Cited by: 1st item.
[3] J. S. Chan, N. Chowdhury, O. Jaffe, J. Aung, D. Sherburn, E. Mays, G. Starace, K. Liu, L. Maksin, T. Patwardhan, et al. (2024) Mle-bench: evaluating machine learning agents on machine learning engineering. arXiv preprint arXiv:2410.07095. Cited by: §1.
[4] U. K. Das, K. S. Tey, M. Seyedmahmoudian, S. Mekhilef, M. Y. I. Idris, W. Van Deventer, B. Horan, and A. Stojcevski (2018) Forecasting of photovoltaic power generation and model optimization: a review. Renewable and Sustainable Energy Reviews 81, pp. 912–928. Cited by: §2.4.
[5] M. Feurer, A. Klein, K. Eggensperger, J. Springenberg, M. Blum, and F. Hutter (2015) Efficient and robust automated machine learning. Advances in neural information processing systems 28. Cited by: §2.1.
[6] P. Gao and C. Peng (2025) More with less: an empirical study of turn-control strategies for efficient coding agents. arXiv preprint arXiv:2510.16786. Cited by: §4.1.3.
[7] X. He, K. Zhao, and X. Chu (2021) AutoML: a survey of the state-of-the-art. Knowledge-Based Systems 212, pp. 106622. Cited by: item (iii).
[8] T. Hong, P. Pinson, S. Fan, H. Zareipour, A. Troccoli, and R. J. Hyndman (2016) Probabilistic energy forecasting: global energy forecasting competition 2014 and beyond. International Journal of Forecasting 32 ( 3), pp. 896–913. Cited by: §1, §2.4.
[9] Q. Huang, J. Vora, P. Liang, and J. Leskovec (2024) MLAgentBench: evaluating language agents on machine learning experimentation. In Proceedings of the International Conference on Machine Learning, Cited by: §1.
[10] C. S. Lai, Y. Jia, M. D. McCulloch, and Z. Xu (2017) Daily clearness index profiles cluster analysis for photovoltaic system. IEEE Transactions on Industrial Informatics 13 ( 5), pp. 2322–2332. Cited by: §2.4.
[11] G. Lai, W. Chang, Y. Yang, and H. Liu (2018) Modeling long-and short-term temporal patterns with deep neural networks. In The 41st International ACM SIGIR Conference on Research & Development in Information Retrieval, pp. 95–104. Cited by: §4.1.1, Table 2.
[12] Z. Liang, F. Wei, W. Xu, L. Chen, Y. Qian, and X. Wu (2025) I-mcts: enhancing agentic automl via introspective monte carlo tree search. arXiv preprint arXiv:2502.14693. Cited by: §2.2.
[13] H. Liu, K. Simonyan, and Y. Yang (2019) DARTS: differentiable architecture search. In International Conference on Learning Representations, Cited by: §2.1.
[14] Y. Liu, T. Hu, H. Zhang, H. Wu, S. Wang, L. Ma, and M. Long (2024) ITransformer: inverted transformers are effective for time series forecasting. In International Conference on Learning Representations, Cited by: §2.4.
[15] Y. Liu, H. Zhang, C. Li, X. Huang, J. Wang, and M. Long (2024) Timer: generative pre-trained transformers are large time series models. arXiv preprint arXiv:2402.02368. Cited by: §4.1.2, §4.2.3, Table 2.
[16] Z. Liu, Y. Cai, X. Zhu, et al. (2025) ML-master: towards ai-for-ai via integration of exploration and reasoning. arXiv preprint arXiv:2506.16499. Cited by: 2nd item, §1, §2.2, §3.5.1.
[17] J. Mouret and J. Clune (2015) Illuminating search spaces by mapping elites. arXiv preprint arXiv:1504.04909. Cited by: §1, §2.3.
[18] Y. Nie, N. H. Nguyen, P. Sinthong, and J. Kalagnanam (2023) A time series is worth 64 words: long-term forecasting with transformers. In International Conference on Learning Representations, Cited by: §2.4.
[19] A. Novikov, N. Vũ, M. Eisenberger, E. Dupont, P. Huang, A. Z. Wagner, S. Shirobokov, B. Kozlovskii, F. J. Ruiz, A. Mehrabian, et al. (2025) AlphaEvolve: a coding agent for scientific and algorithmic discovery. arXiv preprint arXiv:2506.13131. Cited by: §2.3.
[20] OpenEvolve: an open-source evolutionary coding agent External Links: Link Cited by: §2.3.
[21] H. Shi, M. Xu, and R. Li (2018) Deep learning for household load forecasting—a novel pooling deep rnn. IEEE Transactions on Smart Grid 9 ( 5), pp. 5271–5280. Cited by: item (i).
[22] I. O. Tolstikhin, N. Houlsby, A. Kolesnikov, L. Beyer, X. Zhai, T. Unterthiner, J. Yung, A. Steiner, D. Keysers, J. Uszkoreit, et al. (2021) MLP-Mixer: an all-MLP architecture for vision. In Advances in Neural Information Processing Systems, Vol. 34, pp. 24261–24272. Cited by: §4.2.1.
[23] D. Van der Meer, J. Widén, and J. Munkhammar (2018) Review on probabilistic forecasting of photovoltaic power production and electricity consumption. Renewable and Sustainable Energy Reviews 81, pp. 1484–1512. Cited by: §1.
[24] S. Wang, H. Wu, X. Shi, T. Hu, H. Luo, L. Ma, J. Y. Zhang, and J. Zhou (2024) TimeMixer: decomposable multiscale mixing for time series forecasting. In International Conference on Learning Representations, Cited by: §2.4, §4.1.1, §4.1.2, §4.2.1, §4.2.3, Table 2, Table 2, Table 2.
[25] Y. Wang, Q. Chen, T. Hong, and C. Kang (2019) Review of smart meter data analytics: applications, methodologies, and challenges. IEEE Transactions on Smart Grid 10 ( 3), pp. 3125–3148. Cited by: §2.4.
[26] Y. Wang, Y. Shi, M. Yang, R. Zhang, S. He, H. Lian, Y. Chen, S. Ye, K. Cai, and X. Gu (2026) SWE-pruner: self-adaptive context pruning for coding agents. arXiv preprint arXiv:2601.16746. Cited by: 2nd item, 2nd item.
[27] WecoAI (2024) AIDE: the machine learning engineer agent. Note: https://github.com/WecoAI/aideml Cited by: §1, §2.2.
[28] D. Whitley, S. Rana, and R. B. Heckendorn (1999) The island model genetic algorithm: on separability, population size and convergence. Journal of Computing and Information Technology 7, pp. 33–47. Cited by: §3.6.
[29] H. Wu, J. Xu, J. Wang, and M. Long (2021) Autoformer: decomposition transformers with auto-correlation for long-term series forecasting. In Advances in Neural Information Processing Systems, Vol. 34, pp. 22419–22430. Cited by: §2.4.
[30] X. Yang, X. Yang, S. Fang, Y. Zhang, J. Wang, Q. Li, J. Li, M. Xu, Y. Li, H. Pan, et al. (2025) R&D-agent: an llm-agent framework towards autonomous data science. Cited by: §2.2.
[31] A. Zeng, M. Chen, L. Zhang, and Q. Xu (2023) Are transformers effective for time series forecasting?. In Proceedings of the AAAI conference on artificial intelligence, Vol. 37, pp. 11121–11128. Cited by: §2.4.
[32] H. Zhou, S. Zhang, J. Peng, S. Zhang, J. Li, H. Xiong, and W. Zhang (2021) Informer: beyond efficient transformer for long sequence time-series forecasting. In Proceedings of the AAAI Conference on Artificial Intelligence, Vol. 35, pp. 11106–11115. Cited by: §2.4, §4.1.1.
[33] X. Zhu, Y. Cai, Z. Liu, B. Zheng, C. Wang, R. Ye, J. Chen, H. Wang, W. Wang, Y. Zhang, et al. (2026) Toward ultra-long-horizon agentic science: cognitive accumulation for machine learning engineering. arXiv preprint arXiv:2601.10402. Cited by: §2.2.
[34] B. Zoph and Q. V. Le (2017) Neural architecture search with reinforcement learning. In International Conference on Learning Representations, Cited by: §2.1.
Appendix A Prompt Templates
This appendix provides illustrative prompt templates used in SEA-TS. The actual prompts are longer and task-specific; we show simplified versions covering all key components.
A.1 System Prompt (Role Definition)
⬇
You are an expert machine learning engineer.
Your task is to develop a high- performance time
series forecasting model. Generate complete,
self- contained Python code that:
Loads and preprocesses the provided dataset
Implements a novel model architecture
Trains the model and saves checkpoints
Generates predictions on the test set
Saves predictions to ./ submission/ submission. csv
Focus on designing novel and effective core model
architectures rather than writing long helper
functions.
Listing 1: System prompt defining the agent's role (simplified).
A.2 Base Prompt (Task Description)
⬇
Task
Develop a forecasting model for [ TASK_NAME].
Dataset
Format: [ CSV/ Parquet], Path: [ DATA_PATH]
Features: [ FEATURE_LIST]
Target: [ TARGET_VARIABLE]
Split: train [ DATE1- DATE2], val [ DATE3- DATE4],
test [ DATE5- DATE6]
Evaluation Metric
[ METRIC_NAME]: [ FORMULA_DEFINITION]
Lower/ Higher is better.
Reference Code
[ REFERENCE_CODE_EXCERPT]
Remaining Iterations
You have [ N] iterations remaining out of [ T].
Consider trying underexplored approaches.
Listing 2: Base prompt template with task-specific details (simplified).
A.3 Code Review Prompt
⬇
Introduction
You are an expert ML engineer reviewing code.
Identify logical errors that lead to overly
optimistic metrics, such as data leakage and
normalization issues. Focus on logic errors only.
Generated Code
[ FULL_GENERATED_CODE]
Execution Output
[ EXECUTION_LOG_AND_METRICS]
Instructions
Check for data leakage: only flag leakage of
future data from test set.
Check inference code correctness, especially
checkpoint/ parameter matching.
If you find a logical error, print the exact
code snippet causing it.
For each error, review again to prove yourself
wrong. Only flag if 100% confident.
Suggest prompt improvements to prevent similar
errors in future iterations.
At the end, you MUST answer:
' has_logical_error = True' or
' has_logical_error = False'
Listing 3: Code review prompt for logical error detection (simplified).
A.4 Prompt Update Prompt
⬇
Introduction
You are a prompt engineer. Integrate the new
suggestion into the running prompt concisely.
Current Running Prompt
[ EXISTING_ACCUMULATED_INSIGHTS]
New Suggestion for Improvement
[ CODE_REVIEW_FINDINGS_OR_GLOBAL_REASONING]
Instructions
Extract only actionable insights, specific
code patterns, and concrete recommendations.
Organize with clear sections ( e. g.,
'## Model Architecture', '## Data Processing').
Prune contradictory or low- confidence info.
Remove redundancy with existing insights.
Include code snippets or pseudocode where
relevant.
Output ONLY the updated running prompt.
Listing 4: Running prompt update mechanism (simplified).
A.5 Running Prompt (Accumulated Insights)
⬇
Accumulated Insights
Data Processing
Use MAD scaling instead of standard normalization
for robustness to sensor outliers.
Apply . shift(1) before rolling window computations
to prevent data leakage of future information.
Model Architecture
Multi- head gated architectures outperform single
models. Consider per- station specialization.
Physical constraints ( e. g., non- negativity for
solar, monotonic afternoon decay) improve
generalization significantly.
Training
Daylight- weighted loss functions reduce error on
practically important daytime hours.
LR warmup + cosine annealing works well.
Huber loss more robust than MSE for noisy data.
Listing 5: Running prompt example after several iterations (simplified).
Appendix B Evolved Code Examples
B.1 Solar PV: QuadHeadGatedSolar Model (Excerpt)
⬇
1 class QuadHeadGatedSolar( nn. Module):
2 """Seven-head gated solar forecaster."""
3 def forward( self, x_norm, hours_future, hpos,
4 station_ids, y_scaler, y_hist_raw,
5 hours_hist):
6 heads = [ self. residual_head( x_norm, y_scaler),
7 self. fourier( y_hist_raw),
8 self. cycle_residual_head(...),
9 self. period_head( y_hist_raw),
10 self. decay_head( y_hist_raw, hours_future),
11 self. hq_head( x_norm, y_scaler),
12 self. diurnal_bias_head(...)]
13 heads = torch. stack( heads, dim=-1)
14
15 gate_logits = self. gate_mlp( hour_emb + st_emb)
16 gate_logits += self. hour_prior[ hours_future % 24]
17 weights = softmax( gate_logits / tau, dim=-1)
18
19 y = ( heads * weights). sum( dim=-1). clamp_min(0)
20 return y, weights
Listing 6: Gated multi-expert solar forecaster (simplified).
B.2 Load Forecasting: Dual-Branch Network (Excerpt)
⬇
1 class ImprovedDualBranchNet( nn. Module):
2 def init( self, input_dim, num_users,
3 embedding_dim=48, hidden_dim=128):
4 super(). init()
5 self. feature_encoder = MLPFeatureEncoder(
6 input_dim= input_dim,
7 d_model= hidden_dim // 2, dropout=0.1)
8 self. user_embedding = nn. Embedding(
9 num_users, embedding_dim)
10 self. user_branch = nn. Sequential(
11 nn. Linear( embedding_dim, hidden_dim // 2),
12 nn. LayerNorm( hidden_dim // 2), nn. GELU(),
13 nn. Linear( hidden_dim // 2, hidden_dim // 2),
14 nn. LayerNorm( hidden_dim // 2), nn. GELU())
15 self. combined_layer = nn. Sequential(
16 nn. Linear( hidden_dim, hidden_dim),
17 nn. LayerNorm( hidden_dim), nn. GELU(),
18 nn. Linear( hidden_dim, hidden_dim // 2),
19 nn. LayerNorm( hidden_dim // 2), nn. GELU())
20 self. output = nn. Linear( hidden_dim // 2, 1)
21 self. hour_bias = nn. Parameter( torch. zeros(24))
22 with torch. no_grad():
23 self. hour_bias[2:8] = 0.05 # night upward
24 self. hour_bias[8:21] = -0.03 # day downward
25
26 def forward( self, x, user_ids, hours):
27 feat = self. feature_encoder( x)
28 user = self. user_branch(
29 self. user_embedding( user_ids))
30 combined = self. combined_layer(
31 torch. cat([ feat, user], dim=1))
32 out = self. output( combined). squeeze(-1)
33 out = out + self. hour_bias[ hours] \
34 * torch. abs( out) * 0.1
35 return out
Listing 7: Dual-branch load forecasting network (simplified).
Experimental support, please view the build logs for errors. Generated by L A T E xml
.
Instructions for reporting errors
We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:
Click the "Report Issue" ( ) button, located in the page header.
Tip: You can select the relevant text first, to include it in your report.
Our team has already identified the following issues. We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.
Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion, and welcome developer contributions.
BETA 