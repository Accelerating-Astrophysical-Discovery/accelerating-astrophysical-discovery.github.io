The workshop is designed as an open-source project hackathon with a deliberately narrow focus. The goal is to create shared understanding, build momentum, and leave with living assets rather than only discussion notes.

The week has two linked components. Monday is devoted to shared vocabulary, use cases, and evaluation targets: how AI, foundation models, and human-machine collaboration could concretely accelerate discovery, and how we would know whether a proposed use case is working. The rest of the week focuses on the joint-representation foundation model that would make those workflows possible: the data representations, relevancy graph, embedding space, generative capabilities, training path, and deployment inside an agentic scientific system.

The KPAs are not four independent week-long tracks. KPA 4, collaborative scientific reasoning, is the framing lens for Monday. KPAs 1-3 are also handled on Monday as concrete use-case mechanisms and evaluation probes: embeddings for serendipity, generative cross-instrument inference, and simulator-backed observation-to-state inference.

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
| 10:00-10:30 | Morning talk slot | Set shared vocabulary for joint representation, embeddings, conditional generation, simulator-backed data, long context, agentic workflow, provenance, validation, uncertainty, and human judgement. |
| 10:30-11:00 | Coffee break |  |
| 11:00-12:00 | Morning working session | Draft use-case cards. Each card should state the scientific workflow, human role, machine role, required data, model capability, and evidence that the workflow is working. |
| 12:00-13:30 | Lunch |  |
| 13:30-14:00 | Afternoon talk slot | Frame KPAs 1-4 as testable capabilities: embeddings for serendipity, generative reconstruction, simulator-backed observation-to-state inference, and agentic human-machine discovery. |
| 14:00-14:30 | Afternoon working session I | Refine use cases around concrete mechanisms and select a small set of flagship cases. |
| 14:30-15:00 | Coffee break |  |
| 15:00-16:15 | Afternoon working session II | Define evaluation targets: positive controls, rare-class or synthetic anomaly tests, baseline comparisons, forward-model consistency checks, uncertainty labels, provenance requirements, and human review points. |
| 16:15-16:30 | Closeout | Confirm the shared vocabulary, selected use cases, evaluation targets, and owners for writing the Monday artifact. |
| 16:30 onward | Welcome reception | Informal continuation after the formal Monday programme. |

## Tuesday

**Theme:** Data, representation, and provenance  
**Working hours:** 9:30-17:00  
**Deliverable:** Relevancy Graph v0 for Monday's selected use cases

| Time | Session | Focus |
| --- | --- | --- |
| 9:30-10:00 | Morning talk slot | Explain the training corpus as a relevancy graph coupling data, tokenisation, and provenance. |
| 10:00-10:30 | Morning working session I | Map Monday use cases to required data objects: observations, catalogues, simulations, synthetic observations, instrument responses, language, code, and provenance records. |
| 10:30-11:00 | Coffee break |  |
| 11:00-12:00 | Morning working session II | Define node types, edge types, metadata fields, provenance requirements, and known ambiguities. |
| 12:00-13:30 | Lunch |  |
| 13:30-14:00 | Afternoon talk slot | Frame tokenisation choices for heterogeneous physical data without committing to a final implementation. |
| 14:00-14:30 | Afternoon working session I | Identify tokenisation implications for each node and edge type: units, scale, locality, ordering, uncertainty, missingness, modality, provenance, and physical context. |
| 14:30-15:00 | Coffee break |  |
| 15:00-16:30 | Afternoon working session II | Synthesize the Relevancy Graph v0 and the architecture constraints it imposes. |
| 16:30-17:00 | Closeout | Confirm owners for node types, edge types, metadata, provenance fields, tokenisation implications, and open decisions. |

## Wednesday

**Theme:** Long-context architectures and training protocol  
**Working hours:** 9:30-17:00  
**Deliverable:** Architecture and Training Protocol v0

| Time | Session | Focus |
| --- | --- | --- |
| 9:30-10:00 | Morning talk slot | Frame long-context architectures for multimodal physics: retrieval, memory, hierarchical context, modality-specific encoders, shared latent spaces, generative heads, and simulator conditioning. |
| 10:00-10:30 | Morning working session I | Translate the Relevancy Graph v0 into architecture constraints: typed objects, relationships, physical units, coordinates, uncertainty, provenance, missingness, instrument metadata, and simulator metadata. |
| 10:30-11:00 | Coffee break |  |
| 11:00-12:00 | Morning working session II | Sketch candidate architecture families and representation objectives. |
| 12:00-13:30 | Lunch |  |
| 13:30-14:00 | Afternoon talk slot | Frame training protocol and compute-to-data deployment across distributed archives and HPC environments. |
| 14:00-14:30 | Afternoon working session I | Define training objectives: contrastive alignment, reconstruction, cross-modal prediction, conditional generation, forward-model consistency, provenance-aware supervision, and uncertainty-aware validation. |
| 14:30-15:00 | Coffee break |  |
| 15:00-16:30 | Afternoon working session II | Define the staged training protocol: seed corpus, simulator-backed synthetic data, data access model, preprocessing, validation splits, monitoring, scaling path, compute assumptions, and failure modes. |
| 16:30-17:00 | Closeout | Confirm the architecture sketch, training protocol, open decisions, and risk list. |
| 17:00-20:00 | Workshop dinner | Informal continuation after the formal Wednesday programme. |

## Thursday

**Theme:** MVP architecture and hackathon  
**Working hours:** 9:30-17:00  
**Deliverable:** MVP Implementation Plan and Hackathon Artifacts v0

| Time | Session | Focus |
| --- | --- | --- |
| 9:30-10:00 | Morning talk slot | Translate Monday-Wednesday artifacts into a small number of MVP workstreams. |
| 10:00-10:30 | Morning working session I | Define the smallest credible MVP scope: selected use cases, required data types, minimal graph schema, first architecture path, and first evaluation targets. |
| 10:30-11:00 | Coffee break |  |
| 11:00-12:00 | Morning working session II | Create workstreams, owners, and GitHub issues with acceptance criteria. |
| 12:00-13:30 | Lunch |  |
| 13:30-14:00 | Afternoon talk slot | Set the hackathon integration target: every artifact should connect to a use case, model capability, and evaluation target. |
| 14:00-14:30 | Hackathon sprint I | Work on repo artifacts: schemas, manifests, example records, tokenisation examples, evaluation specs, issue templates, prototype code, or CI/CD setup. |
| 14:30-15:00 | Coffee break |  |
| 15:00-16:30 | Hackathon sprint II | Continue implementation and integration, keeping work tied to the MVP scope. |
| 16:30-17:00 | Closeout | Review repository artifacts, unresolved issues, owners, and next technical meeting. |

## Friday

**Theme:** Funding, governance, and continuity  
**Working hours:** 9:30-13:30  
**Deliverable:** Consortium Roadmap and Funding Package v0

| Time | Session | Focus |
| --- | --- | --- |
| 9:30-10:00 | Morning talk slot | Frame compute, data access, funding, data-center partnerships, simulator access, evaluation, deployment, and long-term maintenance. |
| 10:00-10:30 | Morning working session I | Map resource needs for each MVP workstream: compute, data access, simulator access, archive relationships, software expertise, funding, and missing roles. |
| 10:30-11:00 | Coffee break |  |
| 11:00-11:30 | Morning working session II | Build the funding and partnership map, including lead owners where possible. |
| 11:30-12:00 | Roadmap closeout | Confirm 1-month, 3-month, 6-month, and 12-month milestones, working groups, technical owners, white-paper leads, follow-up cadence, unresolved risks, and external invitees. |
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
