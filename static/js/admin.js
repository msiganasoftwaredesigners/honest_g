//statuc/js/admin.js
document.addEventListener("DOMContentLoaded", (event) => {
  const checkboxes = document.querySelectorAll(
    '.field-is_main input[type="checkbox"]'
  );
  let isFirstCheckbox = true;

  checkboxes.forEach((checkbox) => {
    checkbox.addEventListener("change", (event) => {
      if (event.target.checked) {
        checkboxes.forEach((otherCheckbox) => {
          if (otherCheckbox !== event.target) {
            otherCheckbox.checked = false;
          }
        });
      }
    });

    // Set the first checkbox as checked and others as unchecked
    if (isFirstCheckbox) {
      checkbox.checked = true;
      isFirstCheckbox = false;
    } else {
      checkbox.checked = false;
    }
  });

   const nameField = document.querySelector("#id_product_name");
   const slugField = document.querySelector("#id_product_slug");

   if (nameField && slugField) {
     nameField.addEventListener("input", function () {
       // Only auto-fill if the slug field is currently empty
       if (slugField.value === "") {
         // A simple conversion: replace spaces with hyphens
         // This is a basic approach; the backend will clean it during save()
         slugField.value = nameField.value.trim().replace(/\s+/g, "-");
       }
     });
   }
});


