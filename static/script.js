const API = "/api/bookmarks";

async function fetchBookmarks() {
    const res = await fetch(API);
    const data = await res.json();

    const list = document.getElementById("bookmarkList");
    list.innerHTML = "";

    data.forEach(bookmark => {
        list.innerHTML += `
            <li>
                <div>
                    <a href="${bookmark.url}" target="_blank">${bookmark.title}</a>
                </div>
                <div>
                    <button onclick="editBookmark(${bookmark.id}, '${bookmark.title}', '${bookmark.url}')">Edit</button>
                    <button onclick="deleteBookmark(${bookmark.id})">Delete</button>
                </div>
            </li>
        `;
    });
}

async function addBookmark() {
    const title = document.getElementById("title").value;
    const url = document.getElementById("url").value;

    await fetch(API, {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({title, url})
    });

    document.getElementById("title").value = "";
    document.getElementById("url").value = "";

    fetchBookmarks();
}

async function deleteBookmark(id) {
    await fetch(`${API}/${id}`, { method: "DELETE" });
    fetchBookmarks();
}

async function editBookmark(id, oldTitle, oldUrl) {
    const newTitle = prompt("Edit Title:", oldTitle);
    const newUrl = prompt("Edit URL:", oldUrl);

    if (newTitle && newUrl) {
        await fetch(`${API}/${id}`, {
            method: "PUT",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify({title: newTitle, url: newUrl})
        });
        fetchBookmarks();
    }
}

fetchBookmarks();