# 01-intro slides

Slide numbers match the presentation footer. Only the final state of each numbered slide is included; unnumbered title and section pages are also included. Intermediate animation steps and focus slides are omitted. Open the linked images for diagrams, screenshots and details missing from the searchable text.

## Slide unnumbered · PDF page 1 · Title

[Slide image](page-001.png)

Introduction to Agentic AI
A*STAR Leadership Retreat

Dr Gaurav Manek
2026-10-08
ocelliq.com/astar-lr

## Slide unnumbered · PDF page 2 · Title

[Slide image](page-002.png)

OcelliQ.com/astar-lr
   Access course materials
   Ask your TA to help you set up.

## Slide 2 · PDF page 3 · Outline

[Slide image](page-003.png)

Outline
     1. The AI industry landscape
     2. What is AI?                            AI for leadership
     3. What makes AI agentic?
     4. Where AI fails
                                               This course is for business leaders, not
     Hands-on:                                 engineers.
     5. Procurement: a first run               1. Identify high-value applications.
                                               2. Assess specific business risks.
     6. Demystifying the IMDA Agentic AI
                                               3. Define controls and approval rules.
        Governance Framework
                                               4. Assign human oversight and
     Hands-on:                                    accountability.
     7. Set policies for a procurement agent
                                                            Zero coding.
     8. ATLAS: governance in practice
     9. Where do we go from here?
ocelliq.com/astar-lr                                                                      2 / 78

## Slide 3 · PDF page 4 · About Me

[Slide image](page-004.png)

About Me


                       Dr. Gaurav Manek
                       • Founder, Ocellivision
                       • Technical Lead, ATLAS @ IMCB
                       • PhD in AI/ML — Carnegie-Mellon University (2023)
                       • Founder, Visigoth.ai (SaaS)


                       For follow-up questions:
                          gaurav_manek@a-star.edu.sg
                          gauravmanek


ocelliq.com/astar-lr                                                        3 / 78

## Slide 4 · PDF page 5 · About Our TAs

[Slide image](page-005.png)

About Our TAs




         Dr. Aarthi      Dr. Adaikalavan   Dr. Gokce Oguz   Dr. Chinh Tran-To   Ms. Dong Jiahui   Mr. Guai Zi Wei
        Ravikrishnan       Ramasamy                                 Su
            ASRL           ASRL / GIS        ASRL / GIS            BII               BDH               ETO




       Dr. Audrey Lee   Dr. Benedict Wong Dr. Benjamin Chew Dr. Farzam Farbiz Dr. Amhed Missael Mr. Xavier Wilbin
                                                                               Vargas Velazquez
             GIS              IAIC              IAIC              IAIC              IMCB              IMCB




ocelliq.com/astar-lr                                                                                                4 / 78

## Slide unnumbered · PDF page 6 · Industry Landscape

[Slide image](page-006.png)

1.   Industry Landscape

## Slide 6 · PDF page 9 · Public Perception of AI

[Slide image](page-009.png)

1.1 Public Perception of AI

                                                             Promise                                                      Risk



                                                                                            Amazon · 20261
                                                                                                                                   OpenAI · Aug 20265

                     Risk in missing this
                                                                                                                Risk in moving too quickly
                        opportunity
                                  Microsoft · Jan 20252

                                                                                                                                     The Guardian · Apr 2026
                                                                                                                                                               6
                                                                                        Anthropic · Nov 20253
             Gartner newsroom · article excerpt
                                                      · September 16, 2026

            Gartner Forecasts Worldwide AI
                                           Spending
            to Grow 49.5% in 2026
            2026 forecast: $2.7 trillion in global
                                                                    spending on AI.
            Excerpt rendered for this presentation;

                                                                                                                            CNN · Sep 20267
                                                      website screenshot unavailable.
                                                                    Gartner · Sep 2026 · article excerpt4



ocelliq.com/astar-lr                                                                                                                                               6 / 78

## Slide 7 · PDF page 10 · Gold Rush of our age

[Slide image](page-010.png)

1.2 Gold Rush of our age
     Global AI infrastructure spending forecast for 20264

     US$1.48T               ≈5× Apollo missions8 (US$309 billion)
                            ≈3× Great Wall of China rebuild9 (US$452 billion)
                            ≈1× Cumulative global datacenter spend until the
                                mid-2000s10
     Global AI-server electricity consumption forecast for 202611

     175 TWh                ≈3× Singapore electricity consumption in 202412 (58 TWh)
                            ≈2× Three Gorges’ designed annual output13 (88.2 TWh)




                                                                    *All rough estimates
ocelliq.com/astar-lr                                                                   7 / 78

## Slide 8 · PDF page 12 · Who Controls What in AI

[Slide image](page-012.png)

1.3 Who Controls What in AI

                             1. Business need
                             Outcomes · priorities · success metrics
      Your direct control
                             2. Policy                                        This workshop.
                             Rules · accountability · human oversight

                             3. Orchestration
                             Workflows · integrations · approvals
            Your technical
               team owns
                             4. Engineering
                             Tools · prompts · evaluation · deployment

                             5. Infrastructure                                Background.
                             Inference · latency · capacity · cost
      External providers
                             model     chips      power      data
                              dev                           centres network
ocelliq.com/astar-lr                                                                           8 / 78

## Slide unnumbered · PDF page 13 · WhatisAI?

[Slide image](page-013.png)

2.   What is AI?

## Slide 10 · PDF page 15 · What Does"AI"Mean?

[Slide image](page-015.png)

2.1 What Does “AI” Mean?




     • “AI” is a marketing and technical term             Jevons paradox 20
       ‣ From rule-based systems to neural networks
       ‣ Promises to revolutionize everything             AI won’t make working easier.
     • Massive returns in software, marketing, etc.       It raises the bar for everyone
       ‣ Just starting in some conservative industries.   and increases competition.
                                                          The only competitive moat left
     • Turn decisions into a commodity.19                 is your speed of integration.
     Not magic                                            Adopt early, or get left behind.




ocelliq.com/astar-lr                                                                         10 / 78

## Slide 11 · PDF page 17 · What is a Large Language Model?

[Slide image](page-017.png)

2.2 What is a Large Language Model?

                         An LLM is Fancy Autocomplete
     An LLM predicts the next token / word / step
     An LLM predicts the next token given / using / from
     An LLM predicts the next token given every / all / the
     An LLM predicts the next token given every thing / word / token
     An LLM predicts the next token given everything before / so / in
     An LLM predicts the next token given everything before “.” / “,” / “and”
     An LLM predicts the next token given everything before . (end) / It / This

     1 token ≈ ¾ of an English word, a punctuation mark, or a digit.22
     Unit of computation: pay per token in and out. The context window is sized in tokens.



ocelliq.com/astar-lr                                                                         11 / 78

## Slide 12 · PDF page 19 · What is a Large Language Model?

[Slide image](page-019.png)

2.3 What is a Large Language Model?


                         An LLM is Fancy Autocomplete
     • Blocks of linear algebra                     LLMs are black boxes: we have ability to
       ‣ arranged in creative ways                  predict and explain their behaviour.
       ‣ trained on every scrap of human media
                                                    LLMs are stochastic: Identical runs often
       ‣ unimaginable amounts of computation
                                                    produce different output.
       ‣ learn statistical patterns, not explicit
         rules about the world                      • Sunny skies ☀️, 30°C.
                                                    • 30°C with plenty of sunshine.
     • Behaviour surprisingly emerges at scale
                                                    • It's sunny and 30°C today.
       ‣ Exhibits strengths and weaknesses very
         different from humans                      Agent engineering extracts useful work
                                                    despite these limits.

ocelliq.com/astar-lr                                                                            12 / 78

## Slide 13 · PDF page 22 · Cost of AI

[Slide image](page-022.png)

2.4 Cost of AI
                                         60                                                                                                                          Claude Opus 5.5

                                                Tremendous variety available!                                                                         Claude Sonnet 5.5
                                                                                                                                                                                       GPT-6 Astra

                                                Prices span three orders of magnitude.                                                   Grok 4.7
                                                                                                                                                    Gemini 4 Argon
                                                                                                                                                      GPT-6.1 Sol                        Claude Fable 5.1
Artificial Analysis Intelligence Index




                                         50                                                                             Muse Spark 1.3
                                                                                                               MiMo-V2.6-Pro
                                                                                           GLM 5.3 Flash
                                                                                                                             Kimi K3
                                                                                                               GLM 5.3
                                                                                         DeepSeek V4.1 Flash
                                         40
                                                       Qwen3.8 27B




                                         30




                                         20




                                         10                                                                                                                                   Open weights
                                                  →      OpenRouter volume                                                                                                    Closed

                                              $0.001                             $0.01                                   $0.10                                              $1.00
                                                                             Cost per task (100K input / 8K output tokens), log scale

          ocelliq.com/astar-lr                                                                                                                                                                 13 / 78

## Slide 14 · PDF page 24 · Cost of AI by Lab(Closed-Source)

[Slide image](page-024.png)

2.5 Cost of AI by Lab (Closed-Source)
                                         60                                                                                                                          Claude Opus 5.5

                                                OpenAI and Anthropic compete at the frontier.                                                         Claude Sonnet 5.5
                                                                                                                                                                                        GPT-6 Astra

                                                Both have imminent IPOs.                                                                 Grok 4.7
                                                                                                                                                    Gemini 4 Argon
                                                                                                                                                      GPT-6.1 Sol                           Claude Fable 5.1
Artificial Analysis Intelligence Index




                                         50                                                                             Muse Spark 1.3
                                                                                                               MiMo-V2.6-Pro
                                                                                           GLM 5.3 Flash
                                                                                                                             Kimi K3
                                                                                                               GLM 5.3
                                                                                         DeepSeek V4.1 Flash
                                         40
                                                       Qwen3.8 27B




                                         30




                                         20
                                                                                                                                                                                   OpenAI
                                                                                                                                                                                   Google
                                                                                                                                                                                   Anthropic
                                         10                                                                                                                                        SpaceXAI
                                                  →      OpenRouter volume                                                                                                         Other

                                              $0.001                             $0.01                                   $0.10                                              $1.00
                                                                             Cost per task (100K input / 8K output tokens), log scale

          ocelliq.com/astar-lr                                                                                                                                                                    14 / 78

## Slide 15 · PDF page 26 · Cost of AI by Launch DateNew→12+ months

[Slide image](page-026.png)

2.6 Cost of AI by Launch Date                                     New           →   12+ months

                                         60                                                                                                                                          Claude Opus 5.5

                                                The AI revolution is ongoing, not complete.                                                                           Claude Sonnet 5.5
                                                                                                                                                                                                       GPT-6 Astra

                                                Frontier to budget in ~4 months.                                                                         Grok 4.7
                                                                                                                                                                    Gemini 4 Argon
                                                                                                                                                                      GPT-6.1 Sol                        Claude Fable 5.1
Artificial Analysis Intelligence Index




                                         50                                                                                             Muse Spark 1.3
                                                                                                                               MiMo-V2.6-Pro
                                                                                                     GLM 5.3 Flash
                                                Highest intelligence prior to 9 Jun 2026                                                     Kimi K3
                                                                                                                               GLM 5.3
                                                                                                   DeepSeek V4.1 Flash
                                         40
                                                       Qwen3.8 27B




                                         30




                                         20




                                         10
                                                  →      OpenRouter volume

                                              $0.001                                       $0.01                                         $0.10                                              $1.00
                                                                                     Cost per task (100K input / 8K output tokens), log scale

          ocelliq.com/astar-lr                                                                                                                                                                                 15 / 78

## Slide 16 · PDF page 27 · Cost of AI by Minimum CAPEX

[Slide image](page-027.png)

2.7 Cost of AI by Minimum CAPEX
                                         60                                                                                                                                Claude Opus 5.5
                                                                                                                                                           Claude Sonnet 5.5
                                                                                                                                                                                               GPT-6 Astra
                                                                                                                                                         Gemini 4 Argon
                                                                                                                                              Grok 4.7     GPT-6.1 Sol                            Claude Fable 5.1
Artificial Analysis Intelligence Index




                                         50                                                                                 Muse Spark 1.3
                                                                                                                   MiMo-V2.6-Pro
                                                                                                   GLM 5.3 Flash
                                                                                                                             Kimi K3 (2.8T)

                                                                             DeepSeek V4.1 Flash                   GLM 5.3
                                         40
                                                       Qwen3.8 27B




                                         30




                                         20                                                                                                                  Indicative hosting hardware (SGD)
                                                                                                                                                                     ≤S$5k            ≤S$500k
                                                                                                                                                                     ≤S$10k           >S$500k
                                                                                                                                                                     ≤S$25k           Other
                                                                                                                                                                     ≤S$100k
                                         10
                                                  →      OpenRouter volume                                                                               Higher tiers: 4 / 8 / 16 sessions budgeted

                                              $0.001                                      $0.01                               $0.10                                                $1.00
                                                                                 API cost per task (US$, 100K input / 8K output), log scale

          ocelliq.com/astar-lr                                                                                                                                                                          16 / 78

## Slide unnumbered · PDF page 28 · What makes AI Agentic?

[Slide image](page-028.png)

3.   What makes AI Agentic?

## Slide 18 · PDF page 29 · What makes AIAgentic?

[Slide image](page-029.png)

3.1 What makes AI Agentic?

     Simple LLM                                      Agentic AI
                       Your prompt                                                              Your prompt             System
                                                                                           agentic loop




                                                       observe, steer, or add context
                                                                                                                         Tools
                                                                                                     LLM            • Web search
                        Inference                                                                                   • Code execution
                                                                                                                    • File read/write
                                                                                                   Harness          • MCP Tools
                                                                                                                    • APIs / databases
                                                                                                                    • Other agents

                                                                                                                         Skills
                          Done                                                                      Done


        “Given this question, what do I answer?”                                        “Given this goal, what do I do next?”

     A agent is an LLM with a harness, which provides tools to interact the world.
ocelliq.com/astar-lr                                                                                                                     18 / 78

## Slide 19 · PDF page 30 · Anatomy of an Agent

[Slide image](page-030.png)

3.2 Anatomy of an Agent


     Tools include:
     • Sending and receiving emails/messages     Agentic AI
     • Interacting with your ERP software                                                Your prompt       System
       ‣ Approving/denying transactions
                                                                                    agentic loop
     • Controlling machines




                                                   observe, steer, or add context
                                                                                                            Tools
     • Performing scientific analysis                                                         LLM      • Web search
     • Spending money or resources                                                                     • Code execution
                                                                                                       • File read/write
       ‣ Reserving rooms                                                                    Harness    • MCP Tools
       ‣ Purchasing equipment                                                                          • APIs / databases
                                                                                                       • Other agents
     • Connecting to a database
                                                                                                            Skills
                                                                                             Done
     Skills are human-language instructions on
     how to do something.

ocelliq.com/astar-lr                                                                                                        19 / 78

## Slide 20 · PDF page 31 · What does this look like?

[Slide image](page-031.png)

3.3 What does this look like?




     • Everyday AI apps hide what           Your input →
       happens behind the scenes.
     • Today, you’ll get a first taste
       of the professional AI tools
       your technical teams use.             Tool call →

     • You’ll see the full trace: your     Tool output →
       input, tool calls, tool outputs,
       and the agent’s response.          Agent output →




ocelliq.com/astar-lr                                       20 / 78

## Slide unnumbered · PDF page 32 · LLM intelligence ≠ Human intelligence

[Slide image](page-032.png)

4.
     LLM intelligence
     ≠ Human intelligence

## Slide 22 · PDF page 33 · LLM intelligence fails in common ways

[Slide image](page-033.png)

4.1 LLM intelligence fails in common ways

                 LLMs fail in common ways that are a foreseeable source of business risk.

     • Overconfidence
       expresses certainty independent of correctness.30
     • Hallucinations
       invents facts, citations, or details that sound plausible.
     • Credulity/Sycophancy
       accepts falsehoods or agrees with you despite contradictions.31
     • Theory-of-mind / world-model failure
       misjudges what people know or how actions affect the world.32         AI Alignment

     • Specification gaming / reward hacking
       exploits a rule or reward while missing the intended goal.33

ocelliq.com/astar-lr                                                                        22 / 78

## Slide 23 · PDF page 34 · Theory of Mind:Understanding Intentions

[Slide image](page-034.png)

4.2 Theory of Mind: Understanding Intentions
     Project Vend: an AI shopkeeper37
     Anthropic ran an experiment with an AI
     shopkeeper that could set prices.
     • Employees persuaded it to offer discounts
       and give away stock.
     • 25% employee discount when
       approximately 99% of customers were
       employees.
     • Products sold below cost; the shop lost
       money.

     Should the agent represent the owner’s
     or shoppers’ interests?

                                                   Anthropic · 27 June 202537
ocelliq.com/astar-lr                                                            23 / 78

## Slide 24 · PDF page 35 · Hallucinations

[Slide image](page-035.png)

4.3 Hallucinations


     Hallucination: the model        TechCrunch38

     states something confidently,
     fluently, and wrong.

     An American military AI
     hallucinated nuclear
     weapons components on a
     Chinese vessel’s cargo
     manifest.7
     “entirely false” but it also
     “almost started a war”


ocelliq.com/astar-lr                           24 / 78

## Slide 25 · PDF page 36 · Hallucinations

[Slide image](page-036.png)

4.4 Hallucinations




     AI may hallucinate medically relevant
     abnormalities when denoising scans.

     AI-enhanced PET/SPECT denoising can look
     “visually compelling and nearly
     indistinguishable” from a reference scan —
     while inventing lesions or erasing real ones.39




                                                       Xia et al. · DREAM · Fig. 539
ocelliq.com/astar-lr                                                              25 / 78

## Slide 26 · PDF page 37 · Hallucinations

[Slide image](page-037.png)

4.5 Hallucinations

     South Africa withdrew its
     draft AI policy.

     Its reference list contained fictitious
     sources that appeared to have been
     generated by AI.40


      “AI-generated citations were included
      without proper verification. This
      should not have happened.”
      Solly Malatsi, Minister of Communications and Digital
      Technologies

                                                              Reuters / MyJoyOnline40
ocelliq.com/astar-lr                                                                    26 / 78

## Slide unnumbered · PDF page 38 · Procurement:a first run

[Slide image](page-038.png)

5.   Procurement: a first run

## Slide 28 · PDF page 39 · The procurement case

[Slide image](page-039.png)

5.1 The procurement case




     A complex procurement for a research test platform:
     • Five suppliers offer different machines with overlapping capabilities.
     • Stakeholders: the PI, Procurement, Finance, Evaluation Panel and Executive
       Approval Committee.
     • Compare technical capability, total cost, acceptance dates and years of support.
     • 86 pages across 47 PDFs: grant records, tender requirements, bids, clarifications and
       evaluation material.
ocelliq.com/astar-lr                                                                           28 / 78

## Slide 29 · PDF page 42 · A convincing recommendation

[Slide image](page-042.png)

5.2 A convincing recommendation

                                       1


                                           2
                                                                            3
                                           4



                                                                            5

     1. Wrong supplier                 4. M2 wrongly passed           5. Misses support extension
     2. M6/M7 wrongly passed           5. Price conflict ignored

                               Now: Understand the procurement problem.
                       Later: Use governance principles to make the process reliable.
ocelliq.com/astar-lr                                                                            29 / 78

## Slide 30 · PDF page 44 · Your AI workspace

[Slide image](page-044.png)

5.3 Your AI workspace

                                            Click to open Claude
                                                if the chat is missing




           Files         Current Document          Claude




ocelliq.com/astar-lr                                                     30 / 78

## Slide 31 · PDF page 46 · Ask your agent

[Slide image](page-046.png)

5.4 Ask your agent

     Understand the case
     Explain the procurement case to me in plain language.

           Also try
           Explain this case in two sentences for our finance
           director.                                     Specify target audience


           Explain what we are buying, why we need it, and what the
           different documents cover.                       Specify a structure


           Explain what an encabulator does to someone without a
           technical background. Use an analogy.    Explain unfamiliar terminology


ocelliq.com/astar-lr                                                            31 / 78

## Slide 32 · PDF page 48 · Starter tasks:make a procurement brief

[Slide image](page-048.png)

5.5 Starter tasks: make a procurement brief

     1. Identify the sources
     Which documents specify the requirements and criteria?

     2. Develop the prompt
     Write a prompt for another agent to turn these documents into a
     procurement brief in BRIEF.md              Let AI help you write the prompt.


     3. Run it
     Run an agent with that prompt. Don’t let it read submitted bids
     and earlier evaluation results.                            ~3 min


                       Why do we prevent it from reading submitted bids?
                                    We’ll come back to this!
ocelliq.com/astar-lr                                                           32 / 78

## Slide 33 · PDF page 49 · Starter tasks:make something useful

[Slide image](page-049.png)

5.6 Starter tasks: make something useful

     Make a presentation
     /pptx Make a three-slide presentation using the A*STAR template
     explaining this procurement: what we need, how we will evaluate
     the bids, and the questions still to resolve.

           /pptx skill helps your agent create PowerPoint slides.

           Also try
           Include a pie chart showing the weights of the scored
           evaluation criteria. Label each slice with its percentage.


                            Open the presentation your agent creates.

ocelliq.com/astar-lr                                                    33 / 78

## Slide 34 · PDF page 50 · Optional:check a claim from the slides

[Slide image](page-050.png)

5.7 Optional: check a claim from the slides




     /slides Find the “A convincing recommendation” slide. Check the
     five errors identified against the original case documents, and
     tell me what the correct answers are.

           /slides skill gives your agent our slides.




ocelliq.com/astar-lr                                               34 / 78

## Slide 35 · PDF page 51 · Understand/usageand/context

[Slide image](page-051.png)

5.8 Understand /usage and /context
            /usage: how much have I used?   /context: what is taking up space?




ocelliq.com/astar-lr                                                             35 / 78

## Slide unnumbered · PDF page 52 · Governing Agentic AI

[Slide image](page-052.png)

6.   Governing Agentic AI

## Slide 37 · PDF page 53 · Humans are still in charge

[Slide image](page-053.png)

6.1 Humans are still in charge




                                                             Even if AI does the work,
                                                             humans still bear the
                                                             consequences.
                                                             This is why a human must
                                                             remain accountable for what
                                                             AI does.
                 Attributed to IBM internal training, 1979




ocelliq.com/astar-lr                                                                       37 / 78

## Slide 38 · PDF page 55 · IMDA Model Governance framework

[Slide image](page-055.png)

6.2 IMDA Model Governance framework


                        IMDA Model AI Governance Framework for Agentic AI
                        (v1.5, May 2026)44
                        It gives you the structure and tools to weigh risks and write
                        policies for your own organization.
                        Others include:
                                     ISO/IEC 4200145                  OWASP46
                                     AI management                    Agentic AI:
                                     systems                          Threats and
                                                                      Mitigations




ocelliq.com/astar-lr                                                                    38 / 78

## Slide 39 · PDF page 56 · The Four Pillars

[Slide image](page-056.png)

6.3 The Four Pillars 44


                           A.   Assess and bound the risks upfront
                                is an agent appropriate? what is the minimum
                                authority it needs? what’s the blast radius?


                           B.
                            Make humans meaningfully accountable
                            name individuals, responsibilities, and require human
                            approval at real decision points.


                           C.   Implement technical controls and processes
                                enforce access and action limits at the infrastructure
                                level, not only in the prompt.


                           D.   Enable end-user responsibility
                                equip end-users and consumers to operate and
                                oversee the agent responsibly.

ocelliq.com/astar-lr                                                                     39 / 78

## Slide 40 · PDF page 57 · The Seven Risks

[Slide image](page-057.png)

6.4 The Seven Risks 44

         Seven Risks
      1. Erroneous actions
      2. Unauthorized actions
                                         old risks, new target
      3. Biased or unfair actions
                                         well-understood problems, established mitigations
      4. Data breaches
      5. Disrupt connected systems
      6. Speed and volume                risk multiplier
      7. Cascading effects               speed and reach outrun existing safeguards
        Four Pillars
     A. Assess and bound risks
     B. Make humans accountable
     C. Technical controls
     D. Enable end-user responsibility
ocelliq.com/astar-lr                                                                         40 / 78

## Slide 41 · PDF page 59 · Even the Experts Get Burned

[Slide image](page-059.png)

6.5 Even the Experts Get Burned

         Seven Risks                 Technical Controls
      ✘ Erroneous actions            Move emails to trash; disable permanent deletion.
      ✘ Unauthorized actions         Only allow deleting emails received in the last 24
      3. Biased or unfair actions    hours.
      4. Data breaches
      5. Disrupt connected systems
      ✘ Speed and volume             Max 10 deletions per run; human approval to
      7. Cascading effects           continue.
        Four Pillars
                                          Meta’s director of AI alignment had OpenClaw
     ✘ Assess and bound risks
                                          expunge her emails without approval.47
     B. Make humans accountable
     ✘ Technical controls                 I had to run to my Mac mini like I was defusing a bomb.
     D. Enable end-user responsibility                                             — Summer Yue

ocelliq.com/astar-lr                                                                           41 / 78

## Slide 42 · PDF page 60 · Getting It Wrong:Klarna

[Slide image](page-060.png)

6.6 Getting It Wrong: Klarna

         Seven Risks
      1. Erroneous actions
      2. Unauthorized actions            Customer support that went “too far”
      ✘ Biased or unfair actions
                                         • Feb 2024: claimed work of 700 reps, projected $40M
      4. Data breaches
                                           profit boost48
      5. Disrupt connected systems
                                         • Quality decayed on disputes, fraud, bereavement
      6. Speed and volume
                                         • May 2025: CEO walked it back49
      7. Cascading effects
                                           ‣ “what you end up having is lower quality”
        Four Pillars
     A. Assess and bound risks
     ✘ Make humans accountable
     C. Technical controls
     D. Enable end-user responsibility
ocelliq.com/astar-lr                                                                        42 / 78

## Slide 43 · PDF page 61 · Getting It Wrong:Bee Cheng Hiang

[Slide image](page-061.png)

6.7 Getting It Wrong: Bee Cheng Hiang 50

         Seven Risks
      ✘ Erroneous actions
      2. Unauthorized actions
      3. Biased or unfair actions
      ✘ Data breaches
      5. Disrupt connected systems
      ✘ Speed and volume
      7. Cascading effects
        Four Pillars
     ✘ Assess and bound risks
     ✘ Make humans accountable
     ✘ Technical controls                Agent exposed recipients’ email addresses by
     D. Enable end-user responsibility   putting them in “To” instead of “BCC”.

ocelliq.com/astar-lr                                                                    43 / 78

## Slide 44 · PDF page 63 · Getting It Wrong:Replit

[Slide image](page-063.png)

6.8 Getting It Wrong: Replit 51

        Seven Risks                     Technical Controls
     1. Erroneous actions
     ✘ Unauthorized actions
     3. Biased or unfair actions
     4. Data breaches
     ✘ Disrupt connected systems        Automatic backup before every change.
     6. Speed and volume
     ✘ Cascading effects
        Four Pillars
     ✘ Assess and bound risks
     B. Make humans accountable
     ✘ Technical controls
     ✓ Enable end-user responsibility Deleted live business
                                      Restore from backup indata despite a code freeze.
                                                             one click.

ocelliq.com/astar-lr                                                                      44 / 78

## Slide unnumbered · PDF page 64 · Set Policies for a Procurement Agent

[Slide image](page-064.png)

7.
     Set Policies for a
     Procurement Agent

## Slide 46 · PDF page 66 · Procurement Agent

[Slide image](page-066.png)

7.1 Procurement Agent

        INGEST                     VERIFY                         DRAFT                  REVIEW
                                     Aperture

                                        Helix
        Prepare                                                 Synthesize                Write
                                     Meridian
         brief                                                   & score                  slide
                                     Northstar

                                     Peregrine
        Understand             Check each bid for         Score each correct bid using    Present
       requirements        completeness and correctness     the competitive criteria

     /imda-ai why is it important to write the procurement brief
     without access to the bids?

           /imda-ai equips your agent with the IMDA framework.
ocelliq.com/astar-lr                                                                                46 / 78

## Slide 47 · PDF page 67 · Use the framework with your agent

[Slide image](page-067.png)

7.2 Use the framework with your agent

        Seven Risks                              INGEST                         VERIFY
     1. Erroneous actions                                                         Aperture
     2. Unauthorized actions
     ✓ Biased or unfair actions                                                      Helix
     4. Data breaches                            Prepare
                                                                                  Meridian
                                                  brief
     5. Disrupt connected systems
     6. Speed and volume                                                          Northstar
     ✓ Cascading effects                                                          Peregrine
        Four Pillars                             Understand                 Check each bid for                   S
                                                requirements            completeness and correctness
     ✓ Assess and bound risks
     B. Make humans accountable          If an agent can’t see the bids, they can’t influence the
     ✓ Technical controls                criteria and unfairly privilege one of the bidders.
     D. Enable end-user responsibility
ocelliq.com/astar-lr                                                                                   47 / 78

## Slide 48 · PDF page 69 · Verify:why separate agents?

[Slide image](page-069.png)

7.3 Verify: why separate agents?

        INGEST                       VERIFY                         DRAFT                  REVIEW
                                       Aperture

                                          Helix
        Prepare                                                   Synthesize                Write
                                       Meridian
         brief                                                     & score                  slide
                                       Northstar
                                       Peregrine
        Understand               Check each bid for         Score each correct bid using    Present
       requirements          completeness and correctness     the competitive criteria



     /imda-ai Why use a separate agent to verify each bidder?

     Separate agents prevent each bidder’s evidence from influencing another’s evaluation.
ocelliq.com/astar-lr                                                                                  48 / 78

## Slide 49 · PDF page 71 · Verify:what else could go wrong?

[Slide image](page-071.png)

7.4 Verify: what else could go wrong?


     Assume each verifier has a correct BRIEF.md and access to only
     its assigned bid. What other risks remain? Use /imda-ai.

           Also try
           Explain the biggest remaining risk in two sentences for our
           evaluation panel.                             Specify target audience


           Make a table linking each failure to its procurement impact
           and its IMDA risk category.                      Specify a structure


           How could a verifier incorrectly pass a bid?              Probe a failure



ocelliq.com/astar-lr                                                              49 / 78

## Slide 50 · PDF page 72 · Choose a risk and manage it

[Slide image](page-072.png)

7.5 Choose a risk and manage it




     Pick one risk from your agent’s suggestions that you want to address.

     Help me develop a control for [chosen risk]. Offer 2-3 options
     with tradeoffs, and guide me to choose the policy.
           Also try
           Interview me like a senior executive and use my responses
           to craft the policy.

ocelliq.com/astar-lr                                                         50 / 78

## Slide 51 · PDF page 73 · Make a Presentation

[Slide image](page-073.png)

7.6 Make a Presentation




     /pptx present the risk assessment for Verify. Include risks,
     controls, residual risk, owners and tests. Flag gaps.

ocelliq.com/astar-lr                                                51 / 78

## Slide 52 · PDF page 75 · Verify:check each offered commitment

[Slide image](page-075.png)

7.7 Verify: check each offered commitment

         Seven Risks
                                          What if it hallucinates a date or price?
      1. Erroneous actions
      2. Unauthorized actions            Mitigations
                                         • Trace each value: quote the source and exact
      3. Biased or unfair actions
                                           clause or row.
      4. Data breaches
                                         • Recalculate: have the agent check totals and
      5. Disrupt connected systems
                                           date arithmetic with a calculator.
      6. Speed and volume
                                         • Stop on uncertainty: keep missing or
      7. Cascading effects
                                           conflicting values unresolved; escalate to a
        Four Pillars                       human.
     A. Assess and bound risks           • Human review: require the Panel to check
     B. Make humans accountable            decisive evidence before accepting a pass.
     C. Technical controls
     D. Enable end-user responsibility

ocelliq.com/astar-lr                                                                      52 / 78

## Slide 53 · PDF page 76 · Optional:test your mitigation

[Slide image](page-076.png)

7.8 Optional: test your mitigation




     Would my mitigation catch any of the errors in /slides “A
     convincing recommendation”? Explain how.

           Also try
           Propose a concrete error that my mitigation would catch.




ocelliq.com/astar-lr                                                  53 / 78

## Slide 54 · PDF page 77 · Optional:run the evaluation

[Slide image](page-077.png)

7.9 Optional: run the evaluation




     Process the bids using the agent in AGENT-DESIGN.md.

           Also try
           /procurement-ingest-check                                 Check BRIEF.md for errors


           Adversarially review the agent and recommendation against
           the original sources and /imda-ai.                   ~8 minutes

                 Ask the agent to challenge assumptions and find flaws.


ocelliq.com/astar-lr                                                                        54 / 78

## Slide unnumbered · PDF page 78 · ATLAS: governance in practice

[Slide image](page-078.png)

8.
     ATLAS:
     governance in practice

## Slide 56 · PDF page 80 · IMCB ATLAS

[Slide image](page-080.png)

8.1 IMCB ATLAS

                       ATLAS is IMCB’s AI business intelligence platform.
                       It answers questions about grants, personnel, and contracts
                       where facts are spread across many business units.
                       • “What is the current renewal/mid-grant reporting?”
                       • “Is the grant extension pending any signatures?”
                       • “Has this PA stalled out?”
                       • “Was the virement complete before the tender?”
                       Answering some of these questions can take days.
                       High-risk application of AI
                       • Consumes a variety of business function documents
                         (LOA, PA, Contracts, etc.)

           AT L A S    • May be used to make business decisions

ocelliq.com/astar-lr                                                            56 / 78

## Slide 57 · PDF page 82 · IMCB ATLAS:Document Flow

[Slide image](page-082.png)

8.2 IMCB ATLAS: Document Flow
         Seven Risks                     Producers            AT L A S          Consumers
      1. Erroneous actions
                                            ED                                      ED
      2. Unauthorized actions
      3. Biased or unfair actions           PI 1                                    PI 1
      4. Data breaches
      5. Disrupt connected systems          PI 2                                    PI 2
      6. Speed and volume
      7. Cascading effects               Contracts                               Contracts

        Four Pillars                        HR                                      HR
     A. Assess and bound risks
     B. Make humans accountable           Tech-biz                                Tech-biz
     C. Technical controls                   ⋯                                        ⋯
     D. Enable end-user responsibility           ATLAS answers questions for consumers,
                                                        depending on their role.
ocelliq.com/astar-lr                                                                         57 / 78

## Slide 58 · PDF page 83 · Unauthorized access& data breach

[Slide image](page-083.png)

8.3 Unauthorized access & data breach
         Seven Risks                     Producers           AT L A S            Consumers
      1. Erroneous actions
                                            ED                  PA                    ED
      2. Unauthorized actions
      3. Biased or unfair actions           PI 1               LOA                   PI 1
      4. Data breaches
      5. Disrupt connected systems          PI 2        PI 1 Project Update          PI 2
      6. Speed and volume
      7. Cascading effects               Contracts      PI 2 Project Update       Contracts

        Four Pillars                        HR               Appraisal                HR
     A. Assess and bound risks
     B. Make humans accountable           Tech-biz           Licensing             Tech-biz
     C. Technical controls                   ⋯                                        ⋯
     D. Enable end-user responsibility     If everyone uses the same chatbot, what stops it
                                               revealing documents they shouldn’t see?
ocelliq.com/astar-lr                                                                          58 / 78

## Slide 59 · PDF page 86 · Unauthorized access& data breach

[Slide image](page-086.png)

8.4 Unauthorized access & data breach
        Seven Risks                      Producers          AT L A S           Consumers
     1. Erroneous actions
                                            ED                 PA                   ED
     ✓ Unauthorized actions
     3. Biased or unfair actions           PI 1               LOA                  PI 1
     ✓ Data breaches
     5. Disrupt connected systems           PI 2       PI 1 Project Update         PI 2
     6. Speed and volume
     7. Cascading effects                Contracts     PI 2 Project Update      Contracts

        Four Pillars                        HR              Appraisal               HR
     A. Assess and bound risks
     B. Make humans accountable           Tech-biz          Licensing            Tech-biz
     C. Technical controls                  ⋯                                         ⋯
     D. Enable end-user responsibility     Policy: When PI 1 uses ATLAS, it can only read
                                                or write PI 1′s authorised documents.
ocelliq.com/astar-lr                                                                        59 / 78

## Slide 60 · PDF page 87 · Unauthorized access:policy and control

[Slide image](page-087.png)

8.5 Unauthorized access: policy and control

         Seven Risks                     The risk
      1. Erroneous actions               Users may access documents (reading or writing)
      2. Unauthorized actions            they are not supposed to, leaking business secrets.
      3. Biased or unfair actions
                                         Policy questions
      4. Data breaches
                                         • Who may read which facts?
      5. Disrupt connected systems
                                         • Who may write, and to which records?
      6. Speed and volume
                                         • How is access revoked when someone leaves?
      7. Cascading effects
                                         • Are there more fine-grained controls for
        Four Pillars                       information?
     A. Assess and bound risks
     B. Make humans accountable          Technical control: Role-Based Access Control
     C. Technical controls               ATLAS can only read/write documents the user has
     D. Enable end-user responsibility   access to.

ocelliq.com/astar-lr                                                                           60 / 78

## Slide 61 · PDF page 88 · Erroneous action

[Slide image](page-088.png)

8.6 Erroneous action
         Seven Risks                     Producers            AT L A S           Consumers
      1. Erroneous actions
                                            ED                   PA                  ED
      2. Unauthorized actions
      3. Biased or unfair actions           PI 1              LOA                    PI 1
      4. Data breaches
      5. Disrupt connected systems          PI 2         PI 1 Project Update         PI 2
      6. Speed and volume
      7. Cascading effects               Contracts       PI 2 Project Update      Contracts

        Four Pillars                        HR                Appraisal              HR
     A. Assess and bound risks
     B. Make humans accountable           Tech-biz            Licensing            Tech-biz
     C. Technical controls                   ⋯                                         ⋯
     D. Enable end-user responsibility           What if the LLM misfiles the document?

ocelliq.com/astar-lr                                                                          61 / 78

## Slide 62 · PDF page 89 · Cascading effects

[Slide image](page-089.png)

8.7 Cascading effects
         Seven Risks                     Producers          AT L A S           Consumers
      1. Erroneous actions
                                            ED                  PA                  ED
      2. Unauthorized actions
      3. Biased or unfair actions           PI 1            LOA                    PI 1
      4. Data breaches
      5. Disrupt connected systems          PI 2       PI 1 Project Update         PI 2
      6. Speed and volume
      7. Cascading effects               Contracts     PI 2 Project Update       Contracts

        Four Pillars                        HR              Appraisal               HR
     A. Assess and bound risks
     B. Make humans accountable           Tech-biz          Licensing            Tech-biz
     C. Technical controls                   ⋯                                        ⋯
     D. Enable end-user responsibility       What if the error cascades into downstream
                                                         business decisions?
ocelliq.com/astar-lr                                                                         62 / 78

## Slide 63 · PDF page 90 · How should humans check AI's filing?

[Slide image](page-090.png)

8.8 How should humans check AI’s filing?

         Seven Risks                     Information is risky depending on its use
      1. Erroneous actions
                                         • A grant end date in
      2. Unauthorized actions              ‣ an internal “congratulations” email, vs.
      3. Biased or unfair actions          ‣ used to extend staff contracts.
      4. Data breaches
      5. Disrupt connected systems       Set policies to balance the risk of using information
      6. Speed and volume                with the effort of checking it.
      7. Cascading effects               Policy questions
                                         • Which conclusions are high-risk and need
        Four Pillars
                                           immediate human verification?
     A. Assess and bound risks
                                         • Which conclusions are safe to check only when
     B. Make humans accountable
                                           an error is discovered?
     C. Technical controls
                                         • Once an error is discovered, who owns the
     D. Enable end-user responsibility
                                           correction?
ocelliq.com/astar-lr                                                                        63 / 78

## Slide 64 · PDF page 91 · Erroneous action:policy and control

[Slide image](page-091.png)

8.9 Erroneous action: policy and control


     Pillar B: Make humans meaningfully         Pillar D: Enable end user responsibility
     accountable
                                                How can we ensure consumers are not led
     How can we get producers to verify that    astray by ATLAS?
     ATLAS understands documents correctly?
                                                • Every answer reports its sources and
     • Every document type has one named          corroboration.
       owner (grants office, HR, procurement)   • Provide a mechanism for reporting wrong
     • ATLAS only flags potential issues, and     answers and feeding back.
       records the human’s exact decision.      • Set risk-based policy for level of scrutiny.
     How can we reduce review fatigue while
     keeping human oversight effective?


ocelliq.com/astar-lr                                                                         64 / 78

## Slide 65 · PDF page 92 · Human oversight in practice

[Slide image](page-092.png)

8.10 Human oversight in practice


     Consumer View (example)


       “Total grant value is $1,225,600.                              It’s our responsibility to
                                verified by leews 11d ago (Report)   design ATLAS defensively,
                                                                      against foreseeable risks.
       Available balance is $318,400.                                 The “easy” path must be
                               AI checked, request human             the safe path, and it must
                                                                      fit cleanly into existing
       Staff contracts end on 30 June 2027.”                                  processes.

                                   AI check failed, request human



ocelliq.com/astar-lr                                                                               65 / 78

## Slide 66 · PDF page 93 · Governance from the start

[Slide image](page-093.png)

8.11 Governance from the start




                              ATLAS is in early development at
                              IMCB.
                              We’re designing these controls in from
                              the start.


           AT L A S
ocelliq.com/astar-lr                                                   66 / 78

## Slide unnumbered · PDF page 94 · Where do we go from here?

[Slide image](page-094.png)

9.   Where do we go from here?

## Slide 68 · PDF page 95 · Workflows get complicated

[Slide image](page-095.png)

9.1 Workflows get complicated


                        web     draft
                   Search agent A        Critic                             Slides    GATE

                               revise
    Task /                                        reject
                   Search agent B        Critic            ✕   Synthesize   Email     GATE       Output
    query

                   Search agent C        Critic                              Log      GATE




                                    Today, we’ve only scratched the surface.
               AI engineering offers new and effective tools for putting policy into practice.


ocelliq.com/astar-lr                                                                                68 / 78

## Slide 69 · PDF page 96 · The future of AI

[Slide image](page-096.png)

9.2 The future of AI


     Regulation                                       Commercial strategy
     • New regulations on the use of AI               • Resist vendor lock-in
       ‣ EU AI Act; South Korea’s AI Basic Act          ‣ Pace of development means long-term
       ‣ China’s AI-content labelling                     value is hard to predict
       ‣ Claude Fable 5 export ban                      ‣ Expensive value-added services may be
                                                          much cheaper or obsolete in months
     • Guardrails to restrict frontier intelligence
                                                        ‣ Keep your data exportable and your
       ‣ Synthetic biology research
                                                          workflows portable
     • Increased interest in “local” models
                                                      • Assess the full cost of ownership
       ‣ Provides freedom and control
                                                        ‣ Account for governance and oversight
         – sometimes cost savings
                                                        ‣ Measure benefit on your tasks
       ‣ Hardware depreciates quickly
                                                        ‣ Scale when the results justify it

ocelliq.com/astar-lr                                                                              69 / 78

## Slide 70 · PDF page 97 · Build something you trust.

[Slide image](page-097.png)

9.3 Build something you trust.




                   Start small
                        ↓               We’re living through a
               Automate part of it     moment of extraordinary
                        ↓
              Keep human oversight            possibility.
                        ↓
             Make evidence checkable   The next chapter is ours
                        ↓
                Build confidence
                                              to shape.


ocelliq.com/astar-lr                                              70 / 78

## Slide unnumbered · PDF page 98 · Build something you trust.

[Slide image](page-098.png)

OcelliQ.com/astar-lr
            /tell-gaurav
Help us improve! Your agent will ask a few   Connect with me on
 questions and send Gaurav your feedback.        LinkedIn.

## Slide 72 · PDF page 99 · References

[Slide image](page-099.png)

References
     1.   Amazon News. Amazon CEO Andy Jassy talks 6 truths surrounding the rise of AI. 2026.
     2.   Microsoft. The golden opportunity for American AI. 3 January 2025.
     3.   Anthropic. Estimating AI productivity gains from Claude conversations. 25 November 2025.
          Research projections.
     4.   Gartner. Worldwide AI Spending Forecast. 16 September 2026. AI infrastructure: US$1.484 trillion
          forecast for 2026.
     5.   OpenAI. The Hugging Face incident and the road ahead. 26 August 2026. Postmortem of the July
          2026 cybersecurity-evaluation incident.
     6.   The Guardian. AI agent deletes a firm’s database. 29 April 2026.
     7.   CNN, syndicated by KTVZ. US military close call after a false AI intelligence report. 18 September
          2026. Reporting based on unnamed sources, not an official incident finding.
     8.   The Planetary Society.
          How much did the Apollo program cost?.
          Apollo, 1960-1973: US$309 billion in 2025 dollars.
     9.   AskEngineers discussion.
          Hypothetical Great Wall rebuilding estimate.
          2015. Informal estimate; not a professional quotation. Exact US$452 billion value not
          independently verified.
ocelliq.com/astar-lr                                                                                           72 / 78

## Slide 73 · PDF page 100 · References

[Slide image](page-100.png)

References
     10. Workshop illustrative model.
         Cumulative global datacenter spending.
         Supplied historical anchors and adjustment assumptions; not a measured historical series.
     11. Gartner.
         Data Center Electricity Consumption Forecast.
         10 June 2026. AI-optimized servers: 175 TWh forecast for 2026.
     12. Energy Market Authority, Singapore.
         Singapore Energy Statistics: Energy Consumption.
         2024 electricity consumption: 58 TWh.
     13. China Three Gorges Corporation.
         Three Gorges annual power generation.
         19 November 2020. Designed annual generation: 88.2 TWh; distinct from actual output.
     14. Info-Tech Research Group. Discover the Enterprise AI Technology Stack.
     15. NIST. AI Risk Management Framework: AI RMF Core.
     16. Andreessen Horowitz. Emerging Architectures for LLM Applications.
     17. Amazon Web Services. Layered approach for a generative AI platform. AWS Prescriptive Guidance.
     18. NVIDIA. AI’s five-layer cake.

ocelliq.com/astar-lr                                                                                  73 / 78

## Slide 74 · PDF page 101 · References

[Slide image](page-101.png)

References
     19. Ajay Agrawal, Joshua Gans, Avi Goldfarb.
         Prediction Machines: The Simple Economics of Artificial Intelligence.
         Harvard Business Review Press, 2018.
     20. William Stanley Jevons.
         The Coal Question, Chapter VII: Of the Economy of Fuel.
         First published 1865; linked text is the second edition, Macmillan, 1866.
     21. Daron Acemoglu, Simon Johnson.
         Power and Progress: Our Thousand-Year Struggle Over Technology and Prosperity.
         PublicAffairs, 2023. Further reading on technology and prosperity.
     22. OpenAI.
         Tokenizer.
         Interactive examples of tokenization.
     23. OpenRouter. Daily token totals for top 50 models. Usage feed. Prices and listing dates: models
         catalog. Snapshot: 30 September 2026.
     24. Artificial Analysis, via OpenRouter. Artificial Analysis Intelligence Index. Benchmark snapshot: 30
         September 2026. Stored curated scores and teaching overrides: 01-intro/data/README.md.
     25. Artificial Analysis. Gemini 4 Argon: Google is back as one of the top three labs in intelligence
         achieved. 30 September 2026. AAII 53 (high); standard input/output pricing of US$4/US$20 per
         million tokens, before the introductory discount.
ocelliq.com/astar-lr                                                                                           74 / 78

## Slide 75 · PDF page 102 · References

[Slide image](page-102.png)

References
     26. Artificial Analysis. Muse Spark 1.3 (max). Read 2 October 2026. AAII 48 under Intelligence Index
         v4.3.2; later benchmark reading than the stored September snapshot.
     27. Moonshot AI. Kimi K3 model card. 2.8T total parameters; native MXFP4 weights. Read 2 October
         2026.
     28. DeepSeek. DeepSeek V4.1 Flash model card. 552B backbone plus 196B Engram lookup parameters.
         Read 2 October 2026.
     29. Z.ai. GLM 5.3 Flash model card. 320B total parameters. Read 2 October 2026.
     30. Tobias Groot and Matias Valdenegro-Toro. Overconfidence is Key: Verbalized Uncertainty Evaluation
         in Large Language and Vision-Language Models. TrustNLP 2024, pp. 145-171.
     31. Sharma et al. Towards Understanding Sycophancy in Language Models. 2023.
     32. Shapira et al. Clever Hans or Neural Theory of Mind? Stress Testing Social Reasoning in Large
         Language Models. arXiv:2305.14763, 2023.
     33. Anthropic. Sycophancy to Subterfuge: Investigating Reward Tampering in Language Models. 17 June
         2024. Controlled training experiments; not established as common production behavior.
     34. John R. Searle.
         Minds, brains, and programs.
         Behavioral and Brain Sciences 3(3), 417-424, 1980. Chinese Room argument.

ocelliq.com/astar-lr                                                                                    75 / 78

## Slide 76 · PDF page 103 · References

[Slide image](page-103.png)

References
     35. Wallace et al. The Instruction Hierarchy: Training LLMs to Prioritize Privileged Instructions. OpenAI,
         2024.
     36. Liu et al. Lost in the Middle: How Language Models Use Long Contexts. arXiv:2307.03172 (2023);
         Transactions of the Association for Computational Linguistics, 2024.
     37. Anthropic. Project Vend, phase one. 27 June 2025. Claude Sonnet 3.7 running a real office shop with
         Andon Labs.
     38. Aditya Mehta, TechCrunch. AI hallucination nearly triggers US military operation. 18 September
         2026.
     39. Menghua Xia et al.
         DREAM: On hallucinations in AI-generated content for nuclear medicine imaging.
         arXiv:2506.13995v2, 18 June 2025. Sections III-IV; displayed image is Figure 5.
     40. Reuters. South Africa withdraws draft AI policy over fictitious references. 27 April 2026. Screenshot:
         Reuters republication on MyJoyOnline, 28 April 2026.
     41. Anthropic. Claude Code commands. /usage, /context and /compact; availability depends on the
         account and environment. Read 4 October 2026.
     42. Anthropic. Manage costs effectively. Session figures are estimates; subscription limits and API
         consumption differ. Read 4 October 2026.


ocelliq.com/astar-lr                                                                                          76 / 78

## Slide 77 · PDF page 104 · References

[Slide image](page-104.png)

References
     43. Anthropic. How Claude Code works. Context, subagents and compaction; early details can be lost
         during summarization. Read 4 October 2026.
     44. Infocomm Media Development Authority (IMDA). Model AI Governance Framework for Agentic AI.
         Version 1.5. Published 20 May 2026; updated 5 June 2026. Local PDF and extracts in references/
         imda-agentic-ai/.
     45. International Organization for Standardization / International Electrotechnical Commission.
         ISO/IEC 42001:2023 — Artificial intelligence — Management system.
         First edition, December 2023.
     46. OWASP GenAI Security Project, Agentic Security Initiative.
         Agentic AI — Threats and Mitigations.
         Version 1.0, 17 February 2025.
     47. Summer Yue.
         First-person account of OpenClaw deleting her inbox.
         22 February 2026. Post and screenshots; does not establish permanent loss of all messages.
     48. Klarna.
         AI assistant handles two-thirds of customer service chats.
         27 February 2024. Company release: work equivalent to 700 agents; projected US$40 million profit
         improvement.

ocelliq.com/astar-lr                                                                                    77 / 78

## Slide 78 · PDF page 105 · References

[Slide image](page-105.png)

References
     49. Charles Daly, Bloomberg.
         Klarna Slows AI-Driven Job Cuts With Call for Real People.
         8 May 2025. CEO interview; full text requires a subscription.
     50. Kenny Chee, The Straits Times.
         Bee Cheng Hiang customer email exposure.
         30 September 2026; updated 2 October 2026.
     51. Lee Chong Ming, Business Insider.
         Replit CEO apologizes after AI agent deletes production data.
         22 July 2025.




ocelliq.com/astar-lr                                                     78 / 78
