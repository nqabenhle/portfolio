const alertResponse = (message, type) => {
    const wrapper = document.createElement("div");
    wrapper.classList = type === "success" ? "alert alert-success alert-dismissible fade show" : "alert alert-danger alert-dismissible fade show";
    wrapper.role = "alert";
    
    wrapper.innerHTML = [
        `${message}`,
        `<button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>`
    ].join('');

    return wrapper;
}

document.querySelector("#submit").addEventListener("click", () => {
    let name = document.querySelector("#id_name").value;
    let email = document.querySelector("#id_email").value;
    let subject = document.querySelector("#id_offer").value;
    let message = document.querySelector("#id_message").value;
    const csrfToken = document.querySelector("input[name='csrfmiddlewaretoken']").value;
    const alertPlaceholder = document.querySelector("#alert-placeholder");

    if (name.length === 0) {
        alertPlaceholder.append(alertResponse("Name is required.", "failure"));
        return;
    }
    else if (email.length === 0) {
        alertPlaceholder.append(alertResponse("Email is required.", "failure"));
        return;
    }
    else if (subject.length === 0) {
        alertPlaceholder.append(alertResponse("Job offer is required.", "failure"));
        return;
    }
    else if (message.length === 0) {
        alertPlaceholder.append(alertResponse("Job description is required.", "failure"));
        return;
    }
    
    const aj = new XMLHttpRequest;

    aj.onreadystatechange = () => {
        if (aj.readyState === 4 && aj.status === 200) {
            name = "";
            email = "";
            subject = "";
            message = "";
            alertPlaceholder.append(alertResponse("Email sent successfully!", "success"));
        }
    }

    const data = JSON.stringify({
        name: name,
        email: email,
        job_offer: subject,
        message: message
    })

    aj.open("POST", "/hire", true);
    aj.setRequestHeader("Data-type", "json");
    aj.setRequestHeader("Content-type", "application/json");
    aj.setRequestHeader("X-CSRFToken", csrfToken);
    aj.send(data);
});