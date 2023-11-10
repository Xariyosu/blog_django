function toggleComments(articleContainer) {
    let comments = articleContainer.querySelectorAll('.comment');
    if (comments.length > 0) {
        comments.forEach(function(comment) {
            if (comment.style.display === 'none' || comment.style.display === '') {
                comment.style.display = 'block';
            } else {
                comment.style.display = 'none';
            }
        });
    } else {
        console.error("Error: No '.comment' elements found within the article container.");
    }
}

document.addEventListener('DOMContentLoaded', function () {
    document.body.addEventListener('click', function (event) {
        let clickedElement = event.target;

        if (clickedElement.classList.contains('showCommentsButton')) {
            let articleContainer = clickedElement.closest('.article-content');

            if (articleContainer) {
                toggleComments(articleContainer);
                clickedElement.textContent = (clickedElement.textContent === 'Show Comments') ? 'Hide Comments' : 'Show Comments';
            }
        }
    });
});
