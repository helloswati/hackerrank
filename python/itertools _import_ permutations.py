itertools.permutations(iterable[, r])
This tool returns successive r length permutations of elements in an iterable.
If r is not specified or is None, then r defaults to the length of the iterable, and all possible full length permutations are generated.
Permutations are printed in a lexicographic sorted order. So, if the input iterable is sorted, the permutation tuples will be produced in a sorted order.


Solution :
from itertools import permutations
string, length = input().split()
output = ["".join(i) for i in permutations(string,int(length))]
output.sort()
print("\n".join(output))s
