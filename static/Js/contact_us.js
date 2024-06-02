function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');


const contact_name = document.getElementById('contact-name'),
    contact_number = document.getElementById('contact-number'),
    messages_style = document.getElementById('messages-style'),
    contact_message = document.getElementById('contact-message');

document.getElementById('create-contact').addEventListener('click', ()=> {
    let message = 'no message'
    if (contact_message) {
        message = contact_message.value
    }
    if (contact_name.value !== '' && contact_number.value !== '') {
        fetch('/contact-us/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken
            },
            body: JSON.stringify({
                'contact_name': contact_name.value,
                'contact_number': contact_number.value,
                'contact_message': message

            })
        })
            .then(res => res.json())
            .then(data => {
                console.log(data)
                contact_name.value = ''
                contact_number.value = ''
                if (contact_message) {
                    contact_message.value = ''
                }
                messages_style.style.opacity = '100'
                messages_style.innerHTML = 'اطلاعات شما ذخیره شد و در اسرع وقت با شما تماس میگیریم'
                setTimeout(() => {
                    messages_style.style.opacity = '0'
                }, 6000)
            })
    }
})

