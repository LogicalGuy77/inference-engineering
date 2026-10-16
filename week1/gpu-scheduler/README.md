# GPU Scheduler (first-fit)

## Assumptions
- A Pod must fit entirely on one node.
- GPUs are whole, identical units.
- Pods and nodes are processed in input order.
- Pod names are unique. Input is not validated.
- One scheduler runs at a time.

## Notes
- Time O(P × N), space O(N + P).
- Order matters: nodes {a: 4, b: 3}; Pods [3, 2, 2] fit 2, Pods [2, 2, 3] fit 3.
- First-fit is not optimal; free GPUs can be fragmented across nodes.
- Two schedulers at once could overallocate a node, because each checks its own copy.