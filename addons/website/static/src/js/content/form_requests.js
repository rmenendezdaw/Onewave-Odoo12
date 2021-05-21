const postRequest = (url, data) => {
    return new Promise(function(resolve, reject) {
        $.ajax({
            url: url,
            type: 'POST',
            accepts: "application/json",
            contentType: "application/json",
            dataType: 'JSON',
            data: JSON.stringify({ "params": data }),
            success: function(result) {
                resolve(result);
            }, error: function(error) {
                reject(error);
            }
        })
    })
}

const formRegisterOrg = () => {
    $("#formregister").submit(function (e) {
        e.preventDefault();

        let form = {
            'name': $("#name").val(),
            'email': $("#email").val(),
            'vat': $("#vat").val(),
            'phone': $("#phone").val(),
            'cargo': $("#cargo").val()
        }// end_form

        postRequest('/organizador/form/submit', form).then(function(res) {
            if (res.result.result === "False") toastr.error('El usuario ya existe.');
            else window.location.replace("/organizador/form/success");
        }).catch(function(error) {
            console.log(error);
        })
    })
}

const formRegisterGroup = () => {
    $("#formregister_group").submit(function (e) {
        e.preventDefault();

        let form = {
            'name': $("#name").val(),
            'email': $("#email").val(),
            'name_group': $("#name_group").val(),
            'phone': $("#phone").val(),
            'carrera': $("#carrera").val(),
            'especialidad': $("#especialidad").val()
        }// end_form

        postRequest('/grupo/form/submit', form).then(function(res) {
            if (res.result.result === "False") toastr.error('El usuario ya existe.');
            else window.location.replace("/organizador/form/success");
        }).catch(function(error) {
            console.log(error);
        })
    })
}

const registerEvent = () => {
    $("#registration_event").submit(function (e) {
        e.preventDefault();
        
        postRequest(`/event/${$("#slug-event").val()}/registration/confirm`, { '1-name': '', '1-email': '', '1-phone': '', '1-ticket_id': '0' }).then(function(res) {
            if (res.result.res === "False") {
                toastr.error('Ya estás inscrito en el evento');
            } else if (res.result.res === 'unknown') {
                toastr.error('No te puedes registrar sin estar dado de alta', 'Haz click aquí para ir al acceso');
                toastr.options.onclick = function () { window.location.replace("/web/login"); }
            } else {
                window.location.replace(`/eventos/registro/${res.result.res}`)
            }
        }).catch(function(error) {
            console.log(error);
        })
    })
}


$(document).ready(function () {
    formRegisterOrg();
    formRegisterGroup();
    registerEvent();
})