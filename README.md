# adaptive-image-compression

This repository is a clone of https://github.com/matterport/Mask_RCNN, as our system depends on Mask R-CNN's Keras model. The implementation of this project can be found in PROJECT_FILES.

app.py initializes a Flask HTTP server which serves our web application and exposes our compression functionality. For the web app, the template it is in templates/index.html, the javascript is in static/js/main.js, and the css is in static/css/main.css.

We modularized our application by implementing our compression in Compressor.py and our mask generation in detector.py. The server just imports these files and calls their functions. In order to generate our experimental data, we wrote separate scripts that also imported these files; one example of this can be found in compression_graph.py.

