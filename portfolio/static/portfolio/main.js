document.addEventListener("DOMContentLoaded", () => {
    document.querySelector("#hamburger-menu").addEventListener("click", () => {
        document.querySelector("#hamburger-menu").style.display = "none";
        document.querySelector("#x-menu").style.display = "block";
        document.querySelector("#off-canvas").style.display = "block";
        document.querySelector("#off-canvas").style.animationPlayState = "running";
    });

    document.querySelector("#x-menu").addEventListener("click", () => {
        document.querySelector("#x-menu").style.display = "none";
        document.querySelector("#hamburger-menu").style.display = "block";
        document.querySelector("#off-canvas").style.opacity = 0;
        document.querySelector("#off-canvas").style.display = "none";
        document.querySelector("#off-canvas").style.animationPlayState = "paused";
    });

    document.querySelector(".bi-brightness-high-fill").addEventListener("click", () => {
        document.querySelector("#toggle-ball").style.animationName = "toggle-ball-left";
    });

    document.querySelector(".bi-moon-fill").addEventListener("click", () => {
        document.querySelector("#toggle-ball").style.animationName = "toggle-ball-right";
    });

    document.querySelectorAll(".copy").forEach(t => {
        new bootstrap.Tooltip(t);
    });

    document.querySelector("#mail").addEventListener("click", () => {

        // Copy text to clipboard

        const copyText = document.querySelector("#mail-content");

        // Add textarea because of some security restrictions that the copy command to be executed
        // only if the user interacted with the page
        const textArea = document.createElement("textarea");
        textArea.value = copyText.textContent;
        document.body.appendChild(textArea);

        textArea.select();
        const clipBoard = document.execCommand("Copy");
        textArea.remove();

        // clipBoard returns true if the copy command was executed
        if (clipBoard) {
            document.querySelector("#mail").dataset.tooltip = "Copied!";
        }
        else {
            document.querySelector("#mail").dataset.tooltip = "Unable to Copy";
        }
    });
});