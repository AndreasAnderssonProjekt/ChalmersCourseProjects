# Network Flow

Imagine that you are trying to transport some kind of fluid through a complex pipeline network. The network consist of three components: a source, internal pipelines and a sink. The source and sink can be thought of as reservoirs where fluid can be stored. Initially, all fluid is located at the source. The fluid is then pushed from the source through the internal pipelines to the sink. Due to physical constraints such as volume and robustness, each internal pipeline is only able to carry a certain amount of flow. Naturally, a topic of interest is to arrange the flow through the network such that all constraints are respected while pushing the maximum amount of fluid from the source to the sink.. This problem is called the Maximum-Flow Problem (MFP).

The pipeline network described above can be thought of as a flow network. A flow network is a directed graph G=(V,E) with the following features:
* Each edge $e$ is associated with a capacity, which is a nonnegative integer denoted $c_{e}$.
* There is a single source node denoted $s\in V$.
* There is a single sink node denoted $t \in V$.

Nodes other than the source and sink are called internal nodes.

To make sure that our flow network obey the laws of physics we introduce the following constraints:
* $0 \leq f(e) \leq c_{e}, \forall e\in E$
