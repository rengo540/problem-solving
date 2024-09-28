public class BinaryTree {


    public TreeNode invertBinaryTree(TreeNode root){

        if(root == null){
            return null;
        }

        TreeNode temp = root.right;
        root.right = root.left ;
        root.left = temp;

        invertBinaryTree(root.left);
        invertBinaryTree(root.right);

        return root;

    }


}

 class TreeNode {
      int val;
      TreeNode left;
      TreeNode right;
      TreeNode() {}
      TreeNode(int val) { this.val = val; }
      TreeNode(int val, TreeNode left, TreeNode right) {
          this.val = val;
          this.left = left;
          this.right = right;
      }
}