# Compute the square difference between x and y.
Square.Difference <- function(x, y) {
    sum((x - y) ^ 2)
}

# Compute the coefficient of determination between x and y.
Coefficient.Of.Determination <- function(x, y) {
    m <- mean(x)
    sum((y - m) ^ 2) / sum((x - m) ^ 2)
}
