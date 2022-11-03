# PROBLEM STATEMENT

A social media company is trying to monitor activity on their site by analyzing the number of tweets that occur in select periods of time. These periods can be partitioned into smaller time chunks based on a certain frequency (every minute, hour, or day).

For example, the period [10, 10000] (in seconds) would be partitioned into the following time chunks with these frequencies:

    Every minute (60-second chunks): [10,69], [70,129], [130,189], ..., [9970,10000]
    Every hour (3600-second chunks): [10,3609], [3610,7209], [7210,10000]
    Every day (86400-second chunks): [10,10000]

Notice that the last chunk may be shorter than the specified frequency's chunk size and will always end with the end time of the period (10000 in the above example).

Design and implement an API to help the company with their analysis.

Implement the TweetCounts class:

    TweetCounts() Initializes the TweetCounts object.
    void recordTweet(String tweetName, int time) Stores the tweetName at the recorded time (in seconds).
    List<Integer> getTweetCountsPerFrequency(String freq, String tweetName, int startTime, int endTime) Returns a list of integers representing the number of tweets with tweetName in each time chunk for the given period of time [startTime, endTime] (in seconds) and frequency freq.
        freq is one of "minute", "hour", or "day" representing a frequency of every minute, hour, or day respectively.


# EXAMPLE

Input
["TweetCounts","recordTweet","recordTweet","recordTweet","getTweetCountsPerFrequency","getTweetCountsPerFrequency","recordTweet","getTweetCountsPerFrequency"]
[[],["tweet3",0],["tweet3",60],["tweet3",10],["minute","tweet3",0,59],["minute","tweet3",0,60],["tweet3",120],["hour","tweet3",0,210]]

Output
[null,null,null,null,[2],[2,1],null,[4]]

Explanation
TweetCounts tweetCounts = new TweetCounts();
tweetCounts.recordTweet("tweet3", 0);                              // New tweet "tweet3" at time 0
tweetCounts.recordTweet("tweet3", 60);                             // New tweet "tweet3" at time 60
tweetCounts.recordTweet("tweet3", 10);                             // New tweet "tweet3" at time 10
tweetCounts.getTweetCountsPerFrequency("minute", "tweet3", 0, 59); // return [2]; chunk [0,59] had 2 tweets
tweetCounts.getTweetCountsPerFrequency("minute", "tweet3", 0, 60); // return [2,1]; chunk [0,59] had 2 tweets, chunk [60,60] had 1 tweet
tweetCounts.recordTweet("tweet3", 120);                            // New tweet "tweet3" at time 120
tweetCounts.getTweetCountsPerFrequency("hour", "tweet3", 0, 210);  // return [4]; chunk [0,210] had 4 tweets

# SORTED LIST + BINARY SEARCH APPRAOCH

First, we want a way to keep track of the time values at which each tweet happened. The best way is for each tweet, we can keep a list of time values. So, we will use a map where each key is the "tweet name" and each value is a "list of time values" for that tweet.

To use Binary Search, these time values need to be in a sorted order so to make sure as we insert the time values in the list they are automatically placed at their right position, we can use the "SortedList" container in Python. The complexity of an insertion operation is almost O(LogN) and it will place the item at its correct place to maintain the sorted order.

Next, we have to find a way to get the count of the particular tweet in a certain timeframe. And the twist is that this timeframe is further divided into chunks, based on the frequency string. The timeframe has startTime and endTime values which are in "seconds" but the "freq" can be "minute" or "hour" or even "day". So we have to divide this timeframe in chunks based on this "freq" value.

    e.g., If "freq" = "minute", then if we have a timeframe as [10, 100]
	Then it will be divided into chunks of 60 seconds that is - 
		[0, 59], [60, 100]
		
	The last chunk may or may not have exactly 60 seconds as it depends on timeframe.
	
	And now, for each chunk we need to find how many times a particular tweet happened.
	
	Since for each tweet, its time value list is sorted, we can use Binary Search here.
	
	We find the leftmost index of the time value that is >= start value of a chunk
	And then we find the rightmost index of the time value that is  <= end value of a chunk
	
	And the number of tweets is => rightmostIndex - leftmostIndex + 1
 


# GETTING BETTER SPACE COMPLEXITY FROM ABOVE APPROACH

Instead of creating a new list of chunks and then looping over that list, we can skip this process by simply running a loop same number of times as number of chunks and in each iteration, we first set the start and end values of a chunk and then we apply Binary Search to find the count.

In this way, there is no need to create a separate list of chunks and that will result in a better Space Complexity than the previous approach.