let hospitals_array = [];
let hospitals_tbody = document.getElementById('hospitals_tbody');

function load_hospitals() {
    fetch('static/data/hospitals.json')
        .then(
            function (response) {
                if (response.status !== 200) {
                    console.log('Looks like there was a problem fetching data for hospitals. Status Code: ' +
                        response.status);
                    return;
                }

                // Examine the text in the response
                response.json().then(function (data) {

                    hospitals_array = data;
                    console.log('Hospitals successfully loaded');

                    //populate hospitals table
                    if (hospitals_array.length == 0) {
                        hospitals_tbody.innerHTML = '<td colspan="5">0 records found...</td>';
                    } else {
                        hospitals_tbody.innerHTML = '';
                    }
                    for (let tr = 0; tr < hospitals_array.length; tr++) {

                        hospitals_tbody.innerHTML += `<tr>
                                <td>${hospitals_array[tr].name}</td>
                                <td>${hospitals_array[tr].location}</td>
                                <td><a class='hospital_link' target='_blank' href='${hospitals_array[tr].map_url}'>Get directions</a></td>
                                <td>${hospitals_array[tr].contacts}</td>
                                <td>${hospitals_array[tr].rating}</td>
                            </tr>`;
                    }
                });
            }
        )
        .catch(function (err) {
            console.log('Error encountered while fetching hospitals data');
        });
}


