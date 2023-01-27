document.getElementById("myButton").onclick = function(){
    var prin=document.getElementById("principal").value;
    console.log(prin);

    var time=document.getElementById("years").value;
    console.log(time);

    var cycle=document.getElementById("cycles").value;
    console.log(cycle);

    var trate=document.getElementById("int-rate").value;
    console.log(trate);


/* Calculate compound interest */
let rate=trate/cycle;
let A = prin *
    (Math.pow((1 + rate / 100), time));
let CI = A - prin;

//document.write("Compound interest is " + CI);
alert("COMPOUND INTEREST : " + CI);
}