/** These variables refer to the selected buttons */

const editDiscussionBtn = document.getElementById("editDiscussionBtn");
const submitBtn = document.getElementById("submitBtn");

/** These variables refer to the selected text fields */
const discussionText = document.getElementById("id_content");
const discussionTitleField = document.getElementById("id_title");
const discussionTitle = document.getElementById("discussionTitle");
const discussionContent = document.getElementById("discussionContent");

/** These variables refer to the modals  */
const editDiscussionModal = new bootstrap.Modal(document.getElementById("editDiscussionModal"));

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

    editDiscussionModal.show();
});