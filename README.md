# Fetch Rewards Machine Learning Assessment
GitHub repo for Fetch Rewards Machine Learning Assessment submission, dated April 6th, 2022.

Instructions to run the program:

1. Make sure you have Docker installed on your system (instructions can be found [here](https://docs.docker.com/get-docker/).)
2. Run the following command inside Terminal/PowerShell:

```commandline
docker run --publish 8000:5000 tanmaydubey/fetch-rewards-assessment
```

This will start the web service, listening at `localhost:8000`.

3. The following is the syntax for the request payload:
```python
{ 
    'image_dimensions': (x,y),
    'corners': [(a0,a1),(b0,b1),(c0,c1),(d0,d1)]
}
```
Here, `(x,y)` is a tuple of two positive integers, while `(a0,a1)...(d0,d1)` are all tuples of two numbers (`float` or `int`).

4. Send a POST request with the payload as described above, to the endpoint `127.0.0.1:8000`. The response will be a string representing the pixel co-ordinate grid, as specified in the problem.

In case of any questions, please feel free to reach out to me at tanmaydubey at gmail.com. Thank you so much for considering my application!