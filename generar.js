
var name = document.getElementById("name"),
    email = document.getElementById("email"),
    id = document.getElementById("id"),
    movil = document.getElementById("movil"),
    btnEPS = document.getElementById('epsbtn'),
    btnBanco = document.getElementById('bancobtn'),
    epsDropdown = document.getElementById('epsDropdown'),
    bancoDropdown = document.getElementById('bancoDropdown'),
    datet = document.getElementById("date"),
    agendarbtn = document.getElementById("agendarbtn");

var tipoTurno = "";
var lugarSeleccionado = "";
var contadorTurno = 1;

epsDropdown.style.display = 'none';
bancoDropdown.style.display = 'none';

btnEPS.addEventListener('click', () => {
    epsDropdown.style.display = 'block';
    bancoDropdown.style.display = 'none';
    tipoTurno = 'EPS';
});

btnBanco.addEventListener('click', () => {
    bancoDropdown.style.display = 'block';
    epsDropdown.style.display = 'none';
    tipoTurno = 'Banco';
});

epsDropdown.addEventListener('change', function() {
    lugarSeleccionado = epsDropdown.options[epsDropdown.selectedIndex].text;
});

bancoDropdown.addEventListener('change', function() {
    lugarSeleccionado = bancoDropdown.options[bancoDropdown.selectedIndex].text;
});



function formatearNumeroTurno(numero) {
  return String(numero).padStart(4, '0');
}


agendarbtn.addEventListener('click', (e) => {
    e.preventDefault();
    let turno = tipoTurno === 'EPS' ? 'e' : 'b';
    if (tipoTurno=='Banco'){
        if(lugarSeleccionado=="Bancolombia"){
            turno = turno + 'bco';
        }
        if(lugarSeleccionado=="Bancobogota"){
            turno = turno + 'bbo';
        }
        if(lugarSeleccionado=="Davivienda"){
            turno = turno + 'dav';
        }
    }

    if (tipoTurno=='EPS'){
        if(lugarSeleccionado=="Sanitas"){
            turno = turno + 'san';
        }
        if(lugarSeleccionado=="Compensar"){
            turno = turno + 'com';
        }
        if(lugarSeleccionado=="Colsubsidio"){
            turno = turno + 'col';
        }
    }
    if (id.value > 0 && movil.value > 0 && datet.value) {
        numeroTurno = formatearNumeroTurno(contadorTurno);
        let fe = datet.value;
        let dia = fe.split('-')[2]; 
        turno = turno +dia +numeroTurno;
        this.contadorTurno++;
        console.log(datet.value)
        console.log('Turno:', turno);
        console.log('Lugar seleccionado:', lugarSeleccionado);
        document.getElementById('turno').textContent = 'Turno: ' + turno;
    } else {
        alert("No pueden estar los campos vacios");
    }
});




function agregarFilaTabla(turno, nombre, correo, identificacion, movil, fecha, tipo) {
    var tabla = document.getElementById('tablaTurnos').getElementsByTagName('tbody')[0];
    var nuevaFila = tabla.insertRow(tabla.rows.length);

    nuevaFila.insertCell(0).textContent = turno;
    nuevaFila.insertCell(1).textContent = nombre;
    nuevaFila.insertCell(2).textContent = correo;
    nuevaFila.insertCell(3).textContent = identificacion;
    nuevaFila.insertCell(4).textContent = movil;
    nuevaFila.insertCell(5).textContent = fecha;
    nuevaFila.insertCell(6).textContent = tipo;
}