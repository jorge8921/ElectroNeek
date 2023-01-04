function test(a){
    const func = a["var1"];
    const data = a["var2"];

    switch (func) {
    case 'Splt':
        var res = data.split(" ");
        return res[0];
    case 'Slc':
        var res = data.slice(2,4)
        return res;
    default:
        console.log(`Sorry, we are out of ${func}.`);
    }


}