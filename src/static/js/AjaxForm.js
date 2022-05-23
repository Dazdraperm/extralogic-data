async function update_form() {
    let form = document.querySelector('#update-form');

    let url = '/v1/form/' + form.elements.old_form_uid.value;

    let body = new FormData(form);



    let response = await fetch(url, {
        method: 'PUT',
        body: body
    });
    if (response.ok) {
        alert('Вы обновили данные')
    } else {
        alert("Ошибка HTTP: " + response.status);
    }

}