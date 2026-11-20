# Research data for the SRCoT dissertation

This repository accompanies Fabian Broszio’s monograph *AI Self-Reasoning Chain-of-Thought Framework for Training Content Generation in Emergency Medical Services and Emergency Management* (Freie Universität Berlin, 2026). It contains the two original power traces from Chapter 6 and points to the public code and research artifacts for Chapters 5 and 7.

| Dissertation chapter | Public materials |
| --- | --- |
| 5 · SRCoT Generation on Edge | [SRCoT implementation](https://github.com/lowertheentropy/paper-srcot/tree/369246978df2de8de9a1be38fd8a4f31f09257e5) and [EMS and Munich-Sim case exports](https://github.com/lowertheentropy/paper-srcot/tree/369246978df2de8de9a1be38fd8a4f31f09257e5/artifacts/frontiers-cases) |
| 6 · SRCoT Power Consumption on Edge | [Original power traces, field definitions and battery calculation](data/power/README.md) |
| 7 · RAG Hazard Classification on Edge | [Hazard cards, test cases, classification code and evaluation materials](https://github.com/lowertheentropy/paper-hazard-classification/tree/48608c6f500a3b743f5027caf5c152a000198838) |

## Case data and provenance

The SRCoT case exports preserve the generated responses from two synthetic emergency-management scenarios. Their documentation identifies omitted retrieved passages for which redistribution rights have not been established, as well as redactions of local file paths. The linked commits identify the public versions readers can inspect. [Case export documentation](https://github.com/lowertheentropy/paper-srcot/blob/369246978df2de8de9a1be38fd8a4f31f09257e5/artifacts/frontiers-cases/README.md)

## Related publications

Fabian Broszio, Michael Hoffmann and Adrian Paschke describe the framework in *Self-Reflective Chain-of-Thought (SRCoT): Evidence-Based Text Generation via a Closed-Loop Retrieve–Reflect–Revise Pipeline on Edge LLMs*. [arXiv:2610.23311](https://arxiv.org/abs/2610.23311)

Their brief report *Self-Reflective Chain-of-Thought (SRCoT): Inspectable Local Text Generation for Synthetic Emergency-Management Reports* was accepted by *Frontiers in Disaster and Emergency Medicine* (article 2027409).
