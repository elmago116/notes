---
title: "Grounding Methods for Neural-Symbolic AI | IJCAI"
source: "https://www.ijcai.org/proceedings/2025/535"
authors: "[[Rodrigo Castellano Ontiveros]],[[Francesco Giannini]],[[Marco Gori]],[[Giuseppe Marra]],[[Michelangelo Diligenti]]"
published:
created: 2026-03-09
description: "Electronic proceedings of IJCAI 2025"
tags:
DOI:
Type:
year:
---
[[Grounding Methods for Neural-Symbolic AI.pdf]]

## Grounding Methods for Neural-Symbolic AI

## Rodrigo Castellano Ontiveros, Francesco Giannini, Marco Gori, Giuseppe Marra, Michelangelo Diligenti

Proceedings of the Thirty-Fourth International Joint Conference on Artificial Intelligence

Main Track. Pages 4806-4814. [https://doi.org/10.24963/ijcai.2025/535](https://doi.org/10.24963/ijcai.2025/535)

---

A large class of Neural-Symbolic (NeSy) methods employs a machine learner to process the input entities, while relying on a reasoner based on First-Order Logic to represent and process more complex relationships among the entities. A fundamental role for these methods is played by the process of logic grounding, which determines the relevant substitutions for the logic rules using a (sub)set of entities. Some NeSy methods use an exhaustive derivation of all possible substitutions, preserving the full expressive power of the logic knowledge, but leading to a combinatorial explosion of the number of ground formulas to consider and, therefore, strongly limiting their scalability. Other methods rely on heuristic-based selective derivations, which are generally more computationally efficient, but lack a justification and provide no guarantees of preserving the information provided to and returned by the reasoner. Taking inspiration from multi-hop symbolic reasoning, this paper proposes a parametrized family of grounding methods generalizing classic Backward Chaining. Different selections within this family allow to obtain commonly employed grounding methods as special cases, and to control the trade-off between expressiveness and scalability of the reasoner. The experimental results show that the selection of the grounding criterion is often as important as the NeSy method itself.

Keywords:

Machine Learning: ML: Neuro-symbolic methods/Abductive Learning

Knowledge Representation and Reasoning: KRR: Learning and reasoning