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
| 9:30-10:00 | Kickoff and overnight review: **Architectures for multimodal physics.** Review the primer and overnight graph work; build from basic concepts to long context, recurrent depth, graph-derived attention, modality-specific encoders, shared representations, generative heads, and simulator conditioning. |
| 10:00-10:30 | Translate the Relevancy Graph v0 into architecture constraints. What must the architecture preserve: typed objects and relationships, physical units, coordinates, uncertainty, provenance, missingness, instrument metadata, and simulator metadata? |
| 10:30-11:00 | Coffee break |
| 11:00-12:00 | Architecture working session. Groups use AI to research and sketch candidate architecture families, representation objectives, and training hypotheses tied to Tuesday's graph. |
| 12:00-13:30 | Lunch |
| 13:30-14:30 | Plenary architecture synthesis. Compare candidate designs, identify common components and disagreements, and keep multiple hypotheses where the evidence does not yet justify convergence. |
| 14:30-15:00 | Coffee break |
| 15:00-16:30 | Training protocol and prototype brief. Define alignment, reconstruction, cross-modal prediction, conditional generation, simulator feedback, validation, compute-to-data deployment, staged scaling, risks, and the starter artifacts needed for Thursday. |
| 16:30-17:00 | Closeout and overnight AI brief. Confirm architecture hypotheses, the training protocol, owners, and the prototype code or artifacts the AI should prepare overnight. |

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
- Calibrate the kickoff for a mixed audience: establish basic vocabulary before introducing state-of-the-art options.
- Treat every architecture as a hypothesis to test against the graph and evaluation targets.
