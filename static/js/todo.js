function toggleCompleted(list_slug, todo_slug) {
  fetch(`/toggle-completed/${list_slug}/${todo_slug}/`)
    .then((response) => response.json())
    .then((data) => {
      if (data.success) {
        // Əməliyyat uğurlu olduqda bir şey etməyə gərək yoxdur, çünki səhifə yenilənəcək.
        location.reload();
      } else {
        // Əməliyyat uğursuz olduqda, xəta mesajını göstərin
        alert(data.message);
      }
    })
    .catch((error) => {
      console.error("Xəta baş verdi:", error);
      alert("Xəta baş verdi. Zəhmət olmasa bir daha cəhd edin.");
    });
}


