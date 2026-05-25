#include <iostream> // Required for input/output operations (std::cout, std::endl)
#include <chrono>   // Required for high-resolution timing (std::chrono::high_resolution_clock)
#include <iomanip>  // Required for output formatting (std::fixed, std::setprecision)

// Function to perform the calculation
// Uses double for floating-point precision, matching Python's default float behavior.
// The 'iterations' parameter is an int, as 200,000,000 fits within a standard 32-bit integer.
double calculate(int iterations, double param1, double param2) {
    double result = 1.0;
    // Loop from 1 up to and including 'iterations'
    for (int i = 1; i <= iterations; ++i) {
        // Cast 'i' to double to ensure floating-point arithmetic throughout the calculation
        double current_i = static_cast<double>(i);

        // Calculate the first 'j' value and subtract its reciprocal from the result
        double j_minus = current_i * param1 - param2;
        // Ensure 1.0 is used for floating-point division
        result -= (1.0 / j_minus);

        // Calculate the second 'j' value and add its reciprocal to the result
        double j_plus = current_i * param1 + param2;
        // Ensure 1.0 is used for floating-point division
        result += (1.0 / j_plus);
    }
    return result;
}

int main() {
    // Define the parameters for the calculation
    // Using digit separators (C++14 feature) for readability of large numbers
    int iterations = 200'000'000;
    double param1 = 4.0;
    double param2 = 1.0;

    // Record the start time using a high-resolution clock
    auto start_time = std::chrono::high_resolution_clock::now();

    // Call the calculate function and multiply the result by 4.0
    double result = calculate(iterations, param1, param2) * 4.0;

    // Record the end time
    auto end_time = std::chrono::high_resolution_clock::now();

    // Calculate the duration of the execution
    // std::chrono::duration<double> automatically converts to seconds as a double
    std::chrono::duration<double> duration = end_