# Day 1: Monday - Shared Vocabulary, Use Cases, and Evaluation Targets

Hours: 10:00-16:30

## Purpose

Monday sets the conceptual ground for the workshop. The goal is not to produce a broad taxonomy of possible AI applications. The goal is to agree on vocabulary, select a small number of flagship use cases, and define how we would know whether each use case is working.

KPA 4 frames the day: what should human-machine discovery actually look like? KPAs 1-3 provide the technical mechanisms and test cases: embeddings for serendipity, generative reconstruction across instruments, and simulator-backed observation-to-simulation mappings.

## Central Deliverable

Shared Vocabulary and Discovery-Evaluation Map v0.

This should include:

- a short glossary for joint representation, embedding, conditional generation, simulator-backed data, long context, agentic workflow, provenance, uncertainty, validation, and human judgement;
- 3-5 flagship use-case cards;
- for each use case, the required model capability, required data, human role, machine role, and evaluation target;
- a short list of use cases that are explicitly out of scope for the first MVP.

## Timetable

| Time | Activity |
| --- | --- |
| 09:00-10:00 | Arrival and coffee. The building is open; the formal programme begins at 10:00. |
| 10:00-10:30 | Kickoff talk: **AI-first Science 2.0.** Introduce the two consortium pillars, the live AI-assisted working method, and the KPAs as a starting framework that the workshop may refine, combine, replace, or extend. |
| 10:30-12:00 | Science 2.0 and use-case working session. Groups imagine future scientific workflows, work backwards toward near-term opportunities, and draft candidate use-case cards. Each card must state the human role, machine role, required data, model capability, and evidence of success. |
| 12:00-13:30 | Lunch |
| 13:30-14:30 | Plenary synthesis and selection. Groups share their visions and candidate use cases; AI assists with identifying overlaps and disagreements; the plenary selects 3-5 flagship cases. |
| 14:30-15:00 | Coffee break |
| 15:00-16:15 | Define evaluation targets for each flagship case: positive controls, baseline comparisons, synthetic anomaly tests, forward-model consistency checks, uncertainty labels, provenance requirements, and human review points. |
| 16:15-16:30 | Closeout and overnight AI brief. Confirm the selected cases, evaluation targets, out-of-scope items, artifact owners, and the synthesis to prepare for Tuesday. |

## Use-Case Card Template

Each card should include:

- title;
- scientific workflow;
- current bottleneck;
- human role;
- machine role;
- required data;
- required model capability;
- KPA mechanism;
- evaluation target;
- provenance and uncertainty requirements;
- why this belongs in the first MVP or why it is a stretch case.

## Facilitator Notes

- Keep the group from expanding to too many use cases. The rest of the week needs anchors, not a large catalogue.
- Make evaluation central. If a use case cannot say how success would be tested, it is not ready to drive architecture decisions.
- Treat KPA 4 as the workflow lens, not as a separate end-of-week topic.
- Treat KPAs 1-3 as mechanisms: embeddings, generative reconstruction, and simulator-backed mappings.
- Do not stop the morning session for coffee; participants can have coffee before the 10:00 start and at 14:30.
- Make the overnight AI assignment explicit before closing.
