const createProfileBtn = document.getElementById("createProfileBtn");
const profileModal = new bootstrap.Modal(document.getElementById("createProfileModal"));

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

createProfileBtn.addEventListener('click', (e => {
    profileModal.show();
}));