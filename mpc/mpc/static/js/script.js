function total_M(){
    let arr = [];
    let total = 0;
    let paso = true;
    
    arr.push(dv1_m = document.getElementById("dv1_m").value);
    arr.push(dv2_m = document.getElementById("dv2_m").value);
    arr.push(rigo_m = document.getElementById("rigo_m").value);
    arr.push(si_m = document.getElementById("si_m").value);
    arr.push(si2_m = document.getElementById("si2_m").value);
    arr.push(der_m = document.getElementById("der_m").value);
    arr.push(dea_m = document.getElementById("dea_m").value);
    arr.push(dee_m = document.getElementById("dee_m").value);
    arr.push(sa_m = document.getElementById("sa_m").value);
    arr.push(ceto_m = document.getElementById("ceto_m").value);
    arr.push(gara_m = document.getElementById("gara_m").value);
    arr.push(apodaca_m = document.getElementById("apodaca_m").value);

    total_m = document.getElementById("total_m");
    let total2 = 0
    for(let i=0; i<=arr.length; i++){
        if(arr[i] != ""){
            total = total + parseFloat(arr[i])
            if(!(isNaN(total))){
                total_m.value = total
            }
        }else{
            total = total + total2
            if(!(isNaN(total))){
                total_m.value = total
            }
        }
    }
};

function total_GA(){
    let arr = [];
    let total = 0;
    let paso = true;
    
    arr.push(dv1_ga = document.getElementById("dv1_ga").value);
    arr.push(dv2_ga = document.getElementById("dv2_ga").value);
    arr.push(rigo_ga = document.getElementById("rigo_ga").value);
    arr.push(si_ga = document.getElementById("si_ga").value);
    arr.push(si2_ga = document.getElementById("si2_ga").value);
    arr.push(der_ga = document.getElementById("der_ga").value);
    arr.push(dea_ga = document.getElementById("dea_ga").value);
    arr.push(dee_ga = document.getElementById("dee_ga").value);
    arr.push(sa_ga = document.getElementById("sa_ga").value);
    arr.push(ceto_ga = document.getElementById("ceto_ga").value);
    arr.push(gara_ga = document.getElementById("gara_ga").value);
    arr.push(apodaca_ga = document.getElementById("apodaca_ga").value);

    total_ga = document.getElementById("total_ga");

    let total2 = 0
    for(let i=0; i<=arr.length; i++){
        if(arr[i] != ""){
            total = total + parseFloat(arr[i])
            if(!(isNaN(total))){
                total_ga.value = total
            }
        }else{
            total = total + total2
            if(!(isNaN(total))){
                total_ga.value = total
            }
        }
    }
};