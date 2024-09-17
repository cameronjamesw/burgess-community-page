/** These variables refer to the selected buttons */

const editDiscussionBtn = document.getElementById("editDiscussionBtn");
const delDiscussionBtn = document.getElementById("delDiscussionBtn");
const submitBtn = document.getElementById("submitBtn");
const delDiscussionConfirm = document.getElementById("deleteDiscussionConfirm");

/** These variables refer to the selected text fields */
const discussionText = document.getElementById("id_content");
const discussionTitleField = document.getElementById("id_title");
const discussionTitle = document.getElementById("discussionTitle");
const discussionContent = document.getElementById("discussionContent");
const deleteDiscussionConfirm = document.getElementById("deleteDiscussionConfirm");

/** These variables refer to the modals  */
const editDiscussionModal = new bootstrap.Modal(document.getElementById("editDiscussionModal"));
const deleteDiscussionModal = new bootstrap.Modal(document.getElementById("deleteDiscussionModal"));

const discussionForm = document.getElementById("discussionForm");

/** This event listener shows the Edit Discussion Modal
 * as well as changing the values of the form fields to
 * the current values of the discussion.
 */
editDiscussionBtn.addEventListener("click", (e) => {
    let discussionContentValue = discussionContent.innerText;
    discussionText.value = discussionContentValue;

    let discussionTitleValue = discussionTitle.innerText;
    discussionTitleField.value = discussionTitleValue;

    submitBtn.innerText = "Update";

    discussionForm.setAttribute("action", 'edit_discussion/');

    editDiscussionModal.show();
});

delDiscussionBtn.addEventListener("click", (e) => {
    deleteDiscussionConfirm.href = 'delete_discussion/'
    deleteDiscussionModal.show();
});