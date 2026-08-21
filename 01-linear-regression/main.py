class LinearRegression:
    """A simple Linear Regression model built from scratch."""

    def __init__(
            self,
            learning_rate: float = 0.01,
            target_mse: float = 0.0001,
            max_epochs: int = 10000,
        ):
            self.learning_rate = learning_rate
            self.target_mse = target_mse
            self.max_epochs = max_epochs

            # Model parameters initialized to zero
            self.weight: float = 1.0
            self.bias: float = 0.0

            self._assert_equals(self.predict(1), 1.0)
            self._assert_equals(self._calculate_error(3, 2), 1.0)
            self._assert_equals(self._calculate_mse([1], [3]), 4.0)
            self._assert_equals(self._calculate_gradients([1], [3]), (-4.0, -4.0))
            self._assert_equals(self.fit([1], [3]), self)

    def _assert_equals(self, actual, expected):
        assert actual == expected, f"Expected {expected}, got {actual}"

    def predict(self, x: float) -> float:
        """Runs forward inference for a single input value: y = w*x + b"""
        return self.weight * x + self.bias

    def _calculate_error(self, prediction: float, actual: float) -> float:
        return prediction - actual

    def _calculate_mse(self, x: list[float], y: list[float]) -> float:
        """Internal helper to calculate Mean Squared Error loss."""
        total_loss = 0

        for xi, yi in zip(x, y):
            prediction = self.predict(xi)
            error = self._calculate_error(prediction, yi)

            loss = error ** 2

            total_loss += loss

        return total_loss / len(x)

    def _calculate_gradients(self, x: list[float], y: list[float])-> tuple[float, float]:
        total_dw = 0
        total_db = 0
        n = len(x)

        for xi, yi in zip(x, y):
            prediction = self.predict(xi)
            error = self._calculate_error(prediction, yi)

            weight_gradient = 2 * error * xi # ∂mse/∂weight, differentiate mse with respect to weight
            bias_gradient = 2 * error # ∂mse/∂bias, differentiate mse with respect to bias

            total_dw += weight_gradient
            total_db += bias_gradient

        average_weight_gradient = total_dw / n
        average_bias_gradient = total_db / n

        return average_weight_gradient, average_bias_gradient

    def fit(self, x: list[float], y: list[float]) -> "LinearRegression":
        """Trains the model using Gradient Descent. Returns self for method chaining."""
        for epoch in range(self.max_epochs):
            mse = self._calculate_mse(x, y)

            if mse <= self.target_mse:
                print(f"Converged at epoch {epoch} | Final MSE: {mse:.6f}")
                break

            dw, db = self._calculate_gradients(x, y)

            self.weight -= self.learning_rate * dw
            self.bias -= self.learning_rate * db

            # Every 500 epochs report
            if epoch % 500 == 0:
                print(f"Epoch {epoch:4d} | MSE: {mse:.6f} | Weight: {self.weight:.4f} | Bias: {self.bias:.4f}")

        return self

# =============================================================================
# Execution & Testing
# =============================================================================
if __name__ == "__main__":
    sizes = [1, 2, 3, 4]
    prices = [3, 5, 7, 9]

    # Instantiate and train model
    model = LinearRegression(learning_rate=0.01)
    model.fit(sizes, prices)

    # Predictions
    print("\n--- Final Model Parameters ---")
    print(f"Weight (slope): {model.weight:.4f}")
    print(f"Bias (intercept): {model.bias:.4f}")

    print("\n--- Model Predictions ---")
    print(f"Size 1 (Actual: 3.0) -> Predicted: {model.predict(1.0):.2f}")
    print(f"Size 5 (New House)   -> Predicted: {model.predict(5.0):.2f}")
