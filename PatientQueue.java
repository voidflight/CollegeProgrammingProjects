/*
 * Purpose: This program provides the code for a heap implementation of a priority queue.
 * This particular priority queue contains Patients, objects that represent the patients
 * in line at a hospital. Different patients have different priorities - represented as
 * integers - associated with them, and the patient with the highest priority (lowest integer)
 * is dequeued first, regardless of when they entered the line. The PatientQueue also
 * provides methods to do things like get information about the highest priority patient
 * without dequeueing them, changing a patient's priority, or finding out how many
 * patients are currently in the queue. 
 */

public class PatientQueue {
	private Patient array[];
    private int size;
    private static final int CAPACITY = 10;
    
    /*
     * This is a constructor that creates an empty array that represents the heap
     * to hold the patients and initializes the size to zero.
     */
    public PatientQueue() {
    	array=new Patient[CAPACITY];
    	size=0;
    }
    
    /*
     * This function creates a new Patient object with a given name and
     * priority and adds it to the queue. It does this by passing the 
     * Patient object to the other enqueue() method.
     * @param name is a String.
     * @param priority is an int.
     */
    public void enqueue(String name, int priority) {
    	Patient patient=new Patient(name, priority);
    	enqueue(patient);
    }
    
    /*
     * This function adds a Patient object to the queue. It is placed at the bottom
     * of the heap, or last slot in the array, and is then swapped upwards along
     * the levels of the heap if necessary.
     * @param patient is a Patient.
     */
    public void enqueue(Patient patient) {
    	if (size+1>=array.length)  // if capacity reached, expand array
            resize(2*array.length); 
        array[size+1]=patient;
        size++;
        bubbleUp(size);
    }
    
    
    /* This function removes the highest priority Patient from the queue, or
     * throws an exception if the queue is empty. After the Patient is removed,
     * the element in the last slot of the array is placed at the top and then
     * swapped downwards along the levels of the heap if necessary.
     * @returns a String.
     */
    public String dequeue() throws Exception  {
    	if (!isEmpty()) {
    		Patient patient=array[1];
        	array[1]=array[size];  // put last element in first slot
        	size--;
        	bubbleDown(1);
        	return patient.name;
    	}
    	throw new Exception();
    }
    
    /*
     * This function gets the name of the highest priority Patient in the queue,
     * or throws an exception if the queue is empty.
     * @returns a String.
     */
    public String peek() throws Exception {
    	if (!isEmpty()) {
    		return array[1].name;
    	}
    	throw new Exception();
    }
    
    /*
     * This function gets the priority value of the highest priority Patient in the
     * queue, or throws an exception if the queue is empty.
     * @returns an int.
     */
    public int peekPriority() throws Exception {
    	if (!isEmpty()) {
    		return array[1].priority;
    	}
    	throw new Exception();
    }
    
    /*
     * This function changes the priority of the first Patient in the array
     * with a name matching the one given and the changes the location of the
     * Patient in the array according to their new priority.
     * @param name is a String.
     * @param newPriority is an int.
     */
    public void changePriority(String name, int newPriority) {
    	for (int i=1; i<size+1; i++) {
    		if (array[i].name.equals(name)) {
    			array[i].priority=newPriority;
    			if (i!=1&&isFirst(i, (int) i/2)) {  // not at top and higher priority than parent
    				bubbleUp(i);
    			}
    			else {
    				bubbleDown(i);
    			}
    			break;  // only change first instance
    		}
    	}
    }
    
    /*
     * This function determines whether the PatientQueue is empty.
     * @returns a boolean.
     */
    public boolean isEmpty() {
    	return size==0;
    }
    
    /*
     * This function returns the size of the PatientQueue.
     * @returns an int.
     */
    public int size() {
    	return size;
    }
    
    /*
     * This function empties out the PatientQueue.
     */
    public void clear() {
    	array=new Patient[CAPACITY];
    	size=0;
    }
    
    /*
     * This function returns a String representation of the PatientQueue,
     * where each Patient's name and priority are listed in the order they
     * appear in the array.
     * @returns a String.
     */
    public String toString() {
    	String disp="{";
    	for (int i=1; i<size; i++) {  // add comma and space after each element but the last
    		Patient patient=array[i];
    		disp+=patient.name+" ("+patient.priority+"), ";
    	}
    	if (size>0) {
    		disp+=array[size].name+" ("+array[size].priority+")";
    	}
    	disp+="}";
    	return disp;
    }
    
    /*
     * This function determines whether the Patient at the first given index
     * has a higher priority than the Patient at the second given index.
     * @param i is an int.
     * @param j is an int.
     * @returns a boolean.
     */
    private boolean isFirst(int i, int j) {
    	Patient p1=array[i];
    	Patient p2=array[j];
    	if (p1.priority<p2.priority) {
    		return true;
    	}
    	else {
    		if (p1.priority==p2.priority) {  // tie-breaker
    			if (p1.name.compareTo(p2.name)<0) {  // p1 name comes first alphabetically
    				return true;
    			}
    			return false;
    		}
    		return false;
    	}
    }
    
    /*
     * This function is recursive; it is used to swap a Patient upwards
     * across the levels of the heap until it is in an appropriate position
     * given its priority.
     * @param index is an int.
     */
    private void bubbleUp(int index) {
    	if (index==1) { // already at top
    		return;
    	}
    	Patient patient=array[index];
    	Patient parent=array[(int) index/2];  // parent index
    	if (isFirst(index, index/2)) {
    		array[index]=parent;  // swap
    		array[(int) index/2]=patient;
    		bubbleUp((int) index/2);  // recursive call using new index
    	}
    }
    
    /*
     * This function is recursive; it is used to swap a Patient downwards
     * across the levels of the heap until it is in an appropriate position
     * given its priority.
     * @param index is an int.
     */
    private void bubbleDown(int index) {
    	if (index*2>size) {  // no children in heap
    		return;
    	}
    	Patient patient=array[index];
    	int child_index=index*2;  // left child index
    	Patient child=array[child_index];
    	if (index*2+1<=size) {  // if right child exists
    		Patient right=array[index*2+1];
    		if (isFirst(index*2+1, index*2)) {  // set child to higher priority between left and right
    			child=right;
    			child_index=index*2+1;
    		}
    	}
    	if (isFirst(child_index, index)) {
    		array[child_index]=patient;  // swap
    		array[index]=child;
    		bubbleDown(child_index);  // recursive call using new index
    	}
    }
    
    /*
     * This function resizes the array. It is generally used to increase the
     * capacity when the array gets filled.
     * @param capacity is an int.
     */
    private void resize(int capacity) {
        Patient temp[] = new Patient[capacity];  // temp array with new capacity
        size=capacity<size ? capacity:size;  // smaller of the two
        for (int i=0; i<size+1; i++) 
            temp[i]=array[i];
        array=temp;
    }
}
