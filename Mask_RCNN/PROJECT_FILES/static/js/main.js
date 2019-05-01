function upload() {
    var x = document.getElementById("myFile");

    var request = new XMLHttpRequest();
    // POST to httpbin which returns the POST data as JSON
    request.open('POST', 'http://localhost:5000/api/compress', true);
    request.onload = function (e) {
        if (request.readyState === 4) {
          if (request.status === 200) {
            var mask_image = document.createElement('div');
            mask_image.innerHTML = `<img src="/static/images/mask.png" alt="Related Book 1">`;
            document.body.appendChild(mask_image);
          } else {
            console.error(request.statusText);
          }
        }
      };
    var formData = new FormData();
    formData.append('file', x.files[0], x.files[0].name);
    request.send(formData);
}

function readURL(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();

        reader.onload = function (e) {
            $('#blah')
                .attr('src', e.target.result);
        };

        reader.readAsDataURL(input.files[0]);
    }
}