const createProfileBtn = document.getElementById("createProfileBtn");
const profileModal = new bootstrap.Modal(document.getElementById("createProfileModal"));

createProfileBtn.addEventListener('click', (e => {
    profileModal.show();
}));