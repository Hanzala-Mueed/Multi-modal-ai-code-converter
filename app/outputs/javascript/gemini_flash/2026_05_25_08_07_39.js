// Function to perform a series of calculations
const calculate = (iterations, param1, param2) => {
    let result = 1.0; // Initialize result as a floating-point number
    // Loop from 1 up to and including the specified number of iterations
    for (let i = 1; i <= iterations; i++) {
        // Calculate intermediate value j
        let j = i * param1 - param2;
        // Subtract 1/j from result
        result -= (1 / j);

        // Recalculate j with a different sign for param2
        j = i * param1 + param2;
        // Add 1/j to result
        result += (1 / j);
    }
    return result;
};

// Record the start time using performance.now() for high-resolution timing
// performance.now() returns time in milliseconds
const startTime = performance.now();

// Call the calculate function with specified parameters and multiply the result by 4
// Numeric separators (e.g., 200_000_000) are supported in modern JavaScript (ES2021+)
const finalResult = calculate(200_000_000, 4, 1) * 4;

// Record the end time
const endTime = performance.now();

// Log the final result, formatted to 12 decimal places
console.log(`Result: ${finalResult.toFixed(12)}`);

// Calculate the execution time in seconds and log it, formatted to 6 decimal places
// Convert milliseconds to seconds by dividing by 1000
console.log(`Execution Time: ${((endTime - startTime) / 1000).toFixed(6)} seconds`);