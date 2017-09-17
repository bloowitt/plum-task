# plum-task
Technical test API app for a selection process.

Also, thoughts on it

1. How would your design change if the data was not static (i.e updated frequently
during the day)?
There are various options:
1) Use a proper database of any kind and start querying that database. This has the disadvantage of not having everything in memory every time, which incurs in runtime penalties.
2) Have some kind of push mechanism to inform the running instance it needs to reload data. 
3) Just kill the instance and reload. If you are running more than one instance (as per the answer to 2), then it becomes a matter of orchestration and not of code. The worst case scenario is some users getting old data for an unspecified amount of time. 

2. Do you think your design can handle 1000 concurrent requests per second? If not, what
would you change?

As a single instance, nope, because the time to attend each request is longer than 1ms, and Python has the GIL. You could do it by using Twister or some other concurrency library or taking care of threads, or by throwing more machines into the mix. It's a read only app, so you can have a virtually infinite pool of dynos taking care of it. 

------

I favour the option of running several instances of the app and orchestrating their reboots as a solution for both cases.