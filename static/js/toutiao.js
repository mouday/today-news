function next_page() {
    var data = $("#data");
    var page = parseInt(data.attr("page")) + 1;
    var tag = data.attr("tag");

    if (tag === "") {
        window.location.href = "/?page=" + page;
    }
    else {
        window.location.href = "/?page=" + page + "&tag=" + tag;
    }
}
