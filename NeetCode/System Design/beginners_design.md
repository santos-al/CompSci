# NeetCode System Design for Beginners

## Background

### Computer Architecture  

Storage - or disk or storage
- Anything stored in disk is persisted. Meaning if the computer crashes, anything in the ssd is preserved.
- 1 Gb = 10^9 bytes in storage
- Byte - is a unit of digital information that commonly consists of 8 bits (either a 0 or 1). A byte is used to encode a single character of text. 

RAM - also know as memory. 
- Memory is measured in microseconds (1 second divided by a million). Reading and writing is a lot faster than from disk. 

CPU - is the brain of the computer
- I basically reads and writes information to RAM and Disk
- It can execute code
- CPUs also have a cache, typically MB in size. It helps speed up operations because they get completed in nanoseconds.

<img src="./screenshots/computer_architecture.png" alt="computer architecture" width="400px">

### Application Architecture

Prospective from a Dev

Dev -> Build & Deploy Code -> Server -> Storage

Vertical Scaling - e.g. Upgrading the server

Horizontal Scaling - e.g. Adding more servers
- If we have multiple requests coming into our server, how do we know which one to use?
  - Load Balancer - forwards the request to the server that has the least amount of traffic.
- Servers don't have to work in isolation, can communicate with other servers to handle other tasks.
  - E.g. Payments for an application would be handled by Stripe.

Logging - keeps track of everything happening in our code. Anything logged is time stamped
Metrics - keeps track of resources being used and if any part of the system is failing (e.g. a server is down). Can be visualized using graphs and charts.
- We can use logs to keep track of any requests that fail for users and then use metrics to make sense of that data collected form logs
- We can also have our metrics feed into an alert service, so that as a dev we can be notified if something is going wrong or if a metric has reached a specific threshold.

<img src="./screenshots/app_architecture.png" alt="app architecture" width="400px">

### Design Requirements

