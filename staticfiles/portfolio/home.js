const skills = [
    {name: "Author", article: "an"},
    {name: "Blogger", article: "a"},
    {name: "Content Creator", article: "a"},
    {name: "Mentor", article: "a"},
    {name: "Software Developer", article: "a"},
    {name: "YouTuber", article: "a"},
]

let wordTracker = 0;

document.addEventListener("DOMContentLoaded", () => {
    setInterval(animateExpertise, 3000);

    document.querySelector("#question-submit-btn").addEventListener("click", event => {
        submitQuestion();
    });
})

function animateExpertise() {
    const article = document.querySelector("#article");
    const expertise = document.querySelector("#expertise");

    expertise.innerText = "";
    
    article.innerText = skills[wordTracker].article;
    expertise.innerText = skills[wordTracker].name;

    wordTracker == 4 ? wordTracker = 0 : wordTracker++;
}

function submitQuestion() {
    if (document.querySelector("#question").value === "") {
        alert("Fill in the question box");
        return false;
    }
    else {
        var question = document.querySelector("#question").value;
    }

    if (document.querySelector("#name").value === "" ) {
        var name = "Anonymous";
    }
    else {
        var name = document.querySelector("#name").value;
    }
    
    const aj = new XMLHttpRequest;
    const csrfToken = document.querySelector("input[name='csrfmiddlewaretoken']").value;

    aj.onreadystatechange = () => {
        if (aj.readyState === 4 && aj.status === 200) {
            alert("Submitted");
            document.querySelector("#question").value = "";
            document.querySelector("#name").value = "";
        }
        else if (aj.readyState === 4 && aj.status !== 200) {
            alert("An error occurred. Please try again later.");
        }
    }

    console.log(name);

    data = JSON.stringify({
        "name": name,
        "question": question
    })

    aj.open("POST", "/question/add", true);
    aj.setRequestHeader("Data-type", "json");
    aj.setRequestHeader("Content-type", "application/json");
    aj.setRequestHeader("X-CSRFToken", csrfToken);
    aj.send(data);
}