# Data Engineer Challenge

Thank you for your interest in a position at Flixbus.

You are asked to complete the following task so that we can assess your
programming skills. We estimate ca. 1-2 hours time to complete the task.

## Task
Implement and deploy an API that calculates the n-th Fibonacci number for a
given input number n. As a reminder, the Fibonacci sequence starts with [1, 1]
and then every element is sum of the two previous ones (that is, [1, 1, 2, 3,
5, 8, 13, ...]).

You can use any library or framework that you like, and you are only required
to implement the backend. If you use an implementation of the Fibonacci 
sequence from the internet, please indicate the source.

Your API should accept a GET request with a single integer *n* as a parameter,
and respond with the Fibonacci number *F(n)* corresponding to that integer.

Examples:
```bash
$ curl http://127.0.0.1:5000/1
1
$ curl http://127.0.0.1:5000/3
2
$ curl http://127.0.0.1:5000/7
13
```

The task is simple but the code should be "production ready": add
documentation, tests, docstrings and whatever you think is needed for the user
to run it (e.g. files to build a Docker image, a Makefile, scripts to start the
server, uWSGI/Gunicorn/others).

## Assessment
Please think of your solution as a production-ready codebase. We will assess
functional correctness of your solution, quality and maintainability of your
code, and efficiency for large inputs (in decreasing order of importance).

## Notes
- Please implement the solution in Python.
- If you use additional packages, please provide a requirements.txt file.
- You can decide how the API should be called (e.g. with
`http://127.0.0.1:5000/1` or `http://127.0.0.1:5000/?n=1`). Please provide
instructions accordingly.
