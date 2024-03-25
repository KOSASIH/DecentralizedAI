import math

def gradient_descent(x, y, theta, alpha, num_iterations):
    """
    Gradient Descent algorithm.

    Parameters
    ----------
    x : list
        List of input features.
    y : list
        List of target values.
    theta : list
        List of initialized parameters.
    alpha : float
        Learning rate.
    num_iterations : int
        Number of iterations to run the algorithm.

    Returns
    -------
    list
        List of optimized parameters.

    """
    x = np.insert(x, 0, 1)
    m = len(x)
    for i in range(num_iterations):
        hypothesis = np.dot(x, theta)
        loss = h - y
        gradient = np.dot(x.T, loss) / m
        theta = theta - alpha * gradient

    return theta

def newton_method(x, y, theta, num_iterations):
    """
    Newton Method algorithm.

    Parameters
    ----------
    x : list
        List of input features.
    y : list
        List of target values.
    theta : list
        List of initialized parameters.
    num_iterations : int
        Number of iterations to run the algorithm.

    Returns
    -------
    list
        List of optimized parameters.

    """
    x = np.insert(x, 0, 1)
    m = len(x)
    for i in range(num_iterations):
        hypothesis = np.dot(x, theta)
        error = hypothesis - y
        df = np.dot(x.T, error)
        H = np.dot(x.T, np.dot(np.diag(error), x))
        theta = theta - np.linalg.solve(H, df)

    return theta

if __name__ == "__main__":
    # Example usage
    x = np.array([[1], [2], [3], [4], [5]])
    y = np.array([2, 6, 8, 10, 12])
    theta = np.array([1, 0])

    print("Initial parameters:")
    print(theta)

    theta_gd = gradient_descent(x, y, theta, 0.5, 10000)
    print("\nOptimized parameters (gradient descent):")
    print(theta_gd)

    theta_nm = newton_method(x, y, theta, 100)
    print("\nOptimized parameters (Newton method):")
    print(theta_nm)
