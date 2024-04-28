/*
 * This program provides the code for a generic implementation
 * of a TreeMap, using a Binary Search Tree of Nodes - a private class that holds a key and value and
 * a left and right pointer. It provides typical functionalities like getting a value by its key,
 * putting a new key-value pair in the TreeMap, and retrieving the set of keys. Moreover, it is
 * easy to get the keys in order by doing an in-order traversal of the tree. 
 */

import java.util.Set;
import java.util.HashSet;

public class MyTreeMap<K, V> {
	private class Node{    
    	public K key;
        public V value;    
        public Node left;  
        public Node right;  
        
        /*
         * This is a constructor that initializes the key and value of the Node
         * with given arguments. It also sets the left and right references to null.
         */
        public Node(K key, V value) {    
    		this.key = key;
    		this.value = value;
    		this.left = null;    
            this.right = null;    
        }    
    } 
	private Node root;
	
	/*
	 * This is a constructor that initializes the root node of the tree to null.
	 */
	public MyTreeMap() {
		root=null;
	}
	
	/*
	 * This is a private function that compares two keys of type K. If the
	 * first one is smaller than the second, it outputs -1; if they're equal it
	 * outputs 0, and if the first one is larger it outputs 1.
	 * @param a is a key of type K.
	 * @param b is a key of type K.
	 * @returns an int.
	 */
	private int compareKey(K a, K b){
    	return ((Comparable<K>)a).compareTo(b);
    }
	
	/*
	 * This function gets the size of the TreeMap by calling a recursive
	 * function on the tree.
	 * @returns an int.
	 */
	public int size() {
		return sizeRecur(root);
	}
	
	/*
	 * This is a private function that recursively gets the size of the TreeMap by
	 * adding 1 to the total count for each Node in the tree.
	 * @param curr is a Node.
	 * @returns an int.
	 */
	private int sizeRecur(Node curr) {
		if (curr==null) {
			return 0;  // no subtree
		}
		return 1+sizeRecur(curr.left)+sizeRecur(curr.right);  // 1 for current node, plus subtree total
	}
	
	/*
	 * This function determines whether the TreeMap is empty.
	 * @returns a boolean.
	 */
	public boolean isEmpty() {
		return size()==0;
	}
	
	/*
	 * This function determines whether the TreeMap contains a given key by
	 * calling a recursive function on the tree.
	 * @param key is of type K.
	 * @returns a boolean.
	 */
	public boolean containsKey(K key) {
		return containsKeyRecur(root, key);
	}
	
	/*
	 * This function determines whether a tree contains a given key by recursing
	 * down the tree until it either finds a Node with the correct key, or
	 * reaches the bottom of the tree.
	 * @param curr is a Node.
	 * @param key is of type K.
	 * @returns a boolean.
	 */
	private boolean containsKeyRecur(Node curr, K key) {
		if (curr==null) {
			return false;  // empty tree can't contain key
		}
		if (compareKey(key, curr.key)==0) {
			return true;
		}
		if (compareKey(key, curr.key)<0) {  // go left if key is less
			return containsKeyRecur(curr.left, key);
		}
		return containsKeyRecur(curr.right, key);  // go right if key is greater
	}
	
	/*
	 * This function determines whether the TreeMap contains a given value by
	 * calling a recursive function on the tree.
	 * @param value is of type V.
	 * @returns a boolean.
	 */
	public boolean containsValue(V value) {
		return containsValueRecur(root, value);
	}
	
	/*
	 * This function determines whether a given value is in the tree by searching
	 * over the entire tree to see if any Nodes contain the correct value.
	 * @param curr is a Node.
	 * @param value is of type V.
	 * @returns a boolean.
	 */
	private boolean containsValueRecur(Node curr, V value) {
		if (curr==null) {
			return false;  // empty tree can't contain value
		}
		if (value.equals(curr.value)) {
			return true;
		}
		return containsValueRecur(curr.left, value)||containsValueRecur(curr.right, value);
	}
	
	/*
	 * This function retrieves the value associated with a key, or null
	 * if the key is not in the TreeMap, by passing the tree to a recursive
	 * function.
	 * @param key is of type K.
	 * @returns a value of type V.
	 */
	public V get(K key) {
		return getRecur(root, key);
	}
	
	/*
	 * This is a recursive function that gets the value
	 * corresponding to a given key in the tree, or null
	 * if the key isn't in the tree.
	 * @param curr is a Node.
	 * @param key is of type K.
	 * @returns a value of type V.
	 */
	private V getRecur(Node curr, K key) {
		if (curr==null) {
			return null;
		}
		if (compareKey(key, curr.key)==0) {
			return curr.value;
		}
		if (compareKey(key, curr.key)<0) {
			return getRecur(curr.left, key);
		}
		return getRecur(curr.right, key);
	}
	
	/*
	 * This function gets the set of keys in the TreeMap by
	 * calling a recursive function on the tree.
	 */
	public Set<K> keySet(){
		return keySetRecur(root);
	}
	
	/*
	 * This is a recursive function that gets the set of all
	 * the keys in the tree by taking the union of the set of
	 * a root node's key with the key sets of the left and right
	 * subtrees.
	 * @param curr is a Node.
	 * @returns a Set parameterized on K.
	 */
	private Set<K> keySetRecur(Node curr){
		Set<K> keys=new HashSet<K>();
		if (curr==null) {
			return keys;  // empty set
		}
		keys.add(curr.key);
		keys.addAll(keySetRecur(curr.left));  // union with left keyset
		keys.addAll(keySetRecur(curr.right));  // union with right keyset
		return keys;
	}
	
	/*
	 * This function inserts a new key-value pair into the TreeMap; if the key
	 * already existed in the TreeMap, it is overwritten and the old value
	 * associated with the key is returned. Otherwise, null is returned.
	 * @param key is of type K.
	 * @param value is of type V.
	 * @returns a value of type V.
	 */
	public V put(K key, V value) {
		V prev_value=get(key);
		root=putRecur(root, key, value);
		return prev_value;
	}
	
	/*
	 * This is a recursive function that inserts a new key-value pair into the
	 * tree. The function finds where the key ought to go, then creates a new Node
	 * there with the correct key and value.
	 * @param curr is a Node.
	 * @param key is of type K.
	 * @param value is of type V.
	 * @returns a Node.
	 */
	private Node putRecur(Node curr, K key, V value) {
		if (curr==null) {  // if we've gotten to an empty tree then there's nowhere else to go
			return new Node(key, value);  // insert Node here
		}
		if (compareKey(key, curr.key)==0) {  // key is equal to the current Node's key
			curr.value=value;  // replace value with new one
		}
		else if (compareKey(key, curr.key)<0) {
			curr.left=putRecur(curr.left, key, value);  // recurse left
		}
		else {
			curr.right=putRecur(curr.right, key, value);  // recurse right
		}
		return curr;
		
	}
	
	/*
	 * This function removes a key-value pair from the TreeMap by passing the tree to
	 * a recursive function. It also returns the value that was associated with the key, or
	 * null if the key is not in the TreeMap.
	 * @param key is of type K.
	 * 
	 */
	public V remove(K key) {
		V prev_value=get(key);
		root=removeRecur(root, key);
		return prev_value;
	}
	
	/*
	 * This is a recursive function that removes a key-value pair from the tree. If it finds the key, it
	 * does one of three things to alter the tree. If there's no right child, it replaces the Node with the left child.
	 * If there's no left child, it replaces the Node with the right child. If there is both a left and a right child,
	 * it finds the smallest key in the right subtree, removes it, and uses it and its value to replace the Node.
	 * @param curr is a Node.
	 * @param key is of type K.
	 * @returns a Node.
	 */
	private Node removeRecur(Node curr, K key) {
		if (curr==null) {  // nothing can be removed from an empty tree
			return curr;
		}
		if (compareKey(key, curr.key)==0) {  // found a Node with the right key
			if (curr.left==null) {
				return curr.right;  // replace with right child
			}
			if (curr.right==null) {
				return curr.left;  // replace with left child
			}
			Node node=minval(curr.right);  // smallest in right subtree
			curr.key=node.key;
			curr.value=node.value;
			curr.right=removeRecur(curr.right, curr.key);
		}
		else if (compareKey(key, curr.key)<0) {  // recurse left
			curr.left=removeRecur(curr.left, key);
		}
		else {  // recurse right
			curr.right=removeRecur(curr.right, key);
		}
		return curr;
	}
	
	/*
	 * This function finds the smallest key in a tree by recursing left until
	 * it hits the bottom of the tree, then returns the key-value pair as a Node.
	 * @param curr is a Node.
	 * @returns a Node.
	 */
	public Node minval(Node curr) {
		while (curr.left!=null) {
			curr=curr.left;
		}
		return new Node(curr.key, curr.value);
	}
	
	/*
	 * This function clears the TreeMap of all key-value pairs.
	 */
	public void clear() {
		root=null;
	}
	
	/*
	 * This function prints a graphical representation of the TreeMap by passing
	 * the tree to a recursive function.
	 */
	public void printTree() {
		printTreeRecur(root);
	}
	
	/*
	 * This is a recursive function that prints the keys of the tree with their 
	 * associated values in order by doing an in-order traversal of the tree.
	 * @param curr is a Node.
	 */
	private void printTreeRecur(Node curr) {
		if (curr!=null) {
			printTreeRecur(curr.left);
			System.out.println(curr.key+", "+curr.value);
			printTreeRecur(curr.right);
		}
	}
}
