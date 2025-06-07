  // Toastify function
 function showToast(message, type = "success") {
  Toastify({
    text: message,
    duration: 3000,
    close: true,
    gravity: "top",
    position: "center",
    style: {
      background: type === "success" ? "#28a745" : "#dc3545",
      color: "#fff"  // optional, ensures text is readable
    }
  }).showToast();
}

document.getElementById("addClassForm").addEventListener("submit", function (e) {
    e.preventDefault();

    const form = e.target;
    const formData = new FormData(form);

    fetch(form.getAttribute("data-url"), {
        method: "POST",
        headers: {
            "X-CSRFToken": form.querySelector("[name=csrfmiddlewaretoken]").value,
            "X-Requested-With": "XMLHttpRequest"
        },
        body: formData
    })
    .then(res => res.json())
    .then(data => {
        if (data.success) {
            showToast(data.message, "success");
            form.reset();
            const modal = bootstrap.Modal.getInstance(document.getElementById("addClassModal"));
            modal.hide();
            setTimeout(() => location.reload(), 4000);
        } else {
            showToast(data.message, "error");
        }
    })
    .catch(err => {
        console.error(err);
        showToast("Something went wrong", "error");
    });
});


