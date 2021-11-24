// Create a regular expression to match all red flag and blue flag in a string. You must use | in your expression. Flags can come in any order.

const REGEXP = /blue|red/gi;

a =  "flag red ".match(REGEXP)  // red
b = "blue flag".match(REGEXP)
console.log(a);
console.log(b);  // blue

// Matches "blue" in "blue flag" and "red" in "red flag".