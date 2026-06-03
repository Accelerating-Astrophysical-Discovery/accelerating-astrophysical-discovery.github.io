The proposal defines four Key Problem Areas (KPAs). They are not isolated projects; they are target capabilities of a shared, self-supervised physics foundation model trained on multimodal astrophysical data, simulations, language, code, and provenance.

The central technical challenge is to curate heterogeneous data at scale, define tokenisation semantics for each data type, define explicit relevancy links between related data products, and train over long contexts in a way that preserves physical faithfulness.

## KPA 1: Rare events and anomalies

Large observational surveys contain enormous data volumes, while rare signals are often weak. This KPA asks how a foundation model can use learned embedding spaces, zero-shot clustering, and out-of-distribution scoring to detect rare events or anomalies that may indicate new physics.

Initial anchors include multimessenger transients and variable sources such as compact-object mergers, gamma-ray bursts, and blazar flares, drawing on GWOSC, IceCube, Fermi-LAT, Fermi-GBM, and ZTF-style time-domain context.

## KPA 2: Beyond individual instrument limits

Individual instruments hit angular, spectral, and sensitivity limits. This KPA asks how multimodal context can support conditional reconstruction, super-resolution, deconfusion, and cross-instrument inference without pretending that one modality alone contains all the information.

Seed datasets include shared-sky multiwavelength galaxy, AGN, and cluster populations from COSMOS, HST, Chandra, XMM-Newton, eROSITA, LOFAR, MeerKAT, Euclid, Gaia, SDSS, and related catalogue backbones.

## KPA 3: Ansatz-free simulation initialisation

Simulation initial conditions often depend on an explicit ansatz. This KPA explores observation-to-simulation mappings where multimodal observations constrain latent 3D physical states, backed by forward-model consistency and simulation priors.

Initial simulation corpora include CAMELS, IllustrisTNG, EAGLE, Quijote, and HADES, with synthetic-observation links used to test whether inferred states remain physically plausible.

## KPA 4: Collaborative scientific reasoning

The long-term vision is a human-machine scientific workflow in which foundation models understand physical data, language, code, provenance, and the scientific method. This KPA asks how agentic systems can support collaborative exploration while remaining physically aligned and continuously monitored.

This includes language and code provenance, model/tool orchestration, MCP-like interfaces, experiment tracking, issue-backed collaboration, and explicit governance over what the system can and cannot claim.

## Relevancy graph

The proposal frames the training corpus as a relevancy graph. Nodes are typed data assets such as image patches, event lists, spectra, catalogue rows, simulation snapshots, papers, scripts, or provenance records. Edges state why one asset is relevant to another.

Examples include same-sky WCS alignment, PSF or beam mappings, before/after time windows, transient trigger links, catalogue cross-matches, simulation-to-synthetic-observation forward models, paper-to-dataset links, and code-to-data-product provenance.

## Workshop deliverables

Each KPA team is expected to produce:

- a concrete end-user use case;
- data features and tokenisation semantics;
- a dataset specification using available sources;
- a research use case that can become part of the MVP;
- a one-page concept document and invitee list for post-workshop collaboration.

The implementation team will work in parallel on the open-source stack, training and inference architecture, issue backlog, CI/CD, and technical plan needed to turn the KPA outputs into a working minimum viable product.
