let invoice_array = [];
let invoice_tbody = document.getElementById('invoice_tbody');

function load_invoice() {
    fetch('static/data/invoice.json')
        .then(
            function (response) {
                if (response.status !== 200) {
                    console.log('Looks like there was a problem fetching data for invoice. Status Code: ' +
                        response.status);
                    return;
                }

                // Examine the text in the response
                response.json().then(function (data) {

                    invoice_array = data;
                    console.log('Invoices successfully loaded');

                    //populate invoice table
                    if (invoice_array.length == 0) {
                        invoice_tbody.innerHTML = '<td colspan="4">0 records found...</td>';
                    } else {
                        invoice_tbody.innerHTML = '';
                    }

                    for (let tr = 0; tr < invoice_array.length; tr++) {

                        invoice_tbody.innerHTML += `<tr>
                                <td>${invoice_array[tr].number}</td>
                                <td>${invoice_array[tr].date}</td>
                                <td>${invoice_array[tr].doctor}</td>
                                <td>${invoice_array[tr].amount}</td>
                            </tr>`;
                    }
                });
            }
        )
        .catch(function (err) {
            console.log('Error encountered while fetching invoice data');
        });
}