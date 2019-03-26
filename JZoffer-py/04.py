# 004-重建二叉树



class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 返回构造的TreeNode根节点
def reConstructBinaryTree(self, pre, tin):
    # write code here
    if not pre or not tin:
        return None
    root_val = pre[0]
    root = TreeNode(root_val)
    for i in range(len(tin)):
        if tin[i] == root_val:
            break
    root.left = self.reConstructBinaryTree(pre[1:1+i],tin[:i])  #@ 加self调用
    root.right = self.reConstructBinaryTree(pre[1+i:], tin[i+1:])  #@

    return root


链接：https://www.nowcoder.com/questionTerminal/8a19cbe657394eeaac2f6ea9b0f6fcf6
来源：牛客网

class Solution:
    def reConstructBinaryTree(self, pre, tin):
        if not pre or not tin:
            return None
        root = TreeNode(pre.pop(0))
        index = tin.index(root.val)
        root.left = self.reConstructBinaryTree(pre, tin[:index])
        root.right = self.reConstructBinaryTree(pre, tin[index + 1:])
        return root



#只是为了输出看，与题无关
def preorder(root):
    if root:
        preorder(root.left)
        print(root.val)
        preorder(root.right)

preorder(reConstructBinaryTree([1,2,3,4,5,6,7],[3,2,4,1,6,5,7]))
