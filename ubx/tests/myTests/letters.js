
letters = [
    {alphabet : [
        4,
        2002,
        20003,
        8,
        200002,
        200002
        ]
    },
    {alphabet : [
        6,
        20002,
        200002,
        20002,
        5,
        2002,
        200002,
        20002,
        6
        ]
    },
    {alphabet: [
        9,
        400002,
        30000002,
        2000,
        1000,
        2000,
        30000002,
        400002,
        9
    ]
    },
    {alphabet:[
        8,
        2000002,
        20000002,
        200000002,
        200000002,
        20000002,
        2000002,
        8
    ]
    },
    {alphabet:[
        9,
        20000001,
        2,
        2,
        6,
        2,
        2,
        20000001,
        9
    ]
    },
    {
        alphabet:[
            9,
            20000001,
            2,
            6,
            2,
            2,
            2,
        ]
    }

]

function letterLog(x){
    console.log('\n');
    x.map((n) => {
        n = n.toString().split('');
        printend = '';
        for (i=0; i<=n.length;i++){
            if (n[i] != 0 ){
                printend += '*'.repeat(n[i]);
            } else {
                printend += ' ';
            }
        }
        console.log(printend);
    });
}
console.log('\n\n LETTERS: ')
for (i in letters){
    letterLog(letters[i].alphabet);
}
// letterLog(letters[0].alphabet);
// letterLog(letters[1].alphabet);