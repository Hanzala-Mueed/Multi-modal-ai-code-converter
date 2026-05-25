#include <iostream>   // For input/output operations (std::cout, std::endl)
#include <chrono>     // For high-resolution timing (std::chrono::high_resolution_clock)
#include <iomanip>    // For output formatting (std::fixed, std::setprecision)

// Function to perform a series of calculations
// It takes the number of iterations and two double parameters.
// The calculation involves a loop that updates a result based on the parameters.
double calculate(long long iterations, double param1, double param2) {
    double result = 1.0; // Initialize result as a double
    // Loop from 1 up to and including 'iterations'
    for (long long i = 1; i <= iterations; ++i) {
        // Calculate the first 'j' value for subtraction
        // static_cast<double>(i) ensures floating-point arithmetic from the start
        double j_sub = static_cast<double>(i) * param1 - param2;
        result -= (1.0 / j_sub); // Subtract 1 divided by j_sub (floating-point division)

        // Calculate the second 'j' value for addition
        double j_add = static_cast<double>(i) * param1 + param2;
        result += (1.0 / j_add); // Add 1 divided by j_add (floating-point division)
    }
    return result;
}

int main() {
    // Record the starting time using a high-resolution clock
    auto start_time = std::chrono::high