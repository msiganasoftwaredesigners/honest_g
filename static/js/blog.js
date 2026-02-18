document.addEventListener("DOMContentLoaded", function () {
  let page = 1;
  let loading = false;

  function loadBlogPosts() {
    if (loading) return;
    loading = true;

    fetch(`/news/api/posts/?page=${page}`)
      .then((response) => response.json())
      .then((data) => {
        if (data.results.length === 0) return;

        const container = document.getElementById("blog-gallery");

        data.results.forEach((post) => {
          const div = document.createElement("div");
          div.className =
            "bg-white rounded-xl shadow-md overflow-hidden flex flex-col justify-between h-[450px]";

          div.innerHTML = `
            <a href="/news/${post.slug}/" class="w-full h-64 overflow-hidden">
              <img class="w-full h-full object-cover transition-transform duration-300 hover:scale-105" src="${post.image}" alt="${post.title}" />
            </a>
            <div class="p-5 flex flex-col justify-between flex-grow">
              <p class="text-gray-700 text-sm mb-4 line-clamp-4">${post.short_description}</p>
              <a href="/news/${post.slug}/" class="mt-auto inline-block text-blue-950 font-semibold hover:underline">
                Read More →
              </a>
            </div>
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

  // Load initial posts
  loadBlogPosts();

  // Infinite scroll
  window.addEventListener("scroll", function () {
    if (window.innerHeight + window.scrollY >= document.body.offsetHeight - 150) {
      loadBlogPosts();
    }
  });
});
