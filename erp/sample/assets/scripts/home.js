// Assuming you're using jQuery for simplicity
$(document).ready(function() {
     // Function to retrieve CSRF token from cookie
     function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    var csrftoken = getCookie('csrftoken'); // Get CSRF token from cookie
    console.log(csrftoken)
    $('#ajaxcallbutton').click(function() {
    $.ajax({
        url: '/ajax_view', // URL to your Django view
        type: 'GET',
        dataType: 'html',
        beforeSend: function(xhr) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken); // Include CSRF token in request headers
        },
        success: function(data) {
            console.log(data)
            $('#ajax-content').html(data); // Display the returned HTML in a div with id 'ajax-content'
        },
        error: function(xhr, status, error) {
            console.error(error);
        }
    });
});
});
