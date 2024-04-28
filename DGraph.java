/*
 * This program provides the code for an implementation of a weighted directed graph
 * using a 2D array. Each slot in the array contains the cost for moving from the node specified by
 * the row to the node specified by the column. The DGraph provides functionality for adding edges, finding the
 * minimum cost edge between two nodes, and getting the total cost of a given traversal. It also has methods for
 * three different algorithms to solve the Traveling Salesman Problem: a heuristic approach, a recursive backtracking
 * algorithm that explores every possible path, and my algorithm, which attempts to improve on the runtime of the
 * backtracking algorithm without sacrificing accuracy. 
 */

import java.util.List;
import java.util.ArrayList;

public class DGraph {
	private int nodes;
	private double[][] graph;
	
	/*
	 * This is a constructor that takes in the number of nodes in the graph as an argument
	 * and makes a 2D array of that height and width. It initializes the array to be filled
	 * with zeroes.
	 * @param nodes is an integer.
	 */
	public DGraph(int nodes) {
		this.nodes=nodes;
		graph=new double[nodes][nodes];
		for (int i=0; i<nodes; i++) {
			for (int j=0; j<nodes; j++) {
				graph[i][j]=0;
			}
		}
	}
	
	/*
	 * This function adds an edge to the graph by setting the appropriate
	 * slot to the weight/cost value.
	 * @param v1 is an integer.
	 * @param v2 is an integer.
	 * @param weight is a double.
	 */
	public void addEdge(int v1, int v2, double weight) {
		graph[v1][v2]=weight;
	}
	
	/*
	 * This function finds the node that it would take the lowest cost to get to from
	 * the current node, provided the result node hasn't yet been visited.
	 * @param v is an integer.
	 * @param visited is an array of booleans.
	 * @returns an integer.
	 */
	public int minEdge(int v, boolean[] visited) {
		double[] row=graph[v];  // all edges
		double min=Double.MAX_VALUE;  // initialize min to be greater than any other double
		int min_ind=0;
		for (int i=0; i<row.length; i++) {
			if (!visited[i]) {
				if (row[i]!=0&&row[i]<min) {  // doesn't lead back to the same node
					min=row[i];
					min_ind=i;
				}
			}
		}
		return min_ind;
	}
	
	/*
	 * This function finds a relatively low-cost traversal of the
	 * graph by using a heuristic algorithm: at every juncture, it takes
	 * the lowest cost path. It then returns the traversal as a list of the
	 * nodes in the order they're visited.
	 * @returns a list of integers.
	 */
	public List<Integer> heuristic(){
		List<Integer> traversal=new ArrayList<Integer>();
		boolean[] visited=new boolean[nodes];
		int curr=0;
		traversal.add(0);
		visited[0]=true;
		while (traversal.size()<nodes) {  // haven't made all choices yet
			curr=minEdge(curr, visited);  // move to next node
			traversal.add(curr);
			visited[curr]=true;
		}
		traversal.add(0);  // make full circuit
		return traversal;
	}
	
	/*
	 * This function makes use of a recursive helper function, backtrackRecurse, to find
	 * the lowest cost circuit of the graph. 
	 * @returns a list of integers.
	 */
	public List<Integer> backtrack() {
		boolean[] visited=new boolean[nodes];
		visited[0]=true;
		List<Integer> best_traversal=new ArrayList<Integer>();
		List<Integer> curr_traversal=new ArrayList<Integer>();
		curr_traversal.add(0);
		best_traversal=backtrackRecurse(visited, 0, curr_traversal, best_traversal);
		best_traversal.add(0);
		return best_traversal;
	}
	
	/*
	 * This function recursively finds the lowest cost circuit of the graph
	 * by exploring every possible path and checking to see if its cost is lower
	 * than that of the best circuit found so far.
	 * @param visited is an array of booleans.
	 * @param curr is an integer.
	 * @param curr_traversal is a list of integers.
	 * @param best_traversal is a list of integers.
	 */
	public List<Integer> backtrackRecurse (boolean[] visited, int curr, 
			List<Integer> curr_traversal, List<Integer> best_traversal) {
		if (curr_traversal.size()==nodes&&graph[curr][0]!=0.) {  // found a circuit
			double curr_cost=totalCost(curr_traversal)+graph[curr][0];  // cost of traversal, plus cost to get back to beginning
			double best_cost;
			if (best_traversal.isEmpty()) {  // haven't previously found a circuit; set best_cost to a baseline value
				best_cost=Double.MAX_VALUE;
			}
			else { // cost of traversal, plus cost to get back to beginning
				best_cost=totalCost(best_traversal)+graph[best_traversal.get(best_traversal.size()-1)][0];
			}
			if (curr_cost<best_cost) {  // update best_traversal
				best_traversal=new ArrayList<>(curr_traversal);
			}
			return best_traversal;
		}
		for (int i=0; i<nodes; i++) {  // try every adjacent node
			if (visited[i]==false&&graph[curr][i]!=0) {
				visited[i]=true;
				curr_traversal.add(i);
				best_traversal=backtrackRecurse(visited, i, curr_traversal, best_traversal);  // depth-first search
				visited[i]=false;  // undo after exploring so that algorithm can try a different path
				curr_traversal.remove(curr_traversal.size()-1);
			}
		}
		return best_traversal;
	}
	
	/*
	 * This function calls a recursive helper function, mineRecurse, to find the lowest
	 * cost circuit of the graph.
	 * @returns a list of integers.
	 */
	public List<Integer> mine() {
		boolean[] visited=new boolean[nodes];
		visited[0]=true;
		List<Integer> best_traversal=new ArrayList<Integer>();
		List<Integer> curr_traversal=new ArrayList<Integer>();
		curr_traversal.add(0);
		best_traversal=mineRecurse(visited, 0, curr_traversal, best_traversal);
		best_traversal.add(0);
		return best_traversal;
	}
	
	/*
	 * This function recursively finds the lowest cost circuit of the graph
	 * by using the algorithm described in the text for backtrackRecurse, except
	 * it preemptively stops exploring paths whose cost is already greater than the best
	 * cost.
	 * @param visited is an array of booleans.
	 * @param curr is an integer.
	 * @param curr_traversal is a list of integers.
	 * @param best_traversal is a list of integers.
	 */
	public List<Integer> mineRecurse (boolean[] visited, int curr, 
			List<Integer> curr_traversal, List<Integer> best_traversal) {
		double curr_cost=totalCost(curr_traversal);
		double best_cost;
		if (best_traversal.isEmpty()) {  // set best_cost to a baseline value if no circuit has been found yet
			best_cost=Double.MAX_VALUE;
		}
		else {  // best_cost, plus cost to get back to first node
			best_cost=totalCost(best_traversal)+graph[best_traversal.get(best_traversal.size()-1)][0];
		}
		if (curr_traversal.size()==nodes&&graph[curr][0]!=0.) {  // found a circuit
			if (curr_cost+graph[curr][0]<best_cost) {
				best_traversal=new ArrayList<>(curr_traversal);
			}
			return best_traversal;
		}
		for (int i=0; i<nodes; i++) {  // explore every path
			if (visited[i]==false&&graph[curr][i]!=0) {
				visited[i]=true;
				curr_traversal.add(i);
				if (curr_cost<=best_cost) {  // ensure curr_cost isn't already too high for the traversal to be a solution
					best_traversal=mineRecurse(visited, i, curr_traversal, best_traversal);
				}
				visited[i]=false;  // undo to explore a different path
				curr_traversal.remove(curr_traversal.size()-1);
			}
		}
		return best_traversal;
	}
	
	/*
	 * This function gets the cost of a given traversal.
	 * @param traversal is a list of integers.
	 * @returns a double.
	 */
	public double totalCost(List<Integer> traversal) {
		double total=0;
		for (int i=0; i<traversal.size()-1; i++) {  // only go to second-to-last
			total+=graph[traversal.get(i)][traversal.get(i+1)];  // get cost of edge between the pair of nodes
		}
		return total;
	}
}
