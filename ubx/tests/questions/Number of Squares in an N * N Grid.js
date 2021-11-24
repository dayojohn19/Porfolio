// Create a function that calculates the number of different squares in an n * n square grid. 

// Geometric enumeration

function getSquare(n){
    x = (n * (n+1) * (2*n + 1))/6
    console.log(x)
    return x
}

getSquare(5)