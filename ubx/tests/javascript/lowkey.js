
a = [5,4,3,2,1,];
b = [5,4,2,1,1];


for (i=0;i!=a.length;i++){
    for (ii=0;ii!=b.length;ii++){

        do {
            if (a[i] != b[ii]){
                if (a[i] >= b[ii]){
                    a[i]-=1
                }else {
                a[i]+=1
            }
            } 
            console.log(a[i])
        } while ( a[i] != b[ii])

    }
    console.log(a,b);
}


        // if (a[i]>=b[ii]){
        //     console.log(a[i], ' is greater than ', b[ii]);
        //     a[i]-=1
        // }
        // console.log(a[i], b[ii]);