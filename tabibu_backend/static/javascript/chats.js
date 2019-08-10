let chat_array = [];
let previous_chats = document.getElementById('previouschats');

function load_chat() {
    fetch('static/data/chats.json')
        .then(
            function (response) {
                if (response.status !== 200) {
                    console.log('Looks like there was a problem fetching data for chats. Status Code: ' +
                        response.status);
                    return;
                }

                // Examine the text in the response
                response.json().then(function (data) {

                    chat_array = data;
                    console.log('Chats successfully loaded');

                    //populate all the previous chats if any
                    if (chat_array.length == 0) {
                        previous_chats.innerHTML = '<i>No previous chats found</i>';
                    } else {
                        previous_chats.innerHTML = '';
                    }

                    for (let span = 0; span < chat_array.length; span++) {
                        previous_chats.innerHTML += `<span onclick="chat_thread('${span}')">${chat_array[span].name}</span><br>`;
                    }
                });
            }
        )
        .catch(function (err) {
            console.log('Error encountered while fetching chat data');
        });
}

function chat_thread(chat_number) {
    document.getElementById('overall_chats').style.display = 'none';
    document.getElementById('inside_a_chat').style.display = 'block';

    document.getElementById('chat_patner').innerHTML = `<div style="text-align:center;">${chat_array[chat_number].name}</div>`;

    //past the messages on a thread
    document.getElementById('messages').innerHTML = '';
    for (let i = 0; i < chat_array[chat_number].thread.length; i++) {

        if (chat_array[chat_number].name == chat_array[chat_number].thread[i].sender) {
            //doctor
            document.getElementById('messages').innerHTML += `<div class="chat_container">
            <img src="static/images/doctor.png" alt="Avatar" style="width:100%;">
            <p>${chat_array[chat_number].thread[i].message}</p>
            <span class="chat_time-right">${chat_array[chat_number].thread[i].time}</span></div><br>`;

        } else {
            //patient
            document.getElementById('messages').innerHTML += `<div class="chat_container chat_darker">
            <img src="static/images/profile.png" alt="Avatar" class="chat_right" style="width:100%;">
            <p>${chat_array[chat_number].thread[i].message}</p>
            <span class="chat_time-left">${chat_array[chat_number].thread[i].time}</span></div><br>`;
        }
    }
}

//Insides chats
function back_to_threads() {
    document.getElementById('inside_a_chat').style.display = 'none';
    document.getElementById('symptoms_board').style.display = 'none';
    document.getElementById('overall_chats').style.display = 'block';
}

//when posting symptoms
function symptoms_display() {
    document.getElementById('overall_chats').style.display = 'none';
    document.getElementById('symptoms_board').style.display = 'block';
}

function submit_symptoms() {
    
}