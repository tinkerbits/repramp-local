

let commentsubmitbutton = document.querySelector('button#commentsubmitbutton');
commentsubmitbutton.addEventListener('click', event => addComment(event));

let commentfield = document.querySelector(`input#commentfield[data-action-id="${commentsubmitbutton.attributes.getNamedItem('data-action-id').value}"]`);

function addComment(ev) {

  let url = `http://localhost:8000/?m1-actionid=${ev.target.dataset.actionId}&m1-comment=${commentfield.value}`;
  fetch(url)
    .then(response => response.json())
    .then(data => console.log(data))
    .catch(error => console.log(error));
}
