// GATEWAY.HTML

//// Accept Buttons
let acceptButtons = document.querySelectorAll('button.actionacceptbutton');

for(let acceptbutton of acceptButtons){
  acceptbutton.addEventListener('click', event => {

    event.preventDefault();

    if(event.target.style.backgroundColor===''){
      fetch(`http://localhost:8000/?m1-actionid=${event.target.dataset.actionId}&m1-status=accepted`);
      event.target.style.backgroundColor = 'green';
      matchingRejectButton = document.querySelector(`button.actionrejectbutton[data-action-id="${event.target.dataset.actionId}"]`);
      matchingRejectButton.style.backgroundColor = '';
    }else if(event.target.style.backgroundColor==='green'){
      fetch(`http://localhost:8000/?m1-actionid=${event.target.dataset.actionId}&m1-status=empty`);
      event.target.style.backgroundColor = '';
    }


  })
}

//// Reject Buttons

let rejectButtons = document.querySelectorAll('button.actionrejectbutton');

for(let rejectbutton of rejectButtons){
  rejectbutton.addEventListener('click', event => {

    event.preventDefault();

    if(event.target.style.backgroundColor===''){
      fetch(`http://localhost:8000/?m1-actionid=${event.target.dataset.actionId}&m1-status=rejected`);
      event.target.style.backgroundColor = 'red';
      matchingAcceptButton = document.querySelector(`button.actionacceptbutton[data-action-id="${event.target.dataset.actionId}"]`);
      matchingAcceptButton.style.backgroundColor = '';
    }else if(event.target.style.backgroundColor==='red'){
      fetch(`http://localhost:8000/?m1-actionid=${event.target.dataset.actionId}&m1-status=empty`);
      event.target.style.backgroundColor = '';
    }
  })
}


//// Comment Submit Buttons

let commentsubmitbuttons = document.querySelectorAll('button.commentsubmitbutton');

for(let commentsubmitbutton of commentsubmitbuttons){

  commentsubmitbutton.addEventListener('click', event => {

    event.preventDefault();
    let commentfield = document.querySelector(`input.commentfield[data-action-id="${event.target.dataset.actionId}"]`);
    fetch(`http://localhost:8000/?m1-actionid=${event.target.dataset.actionId}&m1-comment=${commentfield.value}`);

  })
}

// MANAGERS/MANAGE-SOME-USERS.HTML

//// Display Privilege Field if Role is Sender

let rolefields = document.querySelectorAll(`select[name="role"]`)

for(let rolefield of rolefields){
  rolefield.addEventListener('change', event => {
    if(rolefield.value == "sender"){
      console.log("twathead")
      let hiddenspan = document.querySelector(`span[data-user-id="${event.target.dataset.userId}"]`);
      hiddenspan.style.display = "block";
    }else{
      let hiddenspan = document.querySelector(`span[data-user-id="${event.target.dataset.userId}"]`);
      hiddenspan.style.display = "none";
    }
})}

//// User Data Submit Buttons

let someuserdatasubmitbuttons = document.querySelectorAll('button.someuserdatasubmitbutton');

for(let someuserdatasubmitbutton of someuserdatasubmitbuttons){
  someuserdatasubmitbutton.addEventListener('click', event => {

    event.preventDefault();
    let usernamefield = document.querySelector(`input[name="username"][data-user-id="${event.target.dataset.userId}"]`);
    let emailfield = document.querySelector(`input[name="email"][data-user-id="${event.target.dataset.userId}"]`);
    let first_namefield = document.querySelector(`input[name="first_name"][data-user-id="${event.target.dataset.userId}"]`);
    let last_namefield = document.querySelector(`input[name="last_name"][data-user-id="${event.target.dataset.userId}"]`);
    let rolefield = document.querySelector(`select[name="role"][data-user-id="${event.target.dataset.userId}"]`);
    let privilegefield = document.querySelector(`select[name="privilege"][data-user-id="${event.target.dataset.userId}"]`);

    fetch(`http://localhost:8000/manage-some-users/?m2-userid=${event.target.dataset.userId}&m2-username=${usernamefield.value}&m2-email=${emailfield.value}&m2-first_name=${first_namefield.value}&m2-last_name=${last_namefield.value}&m2-role=${rolefield.value}&m2-privilege=${privilegefield.value}`);

  })
}



// DIRECTORS/MANAGE-ALL-USERS.HTML

//// User Data Submit Buttons

let alluserdatasubmitbuttons = document.querySelectorAll('button.alluserdatasubmitbutton');

for(let alluserdatasubmitbutton of alluserdatasubmitbuttons){
  alluserdatasubmitbutton.addEventListener('click', event => {

    event.preventDefault();
    let usernamefield = document.querySelector(`input[name="username"][data-user-id="${event.target.dataset.userId}"]`);
    let emailfield = document.querySelector(`input[name="email"][data-user-id="${event.target.dataset.userId}"]`);
    let first_namefield = document.querySelector(`input[name="first_name"][data-user-id="${event.target.dataset.userId}"]`);
    let last_namefield = document.querySelector(`input[name="last_name"][data-user-id="${event.target.dataset.userId}"]`);
    let rolefield = document.querySelector(`select[name="role"][data-user-id="${event.target.dataset.userId}"]`);
    let privilegefield = document.querySelector(`select[name="privilege"][data-user-id="${event.target.dataset.userId}"]`);
    
    fetch(`http://localhost:8000/manage-all-users/?d1-userid=${event.target.dataset.userId}&d1-username=${usernamefield.value}&d1-email=${emailfield.value}&d1-first_name=${first_namefield.value}&d1-last_name=${last_namefield.value}&d1-role=${rolefield.value}&d1-privilege=${privilegefield.value}`);


  })
}



// MANAGERS/MANAGE-EMAIL_ADDRESSES.HTML

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



