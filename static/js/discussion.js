const discussionBtn = document.getElementById("createDiscussionButton");

const discussionModal = new bootstrap.Modal(document.getElementById("discussionModal"));

discussionBtn.addEventListener("click", (e) => {
    discussionModal.show();
    }
);