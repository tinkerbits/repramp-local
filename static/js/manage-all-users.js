// DIRECTORS/MANAGE-ALL-USERS.HTML

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