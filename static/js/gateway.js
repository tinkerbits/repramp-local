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