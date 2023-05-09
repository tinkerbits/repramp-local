let commentsubmitbuttons = document.querySelectorAll('button.commentsubmitbutton');

for(let commentsubmitbutton of commentsubmitbuttons){

  commentsubmitbutton.addEventListener('click', event => {

    let commentfield = document.querySelector(`input.commentfield[data-action-id="${event.target.dataset.actionId}"]`);
    fetch(`http://localhost:8000/?m1-actionid=${event.target.dataset.actionId}&m1-comment=${commentfield.value}`);

  })
}
