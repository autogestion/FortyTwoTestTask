$(document).ready(function () {

function readURL(input) {

    if (input.files && input.files[0]) {
        var reader = new FileReader();

        reader.onload = function (e) {
            $('#preview_photo').attr('src', e.target.result);
        }

        reader.readAsDataURL(input.files[0]);
    }
}

$("#id_photo").change(function(){
    readURL(this);
});

});
