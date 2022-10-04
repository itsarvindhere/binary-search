# PROBLEM STATEMENT
You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

# BINARY SEARCH APPROACH

We know that if one version is bad, all versions after it are bad too. Similarly, if one version if good, all versions before it are good too. So why go through each and every version from 1 to n?

And since 1 to n is a sorted range, we make use of Binary Search.

If the mid version is not bad, that means, no version before it is bad hence there is no point of checking any version before mid.

Similarly, if mid version is bad, that means, either this version is the first bad version or any previous version is bad which is making all the versions after it bad. So there is no point to search on the right of mid if mid itself is bad.

As soon as we find that mid is bad version, it may or may not be the first bad version. So we continue our search and try to find the first bad version on the left of mid.