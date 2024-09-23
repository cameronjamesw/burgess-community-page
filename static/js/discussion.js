const discussionBtn = document.getElementById("createDiscussionButton");
const discussionModal = new bootstrap.Modal(document.getElementById("discussionModal"));

/**
 * This event listener shows the Create Discussion Modal
 * when the 'Create Discussion' button is clicked by the user
 */
discussionBtn.addEventListener("click", (e) => {
    discussionModal.show();
    }
);