const checkboxes = document.querySelectorAll('input[type="checkbox"]');
const csrfToken = document.currentScript.getAttribute("data-csrf-token");

checkboxes.forEach(function (checkbox) {
  checkbox.addEventListener("change", function () {
    const container = this.parentElement;
    container.classList.add("loading");
    const urlTemplate = "http://127.0.0.1:8000/actu/{{id}}/";
    const url = urlTemplate.replace("{{id}}", this.id.split("-")[2]);
    fetch(url, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": csrfToken,
      },
      body: JSON.stringify({}),
    })
      .then(function (response) {
        container.classList.remove("loading");
        if (response.ok) {
          return response.json();
        } else {
          throw new Error("Error al actualizar el valor.");
        }
      })
      .catch(function (error) {
        console.error(error);
        alert(error);
      });
  });
});
