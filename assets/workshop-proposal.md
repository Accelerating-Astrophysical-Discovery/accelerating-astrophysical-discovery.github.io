Proposal for a Lorentz workshop

# 1\. Title

**Accelerating Astrophysical Discovery with Foundation Models**

***Revisions:***

* ***Extended section 5\.***

# 2\. Organizers

* **Joshua Albert (Caltech, USA & Leiden Observatory, NL)**                                                   Expertise: Machine learning, Computational Physics (Physics) 

* **Roberto Ruiz de Austri (IFIC, CSIC & Universidad de Valencia, Spain)**                                  Expertise: Particle and Astro-particle physics (Physics) 

* **Sascha Caron (Radboud University & Nikhef, NL)**                                                          Expertise: Machine Learning applications in physics (Physics)

* **Gabrijela Zaharijas  (University of Nova Gorica, Slovenia)**                                     Expertise: Astro-particle physics: gamma rays and multi-wavelength/messenger dark matter search (Physics)

* **Francisco Villaescusa (Simons Foundation, NY, USA)**                                             Expertise: Cosmology and astro-physics (Physics)

# 3\. Abstract

This workshop will bring together leading researchers from across the globe, from both academia and industry, with the goal of developing specialised foundation models (LLMs) that can boost discovery in astrophysics. Foundation models can accelerate discovery via at least four key capabilities: anomaly detection in vast datasets, combining multi-modal data to surpass individual instrument limits, ansatz-free simulation initialization, and agentic collaborative scientific exploration of massive heterogeneous physical datasets. The participants will form the basis of a collaboration that brings these foundation models to reality. The workshop will be focused on design and planning the roadmap, but will also involve a hands-on tutorial-like portion. They will learn how state-of-the-art foundation models are built, trained, and continuously improved. They will curate optimal datasets combining multi-modal observational data (radio, optical, X-ray, gravitational waves, etc.), simulation representations (system 3D snapshots, simulation parametrisations, etc.), and language data (scientific analysis, code, etc.). They will map the technical and funding challenges. They will jointly develop science use cases leveraging the foundation models aligned with European funding opportunities. Outcomes will include a clear roadmap for several astrophysical foundation models, curated datasets, and a networked community to publish a white paper and pursue follow-up collaborations.

# 4\. Scientific Case 

Recent advancements in artificial intelligence (AI), particularly in token-based reasoning large scale foundation models, self-supervised models trained on extensive and diverse datasets and refined on human interaction have revolutionized how humans interact with machines to solve problems. So called ‘shadow AI’ is where humans come to rely on AI to boost productivity, and spark new ideas, becoming a new way of life. In spheres such as education, the debate is no longer how to oppose this change, but rather how to safely incorporate it, with countries like Estonia already going so far as to purchase all students and teachers GPT subscriptions. However, the applicability of current AI models to direct scientific discovery is limited, since the models are unable to understand and reason with physical datasets. We want to accelerate astrophysical discovery, by creating specialised foundation models which understand and reason on rich multi-modal physical datasets, and making this widely available to all researchers.

Learning rich context across multimodal datasets is beginning to unlock state-of-the-art reasoning \[1, 2, 3\], anomaly detection \[4\], super resolution \[5\], translations between modalities and dimensional spaces \[6, 7\], astrophysics \[8\], and even machine assisted mathematical proofs \[9, 10\]. These models possess remarkable capabilities in identifying complex patterns, integrating diverse data sources, and generalizing to new scenarios with minimal additional training. Such capabilities position foundation models as highly promising tools to accelerate discovery across astrophysics.

Modern astrophysics and particle physics rely heavily on diverse observational data from gravitational waves, neutrinos, gamma-rays, X-rays, infrared, radio waves, and optical signals. Crucially, multimodal observations in different modalities frequently originate from common astrophysical systems, offering complementary views of the same systems. Each type of observation offers unique physical insights, yet traditionally, these data streams are analysed independently, limiting the full understanding of cosmic phenomena. Jointly analysing these multimodal datasets holds the potential to reveal subtle connections, push instrumental limits, connect data to simulation, and ultimately, hopefully, accelerate discovery of new physics. Foundation models are uniquely positioned to excel in detecting correlations across multimodal data, and communicating it to humans.

The focuses of this workshop are related to high-level functionality we think astrophysical foundation models should have, and are identified by these Key Problem Areas (KPAs):

1. Detecting rare events or anomalies from new physics.  
2. Surpassing the resolution and sensitivity limits of individual instruments.  
3. Sampling ansatz-free initial conditions for astrophysical simulations.  
4. Natural language and collaborative reasoning on multimodal astrophysical datasets.

**KPA 1** Firstly, finding rare events and anomalies in observational data is a challenge given the enormous data volumes. Typically, the signals of such events are very low, which makes blind searches very inefficient. Enhancing these signals would lead to a dramatic increase in detection rate. Multimodal models already accelerate this sort of work in other fields \[4\].

**KPA 2** Secondly, individual instruments are limited by their angular and spectral resolutions, hitting confusion limits at depths where sources are so close together that they can no longer be distinguished. Traditionally, these resolutions cannot be increased without sacrificing sensitivity. This puts a cap on the usefulness and lifetime of instruments. However, these limits could be overcome if sources can be correlated across multimodal data. This is already possible in other fields \[5\].

**KPA 3** Thirdly, currently setting initial conditions for simulations is a fundamental challenge as it requires an ansatz, e.g. how the initial mass is distributed in a system. In the ideal world, initial conditions would be stochastically sampled from observational data. However, since we only have a monocular perspective, this is challenging given traditional methods. State-of-the-art deprojection from multimodal data into 3D physical systems exists in industry \[6, 7\], leveraging physical priors of the scene being deprojected. This trades the initial condition ansatz dependency for a model-learned prior, and given the extensive availability of high quality simulation data, these priors are much richer.

**KPA 4** Finally, the most unified human-machine symbioses of scientific discovery, in the not too distant future, is one where both are able to contribute to the discovery process. In addition to the foundation model being able to understand multi-modal physical datasets, it will also understand language and science, and have the ability to reason and communicate. The formal problem of KPA 4 is to design the process by which reasoning on large multi-modal datasets will optimally lead to accelerated discovery, focusing on aspects such as continuous improvement, physical alignment, embedded scientific method, and autonomous agentic systems. Such multi-media capabilities are not so different from today’s consumer language models, which can already understand and produce images.

A key finding since the start of the AI-boom is that the quality of training data, and implicit structure within said data, is the main factor driving emergent model capability. Physics, the greater sciences, and mathematics being projections of nature produces the ultimate multimodal dataset. Already massive amounts of high-quality multi-modal astrophysical data are being curated \[8\] and it stands to reason that it is only a matter of time before we unlock their potential.

However, leveraging foundation models effectively in this context poses distinct scientific and technical challenges. Firstly, imposing constraints into the foundational models would be necessary to control for hallucination-related problems. Secondly, the ML-related skills required to execute such an endeavour on this scale are typically not found in academia, as industry tends to attract this talent. Thirdly, this is a highly multidisciplinary problem. Hence, a collaborative, interdisciplinary approach is crucial to realistically assess, refine, and develop these methods for application in astronomy and particle physics.

# Workshop Goals 

The primary goal of this workshop is to bring together researchers from astrophysics, particle physics, computational physics, and artificial intelligence (both from academia and industry) under an open science project to carry out the work that will eventually result in specialised astrophysical foundation models that accelerate discovery and exploration of the rapidly growing volume of high quality multi-messenger observational data. This workshop will be largely about creating shared understanding, solving problems that can only be solved via intense collaboration, and creating momentum for the project.

We believe the Lorentz Center is ideal for this due to its historically interdisciplinary nature and strategic location. As well, several of our participants are based at Dutch institutions (Radboud University, Leiden, Amsterdam and  SURF) with some working in experimental collaborations and in Large Language Models (LLMs) technology. We aim to tightly couple the Dutch astrophysics community to this highly collaborative project.

Finally, the proposed topic is timely and holds enormous potential for fundamental research that promises to catalyse a new paradigm in astrophysics, as well as fields beyond, where perhaps our system can be used as a basis for fine-tuning on disparate, but nonetheless physics-based, data, e.g. biological and neuroimaging data, etc.

## Expected Outcomes

###        **By end of workshop**

1. Shared understanding of the different aspects required to create and deploy a foundation model. This includes but is not limited to,  
   1. Understanding if we must train from scratch or fine-tuning existing models works.  
   2. What SOTA models are applicable?  
   3. How do we handle vast mutli-modal data?  
   4. How do we solve the very long context problem?  
   5. What are the latest methods for high performance inference?  
   6. What sort of compute resources are required and what is the cost?  
   7. How do we continuously improve the models?  
   8. What are the costs associated?  
2. Shared understanding of the scientific end user desires  
   1. How will researchers use the system to solve problems under each KPA?  
   2. How do we align the models to physical constraints?  
   3. How achievable is this and what are the risks?  
3. A collaboration structure that is able to carry out the build and deployment.   
   1. A team per KPA responsible for curating datasets and preparing them for training.  
   2. A team of people who will contribute their time to implement the coding requirements under an open source project.  
   3. A list of research proposals that would utilise the end system (i.e. first use cases from within the collaboration).  
   4. An understanding of what skills are missing within the collaboration that need to be procured from industry.  
   5. An understanding of our timeline and plans to reconvene.  
4. An assessment of potential collaboration resources,  
   1. What funding is already available?  
   2. What computational resources are available?  
   3. What development resources are available?  
5. Living assets  
   1. In the spirit of a hackathon, a GitHub repo with all workshop attendees added, and we’ll make use of the repo to track issues and todo items throughout the workshop, and after the workshop.  
   2. Data set specs and tokenisation semantics for each KPA, documented and in the repo.  
   3. Initial foundation-model use case for each KPA, documented and in the repo.  
   4. A workback of backlog work for the collaboration to do over the coming months.  
   5. Initial code committed during the hackathon sessions, which builds momentum for post-workshop.

### In the months following

1. KPA teams curate data sets, and validate tokenisation semantics  
2. The implementation team will implement the distributed model/training/inference setup.  
3. The collaboration will publish a **white paper** outlining the chosen path to success and challenges.  
4. The research use cases defined during the workshop will collectively form the Minimal Viable Product (MVP).  
5. Funding opportunities will be pursued (e.g. EU COST Action), after the necessary publications are made. These funding will cover at least these aspects,  
   * Procuring computational resources (e.g. GPUs, HPC).  
   * Followup workshops or meetings.  
   * Potentially, as necessary, hiring software engineers.  
6. The project will become attached to the European Coalition for AI in Fundamental Physics ([www.https://eucaif.org](http://www.https://eucaif.org)).

# 4.1 Focus of workshop

All above KPAs in this proposal are downstream capabilities of a large self-supervised “physics foundation model” trained on trillions of tokens of physics-rich data a very wide variety of astrophysical data types (images, event lists, spectra, time series, catalogues, and simulations) plus language/code/provenance. The central workshop challenge is therefore not “how to do embeddings / super-resolution / translation” in isolation, but how to:

1. curate and manage the vast heterogeneous data at scale,  
2. define tokenisation semantics per data type (text-like structured representations),  
3. define informed non-autoregressive relationships (“relevancies”) between pieces of data (across modality, time, sky position, instrument response, and simulation-\>observation forward models),  
4. and train continuously over long contexts using data centres / HPC in a way that preserves physical faithfulness.

In other words, the KPAs are pillars of what we hope to be able to do once the self-supervised foundation model has learned the right structure.

1. KPA 1 uses the model’s embedding space for zero-shot clustering / OOD scoring against known classes.  
2. KPA 2 uses the same model (or a closely related vision transformer head) for conditional reconstruction (super-resolution / deconfusion), explicitly conditioned on multi-modal context.  
3. KPA 3 uses the same model for machine-translation-style mappings between observation tokens (2D) and simulation tokens (3D initial conditions / latent state), backed by forward-model consistency.  
4. KPA 4 uses existing widely available language models \+ tooling (like MCPs) to orchestrate agentic copiloting, while enforcing the scientific method.

## Seed datasets

To keep the workshop focused, we prescribe the following seed datasets as our initial set. These cover a range of wavelength/messenger modalities, optical, IR, radio, X-ray, gamma-ray, neutrinos, gravitational waves, and they are chosen due their availability and ease of access.

| Physical system | Datasets | References |
| :---- | :---- | :---- |
| Multimessenger transients and variable sources (compact-object mergers, GRBs, blazar flares; KPA1/KPA4 anchor) | GWOSC public strain \+ event products; IceCube public releases (point-source sample); Fermi–LAT 4FGL-DR4 \+ photon data access; Fermi–GBM GRB burst catalog; ZTF alert stream (time-domain optical context) | \[11–17\] |
| Wide-field multiwavelength galaxy/AGN/cluster populations in shared sky regions (KPA2/KPA4 anchor; also a “known classes” baseline for KPA1) | COSMOS multiwavelength datasets; HST via MAST; Chandra Source Catalog (CSC 2.1); XMM-Newton Science Archive (XSA); eROSITA-DE DR1 (eRASS1); LOFAR LoTSS DR2; MeerKAT MIGHTEE continuum DR1; Euclid Quick Release 1 (Q1) | \[20–26, 29\]  |
| All-sky context priors and cross-match backbone (KPA1/KPA2/KPA4 plumbing) | Gaia DR3 archive; SDSS DR17 | \[18–19\] |
| CMB \+ foregrounds (high-SNR, full-sky multimodal map products; useful for tokenisation \+ long-context experiments) | Planck Legacy Archive (PLA) products | \[28\] |
| 3D simulation corpora for observation|simulation translation (KPA3 anchor; also provides “synthetic truth” for controlled ablations) | CAMELS (and CAMELS data access docs); IllustrisTNG public data; EAGLE public database; Quijote simulations; HADES simulations | \[30–35\] |
| A pre-compiled “multi-instrument multimodal ML dataset” to bootstrap the data-engineering and tokenisation layer quickly (cross-KPA accelerator) | The Multimodal Universe (100TB) | \[36\] |
| Optical simulated surveys and alert semantics (useful for controlled tokenisation \+ realism, and for aligning alert-packet structure with KPA1/KPA4) | Rubin simulations tooling (imSim/PhoSim) \+ Rubin alert packet semantics | \[37–38\] |

## Example relevancies we will explore

We will represent the full training corpus as a relevancy graph: nodes are typed data assets (patches, events, spectra, rows, snapshots), and edges encode “what relates to what” with explicit semantics. The first workshop deliverable is a minimal, versioned relevancy schema that can be expanded.

| Kind of data | Relevancy linkages (examples) |
| :---- | :---- |
| Multi-frequency images (optical/IR/radio/X-ray) | same sky patch (WCS alignment); PSF / beam mapping kernels; “source-centric” cutouts centred on a shared catalogue object; deblending priors (high-res modality \-\> low-res modality); multi-resolution pairs created via controlled degradation (convolve+noise) for self-supervised reconstruction |
| Time-domain optical alerts / lightcurves (ZTF, Rubin-style packets) | same object-id / cross-match; same time window; “before/after” context windows; difference-image patch | reference-image patch | science-image patch; alert packet | full-image provenance pointers |
| Gamma-ray photon/event lists (Fermi LAT/GBM) | same sky localisation; same time window; event-list | binned maps; IRF/config tokens | derived products; transient trigger | multiwavelength context retrieval |
| Neutrino events (IceCube) | same time window; same (possibly large) localisation region; event sample | detector response / effective area metadata; candidate-source catalogue | stacked likelihood context |
| Gravitational-wave data products (GW strain \+ skymaps) | strain segment | event skymap | event parameter posteriors; temporal coincidence edges to EM/neutrino windows; “localisation region” edges driving context retrieval cutouts across modalities |
| Catalogues (Gaia/SDSS/LoTSS/MIGHTEE/CSC/eROSITA/XMM) | cross-match edges (positional \+ probabilistic); measurement provenance edges (which images/events created the row); consistent-object edges (same astrophysical object across catalogues); “class label” edges where trusted labels exist |
| 3D simulation snapshots (CAMELS / IllustrisTNG / EAGLE / Quijote / HADES)  | snapshot|parameter edges; particle/voxel field|derived summary statistics; simulation|synthetic-observation edges (forward model); “paired view” edges (same underlying 3D state rendered into multiple modalities/instruments)  |
| Synthetic observations / forward models | simulator config tokens | generated observables; instrument response tokens | noise/PSF kernels; truth catalogue | rendered image | recovered catalogue (closed-loop consistency)  |
| Language/code/provenance (papers, docs, analysis scripts) | paper|dataset edges; code|data product edges (which tool generated which artefact); notebook|figure/table provenance; commit/issue|data-spec versioning (living assets) |

# 5\. Program

## Workshop Format

The workshop will span five days, structured around team-based collaboration in the style of an *open source project hackathon*. This is inspired by the amazing success this has had in the online open source community, where people of diverse backgrounds come together to solve big problems for all. We also use a spiral method of communication, borrowing concepts from improv. The main focus of the entire workshop is to create shared understanding, excitement, and momentum. We define five teams in total (four KPA teams, and one implementation team). Before proceeding, participants will identify if there are other valuable KPAs, and we’ll modify the structure in-situ. Each team has a target focus during and after the workshop. There will be one ‘facilitator’ in each team that knows the objectives of each session and keeps people on track. All teams are dynamic, and totally self-organised. People are free to switch teams at any point, and are encouraged to hold conversation with others outside their groups. There should be approximately 10 people per team.

To aid recording important information, and free up people’s attention, we’d like to use an AI-based note taker during all discussion sessions. All discussions and progress will be recorded in the collaboration’s GitHub repo.

It is important to point out that the KPAs identified in this proposal will be refined by the participants, and that is the first item of business on the first day.

### KPA Teams

**Objectives**: Each KPA team is responsible for defining how the scientific end-user would use the system, and curation of training data relevant for their KPA.

#### During workshop

1. Determine the desired outputs and functionality, i.e. how end users would solve their problems for that KPA.   
2. Define data features for their KPA, i.e. how data relevant to their KPA can be tokenised, and fed as input to a foundation model.  
3. Specify a comprehensive data set from available sources, i.e. what actual data would be collected and prepared as input.  
4. Create a research use case that would be possible using the system once it’s online.

#### After workshop

1. Curate and prepare data sets.  
2. Join the implementation team, and write code.  
3. Participate in the white paper.  
4. Develop their use case as part of MVP.

### Implementation Team

**Objectives**: This parallel team is for people who would be interested in volunteering software development time in an open science open source effort, to build and run the system. Everyone is encouraged to join this team, and it is not mutually exclusive with KPA teams.

#### During workshop.

1. Identify technical challenges.  
2. Brainstorm how to overcome the challenges.  
3. Participate in hackathon sessions, building momentum that continues after the workshop.

#### After workshop

1. Write code for the data processing, models, training, inference and deployment code in an open source project.  
2. Coordinate external volunteers.  
3. Coordinate execution of the MVP.  
4. Join regular technical and status calls.

## Day Topics

### Monday

**Question of the day:** “Who are we, and what scientific problems are we uniting to solve?”  
Morning – Focus: Who are we, and what do we want ?

* Talk laying out the KPAs and scientific possibilities.  
* Brainstorm: are there missing KPAs?  
* Break people in KPA teams (self-organised). Everyone is also encouraged to join the Implementation team (not mutually exclusive – Ideally everyone joins).  
* KPA teams break out into parallel sessions and   
  * Brainstorm an ideal-world end-user use case (going beyond just next-token prediction but into actual user flows), focusing on how it would be useful to a general community (not science-case specific).  
  * Creating a README in the repo to track their thoughts.  
  * Preparing a lightning talk to “pitch” their idea to the whole group, to be delivered by two people in the group.  
* KPA teams pitch their ideas to the group, and discuss.

Afternoon – Focus: What are the challenges ?

* Talk laying out the practical aspect of building, training, and deploying a foundation model.  
* The implementation team takes a survey of skills, and records in README.  
* KPA teams break out to into parallel sessions and  
  * Brainstorm the challenges of their use case leveraging the information from the talk.  
  * Record in a README in the repo.  
  * What are the main challenges, perhaps using information learned in the session opening talk.  
  * Prepare a few slides to communicate their challenges.  
* KPA teams present one-by-one the challenges to the Implementation group, and dialectically discuss possible solutions.  
* Create a list of skill-gaps in the consortium, and potential ways to fill it.

### Tuesday

**Question of the day:** “What data must flow into the system, and how will we represent and relate it?”  
Morning – What data do we need?

* Talk laying out the importance of data quality, and some specific examples of data for different domains.   
* KPA teams break out into parallel sessions and  
  * Brainstorm the data that is relevant for their use case they developed on Monday, determine the relevance of each data to the output.  
  * Contrast to traditional methods of analysis (what is the gained signal, what missing information is filled in by adding different datatypes).  
  * How accessible is that data?  
  * Do a literature search of existing examples that do what they want to do and discuss some of the findings (they may use AI powered Consensus app – subscription details provided).  
  * Create a README to track their discussion.  
  * Preparing a lightning talk to “pitch” their idea to the whole group, to be delivered by two people in the group.  
* KPA teams pitch their ideas to the group, dialectic discussion with the implementation team.

Afternoon – How do we represent and relate the data?

* Talk laying out some different ways to tokenise different data and relate them.  
* KPA teams break out into parallel sessions and  
  * Determine how to tokenise their data from the morning session.  
  * Discuss the relevancy mapping (what conditionally helps what).  
  * Again do a literature search and discuss a few papers.  
  * Create an initial spec/scheme for tokenising their data based on their findings.  
  * Discuss how it relates to the long-context problem, with back of envelope calculations.  
  * Create a README to track their discussion.  
  * Preparing a lightning talk to “pitch” their idea to the whole group, to be delivered by two people in the group.  
* KPA teams pitch their ideas to the group, dialectic discussion with the implementation team, synthesise overlaps.

### Wednesday

**Question of the day:** “How will we build and align models that transform this data into trusted scientific insight?”  
Morning – Focus: 

* Talk laying out the challenges and solutions of alignment, continuous improvement, monitoring, focusing on physical alignment.  
* KPA teams break out into parallel sessions and  
  * Discuss what it means to be aligned for their KPA.  
  * How would they monitor it?  
  * What would continuous improvement look like for their use case?  
  * What kinds of physical alignment are possible?  
  * Do literature search for ways to perform physical alignment.  
  * Discuss risks for science.  
  * Create a README to track their discussion.  
  * Preparing a lightning talk to “pitch” their idea to the whole group, to be delivered by two people in the group.  
* KPA teams pitch their ideas to the group, dialectic discussion with the implementation team, synthesise overlaps.

Afternoon – Focus: How do we build this ?

* Talk laying out the different approaches varying from fine-tuning to from scratch to agentic operation.  
* KPA team breaks up into smaller parallel sessions and  
  * Brainstorm what would a fine-tuning implementation stack look like for their use case for training and for inference ?  
  * Similarly what would a from-scratch implementation stack look like ?  
  * Look up what industry tools could be leveraged.  
  * Create a README to track their discussion.  
  * Preparing a lightning talk to “pitch” their idea to the whole group, to be delivered by two people in the group.  
* KPA teams pitch their ideas to the group, dialectic discussion with the implementation team, synthesise overlaps.  
* Synthesise a single stack that works for all use cases.

### Thursday

**Question of the day:** “What is the timeline and development effort needed to turn the plan into a working MVP ?” \+ hackathon day  
Morning – Focus: what have we heard and let’s turn this into a roadmap.

* Talk summarising what we’ve heard from the last few days: use cases, unified data sets, unified stack.  
* Collectively, we discuss the practicality and development effort to achieve an MVP.  
* Create an initial workback of work that would need to be done.  
* Create GitHub high-level tickets for work, and assign groups to each ticket.  
* Hackathon session:  
  * Assignees on each ticket get together and work on their ticket.

Afternoon – Focus: More hackathon

* Continue hackathon.  
* Aim for an initial CI/CD pipeline.

### Friday

**Question of the day:** “How do we fund, govern, and sustain the collaboration after the workshop?”  
Morning – Focus: How do we fund this and who else should be a part of this collaboration?

* Talk laying out the cost and funding opportunities and timelines.  
* Discuss:  
  * Scale and estimate costs associated.  
  * Open source and open science governance.  
  * How to grow the network.  
* KPA teams break out into parallel teams and  
  * Create a one-page concept document for KPA and the use case.  
  * Create a list of external people to invite to collaboration.  
  * Store on GitHub.  
* Reconvene and discuss  
  * MVP timeline.  
  * Funding timeline.  
  * Reconvening timeline (virtual and in-person).  
  * How to solve the skill gap (if any).  
* Hackathon

Afternoon: – Focus: goodbye and more hackathon

* Farewell message (summarising the week’s efforts, and next steps).  
* More hackathon for those interested.

# 6\. Participants

The 55 participants consist of:

* 5 organizers (backgrounds in particle physics, astrophysics, cosmology, computational physics, and machine learning). The reason for 5 organizers is that we are trying to connect the different physics disciplines we want to cover. 

* 50 participants.

*  \~ 80 % invited participants from outside the Netherlands.


* \~ 35% women. Our field average is 22%. We have several invitees who are unable to confirm attendance as they are on maternity leave. We plan to follow up with them later.

We have already spent considerable time designing our participant list, and sending out invitations. At the time of writing we have \~42 confirmations of attendance. We have participants from 10+ fields spanning astrophysics/physics/AI/computer science and both inside and outside academia, both early and later stages of career, all of whom will have seen or worked on similar problems but not from the perspective of a unifying foundation model. The scale of cooperation required is the reason this consortium is being formed, and this workshop. We anticipate more people will eventually join the consortium after the workshop. We've covered the necessary bases in invites for this first meeting, and expect to only grow the diversity in the future.

Regarding competition in this area, we are not the only pursuing foundation models (e.g. [EUCaif](https://eucaif.org/)), however we are the only ones with a unifying perspective, and we will have participants from those organisations, making them collaborators and not competitors. 

# 7\. Budget 

We have procured funding to cover lunches of all participants and are searching for funding to help young researchers, from outside of the Netherlands, with travel and accommodation expenses. Please see the Budget document for details and additional sources of funding. We expect that we’ll pursue a diversity grant for 1 to 2 young researchers to help travel and accommodation. None of the organisers meets eligibility to apply for Leiden University’s grants that would normally be useful for organising this workshop.

# 8\. Dates

The ideal time frame for the workshop will be before October 2026, since many who have RSVP’d state they hold teaching responsibilities from October onwards. As well, we are motivated to hold the workshop as soon as possible, as the topic is quite timely. Thus, to be maximally inclusive to our participants we are targeting the following weeks (prioritised in order):

1. 7 \- 11 Sept, 2026  
2. 14 \- 18 Sept, 2026  
3. 21 \- 25 Sept, 2026

# References

## Multimodal contexts and reasoning

\[1\] Machel Reid et al. "Gemini 1.5: Unlocking multimodal understanding across millions of tokens of context." ArXiv: 2403.05530 \[cs.CL\]. Available at  [https://arxiv.org/abs/2403.05530](https://arxiv.org/abs/2403.05530).  
\[2\] Hugo Touvron et al. "Llama 2: Open Foundation and Fine-Tuned Chat Models." *ArXiv*, abs/2307.09288 (2023).  
\[3\] Jones, Cameron R., and Benjamin K. Bergen. “Large Language Models Pass the Turing Test.” ArXiv: 2503.23674 \[cs.CL\]. Available at  [https://arxiv.org/abs/2503.23674](https://arxiv.org/abs/2503.23674).

## Anomaly detection

## \[4\] Yunkang Cao et al. "VarAD: Lightweight High-Resolution Image Anomaly Detection via Visual Autoregressive Modeling."  IEEE Transactions on Industrial Informatics (2025): 3246–3255. Available at  [https://doi.org/10.1109/TII.2024.3523574](https://doi.org/10.1109/TII.2024.3523574).

## Multimodal super resolution

\[5\] Yikai Wang et al. "Multimodal Token Fusion for Vision Transformers." 2022 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR) (2022): 12176-12185. Available at [https://doi.org/10.1109/CVPR52688.2022.01187](https://doi.org/10.1109/CVPR52688.2022.01187).

## Multimodal monocular data to 3D reconstruction

\[6\] Jingbo Zhang et al. "Text2NeRF: Text-Driven 3D Scene Generation With Neural Radiance Fields." IEEE Transactions on Visualization and Computer Graphics, 30 (2023): 7749-7762. Available at [https://doi.org/10.1109/TVCG.2024.3361502](https://doi.org/10.1109/TVCG.2024.3361502).  
\[7\] Weiwei Cai et al. "Instruct Pix-to-3D: Instructional 3D object generation from a single image." Neurocomputing, 600 (2024): 128156\. [https://doi.org/10.1016/j.neucom.2024.128156](https://doi.org/10.1016/j.neucom.2024.128156).

## Multimodal astrophysics

\[8\] Jeroen Audenaert et al. “The Multimodal Universe: Enabling Large-Scale Machine Learning with 100TB of Astronomical Scientific Data”.  ArXiv: 2412.02527 \[astro-ph.IM\]. Available at [https://arxiv.org/abs/2412.02527](https://arxiv.org/abs/2412.02527).

## Machine assisted discovery

\[9\] Tao, T. C.-S. “Machine-Assisted Proof.” Notices of the American Mathematical Society, vol. 72, no. 1, 2025, p. 1\.   
\[10\] Flavio Petruzzellis et al. "Assessing the Emergent Symbolic Reasoning Abilities of Llama Large Language Models." ArXiv: 2406.06588 \[cs.CL\]. Available at  [https://doi.org/10.48550/arXiv.2406.06588](https://doi.org/10.48550/arXiv.2406.06588).

## Additional references for datasets

\[11\] NASA Fermi Science Support Center. “LAT 14-year Source Catalog (4FGL-DR4).” Available at https://fermi.gsfc.nasa.gov/ssc/data/access/lat/14yr\_catalog/.  
\[12\] NASA Fermi Science Support Center. “Fermitools (Fermi Science Tools) and analysis software.” Available at https://fermi.gsfc.nasa.gov/ssc/data/analysis/.  
\[13\] NASA HEASARC. “FERMIGBRST: Fermi GBM Burst Catalog.” Available at https://heasarc.gsfc.nasa.gov/w3browse/fermi/fermigbrst.html.  
\[14\] IceCube Collaboration. “IceCube Data Releases.” Available at https://icecube.wisc.edu/science/data-releases/.  
\[15\] IceCube Collaboration. “All-sky point-source IceCube data: years 2008–2018.” Available at https://icecube.wisc.edu/data-releases/2021/01/all-sky-point-source-icecube-data-years-2008-2018/.  
\[16\] Gravitational Wave Open Science Center (GWOSC). “Data Sets / Open strain data.” Available at https://gwosc.org/data/.  
\[17\] Zwicky Transient Facility (ZTF). “ZTF Alert Stream (ZADS).” Available at https://www.ztf.caltech.edu/ztf-alert-stream.html.  
\[18\] ESA Gaia. “Gaia DR3 contents and Gaia Archive access.” Available at https://www.cosmos.esa.int/web/gaia/dr3 and https://gea.esac.esa.int/archive/.  
\[19\] Sloan Digital Sky Survey (SDSS). “DR17 data access.” Available at https://www.sdss4.org/dr17/data\_access/.  
\[20\] COSMOS Survey. “Multiwavelength datasets.” Available at https://cosmos.astro.caltech.edu/page/datasets.  
\[21\] MAST (STScI). “Mikulski Archive for Space Telescopes (MAST), including HST holdings.” Available at https://archive.stsci.edu/home.  
\[22\] Chandra X-ray Center. “Chandra Source Catalog (CSC) 2.1.” Available at https://cxc.cfa.harvard.edu/csc/.  
\[23\] ESA. “XMM-Newton Science Archive (XSA).” Available at https://www.cosmos.esa.int/web/xmm-newton/xsa.  
\[24\] eROSITA-DE. “eROSITA-DE Data Release 1 (DR1).” Available at https://erosita.mpe.mpg.de/dr1/.  
\[25\] LOFAR Surveys. “LoTSS Data Release 2 (DR2).” Available at https://lofar-surveys.org/dr2\_release.html.  
\[26\] Hale, C. L., et al. “MIGHTEE: The Continuum Survey Data Release 1.” ArXiv: 2411.04958. Available at https://arxiv.org/abs/2411.04958.  
\[27\] SKAO. “SKA Science Data Challenge 1 (SDC1).” Available at https://www.skao.int/en/464/ska-science-data-challenge-1.  
\[28\] ESA Planck. “Planck Legacy Archive (PLA).” Available at https://pla.esac.esa.int/.  
\[29\] NASA/IPAC IRSA. “Euclid Quick Release 1 (Q1) overview.” Available at https://irsa.ipac.caltech.edu/data/Euclid/docs/overview\_q1.html.  
\[30\] Villaescusa-Navarro, F., et al. “The CAMELS project: public data release.” ArXiv: 2201.01300. Available at https://arxiv.org/abs/2201.01300.  
\[31\] CAMELS. “Data access documentation (Globus download and formats).” Available at https://camels.readthedocs.io/en/latest/data\_access.html.  
\[32\] IllustrisTNG. “Public Data Access Overview.” Available at https://www.tng-project.org/data/.  
\[33\] EAGLE Project. “EAGLE Public Data Release.” Available at https://icc.dur.ac.uk/Eagle/database.php.  
\[34\] Quijote Simulations. “Quijote simulations suite (repository).” Available at https://github.com/franciscovillaescusa/Quijote-simulations.  
\[35\] HADES simulations. “HADES simulations data/overview.” Available at https://franciscovillaescusa.github.io/hades.html.  
\[36\] Audenaert, J., et al. “The Multimodal Universe: Enabling Large-Scale Machine Learning with 100TB of Astronomical Scientific Data.” ArXiv: 2412.02527. Available at https://arxiv.org/abs/2412.02527.  
\[37\] Rubin Observatory. “Simulation software (imSim/PhoSim).” Available at https://rubinobservatory.org/for-scientists/data-products/simulations.  
\[38\] Rubin Observatory. “Alerts and brokers (alert packet semantics).” Available at https://rubinobservatory.org/for-scientists/data-products/alerts-and-brokers.