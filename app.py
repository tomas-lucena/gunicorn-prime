from flask import Flask

def is_prime(number):
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True

app = Flask(__name__)

@app.route("/<int:n_range>")
def hello_world(n_range):
    
    primes = list()
    for i in range(n_range):
        if not is_prime(i):
            continue
        
        primes += [i]

    return f"{len(primes)}\n"