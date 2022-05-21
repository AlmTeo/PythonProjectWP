function deleteNote(noteId) {
  fetch("/delete-note", {
    method: "POST",
    body: JSON.stringify({ noteId: noteId }),
  }).then((_res) => {
    window.location.href = "/";
  });
}

function updateNote(noteId) {
  var noteContents = document.getElementById('edit-note').value
  fetch("/update-note", {
    method: "POST",
    body: JSON.stringify({ noteId: noteId , noteContents: noteContents}),
  }).then((_res) => {
    window.location.href = "/";
  });
}

$(document).on('click', '.edit-btn', function() {
  var noteId = $(this).parents('tr').find('.note-text').attr('data-note-id');
  var noteText = $(this).parents('tr').find('.note-text').text();
  $('.note-edit-input').val(noteText);
  $('#modalContactForm').attr('data-edited-note', noteId);
});

$(document).on('click', '.save-edit-note', function() {
  var noteId = $('#modalContactForm').attr('data-edited-note');
  var noteText = $('.note-edit-input').val();
  fetch("/update-note", {
    method: "POST",
    body: JSON.stringify({ noteId: noteId , noteContents: noteText}),
  }).then((_res) => {
    window.location.href = "/";
  });
});
