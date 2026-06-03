The proposal defines four Key Problem Areas (KPAs), but the KPAs are not four separate projects. They are four ways of testing and using the same core object: a joint-representation, generative foundation model for astrophysical data.

The model should learn from heterogeneous observations, simulations, language, code, and provenance. It should map related physical evidence into a shared representation while also supporting conditional generation across linked views of the same physical system. In compact form, the ambition is to learn

$$z = f_\theta(x_{\mathrm{obs}}, x_{\mathrm{sim}}, x_{\mathrm{inst}}, x_{\mathrm{text}}, x_{\mathrm{prov}})$$

where \(z\) is a physically meaningful joint representation, and to use that representation for both retrieval and generation:

$$p_\theta(x_a \mid x_b, c)$$

where \(x_a\) and \(x_b\) may be different modalities, resolutions, instruments, simulation states, or provenance-linked data products, and \(c\) contains the relevant physical, instrumental, and contextual conditions.

The key technical challenge is therefore not to build four disconnected tools. It is to build the data representation, relevancy graph, training protocol, and validation framework that let one model move coherently between embeddings, conditional generation, simulation, instrumentation, language, and human judgement.

## KPA 1: embeddings for serendipity

Large surveys contain enormous data volumes, while rare signals are weak and difficult to specify in advance. KPA 1 asks how the model's embedding space can accelerate serendipity.

If the representation is physically meaningful, then nearby points in embedding space should correspond to related physical situations, not merely similar file formats or superficial morphology. This enables similarity search, clustering, out-of-distribution scoring, counterexample discovery, and retrieval of relevant context that a human may not know to request.

The evaluation question is: can the embedding space surface rare, surprising, or physically meaningful candidates faster and more reliably than existing workflows? Useful tests include held-out rare classes, synthetic anomalies, known transient classes, blind retrieval tasks, and human review of retrieved scientific context.

## KPA 2: generative cross-instrument inference

Individual instruments hit angular, spectral, temporal, and sensitivity limits. KPA 2 asks how a generative model can use multimodal context to infer across those limits without pretending that one modality alone contains all missing information.

The target capability is conditional generation across linked observations: super-resolution, deconfusion, gap filling, missing-modality prediction, and cross-instrument reconstruction. This requires the model to condition on instrument response, resolution, noise, calibration, sky position, time, and provenance.

The evaluation question is: when the model generates or reconstructs a view, is it physically supported by the available evidence? Controlled degradation, held-out modalities, known multi-instrument fields, uncertainty calibration, and comparison against classical baselines are essential.

## KPA 3: simulator-backed observation-to-state inference

Simulation initial conditions often require an explicit ansatz. KPA 3 asks whether multimodal observations can constrain latent physical states or initial conditions through a model trained on system simulators, instrument simulators, and synthetic observations.

The goal is not unconstrained imagination. The goal is conditional generation of physically admissible states that can be pushed through forward models and compared back to observations. System simulators and instrument simulators are therefore part of the training and validation loop, not optional downstream tools.

The evaluation question is: do generated states remain plausible under forward-model consistency checks, uncertainty estimates, and synthetic-to-real domain-gap tests? A useful output is not just a generated initial condition, but an auditable chain linking observations, simulator assumptions, instrument effects, generated state, and validation residuals.

## KPA 4: agentic human-machine discovery

KPA 4 frames how the model is used. The long-term vision is a collaborative scientific system in which humans, reasoning LLMs, tools, simulators, and foundation models form, test, revise, and communicate hypotheses.

The joint-representation model provides embeddings for retrieval and serendipity, and generative capabilities for conditional scientific inference. Strong reasoning LLMs can orchestrate these capabilities: retrieving context, proposing hypotheses, calling tools, requesting simulations, comparing alternatives, and summarising evidence. The system must keep humans in the loop and preserve provenance, uncertainty, negative results, and decision points.

The evaluation question is: does the human-machine workflow produce better scientific search, triage, hypothesis generation, validation, or communication than current practice, while remaining auditable and physically disciplined?

## Why the relevancy graph matters

The training corpus is not just a pile of files. It is a set of related physical and procedural objects. A cutout, spectrum, catalogue row, alert, simulation snapshot, synthetic observation, instrument response, paper, notebook, and code commit may all refer to the same physical question in different ways.

The relevancy graph records those relationships. Nodes are typed data assets. Edges encode why one asset is relevant to another: same sky region, same source, same time window, generated from, degraded from, derived from, conditioned on instrument response, forward-modelled from, produced by code, or supported by a paper or workflow.

This graph constrains both tokenisation and architecture. It tells the model what should be seen together, what can be contrasted, what can be generated from what, and what provenance must travel with any inference.

## Workshop deliverables

The KPAs should drive the workshop through testable use cases. The first output is a small set of flagship use-case cards with explicit evaluation targets. From there, the consortium should produce:

- a Relevancy Graph v0 for the selected use cases;
- tokenisation and provenance requirements for the graph's node and edge types;
- embedding objectives for serendipity and retrieval;
- generative objectives for cross-instrument inference and observation-to-state inference;
- validation targets that distinguish supported inference from plausible completion;
- an MVP architecture for an LLM-guided human-machine discovery system.
