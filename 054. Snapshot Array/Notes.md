# PROBLEM STATEMENT

Implement a SnapshotArray that supports the following interface:

    1. SnapshotArray(int length) initializes an array-like data structure with the given length. Initially, each element equals 0.
    2. void set(index, val) sets the element at the given index to be equal to val.
    3. int snap() takes a snapshot of the array and returns the snap_id: the total number of times we called snap() minus 1.
    4. int get(index, snap_id) returns the value at the given index, at the time we took the snapshot with the given snap_id

# APPROACH

If we use a map and at each snap, we try to set the key as "snap" and value as the current array (We have to copy it). Then it will fail for large test cases due to huge memory usage. So that won't work.

What we want is, whenever we set a new value at any index, we want to still keep the old value(s). And so, what we can do is, at each index in the list, we not only have the value, but a list of pairs. Each pair is like -> (snap_id, value). 

Suppose the list has length = 3. In that case, it will be initialized as - 

		[[(-1,0)], [(-1,0)], [(-1,0)] ]
		
		So, each index has -> [(-1,0)]
		
We also initialize snapId to be 0.

And now, as we set a value, instead of changing the value in list, we simply append another pair. For example, if we now set value at index = 0 as 5. The pair (snap_id, value) will be like (0,5)

And this needs to be appended in the list at first index. So now, our list becomes ->
	
	[[(-1,0), (0,5)], [(-1,0)], [(-1,0)] ]
	
And now if we call get(), we just need to find the rightmost value that has snap_id <= snap_id passed in the get() method. For that, we can use Binary Search since the list is autoamatically sorted based on the snap_id.

	If you are wondering why we are looking for "rightmost" value in list.

	Suppose we call set() multiple times before we even call snap(). 
	
	Initially -> [[(-1,0)], [(-1,0)], [(-1,0)] ]
	
	Now, lets say we call -> 
		
			set(0, 5)
			set(0,6)
			set(0,10)
			
	Now, our list will be like -> [[(-1,0), (0,5), (0,6), (0,10)], [(-1,0)], [(-1,0)]]
	
	So now if we call get() and we want value at index 0 at snap_id 0, then we have to return 10.
	
	Because that was the most recent value to be inserted with snap_id as 0.
	
And that's why we want the rightmost value in the list.

Another thing is that, it is also possible that when we call get(), then whatever snap_id is passed, that is not at all present in any latest pair. Let me explain.

	So far, our list is like -> [[(-1,0), (0,5), (0,6), (0,10)], [(-1,0)], [(-1,0)]]
	
	Now if snap() is called, then we will increment snap_id to 1. 
	
	Now suppose snap() is called again. Then, snap_id becomes 2.
	
	And now, suppose get() is called with snap_id = 2 and index = 0.
	
	It means, at index = 0, what was the value when snap_id was 2?
	
Ofcourse we do not have any entry in the list with snap_id = 2. But that means, at snap_id = 2, the list at first index looked the same as it did at snap_id = 1 and snap_id = 0. And so, the value in the rightmost pair in the list where snap_id is <= the snap_id passed in get() is what we are looking for.