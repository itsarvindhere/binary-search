# PROBLEM STATEMENT

You are implementing a program to use as your calendar. We can add a new event if adding the event will not cause a double booking.

A double booking happens when two events have some non-empty intersection (i.e., some moment is common to both events.).

The event can be represented as a pair of integers start and end that represents a booking on the half-open interval [start, end), the range of real numbers x such that start <= x < end.

Implement the MyCalendar class:

MyCalendar() Initializes the calendar object.
boolean book(int start, int end) Returns true if the event can be added to the calendar successfully without causing a double booking. Otherwise, return false and do not add the event to the calendar.

# **1. WITHOUT BINARY SEARCH**

	An event is not intersecting any other event if -

		The event starts after any other event ends 
						or 
		The event ends before any other event starts
		
And I used this condition to check if the current event can be booked or not.

I kept the start and end values for any event in a List of Tuples. Each Tuples has two values - start and end. 

And I can then loop over the list and compare the start and end values for any event with the start and end values for the current event that we want to check for.

# **2. USING BINARY SEARCH + SORTEDLIST**

To use Binary Search, we need to have the event values in sorted order. So I thought to use the SortedList container because as we insert values in it, they will be kept in sorted order. Insertion and Deletion is an approximately O(LogN) time operation in a SortedList.

And now, its time for some observations.

Suppose, our event list current has two events so in total we will have four values -> 2 start values and 2 end values.

		[10,20,25,30]
		
So instantly, just by looking at this list, we can say that Event 1 starts at 10 and Event 2 starts at 25. Because we know that start value is inserted before end value so it should always be at the even index.

This also means that if we have to insert any new event values in this list, then the start value for that event can only come at even indices (except some special cases).

	For example, if we get an event with start = 15 and end = 25

We will see that the start = 15 will go at index = 1 as we maintain sorted order. But 1 is an odd index. Which means 15 is intersecting with some previously booked event so it is not a valid event. 

So, how can we know without inserting an element where its position should be? Well, we can use Binary search. We can try to look for 15 in the list and as we keep incrementing or decrementing left and right pointers, eventually, after binary search ends, left pointer will point to the index at which "start" value should be inserted for a sorted order.

	Now, suppose, we want to insert an event with start = 21 and end = 24 in the list
	
	Is this a valid event? YES. because it is not intersecting any other event.
	
	For start = 21, we get the index as 2
	For end = 24, we get the index as 2 as well
	
	You might think that since start index is even, this is a valid event so that's the only criteria to check.
	
	
	But suppose if start = 21 and end = 26. Then what?
	
	In that case, for start = 21, index is still 2
	But for end = 26, it will be 3
	
	So this suggest that not only start index needs to be even, but both start and end indices also need to be the same
	
	
And this makes sense if you think about it. If we have a list - 

			[Start, End, Start, End]
			
	Then if an event has to be booked in between, that can only come between End and Start of any two events in the list.
	
	And since End and Start for any two events in list are adjacent, that means, ideal index of start and end should be same.
	
Other possibilites are - 

	1. If event to book starts and ends before any other event. That is, startIndex and endIndex are 0
	2. If event to book starts and ends after any other event. That is, startIndex and endIndex = length of list

These cases will be covered by the two conditions as well.

Hence, all that we need to check is  whether - 

	1. startIndex is even, AND
	2. startIndex == endIndex

If any of the two is not true, then we have an intersection.

# **3. USING BINARY SEARCH + SIMPLE LIST**

Not all online coding platforms may support SortedList so we can also use a simple list in place of that and use binary search to find the index to insert the value. Since list won't be sorted already, we have to explicitely sort it as well.
```
















