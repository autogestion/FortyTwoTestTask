$(document).ready(function() {
        function block_form() {
          $("#loading").show();
          $('textarea').attr('disabled', 'disabled');
          $('input').attr('disabled', 'disabled');
        }

        function unblock_form() {
          $('#loading').hide();
          $('textarea').removeAttr('disabled');
          $('input').removeAttr('disabled');
          $('.errorlist').remove();
        }

        var options = {
          beforeSubmit: function(form, options) {
                block_form();
            },
          success: function() {
            unblock_form();
            $("#form_ajax").show();
            $('.success_msg').html("<p class='ajax_success'>Changes have been saved</p>");
          },
          
          error: function(resp) {
            unblock_form();
            $('.success_msg').html("<p class='ajax_error'>Changes have been not saved</p>");
            // render errors in form fields
            var errors = JSON.parse(resp.responseText);
            for (error in errors) {
              var id = '#id_' + error;
              $(id).parent('p').prepend(errors[error]);
            }
          }
        };

        jQuery(document).ajaxStart(function(){
        var $html = $('html'),
            $body = $('body'),
            $overlay = $("<div id='loading' style='z-index: 9000;'><img src='/static/img/ajax-loader.gif'/>" +
                    '</div>').appendTo($body);
        if($overlay.is(':visible'))
            $overlay.show();
        else
            $overlay.hide();
        
        });

        jQuery(document).ajaxStop(function(){
            $('#loading').remove();
        });

        $('#form_ajax').ajaxForm(options);
});