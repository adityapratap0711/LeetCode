class Solution:
    def deleteNode(self, root, key):
        if root is None:
            return None

        # Search for the key
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)

        # Node found
        else:
            # Case 1: no left child
            if root.left is None:
                return root.right

            # Case 2: no right child
            if root.right is None:
                return root.left

            # Case 3: two children
            # Find the inorder successor:
            # smallest node in the right subtree
            successor = root.right

            while successor.left is not None:
                successor = successor.left

            # Copy successor's value
            root.val = successor.val

            # Delete the duplicate successor node
            root.right = self.deleteNode(root.right, successor.val)

        return root