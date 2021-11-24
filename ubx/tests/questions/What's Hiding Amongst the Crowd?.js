// A word is on the loose and now has tried to hide amongst a crowd of tall letters! Help write a function to detect what the word is, knowing the following rules:


var character = 'bAa';
arr = character.split('');
arr.forEach(element => {
 if (element.match(/[^abc]/gi)){
     console.log('yes')
 }

});
console.log(arr);
if (character == character.toUpperCase()) {
    console.log('lower')

} else {
    console.log('high')
}
