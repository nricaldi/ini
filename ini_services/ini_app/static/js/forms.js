$('#review-form').on('submit', function(event){

    event.preventDefault();

    let results = "";

    if($('#review-name').val() == '' && $('#review-message').val() == '') {
        results += "<p><i class='fas fa-exclamation-circle'></i> Form cannot be empty </p>"
        $('#review_results').html(results);
        return;
    } else if ($('#review-name').val().length < 2 || $('#review-message').val().length < 10 ){
        if($('#review-name').val().length < 2) {
            results += "<p><i class='fas fa-exclamation-circle'></i> Name must be at least 2 characters</p>"
        }   
        if($('#review-message').val().length < 10) {
            results += "<p><i class='fas fa-exclamation-circle'></i> Message must be at least 10 characters</p>"
        }   
        $('#review_results').html(results);
        return;
    } 
    
    console.log("form submitted!")  // sanity check
    create_review();
});

var csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;

// function csrfSafeMethod(method) {
//     // these HTTP methods do not require CSRF protection
//     // csrfmiddlewaretoken = $('[name="csrfmiddlewaretoken"]').val()
//     return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
// }

function create_review() {
    console.log("create review is working!") // sanity check
    $.ajax({
        url : "create_review", // the endpoint
        type : "POST", // http method
        data : { 
            name: $('#review-name').val(),
            rating: $('#review-rating').val(),
            message : $('#review-message').val(),
            csrfmiddlewaretoken: csrftoken
        }, // data sent with the post request

        // handle a successful response
        success : function() {
            $('#review-name').val(''); // remove the value from the input
            $('#review-rating').val(''); // remove the value from the input
            $('#review-message').val(''); // remove the value from the input
            location.reload();
        },
        // handle a non-successful response
        error : function(xhr,errmsg,err) {
            $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg); // add the error to the dom 
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    });
};


// ==================================================
// ==================================================
// ==================================================

//                  CONTACT FORM

// ==================================================
// ==================================================
// ==================================================



$('#contact-form').on('submit', function(event){

    event.preventDefault();
    console.log('contact form go');
    let results = "";

    if($('#contact-name').val() == '' && $('#contact-message').val() == '' && $('#contact-email').val() == '') {
        results += "<p><i class='fas fa-exclamation-circle'></i> Form cannot be empty </p>"
        console.log(results)
        $('#contact_results').html(results);
        console.log('empty form')
        return;
    } else if ($('#contact-name').val().length < 2 || $('#contact-email').val().length < 10 || $('#contact-message').val().length < 10){
        if($('#contact-name').val().length < 2) {
            results += "<p><i class='fas fa-exclamation-circle'></i> Name must be at least 2 characters</p>"
        }   
        if($('#contact-email').val().length < 5) {
            results += "<p><i class='fas fa-exclamation-circle'></i> Invalid Email</p>"
        }   
        if($('#contact-message').val().length < 10) {
            results += "<p><i class='fas fa-exclamation-circle'></i> Message must be at least 10 characters</p>"
        }   
        $('#contact_results').html(results);
        return;
    } 
    
    console.log("form submitted!")  // sanity check
    send_mail();
});

var csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;

function send_mail() {
    console.log("send mail is working!") // sanity check
    $.ajax({
        url : "send_mail", // the endpoint
        type : "POST", // http method
        data : { 
            name: $('#contact-name').val(),
            email: $('#contact-email').val(),
            message : $('#contact-message').val(),
            csrfmiddlewaretoken: csrftoken
        }, // data sent with the post request

        // handle a successful response
        success : function() {
            $('#contact-name').val(''); // remove the value from the input
            $('#contact-email').val(''); // remove the value from the input
            $('#contact-message').val(''); // remove the value from the input
            // location.reload();
            $('#contact_results').html("<p>Email Sent.</p>");
        },
        // handle a non-successful response
        error : function(xhr,errmsg,err) {
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    });
};