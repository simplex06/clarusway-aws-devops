def majority_vote(List): 
    return max(set(List), key = List.count) 

print(majority_vote(["A", "A", "A", "B", "C", "A"]))