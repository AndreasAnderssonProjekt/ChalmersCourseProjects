# Network Flow

Imagine that you are trying to transport some kind of fluid through a complex pipeline network. The network consist of three components: a source, internal pipelines and a sink. The source and sink can be thought of as reservoirs where fluid can be stored. Initially, all fluid is located at the source. The fluid is then pushed from the source through the internal pipelines to the sink. Due to physical constraints such as volume and robustness, each internal pipeline is only able to carry a certain amount of flow. Naturally, a topic of interest is to arrange the flow through the network such that all constraints are respected while pushing the maximum amount of fluid from the source to the sink.. This problem is called the Maximum-Flow Problem (MFP).

The pipeline network described above can be thought of as a flow network. A flow network is a directed graph G=(V,E) with the following features:
* Each edge $e$ is associated with a capacity, which is a nonnegative integer denoted $c_{e}$.
* There is a single source node denoted $s\in V$.
* There is a single sink node denoted $t \in V$.

The source node and sink node have unique properties, different from those of the other nodes. There is no incoming edges to the source node and there is no outgoing edges from the sink node. Nodes other than the source and sink are called internal nodes.

To continue we define flow. Flow is a function $f : E \rightarrow \mathbb{N}$ that maps each edge to a real non-negative integer. The value $f(e)$ corresponds to the amount of flow carried by edge e.

To make sure that our flow network obey the laws of physics we introduce the following constraints:
* $0 \leq f(e) \leq c_{e}, \quad \forall e\in E \quad$ (capacity constraint).
* $\sum_{\text{e in to v}} f(e) = \sum_{\text{e out of v}} f(e) \quad \forall v \neq s,t \in V \quad$ (conservation constraint). 

For convenience, introduce the following notation
* $f(v)^{\text{in}} = \sum_{\text{e in to v}} f(e)$.
* $f(v)^{\text{out}} = \sum_{\text{e out of v}} f(e)$.

The value of a flow is defined as
$v(f) = f(s)^{\text{out}}$,
that is, the flow pushed from the source.

MFP can thus be defined as the optimization problem $\max\limits_{f} v(f)$.

To solve this optimization problem we will use the Ford-Fulkerson algorithm. The Ford-Fulkerson algorithm iteratively push flow from the source in a systematic way that respect the constraints. The implementation of the Ford-Fulkerson utilizes a concept called residual graphs. Given a graph $G=(V,E)$, and a flow $f$ on $G$, we define the residual graph $G_{f}$ of $G$ with respect to $f$ as follows:
* The vertex set of $G$ and $G_{f}$ is identical.
* For each edge $(u,v) = e\in E$ of $G$, the residual graph $G_{f}$ has two edges, a forward edge and a backward edge. The forward edge goes from u to v and has a capacity of $c_{e}-f(e)$, that is, the maximum additional flow that can can be carried by the edge given that it currently carries f(e) flow. The backward edge goes from v to u and has a capacity of $f(e)$, that is, the flow that can be "pushed back".

The Ford-Fulkerson algorithm initially start with a flow network where $f(e)=0$ for all edges. The corresponding residual graph is thus the graph where all its forward edges has a capacity of $c_{e}$ and all its backward edges has a capacity of 0. Given this initial flow network, the Ford-Fulkerson algorithm then iteratively pushes flow from the source in the following way: Let P be a simple s-t path in $G_{f}$ and let b=bottleneck(f,P) be the minimum residual capacity of any edge on P, with respect to the flow f. We then push b units of flow along all edges of P and update their capacities. If we push b units along a forward edge we decrease its capacity by b and increase the capacity of its corresponding backward edge by b. Similarly, if we instead push b units along a backward edge we decrease its capacity by b and increase the capacity of its corresponding forward edge by b. The algorithm is complete when we can no longer find a simple s-t path in $G_{f}$, and the value of the flow is the maximum flow. This can easily be proven by showing that the maximum flow coincide with the min-cut for the bipartite graph $G = (V, E)$ where $V = A\cup B$, where $A=\{s\}$ and $B=V \setminus s$. We leave the proof as an exercise for the reader.

My implementation of the Ford-Fulkerson algorithm is found in the "Ford-Fulkerson Algorithm" folder.
