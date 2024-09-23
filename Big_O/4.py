# What is the Big O of the below function? (Hint, you may want to go line by line)
def anotherFunChallenge(input):
    a = 5  # O(1)
    b = 10  # O(1)
    c = 50  # O(1)

    for i in range(input):  # O(n)
        x = i + 1  # O(n)
        y = i + 2  # O(n)
        z = i + 3  # O(n)

    for j in range(input):  # O(n)
        p = j * 2  # O(n)
        q = j * 2  # O(n)

    who_am_I = "I don't know"  # O(1)

    # Guess it is O(N)
    # 1 + 1 + 1 + N + N + N + N + N + N + N + 1 = 4 + 7N >> O(N)