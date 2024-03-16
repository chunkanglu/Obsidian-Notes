# What is Denormalization
Reversing the normal forms, and introducing back redundant data.
# Why
While normalizing is usually good for removing redundancy, sometimes it may be more beneficial to have the data denormalized if a certain query is used a lot and doing so would require less JOINS than the normalized version therefore increasing performance.