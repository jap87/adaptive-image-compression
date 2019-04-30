function upload() {
    var x = document.getElementById("myFile");
    console.log(x.files[0].name)

    var request = new XMLHttpRequest();
    // POST to httpbin which returns the POST data as JSON
    request.open('POST', 'http://localhost:5000/api/compress', /* async = */ false);

    var formData = new FormData();
    formData.append('file', x.files[0], x.files[0].name);

    request.send(formData);
}