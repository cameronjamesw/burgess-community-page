const editDiscussionBtn = document.getElementById("editDiscussionBtn");
const discussionText = document.getElementById("id_content");
const discussionTitleField = document.getElementById("id_title");
const discussionTitle = document.getElementById("discussionTitle");
const discussionContent = document.getElementById("discussionContent");
const submitBtn = document.getElementById("submitBtn");

const editDiscussionModal = new bootstrap.Modal(document.getElementById("editDiscussionModal"));

editDiscussionBtn.addEventListener("click", (e) => {
    let discussionContentValue = discussionContent.innerText;
    discussionText.value = discussionContentValue;

    let discussionTitleValue = discussionTitle.innerText;
    discussionTitleField.value = discussionTitleValue;

    submitBtn.innerText = "Update";

    editDiscussionModal.show();
});