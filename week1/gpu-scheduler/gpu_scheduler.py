"""
GPU Scheduler

Place each pod on a node with enough free GPUs.

- Go through pods in order.
- For each pod, pick the FIRST node (in order) with enough free GPUs.
- Subtract the pod's GPUs from that node.
- If no node fits, the pod is unscheduled. Move on to the next pod.
- A pod can't be split across nodes.

Example:
    nodes = {"a": 4, "b": 2}
    pods  = [("p1", 3), ("p2", 2), ("p3", 2), ("p4", 1)]

    schedule(nodes, pods) -> (
        {"p1": "a", "p2": "b", "p4": "a"},   # assignments
        ["p3"],                              # unscheduled
        {"a": 0, "b": 0},                    # remaining GPUs
    )
"""


def schedule(nodes, pods):

    assignments = {}
    unscheduled = []
    remaining = dict(nodes)
    
    # iterate through the pod (gpu workloads)
    for pod, gpus_needed in pods:
        
        # iterate through the node (machine with free gpus)
        for node, gpus_free in remaining.items():
            
            if gpus_needed <= gpus_free:
                remaining[node] -= gpus_needed
                assignments[pod] = node
                break
        
        else:
            unscheduled.append(pod)
            
    return assignments, unscheduled, remaining

# Time complexity is O(P x N) and Space Complexity is O(P+N)
# ---------------------------------------------------------------- tests

def test():
    # the example
    assert schedule({"a": 4, "b": 2}, [("p1", 3), ("p2", 2), ("p3", 2), ("p4", 1)]) == (
        {"p1": "a", "p2": "b", "p4": "a"}, ["p3"], {"a": 0, "b": 0})

    # exact fit
    assert schedule({"a": 4}, [("p1", 4)]) == ({"p1": "a"}, [], {"a": 0})

    # 4 GPUs free in total, but no single node has 3
    assert schedule({"a": 2, "b": 2}, [("p1", 3)]) == ({}, ["p1"], {"a": 2, "b": 2})

    # a failed pod doesn't block the next one
    assert schedule({"a": 2}, [("p1", 3), ("p2", 1)]) == ({"p2": "a"}, ["p1"], {"a": 1})

    # first fit, not best fit
    assert schedule({"a": 8, "b": 2}, [("p1", 2)]) == ({"p1": "a"}, [], {"a": 6, "b": 2})

    # order matters
    assert schedule({"a": 4, "b": 3}, [("p1", 3), ("p2", 2), ("p3", 2)])[1] == ["p3"]
    assert schedule({"a": 4, "b": 3}, [("p1", 2), ("p2", 2), ("p3", 3)])[1] == []

    # empty inputs
    assert schedule({}, [("p1", 1)]) == ({}, ["p1"], {})
    assert schedule({"a": 4}, []) == ({}, [], {"a": 4})

    # input is not modified
    nodes = {"a": 4}
    schedule(nodes, [("p1", 4)])
    assert nodes == {"a": 4}

    print("all tests pass")


if __name__ == "__main__":
    test()