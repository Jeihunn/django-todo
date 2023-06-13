function toggleCompleted(todo_slug) {
  fetch(`/toggle-completed/${todo_slug}/`)
    .then((response) => response.json())
    .then((data) => {
      if (data.success) {
        // Əməliyyat uğurlu olarsa, səhifəni yeniləyin
        location.reload();
      } else {
        // Əməliyyat uğursuz olarsa, xəta mesajını göstərin
        alert(data.message);
      }
    })
    .catch((error) => {
      console.error("Xəta baş verdi:", error);
      alert("Xəta baş verdi. Zəhmət olmasa bir daha cəhd edin.");
    });
}
