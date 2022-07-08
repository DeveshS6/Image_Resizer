function fileValidation() {
    var fileInput =
        document.getElementById('file');
     
    var filePath = fileInput.value;
    
    // Allowing file type
    var allowedExtensions =
            /(\.jpg|\.jpeg|\.png)$/i;
     
    if(fileInput.files[0].size > 2097152){
        alert("File is too big it cannot be uploaded!");
        fileInput.value = "";
        };

    if (!allowedExtensions.exec(filePath) || fileInput.files[0].size > 2097152) {
        alert('Invalid file type/size');
        fileInput.value = '';
        return false;
    }
    else
    {
     
        // Image preview
        if (fileInput.files && fileInput.files[0] && fileInput.files[0].size < 2097152 && allowedExtensions.exec(filePath)) {
            var reader = new FileReader();
            reader.onload = function(e) {
                document.getElementById(
                    'imagePreview').innerHTML =
                    '<img src="' + e.target.result
                    + '"/>';
            };
             
            reader.readAsDataURL(fileInput.files[0]);
        }
    }
}


function process() {
    flash("OK")
    const file = document.querySelector("#file").files[0];
  
  
    const reader = new FileReader();
  
    reader.readAsDataURL(file);
  
    reader.onload = function (event) {
      const imgElement = document.createElement("img");
      imgElement.src = event.target.result;
      document.querySelector("#input").src = event.target.result;
  
      imgElement.onload = function (e) {
        const canvas = document.createElement("canvas");
        const MAX_WIDTH = 400;
  
        const scaleSize = MAX_WIDTH / e.target.width;
        canvas.width = MAX_WIDTH;
        canvas.height = e.target.height * scaleSize;
  
        const ctx = canvas.getContext("2d");
  
        ctx.drawImage(e.target, 0, 0, canvas.width, canvas.height);
  
        const srcEncoded = ctx.canvas.toDataURL(e.target, "image/jpeg");
        flash("OK")
        // you can send srcEncoded to the server
        document.querySelector("#output").src = srcEncoded;
        upload(srcEncoded)
      };
    };
  }

  function upload(file) {
    // Create a form using FormData. This holds key value pairs.
    var formdata = new FormData();

    // Add a key value pair ("snap", file) to the FormData object. file is the original file passed sent to the upload function.
    formdata.append("snap", file);

    // create AJAX connection
    // The fetch() method is used to request from the server and load the information in the webpages.
    // The request can be of any APIs that returns the data of the format JSON or XML. This method returns a promise.

    // The fetch() method returns a Promise and has the syntax of if true, do these sequential functions, else in the case of an error do Y.
    fetch("/upload", {
        method: 'POST',
        body: formdata,
    }).then(function(response) {
        return response.blob();
    }).then(function(blob) {
        image.src = URL.createObjectURL(blob);
    }).catch(function(err) {
        console.log('Fetch problem: ' + err.message);
    });
}