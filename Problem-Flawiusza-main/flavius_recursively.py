def flavius_recursively(n,k):
    if n==1:
        return 0
    else:
        return (flavius_recursively(n - 1, k) + k)%n +1