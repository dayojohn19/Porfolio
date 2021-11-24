process.stdin.resume();
process.stdin.setEncoding("utf-8");
var stdin_input = "";
 
process.stdin.on("data", function (input) {
    stdin_input += input;                               // Reading input from STDIN
});
 
process.stdin.on("end", function () {
   main(stdin_input);
});
 
function main(input) {
    myfunction(input);
           // Writing output to STDOUT
}
 
// Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
 
// Write your code here
const myfunction = (data) =>
{
    const inputs = data.split("\n");
    
    if((inputs[0]>=0 && inputs[0]<=10 && !isNaN(inputs[0])) && (inputs[1].length>=1 && inputs[1].length<=15))
    {
        console.log(2*inputs[0]);
        console.log(inputs[1]);
    }
}