###Question: Verify Preorder Serialization of a Binary Tree

You are given an array of strings, where each element is either a number (i.e. '13') or a sentinel value ('#').
If # represents a null element, return whether the array is a valid preorder serialization of a BST.
The binary tree has no particular orderin (it's not necessarily a BST).

Examples
```
[3,#,#]

output: True
    3
   / \
  #   #
would serialize into the above array
```

```
[3,4,5,#,6,#,2,#,#]
output: True

       3
      / \
    4    2
   / \  / \
  5   ##   #
 / \
#   6
would serialize into the above array
```

```
[3]
output: False
Leaf nodes (nodes with no chidlren) clearly need 2 null pointers after, so it's easy to see that this
isn't a valid serialization.
```
