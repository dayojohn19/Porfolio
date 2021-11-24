function bitwiseAND(n1, n2) {
	result = n1 & n2;
    return result
}

function bitwiseOR(n1, n2) {
		result = n1 | n2;
    return result
}

function bitwiseXOR(n1, n2) {
		result = n1 ^ n2;
    return result
}

// ➞ 00000110

console.log(bitwiseAND(7, 12) )
console.log(bitwiseOR(7, 12) )
console.log(bitwiseXOR(7, 12) )