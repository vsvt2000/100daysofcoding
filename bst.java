import java.util.ArrayList;
import java.util.Scanner;

//import com.sun.org.apache.bcel.internal.generic.RETURN;

class Node{
	int val;
	Node left=null;
	Node right=null;
	Node(int value){
		this.val=value;
	}
	public int getval() {
		return this.val;
	}
	public void setLeft(Node node) {
		this.left=node;
	}
	public Node getLeft() {
		return this.left;
	}
	public void setRight(Node node) {
		this.right=node;
	}
	public Node getRight() {
		return this.right;
	}
}
public class BinaryTree1 {
	Node root=null;
	BinaryTree1(int n){
		this.root=new Node(n);
	}
	
	public Node getRoot() {
		return this.root;
	}
	
	public void addElement(Node node,int n) {
		if(n>node.getval()) {
			if(node.getRight()==null) {
				node.setRight(new Node(n));
				return;
			}
			else {
			addElement(node.getRight(),n);
			}
		}
		if(n<node.getval()) {
			if(node.getLeft()==null) {
				node.setLeft(new Node(n));
				return;
			}
			else {
			addElement(node.getLeft(),n);
			}
		}
	}
	
	public void inorder(Node node) {
		if (node.getLeft()!=null) {
			inorder(node.getLeft());
		}
		System.out.println(node.getval());
		if (node.getRight()!=null) {
			inorder(node.getRight());
		}
	}
	public void preorder(Node node) {
		System.out.println(node.getval());
		if (node.getLeft()!=null) {
			preorder(node.getLeft());
		}
		
		if (node.getRight()!=null) {
			preorder(node.getRight());
		}
	}
	public void postorder(Node node) {
		if (node.getLeft()!=null) {
			postorder(node.getLeft());
		}
		
		if (node.getRight()!=null) {
			postorder(node.getRight());
		}
		System.out.println(node.getval());
	}
	public void levelorder(Node node) {
		ArrayList<Node> queue = new ArrayList<>();
		queue.add(node);
		while(queue.isEmpty()==false) {
			Node temp=queue.remove(0);
			System.out.println(temp.getval());
			if (temp.getLeft()!=null) {
				queue.add(temp.getLeft());
			}
			if (temp.getRight()!=null) {
				queue.add(temp.getRight());
			}
		}
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner scan = new Scanner(System.in);
		System.out.println("---Enter the root node value---");
		int n=scan.nextInt();
		BinaryTree1 bt= new BinaryTree1(n);
		bt.addElement(bt.getRoot(),2);
		bt.addElement(bt.getRoot(),8);
		bt.addElement(bt.getRoot(),1);
		bt.addElement(bt.getRoot(),3);
		bt.addElement(bt.getRoot(),7);
		bt.addElement(bt.getRoot(),11);
		System.out.println("--Inorder Traversal--");
		bt.inorder(bt.root);
		System.out.println("--Preorder Traversal--");
		bt.preorder(bt.root);
		System.out.println("--Postorder Traversal--");
		bt.postorder(bt.root);
		System.out.println("--Levelorder Traversal--");
		bt.levelorder(bt.root);
	}

}
