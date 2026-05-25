// Function to perform the calculation
const calculate = (iterations, param1, param2) => {
    let result = 1.0; // Initialize result as a float
    for (let i = 1; i <= iterations; i++) {
        // Calculate j for subtraction
        let jSub = i * param1 - param2;
        result -= (1 / jSub);

        // Calculate j for addition
        let jAdd = i * param1 + param2;
        result += (1 / jAdd);
    }
    return result;
};

// Record the start time using high-resolution timer
const startTime = performance.now();

// Define parameters for the calculation
const iterations = 200000000;
const param1 = 4;
const param2 = 1;

// Perform the calculation
const calculatedResult = calculate(iterations, param1, param2) * 4;

// Record the end time
const endTime = performance.now();

// Calculate execution time in seconds
const executionTimeSeconds = (endTime - startTime) / 1000;

// Print the result and execution time using template literals and toFixed for formatting
console.log(`Result: ${calculatedResult.toFixed(12)}`);
console.log(`Execution Time: ${executionTimeSeconds.toFixed(6)} seconds`);