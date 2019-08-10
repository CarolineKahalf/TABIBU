let records_array = [];
let records_tbody = document.getElementById('records_tbody');

function load_records() {
    fetch('static/data/records.json')
        .then(
            function (response) {
                if (response.status !== 200) {
                    console.log('Looks like there was a problem fetching data for records. Status Code: ' +
                        response.status);
                    return;
                }

                // Examine the text in the response
                response.json().then(function (data) {

                    records_array = data;
                    console.log('Records successfully loaded');
                    
                    if (records_array.length == 1) {
                        document.getElementById('number_of_records').innerHTML = '1 record found';
                    } else {
                        document.getElementById('number_of_records').innerHTML = `${records_array.length} records found`
                    }
                    

                    //populate records table
                    if (records_array.length == 0) {
                        records_tbody.innerHTML = '<td colspan="6">0 records found...</td>';
                    } else {
                        records_tbody.innerHTML = '';
                    }

                    for (let tr = 0; tr < records_array.length; tr++) {

                        records_tbody.innerHTML += `<tr>
                                <td>${records_array[tr].date}</td>
                                <td>${records_array[tr].location}</td>
                                <td>${records_array[tr].doctor}</td>
                                <td>${records_array[tr].illness}</td>
                                <td>${records_array[tr].cost}</td>
                                <td>${records_array[tr].recommendation}</td>
                            </tr>`;
                    }
                });
            }
        )
        .catch(function (err) {
            console.log('Error encountered while fetching records data');
        });
}