// Get the sign_up modal
var signup_modal = document.getElementById('id02');

// When the user clicks anywhere outside of the sign_up modal, close it
window.onclick = function (event) {
  if (event.target == signup_modal) {
    signup_modal.style.display = "none";
  }
}

// Get the login modal
var login_modal = document.getElementById('id01');

// When the user clicks anywhere outside of the login modal, close it
window.onclick = function (event) {
  if (event.target == login_modal) {
    login_modal.style.display = "none";
  }
}

//open the side navigation bar
function openNav() {
  document.getElementById("mySidenav").style.width = "250px";
}

//close the side navigation bar
function closeNav() {
  document.getElementById("mySidenav").style.width = "0";
}

//switch between the various tabs using the side navigation bar
function switch_div(div) {
  let landing_page = document.getElementById('landing_page');
  let home = document.getElementById('home');
  let profile = document.getElementById('profile');
  let ambulance = document.getElementById('ambulance_service');
  let hospital = document.getElementById('hospital_locator');
  let invoices = document.getElementById('invoices');
  let topup = document.getElementById('topup');
  let help = document.getElementById('help');
  let contact = document.getElementById('contact');
  let records = document.getElementById('medical_records');
  let chats = document.getElementById('chats');

  //hide all the tabs
  landing_page.style.display = 'none';
  home.style.display = 'none';
  profile.style.display = 'none';
  ambulance.style.display = 'none';
  hospital.style.display = 'none';
  invoices.style.display = 'none';
  help.style.display = 'none';
  contact.style.display = 'none';
  records.style.display = 'none';
  chats.style.display = 'none';

  document.getElementById('login_btn').style.display = 'none';
  document.getElementById('signup_btn').style.display = 'none';
  document.getElementById('opennav_btn').style.display = 'block';
  document.getElementById('profile_photo_span').style.display = 'block';

  //for the landing page, the top is different from home page
  if (div == 'landing_page') {
    landing_page.style.display = "block";
    document.getElementById('opennav_btn').style.display = 'none';
    document.getElementById('profile_photo_span').style.display = 'none';
    document.getElementById('login_btn').style.display = 'block';
    document.getElementById('signup_btn').style.display = 'block';
  }

  //open the required tab and load its data
  switch (div) {
    case 'home':
      if (logged_in) {
        home.style.display = "block";
        load_records();
      }
      break;

    case 'profile':
      profile.style.display = "block";
      break;

    case 'ambulance_service':
      ambulance.style.display = "block";
      load_ambulance();
      break;

    case 'hospital_locator':
      hospital.style.display = "block";
      load_hospitals();
      break;

    case 'invoices':
      invoices.style.display = "block";
      load_invoice();
      fetch_invoice();
      break;

    case 'help':
      help.style.display = "block";
      break;

    case 'contact':
      contact.style.display = "block";
      break;

    case 'records':
      records.style.display = "block";
      load_records();
      break;

    case 'chats':
      chats.style.display = "block";
      load_chat();
      break;

    default:
      home.style.display = "block";
      break;
  }
  //make sure navigation bar is closed
  closeNav()
}
