Accelerating Astrophysical Discovery is a consortium effort with two connected goals.

The first goal is to design how future astrophysicists and cosmologists will do science in collaboration with AI. This means more than adding chat interfaces to existing tools. It means redesigning scientific workflows so humans, reasoning language models, simulators, data archives, instruments, and foundation models can jointly form hypotheses, retrieve evidence, run checks, update beliefs, and communicate results.

The second goal is to build the technical substrate that makes this possible: a joint-representation model that understands physical data. Such a model should learn across observations, simulations, synthetic observations, language, code, and instrumental context. It should support embeddings for retrieval and serendipity, and generative capabilities for conditional inference across linked views of the same physical system.

## Discovery needs more serendipity

**The main driver of discovery is serendipity.** Modern astronomy now produces high-quality data faster than we can turn it into understanding. The bottleneck is no longer only data collection. It is knowing what to notice, what to compare, what to retrieve, and what surprising relationships deserve human attention.

A joint-representation model can make serendipity operational. If the embedding space is physically meaningful, it can surface rare candidates, unexpected analogues, counterexamples, and neighbouring evidence that a human may not know to ask for. The aim is not to replace scientific judgement, but to widen the field of attention.

## Discovery also needs experimental discipline

**The second main driver of discovery is rigorous control of experimental design.** Scientific progress depends on precise protocols, careful control of priors and uncertainties, and a Bayesian framework for updating hypotheses as evidence accumulates.

AI systems must be designed around that discipline. They should not simply generate plausible explanations. They should expose assumptions, preserve uncertainty, keep track of negative results, and make it clear which data support which hypothesis. Generative capability is scientifically useful only when it remains connected to protocols, controls, forward models, and validation.

## Papers are not the primary object

**Publish or perish should become a thing of the past.** Papers are subjective human summaries. They are essential for communication, but they are not the most fundamental scientific object.

In an AI-native scientific workflow, the central objects are hypotheses, evidence, protocols, and results. Papers become derivations and explanations built from those objects. Results should have durable identifiers. Hypotheses should be explicitly linked to the data, simulations, code, priors, assumptions, and validation steps that support or weaken them. Scientific protocols should reference those objects directly rather than relying only on narrative summaries.

## Science was not built to share with AI

**The current scientific framework was not designed to share the road with AI.** A useful analogy is a city built only for pedestrians into which cars are suddenly introduced. If both are to coexist safely and productively, parts of the city need to be redesigned: roads, sidewalks, signals, rules, and shared expectations.

Scientific infrastructure faces a similar transition. Our papers, archives, code, provenance records, review systems, and collaboration norms were built for human-only workflows. AI systems can already read and generate language, but science requires more than language. It requires traceable relationships between data, hypotheses, simulations, instruments, uncertainty, and claims. We need scientific infrastructure that lets humans and machines reason together without blurring responsibility.

## Physical data needs its own structure

Astrophysical data are heterogeneous and relational. A galaxy image, gravitational-wave strain segment, spectrum, catalogue row, simulation snapshot, or instrument response may describe a shared physical system, but these data do not form one natural sequence. Their relationships can depend on source, position, time, scale, measurement process, simulation history, and provenance.

This matters for AI because the structure used to learn from physical data must express those relationships. Language contributes composable concepts; physical data grounds them in evidence, measurement, simulation, uncertainty, and physical constraints. A useful joint representation must learn across both.

## The role of the joint-representation model

The joint-representation model is the bridge between these ideas. It should learn when different data products refer to the same physical situation, when they are informative about one another, and when a generated completion is physically admissible rather than merely plausible.

We envision the relevancy graph as a large graph database in which nodes are physical data and links encode relevancy between them: the same source, sky region, time window, physical scale, instrument response, simulation-to-observation path, or provenance relationship. It is designed as training structure, not merely as a catalogue of associations.

In autoregressive language modelling, token order supplies a causal attention mask. Physical data have no universal left-to-right ordering, so self-supervised training needs a more general attentional field. When the system samples connected data from the graph, that connectivity becomes the attention mask: it determines which data can attend to one another while the model predicts, reconstructs, or aligns withheld physical information.

The long-term aim is an agentic discovery system in which reasoning LLMs guide retrieval, tool use, hypothesis generation, simulation, validation, and communication, while the joint-representation model provides grounded physical understanding. Humans remain responsible for scientific judgement, but they work with systems that can search, connect, and test evidence at a scale no individual can manage.
