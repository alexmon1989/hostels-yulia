var BookingForm = function () {

    return {
        
        //Booking Form
        initBookingForm: function () {
    	    // Validation
	        $("#booking-form").validate({
	            // Rules for form validation
	            rules:
	            {
	                name:
	                {
	                    required: true
	                },
	                telephone:
	                {
	                    required: true
	                },
	                email:
	                {
	                    email: true
	                },
	                message:
	                {
	                    required: false
	                }
	            },
	                                
	            // Messages for form validation
	            messages:
	            {
	                name:
	                {
	                    required: 'Введите ваше имя'
	                },
	                telephone:
	                {
	                    required: 'Введите ваш телефон'
	                },
	                email:
	                {
	                    email: 'Введите верный email'
	                }
	            },
	                                
	            // Ajax form submition                  
	            submitHandler: function(form)
	            {
	                $(form).ajaxSubmit(
	                {
	                    beforeSend: function()
	                    {
	                        $('#booking-form button[type="submit"]').attr('disabled', true);
	                    },
	                    success: function()
	                    {
	                        $("#booking-form").addClass('submited');
	                    },
						error: function (data) {
							$('#booking-form button[type="submit"]').attr('disabled', false);
							var errors = data.responseJSON.errors;
							if (errors.captcha) {
                                $("#booking-form .recaptcha-errors").html('<em class="invalid">' + errors.captcha[0] + '</em>');
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