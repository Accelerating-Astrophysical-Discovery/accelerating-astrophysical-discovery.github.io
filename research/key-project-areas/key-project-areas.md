The proposal starts with four Key Problem Areas (KPAs). They are a working framework, not four separate projects or a closed list. A central goal of the Leiden workshop is to test whether they frame the right scientific problems and to refine, combine, replace, or add KPAs as the discussions and use cases demand.

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

## The relevancy graph

The relevancy graph is envisioned as a large graph database whose nodes are physical data and whose links encode relevancy between those data. A node might contain or reference an image, spectrum, event list, time series, simulation state, synthetic observation, or instrument response. A link records that two nodes are relevant to one another and why.

Text already provides a natural structure for self-supervision. In autoregressive language modelling, tokens are ordered in a sequence and a causal attention mask allows each token to attend to the tokens that came before it. Physical data do not have one universal left-to-right ordering. An image, spectrum, event list, time series, simulation state, and instrument response may all describe related parts or views of a physical system without forming a single sequence.

The relevancy graph supplies this more general attentional field. An image and spectrum may be linked because they observe the same source. A synthetic observation may be linked to the simulation state and instrument response that produced it. Events may be connected by sky position and time, while different spatial or temporal scales may have their own relationships. These connections can be bidirectional, many-to-many, cross-modal, hierarchical, or probabilistic.

During self-supervised training, the system samples connected data from this database and turns the relevant part of the graph into an attention mask. The mask determines which data can attend to one another as the model predicts, reconstructs, or aligns withheld physical information. The graph database is therefore both the structure of the training corpus and the training topology: it replaces an arbitrary ordering of physical data with an attentional field grounded in their actual relationships.

## A framework to refine

The current KPAs make the consortium's starting assumptions concrete enough to examine. The workshop should determine what the joint-representation model must make easier to find, what it must be able to infer, which physical constraints it must respect, and how it should be used inside a human-machine discovery workflow. The resulting framework may retain these four areas, reshape them, or introduce others.

The refined framework should help turn the model from a generic multimodal system into a scientific instrument. It may imply:

- embedding objectives for serendipity and retrieval;
- generative objectives for cross-instrument and simulator-backed inference;
- validation targets that separate supported inference from plausible completion;
- a large relevancy graph database whose connectivity becomes the attention mask for self-supervised learning;
- an LLM-guided interface that keeps human judgement, uncertainty, and provenance visible.
