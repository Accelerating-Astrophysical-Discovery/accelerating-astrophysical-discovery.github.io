The proposal defines four Key Problem Areas (KPAs), but they should not become four separate projects. They are four ways to specify, test, and use one shared capability: a joint-representation foundation model with generative interfaces for astrophysical data.

The model should learn from heterogeneous observations, simulations, synthetic observations, language, and code. It should place physically related evidence into a shared representation, then use that representation to retrieve, compare, and conditionally generate linked views of the same physical system.

One useful abstraction is:

$$z_i = f_\theta(x_i, c_i)$$

where \(x_i\) is a data product and \(c_i\) is its physical or instrumental context. The same model family should also support conditional generation:

$$p_\theta(x_{\mathrm{target}} \mid x_{\mathrm{context}}, c_{\mathrm{phys}}, c_{\mathrm{inst}}).$$

Provenance is not another variable for the model to hallucinate. It is the audit layer attached to data products, relationships, generated outputs, and scientific claims. It records where things came from, how they were produced, and what assumptions were used.

## KPA 1: embeddings for serendipity

Large surveys contain enormous data volumes, while rare signals are weak and difficult to specify in advance. KPA 1 asks how the shared embedding space can accelerate serendipity.

The core idea is simple: if the representation is physically meaningful, then nearby points should correspond to related physical situations, not merely similar file formats or superficial morphology. This enables similarity search, clustering, out-of-distribution scoring, counterexample discovery, and retrieval of context that a human may not know to request.

The evaluation question is: can the embedding space surface rare, surprising, or physically meaningful candidates faster and more reliably than existing workflows? Useful tests include held-out rare classes, synthetic anomalies, known transient classes, blind retrieval tasks, and human review of retrieved context.

## KPA 2: generative cross-instrument inference

Individual instruments hit angular, spectral, temporal, and sensitivity limits. KPA 2 asks how a generative model can use multimodal context to infer across those limits without pretending that one modality alone contains all missing information.

The capability is conditional generation across linked observations: super-resolution, deconfusion, gap filling, missing-modality prediction, and cross-instrument reconstruction. The model must condition on physical and instrumental context such as sky position, time, resolution, beam or PSF, noise, calibration, and instrument response.

The evaluation question is: when the model generates or reconstructs a view, is it physically supported by the available evidence? Controlled degradation, held-out modalities, known multi-instrument fields, uncertainty calibration, and comparison against classical baselines are essential.

## KPA 3: simulator-backed observation-to-state inference

Simulation initial conditions often require an explicit ansatz. KPA 3 asks whether multimodal observations can constrain latent physical states or initial conditions through a model trained with system simulators, instrument simulators, and synthetic observations.

The goal is not unconstrained imagination. The goal is conditional generation of physically admissible candidate states that can be pushed through forward models and compared back to observations. System simulators and instrument simulators are therefore part of the training and validation loop, not optional downstream tools.

The evaluation question is: do generated states remain plausible under forward-model consistency checks, uncertainty estimates, and synthetic-to-real domain-gap tests? A useful output is not just a generated initial condition, but an auditable chain linking observations, simulator assumptions, instrument effects, generated state, and validation residuals.

## KPA 4: agentic human-machine discovery

KPA 4 frames how the model is used. The long-term vision is a collaborative scientific system in which humans, reasoning LLMs, tools, simulators, and foundation models form, test, revise, and communicate hypotheses.

The joint-representation model provides embeddings for retrieval and serendipity, and generative capabilities for conditional scientific inference. Strong reasoning LLMs can orchestrate these capabilities: retrieving context, proposing hypotheses, calling tools, requesting simulations, comparing alternatives, and summarising evidence. The system must keep humans in the loop and preserve uncertainty, negative results, provenance records, and decision points.

The evaluation question is: does the human-machine workflow produce better scientific search, triage, hypothesis generation, validation, or communication than current practice, while remaining auditable and physically disciplined?

## Why the relevancy graph matters

The training corpus is not just a pile of files. It is a set of related physical and procedural objects. A cutout, spectrum, catalogue row, alert, simulation snapshot, synthetic observation, instrument response, paper, notebook, and code commit may all refer to the same physical question in different ways.

The relevancy graph records those relationships. Nodes are typed data assets. Edges encode why one asset is relevant to another: same sky region, same source, same time window, generated from, degraded from, derived from, conditioned on instrument response, forward-modelled from, produced by code, or supported by a paper or workflow.

This graph constrains both tokenisation and architecture. It tells the model what should be seen together, what can be contrasted, what can be generated from what, and what audit trail must be preserved for any inference.

## Workshop deliverables

The KPAs should drive the workshop through testable use cases. The first output is a small set of flagship use-case cards with explicit evaluation targets. From there, the consortium should produce:

- a Relevancy Graph v0 for the selected use cases;
- tokenisation and metadata requirements for the graph's node and edge types;
- embedding objectives for serendipity and retrieval;
- generative objectives for cross-instrument inference and observation-to-state inference;
- validation targets that distinguish supported inference from plausible completion;
- an MVP architecture for an LLM-guided human-machine discovery system.
