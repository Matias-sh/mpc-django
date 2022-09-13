var numfila = 4;
var total_m_v = 0;
var total_ga_v = 0;
var total_tar_v = 0;
var total_m = document.getElementById("total_m");
var total_ga = document.getElementById("total_ga");
var total_tar = document.getElementById("total_tar");
var total_ga_tar = document.getElementById("total_ga_tar");
var total_m_ga_tar_a = document.getElementById("total_m_ga_tar");
var totaltodos = document.getElementById("totaltodos");


function agregarFila() {
    document.getElementById("tabladet").insertRow(-1).innerHTML = '<td id="td-det-' + numfila + '" style="border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" align="center" valign=bottom bgcolor="#FFFFFF"><strong><font color="#FFFFFF"><input class="form-caja-minuta cod" id="td-det-' + numfila + '" onkeyup="cod_DET(this)" type="text"></font></strong></td><td id ="td-det-' + (numfila + 1) + '" style="border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" align="center" valign=middle bgcolor="#FFFFFF" sdnum="11274;0;&quot;$&quot; #.##0,00"><b><font color="#FFFFFF"><input class="form-caja-minuta" id="det-det-' + (numfila + 1) + '" readonly></font></b></td><td id="td-det-' + (numfila + 2) + '" style="border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" align="center" bgcolor="#FFFFFF"><strong><input class="form-caja-minuta esp-det" type="text"></strong></td><td id="td-det-' + (numfila + 3) + '" style="border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" align="center" valign=middle bgcolor="#FFFFFF" sdval="300" sdnum="11274;0;&quot;$&quot; #.##0,00"><b><font color="#FFFFFF"><input class="form-caja-minuta mont-det"></font></b></td><br>';
    numfila = numfila + 4;
}



function total_M() {
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

    let total2 = 0
    for (let i = 0; i <= arr.length; i++) {
        if (arr[i] != "") {
            total = total + parseFloat(arr[i])
            if (!(isNaN(total))) {
                total_m.innerHTML = '<h6>$' + total + '</h6>'
                total_m_v = total
                totaltodos.value = total_m_v + total_ga_v + total_tar_v;
                total_m_ga_tar_a.innerHTML = '<h6>$' + totaltodos.value + '</h6>'
            }
            
        } else {
            total = total + total2
            if (!(isNaN(total))) {
                total_m.innerHTML = '<h6>$' + total + '</h6>'
                total_m_v = total
                totaltodos.value = total_m_v + total_ga_v + total_tar_v;
                total_m_ga_tar_a.innerHTML = '<h6>$' + totaltodos.value + '</h6>'
            }
        }
    }
};

function total_GA() {
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

    
    

    let total2 = 0
    for (let i = 0; i <= arr.length; i++) {
        if (arr[i] != "") {
            total = total + parseFloat(arr[i])
            if (!(isNaN(total))) {
                total_ga.innerHTML = '<h6>$' + total + '</h6>'
                total_ga_v = total
                totaltodos.value = total_m_v + total_ga_v + total_tar_v;
                total_m_ga_tar_a.innerHTML = '<h6>$' + totaltodos.value + '</h6>'
            }
        } else {
            total = total + total2
            if (!(isNaN(total))) {
                total_ga.innerHTML = '<h6>$' + total + '</h6>'
                total_ga_v = total
                totaltodos.value = total_m_v + total_ga_v + total_tar_v;
                total_m_ga_tar_a.innerHTML = '<h6>$' + totaltodos.value + '</h6>'
            }
        }
    }
};

function total_TAR() {
    let arr = [];
    let total = 0;
    let paso = true;

    arr.push(dv1_tar = document.getElementById("dv1_tar").value);
    arr.push(dv2_tar = document.getElementById("dv2_tar").value);
    arr.push(rigo_tar = document.getElementById("rigo_tar").value);
    arr.push(si_tar = document.getElementById("si_tar").value);
    arr.push(si2_tar = document.getElementById("si2_tar").value);
    arr.push(der_tar = document.getElementById("der_tar").value);
    arr.push(dea_tar = document.getElementById("dea_tar").value);
    arr.push(dee_tar = document.getElementById("dee_tar").value);
    arr.push(sa_tar = document.getElementById("sa_tar").value);
    arr.push(ceto_tar = document.getElementById("ceto_tar").value);
    arr.push(gara_tar = document.getElementById("gara_tar").value);
    arr.push(apodaca_tar = document.getElementById("apodaca_tar").value);

    
    total_m_ga_tar_a = document.getElementById("total_m_ga_tar");

    let total2 = 0
    for (let i = 0; i <= arr.length; i++) {
        if (arr[i] != "") {
            total = total + parseFloat(arr[i])
            if (!(isNaN(total))) {
                total_tar.innerHTML = '<h6>$' + total + '</h6>'
                total_tar_v = total
                totaltodos.value = total_m_v + total_ga_v + total_tar_v;
                total_m_ga_tar_a.innerHTML = '<h6>$' + totaltodos.value + '</h6>'
            }
        } else {
            total = total + total2
            if (!(isNaN(total))) {
                total_tar.innerHTML = '<h6>$' + total + '</h6>'
                total_tar_v = total
                totaltodos.value = total_m_v + total_ga_v + total_tar_v;
                total_m_ga_tar_a.innerHTML = '<h6>$' + totaltodos.value + '</h6>'
            }
        }
    }
};

function total_GA_TAR() {
    let arr = [];
    let total = 0;
    let paso = true;

    arr.push(dv1_ga_tar = document.getElementById("dv1_ga_tar").value);
    arr.push(dv2_ga_tar = document.getElementById("dv2_ga_tar").value);
    arr.push(rigo_ga_tar = document.getElementById("rigo_ga_tar").value);
    arr.push(si_ga_tar = document.getElementById("si_ga_tar").value);
    arr.push(si2_ga_tar = document.getElementById("si2_ga_tar").value);
    arr.push(der_ga_tar = document.getElementById("der_ga_tar").value);
    arr.push(dea_ga_tar = document.getElementById("dea_ga_tar").value);
    arr.push(dee_ga_tar = document.getElementById("dee_ga_tar").value);
    arr.push(sa_ga_tar = document.getElementById("sa_ga_tar").value);
    arr.push(ceto_ga_tar = document.getElementById("ceto_ga_tar").value);
    arr.push(gara_ga_tar = document.getElementById("gara_ga_tar").value);
    arr.push(apodaca_ga_tar = document.getElementById("apodaca_ga_tar").value);

    

    let total2 = 0
    for (let i = 0; i <= arr.length; i++) {
        if (arr[i] != "") {
            total = total + parseFloat(arr[i])
            if (!(isNaN(total))) {
                total_ga_tar.innerHTML = '<h6>$' + total + '</h6>'
            }
        } else {
            total = total + total2
            if (!(isNaN(total))) {
                total_ga_tar.innerHTML = '<h6>$' + total + '</h6>'
            }
        }
    }
};
