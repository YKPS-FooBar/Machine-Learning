package cn.davidma.practice;

import java.util.ArrayList;
import java.util.Collection;
import java.util.Iterator;
import java.util.List;

/**
 * Zis iz a vecta, it vecs tar.
 * 3e+5 times better than Thomas' vector because
 * this one is written in Java! Yay!
 * 
 * Normally this class should extend ArrayList (or at least Collection);
 * however, George said we cannot use any standard libraries.
 * 
 * @author David Ma
 */
public class Vector implements Iterable<Double> {
	
	private List<Double> vec;
	
	/**
	 * Constructs an empty vector.
	 */
	public Vector() {
		this.vec = new ArrayList<Double>();
	}
	
	/**
	 * Constructs an vector with a collection of doubles.
	 * 
	 * @param vec A collection of doubles.
	 */
	public Vector(Collection<Double> vec) {
		this.vec = new ArrayList<Double>(vec);
	}
	
	/**
	 * Because why not?
	 * 
	 * @param nums Numbers!
	 */
	public Vector(double... nums) {
		this();
		for (double i: nums) this.vec.add(i);
	}
	
	/**
	 * Copies a vector.
	 * 
	 * @param vec The vector to be copied.
	 */
	public Vector(Vector vec) {
		this();
		vec.forEach((Double i) -> this.vec.add(i));
	}
	
	/**
	 * Size of this vector.
	 * 
	 * @return The size of this vector.
	 */
	public int size() {
		return this.vec.size();
	}
	
	/**
	 * Errrg why can't I extend ArrayList!
	 * 
	 * @param index The index to get.
	 * @return The value of index.
	 */
	public double get(int index) {
		return this.vec.get(index);
	}
	
	public void set(int index, double value) {
		this.vec.set(index, value);
	}
	
	/**
	 * Sums the two vector.
	 * 
	 * @param other The other vector.
	 * @return this.
	 */
	public Vector add(Vector other) {
		for (int i = 0; i < other.size(); i++) {
			this.vec.set(i, this.vec.get(i) + other.get(i));
		}
		
		return this;
	}
	
	/**
	 * Scales the vector.
	 * 
	 * @param other The scale.
	 * @return this.
	 */
	public Vector scale(double scale) {
		for (int i = 0; i < this.vec.size(); i++) {
			this.vec.set(i, this.vec.get(i) * scale);
		}
		
		return this;
	}
	
	/**
	 * Not dot product.
	 * 
	 * @param other The other vector.
	 * @return this.
	 */
	public Vector mul(Vector other) {
		for (int i = 0; i < other.size(); i++) {
			this.vec.set(i, this.vec.get(i) * other.get(i));
		}
		
		return this;
	}
	
	/**
	 * Dot product.
	 * Does not edit the current vector.
	 * 
	 * @param other The other vector.
	 * @return The result.
	 */
	public int dot(Vector other) {
		int sum = 0;
		for (int i = 0; i < other.size(); i++) {
			sum += this.vec.get(i) * other.get(i);
		}
		
		return sum;
	}
	
	public static void main(String args[]) {
		Vector vector = new Vector(1,2,3);
		vector.scale(5);
		System.out.println(vector);
	}

	@Override
	public Iterator<Double> iterator() {
		return this.vec.iterator();
	}
	
	@Override
	public String toString() {
		String out = "";
		for (Double i: this.vec) {
			out += String.valueOf(i) + " ";
		}
		
		return out;
	}
}
