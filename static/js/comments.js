const editButtons = document.getElementsByClassName("btn-edit");
const commentText = document.getElementById("id_body");
const commentForm = document.getElementById("commentForm");
const submitButton = document.getElementById("submitButton");

const deleteModal = new bootstrap.Modal(document.getElementById("deleteCommentModal"));
const deleteButtons = document.getElementsByClassName("btn-delete");
const deleteConfirm = document.getElementById("deleteCommentConfirm");

document.addEventListener("DOMContentLoaded", function () {
  document.addEventListener('hide.bs.modal', function (event) {
    if (document.activeElement) {
      document.activeElement.blur();
    }
  });
});

/**
* This code overrides standard Bootstrap which was causing
 * issues between modals and screenreaders. This code allows
 * screenreaders to recognise that the modal is hidden and when
 * it is active.
 */
for (let button of editButtons) {
  button.addEventListener("click", () => {
    let commentId = button.getAttribute("comment_id");
    console.log(commentId);
    let commentContent = document.getElementById(`comment${commentId}`).innerText;
    commentText.value = commentContent;
    submitButton.innerText = "Update";
    commentForm.setAttribute("action", `edit_comment/${commentId}`);
  });
}


/**
 * These variables add event listeners to the delete
 * buttons within the comments of a discussion. Upon clicking
 * the button, a confirmation modal is shown to the user so
 * that they can confirm their deletion.
 */
for (let button of deleteButtons) {
  button.addEventListener("click", (e) => {
    let commentId = button.getAttribute("comment_id");
    console.log(commentId);
    deleteConfirm.href = `delete_comment/${commentId}`;
    deleteModal.show();
  });
}