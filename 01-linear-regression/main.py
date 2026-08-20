sizes = [1, 2, 3, 4]
prices = [3, 5, 7, 9]

weight = 1
bias = 0

def predict(size, weight, bias):
    return weight * size + bias

assert predict(80, 2500, 10000) == 210000

def calculate_error(prediction, actual):
    return prediction - actual

assert calculate_error(210000, 190000) == 20000

def calculate_mse(sizes, prices, weight, bias):
    total_loss = 0

    for size, actual_price in zip(sizes, prices):
        prediction = predict(size, weight, bias)
        error = calculate_error(prediction, actual_price)

        loss = error ** 2

        print("---")
        print (f"p {prediction}")
        print (f"e: {error}")
        print (f"l: {loss}")
        total_loss += loss

    return total_loss / len(sizes)

assert calculate_mse([80], [1900000], 2500, 10000) == 2856100000000.0

def weight_gradient(sizes, prices, weight, bias):
    total_gradient = 0

    for size, actual_price in zip(sizes, prices):
        prediction = predict(size, weight, bias)
        error = calculate_error(prediction, actual_price)

        gradient = 2 * error * size

        total_gradient += gradient

    print("---")
    print (f"total weight gradient: {total_gradient}")

    return total_gradient / len(sizes)

assert weight_gradient([80], [190000], 2500, 10000) == 3200000.0

def bias_gradient(sizes, prices, weight, bias):
    total_gradient = 0

    for size, actual_price in zip(sizes, prices):
        prediction = predict(size, weight, bias)
        error = calculate_error(prediction, actual_price)

        gradient = 2 * error

        total_gradient += gradient

    print("---")
    print (f"total bias gradient: {total_gradient}")

    return total_gradient / len(sizes)

assert bias_gradient([80], [190000], 2500, 10000) == 40000.0

def learn(sizes, prices, weight, bias):
    learning_rate = 0.01
    mse = calculate_mse(sizes, prices, weight, bias)
    i = 1
    print(f"mse: {mse}")
    while mse > 0.0001:
        wg = weight_gradient(sizes, prices, weight, bias)
        bg = bias_gradient(sizes, prices, weight, bias)
        weight -= learning_rate * wg
        bias -= learning_rate * bg
        mse = calculate_mse(sizes, prices, weight, bias)
        print(f"weight: {weight}")
        print(f"bias: {bias}")
        print(f"mse: {mse}")
        i += 1
        print(f"i: {i}")

    return weight, bias

weight, bias = learn(sizes, prices, weight, bias)

print(predict (1, weight, bias))
print(predict (5, weight, bias))