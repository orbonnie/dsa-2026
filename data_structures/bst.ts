class TreeNode {
  value: any;
  left: TreeNode | null;
  right: TreeNode | null;
  frequency: number;

  constructor(value: any) {
    this.value = value;
    this.left = null;
    this.right = null;
    this.frequency = 0;
  }
}

class BinarySearchTree {
  root: TreeNode | null;

  constructor() {
    this.root = null;
  }

  insert(val: any) {
    const node = new TreeNode(val);

    if (this.root === null) {
      node.frequency++;
      this.root = node;

      return this;
    }

    let current = this.root;

    while (true) {
      if (val === current.value) {
        current.frequency++;
        return this;
      }

      if (val < current.value) {
        if (current.left === null) {
          node.frequency++;
          current.left = node;
          return this;
        }
        current = current.left;
      } else {
        if (current.right === null) {
          node.frequency++;
          current.right = node;
          return this;
        }
        current = current.right;
      }
    }
  }

  find(target: any, node: TreeNode = this.root!): null | TreeNode {
    if (node === null) return node;

    if (node.value === target) return node;

    if (target < node.value) {
      return this.find(target, node.left!);
    } else {
      return this.find(target, node.right!);
    }
  }

  bfs() {
    if (!this.root) return [];
    const queue: TreeNode[] = [this.root];
    const visited: any[] = [];

    while(queue.length) {
      let node = queue.shift();
      visited.push(node!.value);

      if(node!.left) queue.push(node!.left);
      if(node!.right) queue.push(node!.right);
    }

    return visited;
  }

  bfsRecursive(queue: TreeNode[] = [this.root!], visited: any[] = []): (any[] | TreeNode[]) {
    if (!this.root) return [];
    if (!queue.length) return visited;

    let node = queue.shift()!;
    visited.push(node!.value);

    if(node!.left) queue.push(node!.left);
    if(node!.right) queue.push(node!.right);

    return this.bfsRecursive(queue, visited);
  }

  dfsPreOrder() {
    if (!this.root) return [];
    const visited: TreeNode[] = [];

    function traverse(current: TreeNode) {
      if (!current) return;

      visited.push(current.value);

      if (current.left) {
        traverse(current.left);
      }

      if (current.right) {
        traverse(current.right)
      }
    }
    traverse(this.root!)

    return visited;
  }

    dfsPostOrder() {
    if (!this.root) return [];
    const visited: TreeNode[] = [];

    function traverse(current: TreeNode) {
      if (!current) return;

      if (current.left) {
        traverse(current.left);
      }

      if (current.right) {
        traverse(current.right)
      }

      visited.push(current.value);
    }
    traverse(this.root!)

    return visited;
  }

  dfsInOrder() {
    if(!this.root) return [];

    const visited: TreeNode[] = [];

    function traverse(node: TreeNode) {
      if(node.left) traverse(node.left);
      visited.push(node.value);
      if(node.right) traverse(node.right);
    }

    traverse(this.root);
    return visited;
  }
}



const tree = new BinarySearchTree();

tree.insert(10);
tree.insert(5);
tree.insert(13);
tree.insert(2);
tree.insert(5);
tree.insert(11);
tree.insert(16);
tree.insert(5);
tree.insert(7);
tree.insert(13);

// console.log(tree.find(5));
// console.log(tree.find(8));

console.log(tree.bfsRecursive());
console.log(tree.dfsPreOrder());
console.log(tree.dfsPostOrder());
console.log(tree.dfsInOrder());

// console.log(tree);
