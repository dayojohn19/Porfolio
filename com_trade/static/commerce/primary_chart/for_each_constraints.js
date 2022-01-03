buy_position    = 0;
buy_value       = 0;
sell_value      = 0;
sell_position   = 0;
third_constraints   =0
black_position  =0;
test_cases      = [];
markers         =[];

function Constraint_series(time, side, value) {
    if (side == 'buy'){
        markers.push({
            time    :time,
            position    :'aboveBar',
            color   :'green',
            shape   :'circle'
        });
        buy_position +=1;
        buy_value += value;
    }
    if  (side == 'sell'){
        markers.push({
            time    :time,
            position    :'belowBar',
            color   :'red',
            shape   :'circle'
        });      
        sell_position +=1;
        sell_value += value;
    }
    black_position +=1;
}

function get_Average_Ratio(test_cases){
    if (test_cases.length >=450){ //algo_adjust test_case
        test_cases.shift()
    }
    case_highest_position = Math.max.apply(Math, test_cases.map(function(o) { return o.position }))
    case_highest_position_index = test_cases.find(e=>e.position == case_highest_position)

    case_lowest_position = Math.min.apply(Math, test_cases.map(function(o) { return o.position }))
    case_lowest_position_index = test_cases.find(e=>e.position == case_lowest_position)
    
    case_highest_ratio  = Math.max.apply(Math, test_cases.map(function(o) { return o.ratio }))
    case_highest_ratio_index = test_cases.find(e=>e.ratio == case_highest_ratio)

    case_lowest_ratio   =  Math.min.apply(Math, test_cases.map(function(o) { return o.ratio }))
    case_lowest_ratio_index = test_cases.find(e=>e.ratio == case_lowest_ratio)

    // console.log('Index: ',case_highest_position_index)
    max_average=    parseFloat(case_highest_position_index.ratio) * 1.0020376 ;//1.0037 // algo_adjust ratio //BOOSTS SELL
    min_average=    parseFloat(case_highest_position_index.ratio) * 0.996590  ;// 9963 // algo_adjust ratio //BOOSTS BUY
    // console.log('Max Average: ',max_average)
    // console.log('Min Average: ', min_average)
}

function for_Each_Constraints(trade,close,open,base,line, time){
    
    testcase=0;
    // console.log('for Each Starting');
    arr = [trade,close,open,base,line]
        for (i1  =0; i1 <=arr.length-1;  i1++){
            for (i2 =0; i2  <=arr.length-1;   i2++){
                for (i3 =0; i3  <=arr.length-1;   i3++){
                    for (i4=0;  i4  <=arr.length-1;   i4++){
                        for (i5=0;  i5  <=arr.length-1;   i5++){
                            // ---- ------ CONSTRAINTS  --------    -------
                            // if (arr[i1] < arr[i2] && arr[i2] < arr[i3] && arr[i3] < arr[i4] && arr[i4] < arr[i5]){ // algo adjust greater or less than
                                //CHANGE ITS VALUE
                                // console.log('First Constraint ')

                                if (current = test_cases.find(e=>e.case == testcase)){
                                    current.position ++;
                                    current.value += line;
                                    current.ratio = parseFloat(current.value) /   parseFloat(current.position)
                                    // current.ratio = (parseFloat(current.value) * 96000) /   parseFloat(current.position)
                                    get_Average_Ratio(test_cases)
                                    if (current.ratio > max_average){
                                        // Constraint_series(time, 'sell')
                                        side = 'sell';
                                        Constraint_series(time,side,line)
                                    }
                                    if (current.ratio < min_average){
                                        side = 'buy';
                                        // Constraint_series(time, 'buy')
                                        Constraint_series(time,side,line)
                                    }
                                    
                                    // current.ratio = parseFloat(current.value) */ parseFloat(current.position)
                                    // current.ratio = (parseFloat(current.value) * 96000 ) / parseFloat(current.position)
                                    current.ratio = parseFloat(current.value) /   parseFloat(current.position)
                                    // console.log('first: ',current.case,   current.value)
                                } else {
                                    new_case = {
                                        case    :testcase,
                                        position    :1,
                                        value   :line,
                                        // ratio   :(parseFloat(line)* 96000) / parseFloat(1)
                                        ratio : line
                                    }
                                    test_cases.push(new_case)
                                    // console.log('done UPDATING' )
                                }
                                // console.log('TestCase: ',testcase)

                            // }
                            if (arr[i1] > arr[i2] && arr[i2] > arr[i3] && arr[i3] < arr[i4] && arr[i4] < arr[i5]) { // algo_adjust greater or less than
                                // console.log('Second Constraint ')

                                //CHANGE ITS VALUE
                                if (current = test_cases.find(e=>e.case == testcase)){
                                    current.position ++;
                                    current.value += line;
                                    current.ratio = parseFloat(current.value) /   parseFloat(current.position)
                                    // current.ratio = (parseFloat(current.value) * 96000) /   parseFloat(current.position)    //algo_adjust 96000
                                    get_Average_Ratio(test_cases)
                                    if (current.ratio > max_average){
                                        // Constraint_series(time, 'sell')
                                        side = 'sell';
                                        Constraint_series(time,side,line)
                                    }
                                    if (current.ratio < min_average){
                                        side = 'buy';
                                        // Constraint_series(time, 'buy')
                                        Constraint_series(time,side,line)
                                    }
                                    // console.log(current.value)
                                    // console.log('second: ',current.case,   current.value)
                                } else {
                                    new_case = {
                                        case    :testcase,
                                        position    :1,
                                        value   :line,
                                        // ratio   : (parseFloat(line)* 96000) / parseFloat(1)//algo_adjust 96000
                                        ratio   :line
                                    }
                                    test_cases.push(new_case)
                                    console.log('done UPDATING elseif' )
                                }
                                // console.log('TestCase: ',testcase)
                            }
                            testcase++;
                            
                        }
                    }
                }
            }
        }
    // console.log('for Each Ending')
    // console.log('Third Constraints: ',third_constraints)
}

