# Day 2: Tuesday - Data, Representation, and Provenance

Hours: 9:30-17:00

## Purpose

Tuesday turns Monday's flagship use cases into a concrete description of what data must be related, why those relationships matter, and what information must travel with the data. This should constrain Wednesday's architecture discussion. Without a clear relevancy graph, architecture discussion will stay too general.

## Central Deliverable

Relevancy Graph v0 for Monday Use Cases.

This should include:

- the selected Monday use cases that the graph supports;
- node types required for those use cases;
- relevancy edge types and their physical or procedural meaning;
- required metadata and provenance fields;
- tokenisation implications for each node and edge type;
- known ambiguities, including probabilistic crossmatches, uncertain time or sky associations, simulator domain gaps, inconsistent calibration, and incomplete provenance;
- architecture constraints implied by the graph.

The consortium envisions a large graph database, but this deliverable should define the scientific relationships and training role before committing to a query language or storage implementation.

## Timetable

| Time | Activity |
| --- | --- |
| 9:30-10:00 | Kickoff and overnight review: **The training corpus as a relevancy graph.** Correct Monday's AI-assisted synthesis, explain how graph connectivity becomes the training attention mask, and introduce tokenisation challenges alongside current multimodal examples. |
| 10:00-10:30 | Working groups map Monday's selected use cases to participants' dataset lists: observations, catalogues, simulations, synthetic observations, instrument responses, language, code, and provenance records. |
| 10:30-11:00 | Coffee break |
| 11:00-12:00 | Graph working session. Groups define node types, relevancy links, metadata, provenance, ambiguities, and what the connectivity should mean during self-supervised training. |
| 12:00-13:30 | Lunch |
| 13:30-14:30 | Plenary graph synthesis. Groups share their proposals and assemble the common Relevancy Graph v0 for Monday's use cases. |
| 14:30-15:00 | Coffee break |
| 15:00-16:30 | Tokenisation and architecture constraints. For each node and link type, identify what representations must preserve: units, scale, locality, ordering, uncertainty, missingness, modality, provenance, and physical context. Record ambiguities and constraints for Wednesday. |
| 16:30-17:00 | Closeout and overnight AI brief. Assign owners and commission a draft graph schema or prototype plus a one- or two-page architecture vocabulary primer. |

## Relevancy Graph v0 Template

The Tuesday artifact should include:

- supported use cases;
- node type inventory;
- edge type inventory;
- required metadata;
- provenance requirements;
- tokenisation implications;
- known ambiguities;
- architecture constraints;
- open decisions.

## Facilitator Notes

- Do not jump to database implementation.
- Keep the graph grounded in Monday's selected use cases.
- Make provenance mandatory, not an afterthought.
- Keep tokenisation at the level needed to inform architecture. Full tokeniser implementation is not Tuesday's goal.
- Treat the graph as training topology: sampled connectivity supplies a general attention mask for physical data.
- End with a reviewed prompt for the overnight schema/prototype and Wednesday primer.
