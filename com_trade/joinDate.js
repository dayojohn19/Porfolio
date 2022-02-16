
function processDate(rawDate){

    splitDate = rawDate.split('-')
    year = splitDate[0]
    day = splitDate[2]
    month = splitDate[1] - 1
    
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'June', 'July', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec']
    month = months[month]
    
    return month+' '+ day+','+' '+ year
}

console.log(processDate('2022-01-12'))