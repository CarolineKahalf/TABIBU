let ambulance_array = [];
let ambulance_tbody = document.getElementById('ambulance_tbody');

function load_ambulance() {
    fetch('static/data/ambulance.json')
        .then(
            function (response) {
                if (response.status !== 200) {
                    console.log('Looks like there was a problem fetching data for ambulance. Status Code: ' +
                        response.status);
                    return;
                }

                // Examine the text in the response
                response.json().then(function (data) {

                    ambulance_array = data;
                    console.log('Ambulances successfully loaded');

                    //populate ambulance table
                    if (ambulance_array.length == 0) {
                        ambulance_tbody.innerHTML = '<td colspan="3">0 records found...</td>';
                    } else {
                        ambulance_tbody.innerHTML = '';
                    }

                    for (let tr = 0; tr < ambulance_array.length; tr++) {

                        ambulance_tbody.innerHTML += `<tr>
                                <td>${ambulance_array[tr].date}</td>
                                <td>${ambulance_array[tr].location}</td>
                                <td>${ambulance_array[tr].hospital}</td>
                            </tr>`;
                    }
                });
            }
        )
        .catch(function (err) {
            console.log('Error encountered while fetching ambulance data');
        });
}