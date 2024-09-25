const discussionBtn = document.getElementById("createDiscussionButton");
const discussionModal = new bootstrap.Modal(document.getElementById("discussionModal"));

const popoverTriggerList = document.querySelectorAll('[data-bs-toggle="popover"]')
const popoverList = [...popoverTriggerList].map(popoverTriggerEl => new bootstrap.Popover(popoverTriggerEl))

/**
 * This event listener shows the Create Discussion Modal
 * when the 'Create Discussion' button is clicked by the user
 */
discussionBtn.addEventListener("click", (e) => {
    discussionModal.show();
    }
);