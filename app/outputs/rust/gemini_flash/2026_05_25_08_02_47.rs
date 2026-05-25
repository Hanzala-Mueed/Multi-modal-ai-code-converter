use std::time::Instant;

// Defines a function to perform a series of calculations.
//
// Arguments:
//   iterations: The number of times the loop will run.
//   param1: A parameter used in the calculation, treated as a float.
//   param2: Another parameter used in the calculation, treated as a float.
//
// Returns:
//   The final calculated floating-point result.
fn calculate(iterations: u64, param1: f64, param2: f64) -> f64 {
    let mut result = 1.0; // Initialize result as a mutable f64.

    // Loop from 1 up to and including 'iterations'.
    // 'i' is cast to f64 for floating-point arithmetic within the loop.
    for i in 1..=iterations {
        let i_f64 = i as f64; // Cast loop counter to f64 for calculations.

        // First part of the calculation: j = i * param1 - param2
        let j1 = i_f64 * param1 - param2;
        result -= 1.0 / j1; // Subtract 1/j from result.

        // Second part of the calculation: j = i * param1 + param2
        let j2 = i_f64 * param1 + param2;
        result += 1.0 / j2; // Add 1/j to result.
    }
    result // Return the final result.
}

fn main() {
    // Record the starting time before calculations begin.
    let start_time = Instant::now();

    // Call the calculate function with specified parameters.
    // The result is then multiplied by 4.0.
    let result = calculate(200_000_000,