$(document).ready(function () {
    // example: https://getbootstrap.com/docs/4.2/components/modal/
    // show modal
    $('#task-modal').on('show.bs.modal', function (event) {
        const button = $(event.relatedTarget) // Button that triggered the modal
        const taskID = button.data('source') // Extract info from data-* attributes
        const content = button.data('content') // Extract info from data-* attributes

        const modal = $(this)
        if (taskID === 'Add Wish') {
            modal.find('.modal-title').text(taskID)
            $('#task-form-display').removeAttr('taskID')
        } else if (taskID === "Search"){
            modal.find('.modal-title').text(taskID)
        } 
        else if (taskID === "Query"){
            modal.find('.modal-title').text(taskID)
        } else{
            modal.find('.modal-title').text('Change Wish #' + taskID)
            $('#task-form-display').attr('taskID', taskID)
        }
    })

    $('#task-modal-offer').on('show.bs.modal', function (event) {
        const button = $(event.relatedTarget) // Button that triggered the modal
        const taskID = button.data('source') // Extract info from data-* attributes
        const content = button.data('content') // Extract info from data-* attributes

        const modal = $(this)
        if (taskID === 'Add Offer') {
            modal.find('.modal-title').text(taskID)
            $('#task-form-display').removeAttr('taskID')
        } else if (taskID === "Search"){
            modal.find('.modal-title').text(taskID)
        } 
        else if (taskID === "Query"){
            modal.find('.modal-title').text(taskID)
        } else{
            modal.find('.modal-title').text('Change Offer #' + taskID)
            $('#task-form-display').attr('taskID', taskID)
        }
    })


    $('#task-modal2').on('show.bs.modal', function (event) {
        const button = $(event.relatedTarget) // Button that triggered the modal
        const taskID = button.data('source') // Extract info from data-* attributes
        const content = button.data('content') // Extract info from data-* attributes

        const modal = $(this)
        if (taskID === 'Search') {
            modal.find('.modal-title').text(taskID)
            $('#task-form-display2').removeAttr('taskID')
        } else{
            modal.find('.modal-title').text('Change Wish #' + taskID)
            $('#task-form-display2').attr('taskID', taskID)
        }
    })

    $('#task-modal2-offer').on('show.bs.modal', function (event) {
        const button = $(event.relatedTarget) // Button that triggered the modal
        const taskID = button.data('source') // Extract info from data-* attributes
        const content = button.data('content') // Extract info from data-* attributes

        const modal = $(this)
        if (taskID === 'Search') {
            modal.find('.modal-title').text(taskID)
            $('#task-form-display2').removeAttr('taskID')
        } else{
            modal.find('.modal-title').text('Change Offer #' + taskID)
            $('#task-form-display2').attr('taskID', taskID)
        }
    })

    $('#task-modal3').on('show.bs.modal', function (event) {
        const button = $(event.relatedTarget) // Button that triggered the modal
        const taskID = button.data('source') // Extract info from data-* attributes
        const content = button.data('content') // Extract info from data-* attributes

        const modal = $(this)
        if (taskID === 'Query') {
            modal.find('.modal-title').text(taskID)
            $('#task-form-display3').removeAttr('taskID')
        } else{
            modal.find('.modal-title').text('Change Wish #' + taskID)
            $('#task-form-display3').attr('taskID', taskID)
        }
    })

    $('#task-modal4').on('show.bs.modal', function (event) {
        const button = $(event.relatedTarget) // Button that triggered the modal
        const taskID = button.data('source') // Extract info from data-* attributes
        const content = button.data('content') // Extract info from data-* attributes

        const modal = $(this)
        modal.find('.modal-title').text(taskID)
    })


    $('#submit-change').click(function () {
        const tID = $('#task-form-display').attr('taskID');
        // console.log($('#task-modal').find('.form-control').val())
        $.ajax({
            type: 'POST',
            url: tID ? '/edit/' + tID : '/create',
            contentType: 'application/json;charset=UTF-8',
            data: JSON.stringify({
                'Product Name': $('#task-modal').find('input[name=product]').val(),
                'Acceptable Price': $('#task-modal').find('input[name=price]').val(),
                'Your Name':$('#task-modal').find('input[name=name]').val(),
            }),
            success: function (res) {
                console.log(res.response)
                location.reload();
            },
            error: function () {
                console.log('Error');
            }
        });
    });

    $('#submit-change-offer').click(function () {
        const tID = $('#task-form-display').attr('taskID');
        // console.log($('#task-modal').find('.form-control').val())
        // console.log("tID is",tID);
        $.ajax({
            type: 'POST',
            url: tID ? '/edit-offer/' + tID : '/create-offer',
            contentType: 'application/json;charset=UTF-8',
            data: JSON.stringify({
                'Product Name': $('#task-modal-offer').find('input[name=product]').val(),
                'Offer Price': $('#task-modal-offer').find('input[name=price]').val(),
                'Your Name':$('#task-modal-offer').find('input[name=name]').val(),
            }),
            success: function (res) {
                console.log(res.response)
                location.reload();
            },
            error: function () {
                console.log('Error');
            }
        });
    });

    // added by gyh
    $('#go_register').click(function () {
        $.ajax({
            type: 'POST',
            url: '/add_user',
            contentType: 'application/json;charset=UTF-8',
            data: JSON.stringify({
                'User': $('#register').find('input[name=name]').val(),
                'Password': $('#register').find('input[name=password]').val(),
                'Birthday':$('#register').find('input[name=birth]').val(),
            }),
            success: function () {
                // console.log(res.response)
                // location.reload();
                location.href = "/" // jump to next
            },
            error: function () {
                console.log('Error');
            }
        });
    });

   // added by gyh
   $('#go_compare').click(function () {
    $.ajax({
        type: 'POST',
        url: '/compare',
        contentType: 'application/json;charset=UTF-8',
        data: JSON.stringify({
            'Product Name': $('#datain').find('input[name=name]').val(),
            'Price': $('#datain').find('input[name=price]').val(),
        }),
        success: function () {
            // console.log(res.response)
            // location.reload();
            location.href = "/match" // jump to next
        },
        error: function () {
            console.log('Error');
        }
    });
});


    // modi
    $('#check_but').click(function () {
        $.ajax({
            type: 'POST',
            url: '/check_user',
            contentType: 'application/json;charset=UTF-8',
            data: JSON.stringify({
                'User': $('#user_input').find('input[name=name]').val(),
                'Password': $('#user_input').find('input[name=password]').val(),
                // 'Birthday':$('#register').find('input[name=birth]').val(),
            }),
            success: function (res) {
                var count = res.response
                console.log(count)   //# newone
                // location.reload();
                if (count == 0){
                    // location.href = "/" // jump to next   
                    alert("User Doesn't Exist Or Wrong Password");
                    location.href = "/user_in" // jump to next
                } else{
                    alert("Welcome back!");
                    location.href = "/logined" // jump to next
                }
                
            },
            error: function () {
                console.log('Error');
            }
        });
    });

    $('#ask-search').click(function () {
        const tID = $('#task-form-display2').attr('taskID');
        // console.log($('#task-modal').find('.form-control').val())
        $.ajax({
            type: 'POST',
            url: tID ? '/edit/' + tID : '/search',
            contentType: 'application/json;charset=UTF-8',
            data: JSON.stringify({
                'Product Name': $('#task-modal2').find('input[name=product]').val(),
            }),
            success: function (res) {
                console.log(res.return_value)
                // location.reload();
                location.href = "/search_result"
            },
            error: function () {
                console.log('Error');
            }
        });
    });

    $('#ask-search-offer').click(function () {
        const tID = $('#task-form-display2').attr('taskID');
        // console.log($('#task-modal').find('.form-control').val())
        $.ajax({
            type: 'POST',
            url: tID ? '/edit/' + tID : '/search-offer',
            contentType: 'application/json;charset=UTF-8',
            data: JSON.stringify({
                'Product Name': $('#task-modal2-offer').find('input[name=product]').val(),
            }),
            success: function (res) {
                console.log(res.return_value)
                // location.reload();
                location.href = "/search_result_offer"
            },
            error: function () {
                console.log('Error');
            }
        });
    });

    $('#ask-query').click(function () {
        const tID = $('#task-form-display3').attr('taskID');
        // console.log($('#task-modal').find('.form-control').val())
        // location.href = "/";
        $.ajax({
            type: 'POST',
            url: tID ? '/edit/' + tID : '/query',
            contentType: 'application/json;charset=UTF-8',
            success: function (res) {
                console.log(res.return_value)
                // location.reload();
                location.href = "/match"
            },
            error: function () {
                console.log('Error');
            }
        });
    });

    $('#match_q').click(function () {
        // const tID = $('#task-form-display3').attr('taskID');
        // console.log($('#task-modal').find('.form-control').val())
        // location.href = "/";
        $.ajax({
            type: 'POST',
            url: '/query',
            contentType: 'application/json;charset=UTF-8',
            success: function (res) {
                console.log(res.return_value)
                // location.reload();
                location.href = "/match"
            },
            error: function () {
                console.log('Error');
            }
        });
    });


    $('#ask-query1').click(function () {
        const tID = $('#task-form-display4').attr('taskID');
        // console.log($('#task-modal').find('.form-control').val())
        // location.href = "/";
        $.ajax({
            type: 'POST',
            url: tID ? '/edit/' + tID : '/query1',
            contentType: 'application/json;charset=UTF-8',
            data: JSON.stringify({
                'Product Name': $('#task-modal4').find('input[name=product]').val(),
                /*'Prodiving Price': $('#task-modal3').find('input[name=price]').val(),
                'Provider Name':$('#task-modal3').find('input[name=name]').val(),
                'Wisher Name':$('#task-modal3').find('input[name=]').val(),
                'Condition Status':$('#task-modal3').find('input[name=name]').val() */
            }),
            success: function (res) {
                console.log(res.return_value)
                // location.reload();
                location.href = "/advanced_query1"
            },
            error: function () {
                console.log('Error');
            }
        });
    });

    $('.remove').click(function () {
        const remove = $(this)
        $.ajax({
            type: 'POST',
            url: '/delete/' + remove.data('source'),
            success: function (res) {
                console.log(res.response)
                location.reload();
            },
            error: function () {
                console.log('Error');
            }
        });
    });

    $('.remove-offer').click(function () {
        const remove = $(this)
        $.ajax({
            type: 'POST',
            url: '/delete-offer/' + remove.data('source'),
            success: function (res) {
                console.log(res.response)
                location.reload();
            },
            error: function () {
                console.log('Error');
            }
        });
    });

    $('.state').click(function () {
        const state = $(this)
        const tID = state.data('source')
        const new_state =""
        if (state.text() === "In Progress") {
            new_state = "Complete"
        } else if (state.text() === "Complete") {
            new_state = "Todo"
        } else if (state.text() === "Todo") {
            new_state = "In Progress"
        }

        $.ajax({
            type: 'POST',
            url: '/edit/' + tID,
            contentType: 'application/json;charset=UTF-8',
            data: JSON.stringify({
                'status': new_state
            }),
            success: function (res) {
                console.log(res)
                location.reload();
            },
            error: function () {
                console.log('Error');
            }
        });
    });

});
