document.addEventListener("DOMContentLoaded", function () {
  let page = 1;
  let loading = false;

  function loadImages() {
    if (loading) return;
    loading = true;

    fetch(`/gallery/api/images/?page=${page}`)
      .then((response) => response.json())
      .then((data) => {
        console.log(data);
        if (data.results.length === 0) return;
        const container = document.getElementById("image-gallery");

        data.results.forEach((img) => {
          const div = document.createElement("div");
          div.className = "p-2";
          div.innerHTML = `
                      
                            <img src="${img.image}" alt="${img.name}" class="w-full h-64 object-cover">
                         
                   
                    `;
          container.appendChild(div);
        });

        page++;
        loading = false;
      })
      .catch(() => {
        loading = false;
      });
  }

  // Load initial images
  loadImages();

  // Infinite scrolling
  window.addEventListener("scroll", function () {
    if (
      window.innerHeight + window.scrollY >=
      document.body.offsetHeight - 150
    ) {
      loadImages();
    }
  });
});
