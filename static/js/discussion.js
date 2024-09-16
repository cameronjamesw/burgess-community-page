const discussionBtn = document.getElementById("createDiscussionButton");
const editDiscussionBtns = document.getElementsByClassName("editDiscussionBtns");

const discussionModal = new bootstrap.Modal(document.getElementById("discussionModal"));

discussionBtn.addEventListener("click", (e) => {
    discussionModal.show();
    }
);

for (let btn of editDiscussionBtns){
btn.addEventListener("click", (e) => {
    console.log("You have clicked the Edit Discussion Button!!");
});
};