// GATEWAY.HTML

//// Accept Buttons
let acceptButtons = document.querySelectorAll('button.actionacceptbutton');

for(let acceptbutton of acceptButtons){
  acceptbutton.addEventListener('click', event => {

    event.preventDefault();

    console.log(event.target)

    if(!event.target.classList.contains('bg-green-400')){
      fetch(`http://localhost:8000/?m1-actionid=${event.target.dataset.actionId}&m1-status=accepted`);
      event.target.classList.add('bg-green-400');
      matchingRejectButton = document.querySelector(`button.actionrejectbutton[data-action-id="${event.target.dataset.actionId}"]`);
      matchingRejectButton.classList.remove('bg-red-400');
    }else if(event.target.classList.contains('bg-green-400')){
      fetch(`http://localhost:8000/?m1-actionid=${event.target.dataset.actionId}&m1-status=empty`);
      event.target.classList.remove('bg-green-400');
    }


  })
}

//// Reject Buttons

let rejectButtons = document.querySelectorAll('button.actionrejectbutton');

for(let rejectbutton of rejectButtons){
  rejectbutton.addEventListener('click', event => {

    event.preventDefault();

    if(!event.target.classList.contains('bg-red-400')){
      fetch(`http://localhost:8000/?m1-actionid=${event.target.dataset.actionId}&m1-status=rejected`);
      event.target.classList.add('bg-red-400');
      matchingAcceptButton = document.querySelector(`button.actionacceptbutton[data-action-id="${event.target.dataset.actionId}"]`);
      matchingAcceptButton.classList.remove('bg-green-400');
    }else if(event.target.classList.contains('bg-red-400')){
      fetch(`http://localhost:8000/?m1-actionid=${event.target.dataset.actionId}&m1-status=empty`);
      event.target.classList.remove('bg-red-400');
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