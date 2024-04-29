$(document).ready(function() {
    $('#formulario').submit(function(event) {
        if (!validarRut() || !validarNombre() || !validarApellidoPaterno() || !validarApellidoMaterno() || !validarEdad() || !validarGenero() || !validarCelular()) {
            event.preventDefault();
        }
    });

    function validarRut() {
        var rut = $('#rut').val();
        if (rut.length < 9 || rut.length > 10) {
            alert('El rut debe tener entre 9 y 10 caracteres');
            return false;
        }
        return true;
    }

    function validarNombre() {
        var nombre = $('#nombre').val();
        if (nombre.length < 3 || nombre.length > 20) {
            alert('El nombre debe tener entre 3 y 20 caracteres');
            return false;
        }
        return true;
    }

    function validarApellidoPaterno() {
        var apellidoPaterno = $('#apellido_paterno').val();
        if (apellidoPaterno.length < 3 || apellidoPaterno.length > 20) {
            alert('El apellido paterno debe tener entre 3 y 20 caracteres');
            return false;
        }
        return true;
    }

    function validarApellidoMaterno() {
        var apellidoMaterno = $('#apellido_materno').val();
        if (apellidoMaterno.length < 3 || apellidoMaterno.length > 20) {
            alert('El apellido materno debe tener entre 3 y 20 caracteres');
            return false;
        }
        return true;
    }

    function validarEdad() {
        var edad = parseInt($('#edad').val());
        if (edad < 18 || edad > 35) {
            alert('La edad debe estar entre 18 y 35 años');
            return false;
        }
        return true;
    }

    function validarGenero() {
        var genero = $('#genero').val();
        if (genero === '') {
            alert('Debes seleccionar un género');
            return false;
        }
        return true;
    }

    function validarTelefono() {
        var celular = $('#telefono').val();
        if (telefono.length < 9 || telefono.length > 12) {
            alert('El telefono debe tener entre 9 y 12 caracteres');
            return false;
        }
        return true;
    }
    function crearCarta() {
        var rut = document.getElementById('rut').value;
        var nombre = document.getElementById('nombre').value;
        var apellido_paterno = document.getElementById('apellido_paterno').value;
        var apellido_materno = document.getElementById('apellido_materno').value;
        var fecha_nacimiento = document.getElementById('fecha_nacimiento').value;
        var edad = document.getElementById('edad').value;
        var genero = document.getElementById('genero').value;
        var correo = document.getElementById('correo').value;
        var telefono = document.getElementById('telefono').value;
        var profesion = document.getElementById('profesion').value;
        var motivacion_trabajo = document.getElementById('motivacion_trabajo').value;
        
        var cartaTexto = "Estimado/a reclutador/a,\n\n";
        cartaTexto += "Mi nombre es " + nombre +""+ apellido_paterno +""+ apellido_materno +" y estoy interesado/a en el puesto de " + puesto + ".\n";
        cartaTexto += "Quiero compartir mi experiencia en el campo: " + experiencia + "\n\n";
        cartaTexto += "Quedo a disposición para cualquier consulta adicional.\n\n";
        cartaTexto += "Atentamente,\n" + nombre;
        
        document.getElementById('carta').value = cartaTexto;
    }
    
});
