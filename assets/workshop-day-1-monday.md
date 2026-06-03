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
| 10:00-10:30 | Morning kickoff talk: **Shared vocabulary for AI-accelerated discovery.** Align on the meanings of joint representation, embeddings, conditional generation, simulator-backed data, long context, agentic workflow, provenance, validation, and human judgement. |
| 10:30-11:00 | Coffee break |
| 11:00-11:30 | Use-case card setup. Facilitators introduce the card template and split participants into working groups. |
| 11:30-12:00 | Working groups draft candidate use-case cards. Each card must state the scientific workflow, human role, machine role, required data, required model capability, and proposed evaluation target. |
| 12:00-13:30 | Lunch |
| 13:30-14:00 | Afternoon kickoff talk: **KPAs as testable model capabilities.** Connect use cases to embeddings for KPA 1, generative reconstruction for KPA 2, simulator-backed observation-to-simulation mappings for KPA 3, and LLM-guided collaboration for KPA 4. |
| 14:00-14:30 | Groups refine use-case cards around explicit mechanisms: embedding search, conditional generation, simulator conditioning, long-context retrieval, or agentic tool use. |
| 14:30-15:00 | Coffee break |
| 15:00-15:45 | Groups define evaluation targets for each flagship case: positive controls, baseline comparisons, synthetic anomaly tests, forward-model consistency checks, uncertainty labels, provenance requirements, and human review points. |
| 15:45-16:15 | Plenary selection of 3-5 flagship use cases. The group chooses the cases that will drive Tuesday-Friday. |
| 16:15-16:30 | Closeout. Confirm vocabulary, selected use cases, out-of-scope items, and owners for writing the Monday artifact into the repo. |

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
