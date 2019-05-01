class_names = ['BG', 'person', 'bicycle', 'car', 'motorcycle', 'airplane',
'bus', 'train', 'truck', 'boat', 'traffic light',
'fire hydrant', 'stop sign', 'parking meter', 'bench', 'bird',
'cat', 'dog', 'horse', 'sheep', 'cow', 'elephant', 'bear',
'zebra', 'giraffe', 'backpack', 'umbrella', 'handbag', 'tie',
'suitcase', 'frisbee', 'skis', 'snowboard', 'sports ball',
'kite', 'baseball bat', 'baseball glove', 'skateboard',
'surfboard', 'tennis racket', 'bottle', 'wine glass', 'cup',
'fork', 'knife', 'spoon', 'bowl', 'banana', 'apple',
'sandwich', 'orange', 'broccoli', 'carrot', 'hot dog', 'pizza',
'donut', 'cake', 'chair', 'couch', 'potted plant', 'bed',
'dining table', 'toilet', 'tv', 'laptop', 'mouse', 'remote',
'keyboard', 'cell phone', 'microwave', 'oven', 'toaster',
'sink', 'refrigerator', 'book', 'clock', 'vase', 'scissors',
'teddy bear', 'hair drier', 'toothbrush'];

var stuff = document.getElementById('testform');
var toRender = ``;

var arrayLength = class_names.length;
    for (var i = 0; i < arrayLength; i++) {
        if (i > 0) {
            toRender += `<input type="checkbox" name="colors" value="${class_names[i]}" ${i==1 ? 'checked' : ''}/> ${class_names[i]}<br>`
        }
    }

stuff.innerHTML = toRender;


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

    var cbs = document.forms['test'].elements['colors'];
    var toForm = [];
    for(var i=0,cbLen=cbs.length;i<cbLen;i++){
        if(cbs[i].checked){
            toForm.push(cbs[i].value);
        } 
    }
    formData.append('selected', JSON.stringify(toForm));
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