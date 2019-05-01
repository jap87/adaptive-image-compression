function upload() {
    var x = document.getElementById("myFile");

    var request = new XMLHttpRequest();
    // POST to httpbin which returns the POST data as JSON
    request.open('POST', 'http://localhost:5000/api/compress', true);
    request.onload = function (e) {
        if (request.readyState === 4) {
          if (request.status === 200) {
            


           direct = JSON.parse(request.response)


            var mask_image = document.createElement('div');     
            mask_image.innerHTML = `
            <h2>Feature Masks</h2>
            <img src="/static/images/mask.png" alt="Related Book 1">`;
            document.body.appendChild(mask_image);
            mask_image.setAttribute('class', 'imgDisplay')


            var lossless_image = document.createElement('div');
            lossless_image.innerHTML = `
            <h2>Lossless Compression</h2>
            <img src="/static/images/lossless.png" alt="Related Book 4">
             <br> 
             <p>File Size = ${(direct['lossless.png']/1024).toFixed(2)} kb</p>`;
            document.body.appendChild(lossless_image);
            lossless_image.setAttribute('class', 'imgDisplay')

            var lossy_image = document.createElement('div');
            lossy_image.innerHTML = `
            <h2>Lossy Compression</h2>
            <img src="/static/images/lossy.jpg" alt="Related Book 3">
             <br> 
             <p>File Size = ${(direct['lossy.jpg']/1024).toFixed(2)} kb</p>`;
            document.body.appendChild(lossy_image);
            lossy_image.setAttribute('class', 'imgDisplay')

            var hybrid_image = document.createElement('div');
            hybrid_image.innerHTML = `
            <h2>Hybrid Compression</h2>
            <img src="/static/images/hybrid.png" alt="Related Book 2">
             <br> 
             <p>File Size = ${(direct['hybrid.png']/1024).toFixed(2)} kb</p>`;
            document.body.appendChild(hybrid_image);
            hybrid_image.setAttribute('class', 'imgDisplay')


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