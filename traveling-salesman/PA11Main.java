import java.util.List;
import java.util.Scanner;
import java.io.File;
import java.io.FileNotFoundException;

public class PA11Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner file = null;
        try {
        	file = new Scanner(new File(args[0]));  // open file if it exists
        	} 
        catch (FileNotFoundException e) {
            e.printStackTrace();}   
		DGraph dg = createGraph(file);
		String command=args[1];
		if (command.equals("HEURISTIC")) {
			display(dg, "heuristic");
		}
		else if (command.equals("BACKTRACK")) {
			display(dg, "backtrack");
		}
		else if (command.equals("MINE")) {
			display(dg, "mine");
		}
		else if (command.equals("TIME")) {
			time(dg);
		}
	}
	
	/*
	 * This function makes a DGraph from the contents of a file in a specific format.
	 * The file might have comments preceded by the % character at the top; the line immediately
	 * after should specify the number of nodes in the graph. After that, each line should be formatted:
	 * node1 node2 cost. For instance: 3 7 12.1098.
	 * @param file is a Scanner object.
	 * @returns a DGraph.
	 */
    public static DGraph createGraph(Scanner file) 
    {
    	//---- read past comments
        String startLine = null;
        while (file.hasNextLine()) {
        	startLine = file.nextLine();
            if (!startLine.startsWith("%"))  // skip lines until Scanner gets to line without comment
                break;
        }
        
        //---- read the number of vertices and create a MyGraph
        String[] startLineSplit = startLine.split(" ");
        int numVertices = Integer.parseInt(startLineSplit[0]);  // first element will be number of nodes
        DGraph graph = new DGraph(numVertices);
        
        //---- read the edge info and add the edges to the graph
        while (file.hasNextLine()) {  // loop through the rest of the lines
            String[] s = file.nextLine().split("\\s+");  // split on any number of spaces
            graph.addEdge(Integer.parseInt(s[0])-1, Integer.parseInt(s[1])-1, Double.parseDouble(s[2]));
        }
        return graph;
    }	
    
    /*
     * This function handles the display for any of the three algorithms. It
     * takes the algorithm type as an algorithm, runs it, and then displays some information
     * about the cost and the traversal order.
     * @param dg is a DGraph.
     * @type is a String.
     */
	public static void display(DGraph dg, String type) {
		List<Integer> traversal;
		if (type.equals("heuristic")) {
			traversal=dg.heuristic();
		}
		else if(type.equals("backtrack")) {
			traversal=dg.backtrack();
		}
		else {  // "mine" is the only other supported algorithm
			traversal=dg.mine();
		}
		double cost=dg.totalCost(traversal);
		String disp="[";  // make list of traversed nodes
		for (int i=0; i<traversal.size()-2; i++) {  // leave off return to beginning
			disp+=(traversal.get(i)+1)+", "; // display uses 1-indexing, but DGraph uses 0-indexing internally
		}
		disp+=(traversal.get(traversal.size()-2)+1)+"]";  // don't add comma after last element
		System.out.println(String.format("cost = %.1f, visitOrder = ", cost)+disp);  // round to one decimal place
	}
	
	/*
	 * This function runs each algorithm and shows the cost of the solution it found, as well
	 * as how long it took to run.
	 * @param dg is a DGraph.
	 */
	public static void time(DGraph dg) {
		long start=System.currentTimeMillis();  // heuristic
		double cost=dg.totalCost(dg.heuristic());
		long end=System.currentTimeMillis();
		System.out.println("heuristic: cost = "+cost+", "+(end-start)+" milliseconds");
		
		start=System.currentTimeMillis();  // my algorithm
		cost=dg.totalCost(dg.mine());
		end=System.currentTimeMillis();
		System.out.println("mine: cost = "+cost+", "+(end-start)+" milliseconds");
		
		start=System.currentTimeMillis();  // backtracking
		cost=dg.totalCost(dg.backtrack());
		end=System.currentTimeMillis();
		System.out.println("backtrack: cost = "+cost+", "+(end-start)+" milliseconds");
	}

}
