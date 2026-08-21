The workshop is designed as an open-source project hackathon with a deliberately narrow focus. The goal is to create shared understanding, build momentum, and leave with living assets rather than only discussion notes.

The week has two linked components. Monday is devoted to shared vocabulary, use cases, and evaluation targets: how AI, foundation models, and human-machine collaboration could concretely accelerate discovery, and how we would know whether a proposed use case is working. The rest of the week focuses on the joint-representation foundation model that would make those workflows possible: the data representations, relevancy graph, embedding space, generative capabilities, training path, and deployment inside an agentic scientific system.

The KPAs are not four independent week-long tracks. KPA 4, collaborative scientific reasoning, is the framing lens for Monday. KPAs 1-3 are also handled on Monday as concrete use-case mechanisms and evaluation probes: embeddings for serendipity, generative cross-instrument inference, and simulator-backed observation-to-state inference.

The working rhythm includes an AI handoff between days. Tuesday through Thursday begin by reviewing and correcting the previous night's AI-assisted synthesis or prototype. Monday through Wednesday end by agreeing what the AI should prepare overnight for the following morning; Thursday closes by preparing the material Friday needs for decisions about continuity.

## Daily deliverables

| Day | Focus | Main deliverable |
| --- | --- | --- |
| Monday | Vocabulary, use cases, and evaluation targets | Shared Vocabulary and Discovery-Evaluation Map v0 |
| Tuesday | Data, representation, tokenisation, and provenance | Relevancy Graph v0 for Monday's selected use cases |
| Wednesday | Long-context model architecture and training protocol | Architecture and Training Protocol v0 |
| Thursday | MVP architecture and hackathon | MVP Implementation Plan and Hackathon Artifacts v0 |
| Friday | Funding, governance, and continuity | Consortium Roadmap and Funding Package v0 |

## Monday

**Theme:** Use cases and discovery workflows  
**Working hours:** 10:00-16:30  
**Deliverable:** Shared Vocabulary and Discovery-Evaluation Map v0

| Time | Session | Focus |
| --- | --- | --- |
| 09:00-10:00 | Arrival and coffee | The building is open from 09:00; the formal programme begins at 10:00. |
| 10:00-10:30 | Kickoff talk | Frame AI-first science, the two consortium pillars, and the KPAs as a starting point that the workshop may reshape. |
| 10:30-12:00 | Science 2.0 and use-case working session | Work from long-term visions back to concrete use cases. Each candidate should state the scientific workflow, human role, machine role, required data, model capability, and evidence of success. |
| 12:00-13:30 | Lunch |  |
| 13:30-14:30 | Plenary synthesis and selection | Groups share their visions and candidate use cases; the plenary refines and selects a small set of flagship cases. |
| 14:30-15:00 | Coffee break |  |
| 15:00-16:15 | Define evaluation targets | Set positive controls, rare-class or synthetic anomaly tests, baseline comparisons, forward-model consistency checks, uncertainty labels, provenance requirements, and human review points. |
| 16:15-16:30 | Closeout and overnight AI brief | Confirm the selected cases, evaluation targets, artifact owners, and the synthesis the AI should prepare for Tuesday. |
| 16:30 onward | Welcome reception | Informal continuation after the formal Monday programme. |

## Tuesday

**Theme:** Data, representation, and provenance  
**Working hours:** 9:30-17:00  
**Deliverable:** Relevancy Graph v0 for Monday's selected use cases

| Time | Session | Focus |
| --- | --- | --- |
| 9:30-10:00 | Kickoff and overnight review | Correct Monday's AI-assisted synthesis; introduce the relevancy graph, current multimodal examples, and tokenisation challenges. |
| 10:00-10:30 | Map data objects | Use participants' dataset lists to connect Monday's cases to observations, catalogues, simulations, synthetic observations, instrument responses, language, code, and provenance. |
| 10:30-11:00 | Coffee break |  |
| 11:00-12:00 | Graph working session | Define node types, relevancy links, metadata, provenance, known ambiguities, and how graph connectivity should structure training. |
| 12:00-13:30 | Lunch |  |
| 13:30-14:30 | Plenary graph synthesis | Share group results and assemble the common Relevancy Graph v0 for the selected use cases. |
| 14:30-15:00 | Coffee break |  |
| 15:00-16:30 | Tokenisation and architecture constraints | Decide what representations must preserve—units, scale, locality, ordering, uncertainty, missingness, modality, provenance, and physical context—and record the constraints imposed on Wednesday. |
| 16:30-17:00 | Closeout and overnight AI brief | Confirm owners and open decisions; commission a draft schema or prototype plus a short architecture primer for Wednesday. |

## Wednesday

**Theme:** Long-context architectures and training protocol  
**Working hours:** 9:30-17:00  
**Deliverable:** Architecture and Training Protocol v0

| Time | Session | Focus |
| --- | --- | --- |
| 9:30-10:00 | Kickoff and overnight review | Review the primer and overnight graph work; frame long-context, recurrent-depth, graph-attention, multimodal, and simulator-backed architecture challenges from basic concepts upward. |
| 10:00-10:30 | Translate graph constraints | Identify what the architecture must preserve: typed objects and relationships, physical units, coordinates, uncertainty, provenance, missingness, instrument metadata, and simulator metadata. |
| 10:30-11:00 | Coffee break |  |
| 11:00-12:00 | Architecture working session | Groups use AI to sketch candidate architecture families, representation objectives, and training hypotheses tied to Tuesday's graph. |
| 12:00-13:30 | Lunch |  |
| 13:30-14:30 | Plenary architecture synthesis | Compare the candidate designs, identify common components and disagreements, and retain multiple hypotheses where evidence is insufficient. |
| 14:30-15:00 | Coffee break |  |
| 15:00-16:30 | Training protocol and prototype brief | Define objectives, simulator feedback, compute-to-data deployment, validation, staged scaling, risks, and the starter code or artifacts needed for Thursday. |
| 16:30-17:00 | Closeout and overnight AI brief | Confirm architecture hypotheses, the training protocol, owners, and the prototype work the AI should prepare overnight. |
| 17:00-20:00 | Workshop dinner | Informal continuation after the formal Wednesday programme. |

## Thursday

**Theme:** MVP architecture and hackathon  
**Working hours:** 9:30-17:00  
**Deliverable:** MVP Implementation Plan and Hackathon Artifacts v0

| Time | Session | Focus |
| --- | --- | --- |
| 9:30-10:00 | Kickoff and overnight review | Summarise Monday-Wednesday, inspect the overnight prototype, state the MVP target, and share practical AI-assisted coding approaches. |
| 10:00-10:30 | Self-organise workstreams | Choose concrete data/graph, tokenisation, architecture, training, evaluation, infrastructure, documentation/white-paper, or roadmap/funding artifacts and name owners. |
| 10:30-11:00 | Coffee break |  |
| 11:00-12:00 | Open hackathon I | Build the first artifacts at toy scale; participants may move to breakout rooms and whiteboards as needed. |
| 12:00-13:30 | Lunch |  |
| 13:30-14:30 | Open hackathon II | Continue building and integrating artifacts, with immediate demonstrations when something begins to work. |
| 14:30-15:00 | Coffee break |  |
| 15:00-16:15 | Show-and-tell and integration | Demonstrate code and designs, connect each artifact to a use case and evaluation target, and identify gaps. |
| 16:15-17:00 | Closeout and Friday handoff | Review repository artifacts, unresolved issues, owners, next technical work, and the funding or governance questions Friday must resolve. |

## Friday

**Theme:** Funding, governance, and continuity  
**Working hours:** 9:30-13:30  
**Deliverable:** Consortium Roadmap and Funding Package v0

| Time | Session | Focus |
| --- | --- | --- |
| 9:30-10:00 | Funding and continuity kickoff | Review the week's artifacts and frame compute, data access, funding, partnerships, deployment, and long-term maintenance. |
| 10:00-10:30 | Morning working session I | Map resource needs for each MVP workstream: compute, data access, simulator access, archive relationships, software expertise, funding, and missing roles. |
| 10:30-11:00 | Coffee break |  |
| 11:00-11:30 | Morning working session II | Build the funding and partnership map, including lead owners where possible. |
| 11:30-12:00 | Commitments and roadmap closeout | Record desired participation and responsibilities; confirm 1-, 3-, 6-, and 12-month milestones, owners, white-paper leads, follow-up cadence, unresolved risks, and external invitees. |
| 12:00-13:30 | Closing lunch | Informal continuation, final owner confirmations, and departures. |

## Expected outcomes

By the end of the workshop, the collaboration should have:

- a shared vocabulary for joint-representation, embedding, generative, simulator-backed, long-context, and agentic concepts;
- a focused map of scientific discovery workflows with explicit evaluation targets;
- a Relevancy Graph v0 coupling multimodal data, tokenisation, and provenance;
- a long-context architecture and compute-to-data training protocol;
- embedding and generative objectives for a joint-representation foundation model;
- an MVP architecture for an LLM-guided agentic discovery system;
- an open GitHub repo with attendees, issues, todos, schemas, and initial code where useful;
- a consortium roadmap with owners, funding targets, and follow-up cadence.

In the months after the workshop, the consortium will curate datasets, build data processing, training, inference, and deployment code, and work toward a white paper, MVP, follow-up funding, and alignment with the European Coalition for AI in Fundamental Physics.
