const editDiscussionBtn = document.getElementById("editDiscussionBtn");

const editDiscussionModal = new bootstrap.Modal(document.getElementById("editDiscussionModal"));

editDiscussionBtn.addEventListener("click", (e) => {
    editDiscussionModal.show();
});