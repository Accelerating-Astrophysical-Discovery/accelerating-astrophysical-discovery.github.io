The proposal defines four Key Problem Areas (KPAs). They are not four separate projects. They are four tests of one shared ambition: a joint-representation foundation model that can understand astrophysical data well enough to accelerate discovery.

The model must learn across observations, simulations, synthetic observations, language, code, and instrumental context. It should answer two linked questions: what evidence belongs together, and what can be inferred or generated from that evidence?

One compact way to say this is that each data product \(x_i\), together with its physical and instrumental context \(c_i\), is mapped into a shared representation:

$$z_i = f_\theta(x_i, c_i).$$

The same model family should support conditional generation:

$$p_\theta(x_{\mathrm{target}} \mid x_{\mathrm{context}}, c_{\mathrm{phys}}, c_{\mathrm{inst}}).$$

## KPA 1: serendipity through embeddings

Modern surveys produce more high-quality data than humans can inspect with full scientific attention. The first KPA asks whether a shared embedding space can make serendipity operational.

If the representation is physically meaningful, nearby points should reflect related physical situations. That opens a path to rare-object discovery, anomaly triage, counterexample search, similarity retrieval, and context discovery that a scientist may not know to request.

The test is simple: can the embedding space surface rare, surprising, or physically meaningful candidates faster and more reliably than current workflows?

## KPA 2: generative inference across instruments

Every instrument sees the universe through limits: angular resolution, spectral coverage, cadence, noise, calibration, sensitivity, and selection effects. The second KPA asks whether a generative model can reason across those limits without pretending that missing information is known.

The capability is conditional generation across linked observations: super-resolution, deconfusion, gap filling, missing-modality prediction, and cross-instrument reconstruction. The model must condition on the evidence, the physical setting, and the instrument response.

The test is whether a generated view is physically supported. Controlled degradation, held-out modalities, uncertainty calibration, forward-model checks, and comparison with classical baselines should distinguish scientific inference from plausible-looking completion.

## KPA 3: observations to physical states

Astrophysical simulations often begin from an ansatz. The third KPA asks whether multimodal observations can instead constrain candidate physical states or simulation initial conditions (ICs).

The aim is not unconstrained imagination. The aim is to generate physically admissible ICs that can be pushed through system simulators and instrument simulators, then compared back to observations. Simulators are part of the training and validation loop, not a downstream decoration.

This also gives a route to reinforcement-learning-style improvement of the model. Model-produced ICs can be evolved forward and scored by physical and observational checks. Do the evolved systems become virialised where they should? Do short forward runs preserve stable physical structure, or do they diverge into unphysical states? Do residuals reveal missing conditioning variables or systematic failure modes? These signals can feed back into the generative policy, proposal distribution, conditioning strategy, and uncertainty estimates.

The test is forward-model consistency. A useful output is not just a candidate state, but an auditable chain linking observations, assumptions, simulator choices, instrument effects, generated states, uncertainties, feedback signals, and residuals.

## KPA 4: human-machine discovery

The fourth KPA is the workflow lens. It asks how scientists, reasoning LLMs, tools, simulators, archives, and the joint-representation model should work together to form, test, revise, and communicate hypotheses.

The joint-representation model supplies grounded embeddings and generative physical inference. Reasoning LLMs can orchestrate retrieval, tool use, simulation, comparison, and explanation. Humans remain responsible for scientific judgement, but the system should expand what they can notice and test.

The test is whether the combined workflow improves scientific search, triage, hypothesis generation, validation, or communication while preserving uncertainty, negative results, provenance, and decision points.

## Why the relevancy graph matters

The relevancy graph is not only a way to organise training data. It is part of the scientific infrastructure needed when papers become less central as the primary scientific object.

Papers are human summaries. The durable objects of future scientific work are results, hypotheses, computations, data products, simulations, protocols, and the relationships between them. A cutout, spectrum, catalogue row, alert, simulation snapshot, synthetic observation, instrument response, result identifier, hypothesis, notebook, and code commit may all speak to the same physical question.

The relevancy graph records why those objects belong together: same source, same sky region, same time window, generated from, degraded from, derived from, conditioned on an instrument response, forward-modelled from, produced by code, used in a computation, evidence for a hypothesis, or part of a workflow.

This graph is the bridge from scientific intent to model design and from model outputs back to scientific accountability. It tells the model what should be compared, what can be generated from what, and what audit trail must remain attached to any claim.

## What the KPAs define

The KPAs define the scientific contract for the joint-representation model. They specify what the model must make easier to find, what it must be able to infer, what physical constraints it must respect, and how it should be used inside a human-machine discovery workflow.

That contract turns the model from a generic multimodal system into a scientific instrument. It implies:

- embedding objectives for serendipity and retrieval;
- generative objectives for cross-instrument and simulator-backed inference;
- validation targets that separate supported inference from plausible completion;
- an auditable relevancy graph connecting data, context, computations, hypotheses, models, and claims;
- an LLM-guided interface that keeps human judgement, uncertainty, and provenance visible.
