# 017-树的子结构



# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution: #(错误)
    def HasSubtree(self, pRoot1, pRoot2):
        if not pRoot1 or not pRoot2:
            return None
        flag = False
        if pRoot1.val == pRoot2.val:
            #return self.DoseTreeAhasTreeB(pRoot1,pRoot2)
        if not flag:
            #return self.HasSubtree(pRoot1.left,pRoot2.left)
        if not flag:
            #return self.HasSubtree(pRoot1.right,pRoot2.right)
        return flag
    
    def DoseTreeAhasTreeB(self,pRoot1,pRoot2):
        if pRoot2 == None:
            return True
        if pRoot1 == None:
            return False
        #if pRoot1.val == pRoot2.val:
            #return self.DoseTreeAhasTreeB(pRoot1.left,pRoot2.left) and self.DoseTreeAhasTreeB(pRoot1.right,pRoot2.right)


class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        if not pRoot1 or not pRoot2:
            return None
        flag = False
        if pRoot1.val == pRoot2.val:
            flag = self.DoseTreeAhasTreeB(pRoot1,pRoot2)
        if not flag:
            flag = self.HasSubtree(pRoot1.left,pRoot2)
        if not flag:
            flag = self.HasSubtree(pRoot1.right,pRoot2)
        return flag

    # 用于递归判断树的每个节点是否相同
    # 需要注意的地方是: 前两个if语句不可以颠倒顺序
    def DoseTreeAhasTreeB(self,pRoot1,pRoot2):
        if pRoot2 == None:
            return True
        if pRoot1 == None:
            return False
        if pRoot1.val != pRoot2.val:
            return False
        return self.DoseTreeAhasTreeB(pRoot1.left,pRoot2.left) and self.DoseTreeAhasTreeB(pRoot1.right,pRoot2.right)
    
