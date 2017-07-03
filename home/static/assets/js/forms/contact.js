var ContactForm = function () {

    return {
        
        //Contact Form
        initContactForm: function () {
	        // Validation
	        $("#form-contact").validate({
	            // Rules for form validation
	            rules:
	            {
	                name:
	                {
	                    required: true
	                },
	                email:
	                {
	                    required: true,
	                    email: true
	                },
	                message:
	                {
	                    required: true,
	                    minlength: 10
	                }
	            },
	                                
	            // Messages for form validation
	            messages:
	            {
	                name:
	                {
	                    required: 'Введите ваше имя'
	                },
	                email:
	                {
	                    required: 'Введите ваш E-mail',
	                    email: 'Введите правильный E-mail'
	                },
	                message:
	                {
	                    required: 'Введите ваше сообщение',
						minlength: 'Сообщение должно содержать не менее 10 символов'
	                }
	            },
	                                
	            // Ajax form submition                  
	            submitHandler: function(form)
	            {
	                $(form).ajaxSubmit(
	                {
	                    beforeSend: function()
	                    {
	                        $('#form-contact button[type="submit"]').attr('disabled', true);
	                    },
	                    success: function()
	                    {
	                        $("#form-contact").addClass('submited');
	                    },
						error: function (data)
						{
							$('#form-contact button[type="submit"]').attr('disabled', false);
							var errors = data.responseJSON.errors;
							if (errors.captcha) {
                                $("#form-contact .recaptcha-errors").html('<em class="invalid">' + errors.captcha[0] + '</em>');
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