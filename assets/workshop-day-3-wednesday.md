# Day 3: Wednesday - Long-Context Architectures and Training Protocol

Hours: 9:30-17:00

## Purpose

Wednesday asks what kind of model and training process can learn from Tuesday's Relevancy Graph v0. The goal is not to settle every architecture detail. The goal is to define a plausible architecture family, representation objectives, training objectives, long-context strategy, and staged training protocol.

## Central Deliverable

Architecture and Training Protocol v0.

This should include:

- shared vocabulary for encoders, embeddings, tokens, latent states, long context, retrieval, generative heads, simulator conditioning, provenance, uncertainty, and alignment;
- a candidate architecture sketch;
- representation objectives;
- training objectives;
- long-context strategy;
- compute-to-data training protocol;
- architecture constraints inherited from Tuesday;
- open decisions and risks.

## Timetable

| Time | Activity |
| --- | --- |
| 9:30-10:00 | Morning kickoff talk: **Long-context architectures for multimodal physics.** Cover retrieval, memory, sparse or hierarchical context, modality-specific encoders, shared latent spaces, generative heads, and how a model can reason over data products that cannot all fit into one naive context window. |
| 10:00-10:30 | Groups translate the Relevancy Graph v0 into architecture constraints. What must the architecture preserve from the graph: typed objects, typed relationships, physical units, coordinates, uncertainty, provenance, missingness, instrument metadata, and simulator metadata? |
| 10:30-11:00 | Coffee break |
| 11:00-11:30 | Groups sketch architecture options: modular encoders plus shared representation, retrieval-augmented multimodal model, generative heads, simulator-conditioned components, LLM/tool interface, or staged hybrids. |
| 11:30-12:00 | Groups define representation objectives: what should be close in embedding space, what should be separable, what linked observations should predict, what provenance should remain traceable, and what uncertainty should be represented. |
| 12:00-13:30 | Lunch |
| 13:30-14:00 | Afternoon kickoff talk: **Training protocol and compute-to-data deployment.** Cover how to bring compute to data as much as possible, how to train across distributed archives and HPC environments, and how to stage the path from small controlled corpora to a large multimodal training run. |
| 14:00-14:30 | Groups define training objectives: contrastive alignment, masked or reconstruction objectives, cross-modal prediction, conditional generation, forward-model consistency, provenance-aware supervision, and uncertainty-aware evaluation. |
| 14:30-15:00 | Coffee break |
| 15:00-15:45 | Groups define the staged training protocol: seed corpus, controlled paired datasets, simulator-backed synthetic data, data access model, preprocessing, validation splits, monitoring, scaling path, and compute assumptions. |
| 15:45-16:30 | Plenary synthesis. Compare architecture options and converge on the Architecture and Training Protocol v0 outline. |
| 16:30-17:00 | Closeout. Assign owners for architecture sketch, training objectives, compute-to-data plan, open decisions, and risk list. |

## Architecture and Training Protocol v0 Template

The Wednesday artifact should include:

- architecture vocabulary;
- candidate architecture diagram or structured description;
- representation objectives;
- training objectives;
- long-context strategy;
- compute-to-data training protocol;
- validation strategy;
- risks and open decisions.

## Facilitator Notes

- Keep architecture tied to Tuesday's graph. Avoid generic architecture debates.
- Separate near-term MVP architecture from long-term foundation-model ambition.
- Make compute-to-data constraints explicit.
- Do not let fine-tune vs from-scratch dominate unless the discussion is tied to concrete stages and data constraints.
