document.addEventListener('DOMContentLoaded', function () {
    let comments = document.querySelectorAll('.comment');
    let showButton = document.getElementById('showCommentsButton');

    showButton.addEventListener('click', function () {
        comments.forEach(function (comment) {
            comment.style.display = 'block';
        });

        showButton.style.display = 'none';
    });
});
