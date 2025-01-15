const discussionBtn = document.getElementById("createDiscussionButton");
const discussionModal = new bootstrap.Modal(document.getElementById("discussionModal"));

const popoverTriggerList = document.querySelectorAll('[data-bs-toggle="popover"]');
const popoverList = [...popoverTriggerList].map(popoverTriggerEl => new bootstrap.Popover(popoverTriggerEl));

/**
 * This code overrides standard Bootstrap which was causing
 * issues between modals and screenreaders. This code allows
 * screenreaders to recognise that the modal is hidden and when
 * it is active.
 */
document.addEventListener("DOMContentLoaded", function () {
    document.addEventListener('hide.bs.modal', function (event) {
        if (document.activeElement) {
            document.activeElement.blur();
        }
    });
});

/**
 * This event listener shows the Create Discussion Modal
 * when the 'Create Discussion' button is clicked by the user
 */
discussionBtn.addEventListener("click", (e) => {
    discussionModal.show();
    }
);