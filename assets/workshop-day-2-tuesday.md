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

This deliverable should not assume a graph database, query language, or implementation architecture. It should define the data relationships the model and system must respect.

## Timetable

| Time | Activity |
| --- | --- |
| 9:30-10:00 | Morning kickoff talk: **The training corpus as a relevancy graph.** Introduce the idea that data, tokenisation, and provenance are coupled. Explain node types, relationship types, and why relationships should carry physical and procedural meaning. |
| 10:00-10:30 | Working groups map the selected Monday use cases to required data objects. Start from the use-case cards and list the observations, catalogues, simulations, synthetic observations, instrument responses, language, code, and provenance records needed. |
| 10:30-11:00 | Coffee break |
| 11:00-11:30 | Define node types. Groups identify the minimum useful node types and required metadata for each. |
| 11:30-12:00 | Define relevancy edge types. Groups identify relationships such as same sky region, same source, same time window, generated from, degraded from, derived from, forward-modelled from, conditioned on instrument response, produced by code, and supported by paper or workflow lineage. |
| 12:00-13:30 | Lunch |
| 13:30-14:00 | Afternoon kickoff talk: **Tokenising heterogeneous physical data.** Cover representation choices for images, event lists, spectra, time series, catalogues, simulations, language, code, and provenance records. |
| 14:00-14:30 | Groups define tokenisation implications. For each node and edge type, identify what the representation must preserve: units, scale, locality, ordering, uncertainty, missingness, modality, provenance, and physical context. |
| 14:30-15:00 | Coffee break |
| 15:00-15:45 | Groups document known ambiguities and risks: uncertain associations, probabilistic crossmatches, synthetic-to-real transfer, inconsistent units, calibration differences, missing provenance, and access constraints. |
| 15:45-16:30 | Plenary synthesis. Build the shared Relevancy Graph v0 outline and agree on the minimum schema needed for Wednesday. |
| 16:30-17:00 | Closeout. Assign owners for writing the node types, edge types, metadata fields, ambiguities, and architecture constraints into the repo. |

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
