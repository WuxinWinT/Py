# 018-二叉树的镜像（他错误）



#源二叉树 
#    	    8
#    	   /  \
#    	  6   10
#    	 / \  / \
#    	5  7 9 11

class Solution:
    def Mirror(self, root):
        # write code here
        if not root:
            return root
        node=root.left
        root.left=root.right
        root.right=node  
        #这时候下面的树全部交换，例如：
  #      8
    #   /  \
    #  10   6
    # / \  / \
    #9  11 5  7
        self.Mirror(root.left)
        self.Mirror(root.right)
        return root
