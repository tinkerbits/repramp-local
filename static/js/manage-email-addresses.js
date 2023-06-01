// MANAGERS/MANAGE-EMAIL-ADDRESSES.HTML

//// Save Assignments Button

let selectdropdowns = document.querySelectorAll('select[name="warmupper"]');
let savebutton = document.querySelector('button#submitbutton');


savebutton.addEventListener('click', event => {

  event.preventDefault();

  
  //////// build the formData object
  let warmupperupdates = new FormData()

  for(let selectdropdown of selectdropdowns){
    let selectedoption = selectdropdown.options[selectdropdown.selectedIndex];
    warmupperupdates.append(selectedoption.getAttribute('data-email-id'), selectedoption.getAttribute('data-warmupper-id'))
  }

  //////// function to get the csrf token
  function getCookie(name) {
    let cookieValue = document.cookie.match('(^|;)\\s*' + name + '\\s*=\\s*([^;]+)');
    return cookieValue ? cookieValue.pop() : null;
  }

  //////// fetch request to send the formData to the django view
  fetch(`http://localhost:8000/manage-email-addresses/`, {
    method: 'POST',
    headers: {
      'X-CSRFToken': getCookie('csrftoken')
    },
    body: warmupperupdates
  })

});