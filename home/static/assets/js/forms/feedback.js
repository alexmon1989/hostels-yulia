var FeedbackForm = function () {

    return {
        
        //Feedback Form
        initFeedbackForm: function () {
    	    // Validation
	        $("#feedback-form").validate({
	            // Rules for form validation
	            rules:
	            {
	                client_name:
	                {
	                    required: true
	                },
	                text:
	                {
	                    required: true
	                }
	            },
	                                
	            // Messages for form validation
	            messages:
	            {
	                client_name:
	                {
	                    required: 'Введите ваше имя'
	                },
	                text:
	                {
	                    required: 'Введите текст отзыва'
	                }
	            },
	                                
	            // Ajax form submition                  
	            submitHandler: function(form)
	            {
	                $(form).ajaxSubmit(
	                {
	                    beforeSend: function()
	                    {
	                        $('#feedback-form button[type="submit"]').attr('disabled', true);
	                    },
	                    success: function()
	                    {
	                        $("#feedback-form").addClass('submited');
	                    },
						error: function (data) {
							$('#feedback-form button[type="submit"]').attr('disabled', false);
							var errors = data.responseJSON.errors;
							if (errors.captcha) {
                                $("#feedback-form .recaptcha-errors").html('<em class="invalid">' + errors.captcha[0] + '</em>');
                            }
                        }
	                });
	            },
	            
	            // Do not change code below
	            errorPlacement: function(error, element)
	            {
	                error.insertAfter(element.parent());
	            }
	        });
        }

    };
    
}();